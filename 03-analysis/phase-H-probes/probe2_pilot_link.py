"""
Probe 2 — pilot link: build city-level visible vs functional satisfaction
from CLASS 2020 (the only wave with a city field) and correlate cross-
sectionally with text-VAI (2020) and yearbook_bias (2020). One wave =
no within-city FE possible; this is purely a feasibility & magnitude check.

Theme map for B24 (rationale: tangible "what you see in the neighborhood" =
visible; capability / accessibility / governance-resource items =
functional). Sanitation and respect-for-elders are intentionally NOT used
in either side; they are mixed governance items.
  VIS: B24_1 road, B24_2 fitness, B24_7 lighting
  FUN: B24_3 security, B24_6 committee competence, B24_8 accessible facilities
Scale: 1=very satisfied ... 5=very dissatisfied. We reverse-code so higher
= more satisfied.

Inputs (read once):
  /Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/individual -2020  cleaned for user.dta
  /Users/andy/Desktop/Claude/visibility-bias/02-data/processed/analysis_panel_final_v2.csv
  /Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-H-probes/probe1_merged.csv
"""

from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

PROBE_DIR = Path("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-H-probes")
CLASS_DTA = "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/individual -2020  cleaned for user.dta"
PANEL = "/Users/andy/Desktop/Claude/visibility-bias/02-data/processed/analysis_panel_final_v2.csv"
YB = PROBE_DIR / "probe1_merged.csv"


def strip_admin(s):
    if not isinstance(s, str):
        return s
    for suf in ["自治州", "地区", "盟", "市", "县", "区"]:
        if s.endswith(suf):
            return s[: -len(suf)]
    return s


print("Loading CLASS 2020 B24 (single pass) ...")
cols = ["Q3_2"] + [f"B24_{i}" for i in range(1, 9)]
with pd.io.stata.StataReader(CLASS_DTA, convert_categoricals=False, columns=cols) as rdr:
    df = rdr.read()
print(f"  n_individuals: {len(df)}")

for c in [f"B24_{i}" for i in range(1, 9)]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
    df[c + "_sat"] = 6 - df[c]  # reverse: 1=very dissat ... 5=very sat

df["vis_sat"] = df[["B24_1_sat", "B24_2_sat", "B24_7_sat"]].mean(axis=1)
df["fun_sat"] = df[["B24_3_sat", "B24_6_sat", "B24_8_sat"]].mean(axis=1)
df["city_std"] = df["Q3_2"].map(strip_admin)

agg = df.groupby("city_std").agg(
    n=("B24_1", "size"),
    vis_sat_mean=("vis_sat", "mean"),
    fun_sat_mean=("fun_sat", "mean"),
).reset_index()
agg["sat_bias"] = agg["vis_sat_mean"] - agg["fun_sat_mean"]
agg = agg[agg["n"] >= 30].copy()
agg.to_csv(PROBE_DIR / "probe2_class2020_city.csv", index=False)
print(f"  city aggregates (n_indiv >= 30): {len(agg)} cities")

print("Loading analysis panel (one pass) ...")
panel = pd.read_csv(PANEL, usecols=["city_std", "year", "vai", "vai_composite", "CIR"])
p2020 = panel[panel["year"] == 2020].copy()
print(f"  panel 2020 rows non-null vai: {p2020['vai'].notna().sum()}")

m = agg.merge(p2020, on="city_std", how="inner")
print(f"  merge sat_bias × panel 2020: {len(m)} cities")

out = {"n_class_cities_ge30": int(len(agg)),
       "n_merge_with_panel_2020": int(len(m))}

for vcol in ["vai", "vai_composite", "CIR"]:
    sub = m.dropna(subset=[vcol, "sat_bias"])
    if len(sub) < 10:
        out[f"corr_{vcol}_vs_satbias"] = dict(skipped=True, n=len(sub)); continue
    r, p = stats.pearsonr(sub[vcol], sub["sat_bias"])
    rho, p2 = stats.spearmanr(sub[vcol], sub["sat_bias"])
    out[f"corr_{vcol}_vs_satbias"] = dict(
        n=int(len(sub)),
        pearson_r=float(r), pearson_p=float(p),
        spearman_rho=float(rho), spearman_p=float(p2),
    )
    print(f"  {vcol:14s} ↔ sat_bias  n={len(sub)}  Pearson r={r:+.3f} p={p:.3g}  Spearman ρ={rho:+.3f} p={p2:.3g}")

# Link to yearbook_bias 2020
print("Linking to yearbook_bias 2020 ...")
yb = pd.read_csv(YB, usecols=["city_std", "year", "yearbook_bias"])
yb2020 = yb[yb["year"] == 2020].copy()
mm = agg.merge(yb2020, on="city_std", how="inner")
print(f"  CLASS sat_bias × yearbook_bias 2020: n={len(mm)}")
if len(mm) >= 10:
    r, p = stats.pearsonr(mm["sat_bias"].astype(float), mm["yearbook_bias"].astype(float))
    out["corr_yearbookbias_vs_satbias_2020"] = dict(n=int(len(mm)), pearson_r=float(r), pearson_p=float(p))
    print(f"  Pearson r={r:+.3f} p={p:.3g}")
else:
    out["corr_yearbookbias_vs_satbias_2020"] = dict(skipped=True, n=int(len(mm)))

with open(PROBE_DIR / "probe2_pilot_results.json", "w") as f:
    json.dump(out, f, indent=2)
print(f"\nSaved: {PROBE_DIR}/probe2_class2020_city.csv  &  probe2_pilot_results.json")
