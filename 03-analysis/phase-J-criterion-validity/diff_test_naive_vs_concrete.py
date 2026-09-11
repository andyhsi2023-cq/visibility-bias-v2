# -*- coding: utf-8 -*-
"""R2 Comment 1b — direct concrete-vs-naive difference test on COMMON observations.

Stacked two-equation (SUR-equivalent) estimation: both measures as outcomes of the same
turnover regressor, on the identical sample, on a comparable scale (both z-standardized
in-sample). Two-way FE per measure (city x measure, year x measure) via demeaning;
city-clustered VCV on the stack gives cov(b_concrete, b_naive) -> Wald test of equality.

Also reports the unstandardized coefficients on the common sample for direct comparison
with the deposited verify_results_master.csv numbers."""
import pandas as pd, numpy as np
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_params

P = "/Users/andy/Desktop/Research/officials-turnover-cn/02-data/processed/master_2002_2024.csv"
df = pd.read_csv(P).sort_values(["city4","year"])
g = df.groupby("city4")
df["turn_l1"] = g["change"].shift(1)
df["ret_l1"]  = g["retire_driven"].shift(1)
df["city4"] = df["city4"].astype(str); df["yr"] = df["year"].astype(str)

def diff_test(reg):
    d = df.dropna(subset=["wr_visibility","vai_composite",reg]).copy()
    # common sample, standardized measures
    d["z_wr"] = (d.wr_visibility - d.wr_visibility.mean()) / d.wr_visibility.std()
    d["z_naive"] = (d.vai_composite - d.vai_composite.mean()) / d.vai_composite.std()
    n = len(d)
    print(f"\nregressor = {reg}: common sample n = {n}, cities = {d.city4.nunique()}, years {d.year.min()}-{d.year.max()}")

    # unstandardized, same spec as verify_comovement_master.py (two-way FE dummies, cluster city)
    for y, lab in [("wr_visibility","wr_visibility(concrete)"), ("vai_composite","vai_composite(naive)")]:
        dd = d[[y,reg,"city4","yr"]].dropna()
        m = smf_ols(dd, y, reg)
        print(f"  unstandardized {lab:24s} b={m.params[reg]:+.4f}  SE={m.bse[reg]:.4f}  p={m.pvalues[reg]:.4f}  n={int(m.nobs)}")

    # stacked standardized
    rows = []
    for y, lab in [("z_wr","wr"), ("z_naive","naive")]:
        t = d[["city4","yr",y,reg]].dropna().rename(columns={y:"y"})
        t["m"] = lab
        rows.append(t)
    st = pd.concat(rows)
    # demean within (city,m) and (year,m)
    for key in ["city4","yr"]:
        st["y"] = st.y - st.groupby([key,"m"]).y.transform("mean")
        st[reg] = st[reg] - st.groupby([key,"m"])[reg].transform("mean")
    X = pd.DataFrame({
        "turn_wr":    st[reg] * (st.m=="wr").astype(float),
        "turn_naive": st[reg] * (st.m=="naive").astype(float),
    })
    y = st.y
    res = sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": st.city4})
    b1, b2 = res.params["turn_wr"], res.params["turn_naive"]
    V = res.cov_params().loc[["turn_wr","turn_naive"],["turn_wr","turn_naive"]]
    se1, se2 = res.bse["turn_wr"], res.bse["turn_naive"]
    cov12 = V.loc["turn_wr","turn_naive"]
    diff = b1 - b2
    se_diff = np.sqrt(se1**2 + se2**2 - 2*cov12)
    wald = (diff/se_diff)**2
    p_wald = 1 - sm.stats.stattools.stats.chi2.cdf(wald, 1)
    print(f"  standardized (z): concrete b={b1:+.4f} (SE {se1:.4f}), naive b={b2:+.4f} (SE {se2:.4f})")
    print(f"  difference = {diff:+.4f}, SE(diff) = {se_diff:.4f}, Wald chi2(1) = {wald:.2f}, p = {p_wald:.4f}")
    return dict(reg=reg, n=n, b_wr=b1, se_wr=se1, b_naive=b2, se_naive=se2,
                diff=round(diff,4), se_diff=round(se_diff,4), wald=round(wald,2), p=round(p_wald,4))

import statsmodels.formula.api as smf
def smf_ols(d, y, x):
    return smf.ols(f"{y} ~ {x} + C(city4) + C(yr)", data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["city4"]})

out = [diff_test("turn_l1"), diff_test("ret_l1")]
pd.DataFrame(out).to_csv(
    "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-J-criterion-validity/diff_test_results.csv",
    index=False)
print("\nsaved: 03-analysis/phase-J-criterion-validity/diff_test_results.csv")
