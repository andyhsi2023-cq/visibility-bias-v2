# -*- coding: utf-8 -*-
"""VERIFY the criterion-validity pillar on the FULL panel that actually contains the
concrete/valid text measure (wr_visibility). The prior replicate_comovement.py read
main_panel.csv, which has ONLY the naive vai_composite -> it could never test the
decisive claim. master_2002_2024.csv has city4/year/cir/change/retire_driven AND BOTH
vai_composite (naive) and wr_visibility (concrete, Wu-Zhou-aligned). Same methodology:
two-way (city+year) FE OLS, city-clustered SE; turnover_L1 effect, future-turnover LEAD
(pre-trend), retirement-exogenous L1.

Claim to verify (V2-EVIDENCE-CORE.md):
  CIR  : L1 +0.025 p=0.000 ; lead -0.009 p=0.26 ; retire-L1 +0.024 p=0.043
  wr_visibility (concrete/valid): L1 +0.0103 p=0.010 ; lead +0.001 p=0.84 ; retire-L1 +0.0164 p=0.010
  vai_composite (naive)        : L1 +0.002  p=0.54  ; retire-L1 +0.004 p=0.39  (NULL)
"""
import pandas as pd, numpy as np
import statsmodels.formula.api as smf

P = "/Users/andy/Desktop/Research/officials-turnover-cn/02-data/processed/master_2002_2024.csv"
df = pd.read_csv(P)
print("rows:", len(df), "| cols:", df.shape[1])
turn, ret = "change", "retire_driven"
outcomes = [("cir", "CIR(real invest)"), ("wr_visibility", "wr_visibility(concrete)"),
            ("vai_composite", "vai_composite(naive)")]
for c in [turn, ret] + [o[0] for o in outcomes]:
    print(f"   {c}: n_nonnull={df[c].notna().sum()}, mean={pd.to_numeric(df[c],errors='coerce').mean():.4f}")

df = df.sort_values(["city4", "year"]).copy()
g = df.groupby("city4")
df["turn_l1"] = g[turn].shift(1)     # turnover last year -> this year (L1)
df["turn_f1"] = g[turn].shift(-1)    # FUTURE turnover -> pre-trend LEAD, expect ~0
df["ret_l1"]  = g[ret].shift(1)

def fe(y, x):
    d = df.dropna(subset=[y, x]).copy()
    d["city4"] = d["city4"].astype(str); d["yr"] = d["year"].astype(str)
    if d[x].nunique() < 2 or len(d) < 50:
        return None
    m = smf.ols(f"{y} ~ {x} + C(city4) + C(yr)", data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["city4"]})
    return m.params[x], m.bse[x], m.pvalues[x], int(m.nobs)

print("\n=== two-way FE (city+year), city-clustered SE — master_2002_2024.csv ===")
print(f"{'outcome':24}{'regressor':16}{'beta':>10}{'se':>9}{'p':>9}{'n':>7}")
rows = []
for y, yl in outcomes:
    for x, xl in [("turn_l1","turnover L1"), ("turn_f1","turnover LEAD"), ("ret_l1","retirement L1")]:
        r = fe(y, x)
        if r:
            b, se, p, n = r
            print(f"{yl:24}{xl:16}{b:>10.4f}{se:>9.4f}{p:>9.3f}{n:>7}")
            rows.append({"outcome": yl, "regressor": xl, "beta": round(b,4),
                         "se": round(se,4), "p": round(p,4), "n": n})
pd.DataFrame(rows).to_csv(
    "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-J-criterion-validity/verify_results_master.csv",
    index=False, encoding="utf-8")
print("\nPILLAR HOLDS iff: turnover-L1 & retirement-L1 are +sig for BOTH cir AND wr_visibility,")
print("                  vai_composite stays null, and all LEADs ~0 (clean pre-trends).")
