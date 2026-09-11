# -*- coding: utf-8 -*-
"""Independent replication of the criterion-validity pillar for V2:
under (retirement-exogenous) secretary turnover, do BOTH real cosmetic investment (CIR)
and the text measure (VAI) co-move upward, with clean leads (no pre-trend)?

Source panel: officials-turnover-cn main_panel.csv (city4 x year; has cir / inv_cosmetic /
vai_composite / change(turnover) / retire_driven / controls). We rebuild lags/leads
ourselves and run two-way (city+year) FE OLS with city-clustered SE — not trusting the
prior run's numbers. Reference (to confirm): CIR turnover-L1 ~ +0.0285, VAI-L1 ~ +0.0147,
retirement-L1 CIR ~ +0.025 / VAI ~ +0.0183, leads ~ 0.
"""
import pandas as pd, numpy as np
import statsmodels.formula.api as smf
from pathlib import Path

P = "/Users/andy/Desktop/Research/officials-turnover-cn/02-data/processed/main_panel.csv"
df = pd.read_csv(P)
print("rows:", len(df), "| cols:", df.shape[1])
# detect column names
turn = next((c for c in ["change", "turnover", "ch"] if c in df.columns), None)
cir  = next((c for c in ["cir", "CIR"] if c in df.columns), None)
vai  = next((c for c in ["vai_composite", "vai"] if c in df.columns), None)
ret  = "retire_driven" if "retire_driven" in df.columns else None
print(f"detected -> turnover={turn} cir={cir} vai={vai} retire={ret}")
for c in [turn, cir, vai, ret]:
    if c: print(f"   {c}: n_nonnull={df[c].notna().sum()}, mean={pd.to_numeric(df[c],errors='coerce').mean():.4f}")

df = df.sort_values(["city4", "year"]).copy()
g = df.groupby("city4")
df["turn_l1"] = g[turn].shift(1)        # turnover last year -> effect this year (their "L1")
df["turn_f1"] = g[turn].shift(-1)       # FUTURE turnover -> pre-trend (lead) test, expect ~0
if ret:
    df["ret_l1"] = g[ret].shift(1)

def fe(y, x):
    d = df.dropna(subset=[y, x]).copy()
    d["city4"] = d["city4"].astype(str); d["yr"] = d["year"].astype(str)
    if d[x].nunique() < 2 or len(d) < 50:
        return None
    m = smf.ols(f"{y} ~ {x} + C(city4) + C(yr)", data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["city4"]})
    return m.params[x], m.bse[x], m.pvalues[x], int(m.nobs)

print("\n=== two-way FE (city+year), city-clustered SE ===")
print(f"{'outcome':14}{'regressor':16}{'beta':>10}{'se':>9}{'p':>9}{'n':>7}")
rows = []
for y, yl in [(cir, "CIR(invest)"), (vai, "VAI(text)")]:
    if not y: continue
    specs = [("turn_l1", "turnover L1"), ("turn_f1", "turnover LEAD")]
    if ret: specs.append(("ret_l1", "retirement L1"))
    for x, xl in specs:
        r = fe(y, x)
        if r:
            b, se, p, n = r
            print(f"{yl:14}{xl:16}{b:>10.4f}{se:>9.4f}{p:>9.3f}{n:>7}")
            rows.append({"outcome": yl, "regressor": xl, "beta": round(b,4),
                         "se": round(se,4), "p": round(p,4), "n": n})
out = Path(P).parent  # not used; save next to script
Path("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-J-criterion-validity/replication_results.csv").write_text(
    pd.DataFrame(rows).to_csv(index=False), encoding="utf-8")
print("\nVERDICT GUIDE: pillar holds if turnover-L1 (and retirement-L1) are +sig for BOTH "
      "CIR and VAI, and LEADs are ~0/insignificant (clean, no pre-trend).")
