"""
Probe 1 + 3 — Yearbook behavioral measure vs text-VAI, and vs analysis-panel CIR.

Inputs (each read at most once):
  - /Volumes/P1/城市研究/地级市市政设施、环境、绿地指标2002-2024年（源自《中国城乡建设统计年鉴》（CSMAR库））.xlsx
  - /Users/andy/Desktop/Claude/visibility-bias/02-data/processed/analysis_panel_final_v2.csv

Outputs:
  - probe1_merged.csv  (city_std × year × all standardized indicators + composites + vai + CIR)
  - probe1_results.json (correlations + within-city residualized correlations + sample sizes)

Design:
  - Visible indicators (per-year z, then mean):
      vis1  = 人均道路面积（平方米）              col 11
      vis2  = 人均公园绿地面积（平方米）          col 17
      vis3  = 建成区绿化覆盖率%                   col 18
      vis4  = 建成区绿地率%                       col 19
  - Functional indicators (per-year z, then mean):
      fun1  = 供水普及率%                         col 7
      fun2  = 燃气普及率%                         col 9
      fun3  = 污水处理率%                         col 15
      fun4  = 污水处理厂集中处理率%               col 16
      fun5  = 建成区排水管道密度                  col 14
  - yearbook_bias = visible_composite − functional_composite
  - Merge with analysis-panel VAI on city_std × year (panel's city_std already
    stripped of 市/地区/自治州/盟). Strip same suffixes from yearbook city name.

Hard compute constraints respected:
  - n_workers = 1 (no multiprocessing).
  - Yearbook xlsx <1MB, panel <6MB → safe to load whole. Each file read once.
"""

from __future__ import annotations
import json
from pathlib import Path

import numpy as np
import openpyxl
import pandas as pd
from scipy import stats

PROBE_DIR = Path("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-H-probes")
YEARBOOK = Path(
    "/Volumes/P1/城市研究/"
    "地级市市政设施、环境、绿地指标2002-2024年（源自《中国城乡建设统计年鉴》（CSMAR库））.xlsx"
)
PANEL = Path(
    "/Users/andy/Desktop/Claude/visibility-bias/02-data/processed/analysis_panel_final_v2.csv"
)

PROBE_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
# 1. Load yearbook (read-only, one pass)
# ------------------------------------------------------------------
print("Loading yearbook xlsx (one pass) ...")
wb = openpyxl.load_workbook(YEARBOOK, read_only=True, data_only=True)
ws = wb["sheet1"]
rows = list(ws.iter_rows(values_only=True))
wb.close()
header = list(rows[0])
yb = pd.DataFrame(rows[1:], columns=header)
print(f"  yearbook rows={len(yb)}, cols={len(header)}")

# Rename to ASCII handles
rename = {
    "统计年度": "year",
    "城市代码": "city_code",
    "城市名称": "city_name_yb",
    "供水普及率%": "water_supply_rate",
    "燃气普及率%": "gas_supply_rate",
    "建成区排水管道密度": "drainage_density",
    "污水处理率%": "sewage_rate",
    "污水处理厂集中处理率%": "sewage_plant_rate",
    "人均道路面积（平方米）": "road_pc",
    "人均公园绿地面积（平方米）": "park_green_pc",
    "建成区绿化覆盖率%": "greening_cover_rate",
    "建成区绿地率%": "greenspace_rate",
}
yb = yb.rename(columns=rename)
yb = yb[list(rename.values())].copy()
yb["year"] = pd.to_numeric(yb["year"], errors="coerce").astype("Int64")
for c in [
    "water_supply_rate", "gas_supply_rate", "drainage_density",
    "sewage_rate", "sewage_plant_rate",
    "road_pc", "park_green_pc", "greening_cover_rate", "greenspace_rate",
]:
    yb[c] = pd.to_numeric(yb[c], errors="coerce")


def strip_admin(name):
    if not isinstance(name, str):
        return name
    s = name
    for suf in ["自治州", "地区", "盟", "市"]:
        if s.endswith(suf):
            s = s[: -len(suf)]
            break
    return s


yb["city_std"] = yb["city_name_yb"].map(strip_admin)

