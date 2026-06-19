"""
Probe 2 — CLASS B24 community-satisfaction variables.

Goal: confirm we can build a CITY-LEVEL "visible vs functional" satisfaction
index from B24 items, identify the city-link variable, list scales, Ns.

Each .dta is read ONCE in chunks (we only need b24 + geo + weights + the
respondent age/sex sanity columns).

Outputs:
  probe2_summary.json — wave × Ns, scales, geo-id distribution
"""

from __future__ import annotations
import json, warnings
from pathlib import Path
import numpy as np
import pandas as pd

PROBE_DIR = Path("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-H-probes")
PROBE_DIR.mkdir(parents=True, exist_ok=True)

WAVES = {
    "2014": "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/2014class数据_发布版.dta",
    "2016": "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/2016class-individual-发布版.dta",
    "2018": "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/CLASS2018-cleaned release.dta",
    "2020": "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/individual -2020  cleaned for user.dta",
    "2023": "/Volumes/P1/城市研究/CLASS数据全/两种格式/STATA/2023_individual_release_weighted .dta",
}

# B24 labels (8 items in 2018/2020/2023 per Probe step 1 scan)
B24_THEME = {
    1: ("road",         "VIS",  "道路情况"),
    2: ("fitness",      "VIS",  "健身/活动场所"),
    3: ("security",     "FUN",  "治安环境"),
    4: ("sanitation",   "MIX",  "环境卫生"),
    5: ("respect",      "MIX",  "尊老敬老氛围"),
    6: ("committee",    "FUN",  "居委会工作人员能力"),
    7: ("lighting",     "VIS",  "道路/街道照明"),
    8: ("accessible",   "FUN",  "无障碍设施"),
}

summary = {}


def find_geo_columns(labels):
    """Find geographic-id variables: look for column names containing 'prov',
    'city', 'county', 'cbid', 'commun', or labels containing 省/市/县/社区/编/代码."""
    hits = {}
    for c, lab in labels.items():
        cl = c.lower()
        flag = []
        for tok in ["prov", "city", "county", "comm", "cbid", "村居", "sheng", "shi", "xian"]:
            if tok in cl:
                flag.append(f"name~{tok}")
        ll = lab or ""
        for tok in ["省", "市", "县", "社区", "村居", "编码", "代码", "区县"]:
            if tok in ll:
                flag.append(f"label~{tok}")
        if flag:
            hits[c] = (lab, flag)
    return hits


def read_b24_block(path, b24_vars, geo_vars):
    """Read only b24 + geo columns via chunks (avoids loading 800-col frame)."""
    cols = list(set(b24_vars) | set(geo_vars))
    chunks = []
    with pd.io.stata.StataReader(path, convert_categoricals=False, columns=cols) as rdr:
        for ch in rdr.read(chunksize=20000, iterator=False) if False else [rdr.read()]:
            chunks.append(ch)
    return pd.concat(chunks, ignore_index=True) if chunks else pd.DataFrame()


for wave, path in WAVES.items():
    print(f"\n========== CLASS {wave} ==========")
    info = {"path": path}
    try:
        with pd.io.stata.StataReader(path, convert_categoricals=False) as rdr:
            labels = rdr.variable_labels()
        cols = list(labels.keys())
        info["n_cols"] = len(cols)
        b24 = sorted([c for c in cols if c.lower().startswith("b24")])
        info["b24_vars"] = [{"name": c, "label": labels.get(c, "")} for c in b24]
        print(f"  total vars: {len(cols)}; b24 count: {len(b24)}")
        # geographic candidates
        geo_cand = find_geo_columns(labels)
        info["geo_candidates"] = {c: {"label": lab, "hits": flags}
                                  for c, (lab, flags) in geo_cand.items()}
        print(f"  geo candidates (name/label hits): {len(geo_cand)}")
        for c, (lab, flags) in list(geo_cand.items())[:20]:
            print(f"    {c:18s} {(lab or '')[:50]}  [{'|'.join(flags)}]")
        # If no b24, skip distribution
        if not b24:
            summary[wave] = info
            continue
        # Decide which geo vars to actually pull (city/province/community level)
        geo_pull = []
        for c, (lab, flags) in geo_cand.items():
            ll = lab or ""
            if (("市" in ll and "编" in ll or "代码" in ll)
                or ("市" in ll and "code" in c.lower())
                or c.lower() in ("cityid", "citycode", "city_id", "city_code",
                                 "prov", "provid", "provcode", "provcd",
                                 "city", "province", "commid", "commcode", "comm_id")):
                geo_pull.append(c)
        # Fallback: include up to 10 best label-only matches that contain 市/县/区/社区/编/代码
        if not geo_pull:
            for c, (lab, flags) in geo_cand.items():
                ll = lab or ""
                if any(k in ll for k in ["市", "县", "区", "社区", "村居", "编码", "代码"]):
                    geo_pull.append(c)
                if len(geo_pull) >= 12:
                    break
        info["geo_pull"] = geo_pull
        print(f"  geo cols pulled for value scan: {geo_pull}")
        # Read only b24+geo (one pass)
        df = read_b24_block(path, b24, geo_pull)
        info["n_rows"] = len(df)
        print(f"  rows: {len(df)}")
        # Scale/values for each b24
        scales = {}
        for c in b24:
            s = pd.to_numeric(df[c], errors="coerce") if c in df else pd.Series(dtype=float)
            if c not in df:
                scales[c] = {"missing_col": True}; continue
            vc = s.dropna().value_counts().sort_index().to_dict()
            scales[c] = {
                "n_non_null": int(s.notna().sum()),
                "n_null": int(s.isna().sum()),
                "min": float(s.min()) if s.notna().any() else None,
                "max": float(s.max()) if s.notna().any() else None,
                "value_distribution": {str(k): int(v) for k, v in vc.items()},
            }
        info["scales"] = scales
        # Print compact scale row
        for c, sc in scales.items():
            if sc.get("missing_col"):
                print(f"    {c:14s} MISSING"); continue
            vd = sc["value_distribution"]
            print(f"    {c:14s} n={sc['n_non_null']:5d}  range=[{sc['min']},{sc['max']}]  values={list(vd.items())[:6]}")
        # geo content sketch
        geo_summary = {}
        for c in geo_pull:
            if c not in df:
                geo_summary[c] = "missing"; continue
            ser = df[c]
            n_unique = int(ser.nunique(dropna=True))
            sample_vals = ser.dropna().head(5).tolist()
            sample_vals = [str(v)[:30] for v in sample_vals]
            geo_summary[c] = {"n_unique": n_unique, "sample": sample_vals,
                              "dtype": str(ser.dtype)}
        info["geo_value_summary"] = geo_summary
        print("  geo unique counts:")
        for c, g in geo_summary.items():
            if isinstance(g, dict):
                print(f"    {c:18s} unique={g['n_unique']:5d}  dtype={g['dtype']}  ex={g['sample']}")
    except Exception as e:
        info["error"] = str(e)
        print(f"  ERROR: {e}")
    summary[wave] = info

with open(PROBE_DIR / "probe2_summary.json", "w") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)
print(f"\nSaved: {PROBE_DIR}/probe2_summary.json")