# missing rates per indicator (sanity)
miss = {c: float(yb[c].isna().mean()) for c in [
    "road_pc", "park_green_pc", "greening_cover_rate", "greenspace_rate",
    "water_supply_rate", "gas_supply_rate", "sewage_rate",
    "sewage_plant_rate", "drainage_density",
]}
print("Indicator missingness:")
for k, v in miss.items():
    print(f"  {k:24s}  miss={v:.3f}")

# ------------------------------------------------------------------
# 2. Per-year z-standardize each indicator
# ------------------------------------------------------------------
VIS = ["road_pc", "park_green_pc", "greening_cover_rate", "greenspace_rate"]
FUN = ["water_supply_rate", "gas_supply_rate",
       "sewage_rate", "sewage_plant_rate", "drainage_density"]


def zscore_within_year(df, cols):
    out = df.copy()
    for c in cols:
        g = out.groupby("year")[c]
        mu = g.transform("mean")
        sd = g.transform("std")
        out[c + "_z"] = (out[c] - mu) / sd
    return out


yb = zscore_within_year(yb, VIS + FUN)

# Composite = row mean of available z-scores; require ≥2 visible AND ≥2 functional
vis_z_cols = [c + "_z" for c in VIS]
fun_z_cols = [c + "_z" for c in FUN]
yb["n_vis_avail"] = yb[vis_z_cols].notna().sum(axis=1)
yb["n_fun_avail"] = yb[fun_z_cols].notna().sum(axis=1)
yb["visible_composite"] = yb[vis_z_cols].mean(axis=1, skipna=True)
yb["functional_composite"] = yb[fun_z_cols].mean(axis=1, skipna=True)
yb["yearbook_bias"] = yb["visible_composite"] - yb["functional_composite"]

mask_valid = (yb["n_vis_avail"] >= 2) & (yb["n_fun_avail"] >= 2)
print(f"  composites computed; rows valid (≥2 vis & ≥2 fun) = {int(mask_valid.sum())} / {len(yb)}")

# ------------------------------------------------------------------
# 3. Load analysis panel (one pass) — only the columns we need
# ------------------------------------------------------------------
print("Loading analysis_panel_final_v2.csv (one pass, selected cols) ...")
USE = [
    "city_std", "year", "vai", "vai_extended", "vai_contextual",
    "vai_composite", "CIR", "v_count", "f_count", "text_length",
]
panel = pd.read_csv(PANEL, usecols=USE)
panel["year"] = pd.to_numeric(panel["year"], errors="coerce").astype("Int64")
print(f"  panel rows={len(panel)} unique cities={panel['city_std'].nunique()} "
      f"years={panel['year'].min()}-{panel['year'].max()}")

# basic VAI availability
print(f"  panel rows with vai non-null            = {panel['vai'].notna().sum()}")
print(f"  panel rows with CIR non-null            = {panel['CIR'].notna().sum()}")

# ------------------------------------------------------------------
# 4. Merge yearbook ↔ panel on city_std × year
# ------------------------------------------------------------------
print("Merging on city_std × year ...")
yb_keep = yb[mask_valid].copy()
m = panel.merge(yb_keep, on=["city_std", "year"], how="inner")
print(f"  merge rows = {len(m)}")
print(f"  unique cities in merge = {m['city_std'].nunique()}")
print(f"  year range in merge = {m['year'].min()}-{m['year'].max()}")

# How many panel rows had VAI but no yearbook hit, and vice versa?
panel_with_vai = panel[panel["vai"].notna()]
left = panel_with_vai.merge(yb_keep[["city_std", "year"]], on=["city_std", "year"], how="left", indicator=True)
print(f"  panel rows with vai non-null               = {len(panel_with_vai)}")
print(f"    matched to yearbook valid composite      = {(left['_merge'] == 'both').sum()}")
print(f"    NOT matched (likely name/year missing)   = {(left['_merge'] == 'left_only').sum()}")

# ------------------------------------------------------------------
# 5. Correlations: text-VAI vs yearbook_bias (raw + within-city)
# ------------------------------------------------------------------
def pearson_with_ci(x, y):
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    msk = np.isfinite(x) & np.isfinite(y)
    n = int(msk.sum())
    if n < 5:
        return dict(n=n, r=np.nan, p=np.nan, ci_lo=np.nan, ci_hi=np.nan)
    r, p = stats.pearsonr(x[msk], y[msk])
    # Fisher z CI
    z = np.arctanh(r); se = 1 / np.sqrt(n - 3)
    lo, hi = np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)
    return dict(n=n, r=float(r), p=float(p), ci_lo=float(lo), ci_hi=float(hi))


def spearman_(x, y):
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    msk = np.isfinite(x) & np.isfinite(y)
    n = int(msk.sum())
    if n < 5:
        return dict(n=n, rho=np.nan, p=np.nan)
    rho, p = stats.spearmanr(x[msk], y[msk])
    return dict(n=n, rho=float(rho), p=float(p))


def residualize_two_way(df, col, cluster_a="city_std", cluster_b="year"):
    """Demean by city and year (additive 2WFE residual). Returns residual Series."""
    s = df[col].astype(float).copy()
    msk = s.notna()
    work = df.loc[msk, [cluster_a, cluster_b]].copy()
    work["v"] = s[msk].values
    # alternate demeaning (Gauss-Seidel) — small panel, converges fast
    prev = None
    for _ in range(50):
        a_mean = work.groupby(cluster_a)["v"].transform("mean")
        work["v"] = work["v"] - a_mean
        b_mean = work.groupby(cluster_b)["v"].transform("mean")
        work["v"] = work["v"] - b_mean
        ssr = float((work["v"] ** 2).sum())
        if prev is not None and abs(prev - ssr) / max(prev, 1e-9) < 1e-9:
            break
        prev = ssr
    out = pd.Series(np.nan, index=df.index)
    out.loc[msk] = work["v"].values
    return out


results = {}

# --- A. text-VAI vs yearbook_bias, raw and within-city ---
print("\n=== A. text-VAI ↔ yearbook_bias ===")
for vai_col in ["vai", "vai_extended", "vai_contextual", "vai_composite"]:
    sub = m.dropna(subset=[vai_col, "yearbook_bias"]).copy()
    print(f"  -- using {vai_col}: n={len(sub)}")
    if len(sub) < 30:
        results[vai_col] = dict(skipped=True, n=len(sub))
        continue
    raw_p = pearson_with_ci(sub[vai_col], sub["yearbook_bias"])
    raw_s = spearman_(sub[vai_col], sub["yearbook_bias"])
    print(f"     raw Pearson  r={raw_p['r']:+.4f} 95%CI=[{raw_p['ci_lo']:+.3f},{raw_p['ci_hi']:+.3f}] p={raw_p['p']:.3g} n={raw_p['n']}")
    print(f"     raw Spearman ρ={raw_s['rho']:+.4f} p={raw_s['p']:.3g}")
    # within-city + year FE residualized
    sub["_vai_res"] = residualize_two_way(sub, vai_col)
    sub["_bias_res"] = residualize_two_way(sub, "yearbook_bias")
    w_p = pearson_with_ci(sub["_vai_res"], sub["_bias_res"])
    w_s = spearman_(sub["_vai_res"], sub["_bias_res"])
    print(f"     within-city+year FE Pearson  r={w_p['r']:+.4f} 95%CI=[{w_p['ci_lo']:+.3f},{w_p['ci_hi']:+.3f}] p={w_p['p']:.3g} n={w_p['n']}")
    print(f"     within-city+year FE Spearman ρ={w_s['rho']:+.4f} p={w_s['p']:.3g}")
    results[vai_col] = dict(
        n=len(sub),
        raw_pearson=raw_p, raw_spearman=raw_s,
        within_pearson=w_p, within_spearman=w_s,
    )

# --- B. text-VAI vs each individual visible indicator (raw) ---
print("\n=== B. text-VAI(primary) ↔ each visible indicator (raw + within FE) ===")
results["per_visible_indicator"] = {}
for c in VIS:
    sub = m.dropna(subset=["vai", c]).copy()
    if len(sub) < 30:
        results["per_visible_indicator"][c] = dict(skipped=True, n=len(sub))
        continue
    raw = pearson_with_ci(sub["vai"], sub[c])
    sub["_vr"] = residualize_two_way(sub, "vai")
    sub["_cr"] = residualize_two_way(sub, c)
    w = pearson_with_ci(sub["_vr"], sub["_cr"])
    print(f"  {c:22s} raw r={raw['r']:+.3f} (n={raw['n']})  within-FE r={w['r']:+.3f}")
    results["per_visible_indicator"][c] = dict(
        raw=raw, within=w,
    )

# --- C. text-VAI vs each individual functional indicator (raw) ---
print("\n=== C. text-VAI(primary) ↔ each functional indicator (raw + within FE) ===")
results["per_functional_indicator"] = {}
for c in FUN:
    sub = m.dropna(subset=["vai", c]).copy()
    if len(sub) < 30:
        results["per_functional_indicator"][c] = dict(skipped=True, n=len(sub))
        continue
    raw = pearson_with_ci(sub["vai"], sub[c])
    sub["_vr"] = residualize_two_way(sub, "vai")
    sub["_cr"] = residualize_two_way(sub, c)
    w = pearson_with_ci(sub["_vr"], sub["_cr"])
    print(f"  {c:22s} raw r={raw['r']:+.3f} (n={raw['n']})  within-FE r={w['r']:+.3f}")
    results["per_functional_indicator"][c] = dict(
        raw=raw, within=w,
    )

# ------------------------------------------------------------------
# Probe 3: yearbook_bias vs panel's CIR (cosmetic investment ratio)
# ------------------------------------------------------------------
print("\n=== Probe 3: yearbook_bias ↔ panel CIR ===")
sub = m.dropna(subset=["CIR", "yearbook_bias"]).copy()
print(f"  rows with both CIR and yearbook_bias non-null = {len(sub)}")
if len(sub) >= 30:
    raw_p = pearson_with_ci(sub["CIR"], sub["yearbook_bias"])
    raw_s = spearman_(sub["CIR"], sub["yearbook_bias"])
    sub["_cir_r"] = residualize_two_way(sub, "CIR")
    sub["_bias_r"] = residualize_two_way(sub, "yearbook_bias")
    w_p = pearson_with_ci(sub["_cir_r"], sub["_bias_r"])
    print(f"  raw Pearson    r={raw_p['r']:+.4f} 95%CI=[{raw_p['ci_lo']:+.3f},{raw_p['ci_hi']:+.3f}] p={raw_p['p']:.3g} n={raw_p['n']}")
    print(f"  raw Spearman   ρ={raw_s['rho']:+.4f} p={raw_s['p']:.3g}")
    print(f"  within FE r    r={w_p['r']:+.4f} 95%CI=[{w_p['ci_lo']:+.3f},{w_p['ci_hi']:+.3f}] p={w_p['p']:.3g} n={w_p['n']}")
    # Reference: CIR vs VAI in same overlap (for comparison)
    sub2 = m.dropna(subset=["CIR", "vai"]).copy()
    r_vai_cir = pearson_with_ci(sub2["vai"], sub2["CIR"])
    print(f"  for reference: VAI ↔ CIR raw r={r_vai_cir['r']:+.4f} (n={r_vai_cir['n']})")
    results["probe3_cir_yearbookbias"] = dict(
        n=len(sub),
        raw_pearson=raw_p, raw_spearman=raw_s, within_pearson=w_p,
        ref_vai_vs_cir=r_vai_cir,
    )
else:
    results["probe3_cir_yearbookbias"] = dict(skipped=True, n=len(sub))

# ------------------------------------------------------------------
# Save
# ------------------------------------------------------------------
m.to_csv(PROBE_DIR / "probe1_merged.csv", index=False)
with open(PROBE_DIR / "probe1_results.json", "w") as f:
    json.dump(results, f, indent=2, default=lambda v: None if (isinstance(v, float) and np.isnan(v)) else v)

print(f"\nSaved: {PROBE_DIR}/probe1_merged.csv  ({len(m)} rows)")
print(f"Saved: {PROBE_DIR}/probe1_results.json")
