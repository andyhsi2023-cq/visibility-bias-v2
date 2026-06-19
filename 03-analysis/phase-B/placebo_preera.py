"""
Phase B placebo v2 — pre-era falsification test.

Shift each province's treatment year back by 10 years (2013 → 2003, 2014 → 2004),
keeping the same treatment cohort assignment, and re-run the event study on the
earlier pre-Xi period. If the observed β(k=0) = -0.065 reflects a real inspection
effect (rather than generic post-2012 visibility trends), we should see no
significant effect in this pre-era placebo.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from linearmodels.panel import PanelOLS
import warnings
warnings.filterwarnings("ignore")

mpl.rcParams.update({"font.family": "serif", "font.size": 11, "figure.dpi": 110})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
VAI_PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
INSP_CSV = f"{PROJ}/02-data/processed/ccdi_inspection_rounds.csv"
OUT = f"{PROJ}/03-analysis/phase-B"
FIG = f"{PROJ}/04-figures"

# Reuse city→province mapping
with open(f"{PROJ}/03-analysis/phase-B/event_study.py") as f:
    src = f.read()
mapping_src = src.split("df[\"province_code\"]")[0]
exec(mapping_src)

df = pd.read_csv(VAI_PANEL)
insp = pd.read_csv(INSP_CSV).copy()
df["province_code"] = df["city_std"].map(city_to_province)


def fit_and_get_k0(df_panel, year_window):
    """Fit Model 2 on a restricted window, return k_0 coefficient + p."""
    prov_treat = insp[["province_code", "fake_treatment_year"]].drop_duplicates()
    d = df_panel.merge(prov_treat, on="province_code", how="left")
    d["event_time"] = d["year"] - d["fake_treatment_year"]
    d["event_bin"] = d["event_time"].clip(-4, 4)
    samp = d[d.vai.notna() & d.year.between(*year_window) &
             d.fake_treatment_year.notna()].copy()
    if len(samp) < 200:
        return np.nan, np.nan, len(samp)
    samp = samp.set_index(["city_std", "year"])
    event_vals = [-4, -3, -2, 0, 1, 2, 3, 4]
    for k in event_vals:
        samp[f"k_{k}"] = (samp["event_bin"] == k).astype(int)
    for c in ["ln_gdppc", "ln_pop", "ind2_share"]:
        if c in samp.columns:
            samp[c] = samp[c].fillna(samp.groupby(level="city_std")[c].transform("mean"))
    controls = [c for c in ["ln_gdppc", "ln_pop", "ind2_share"] if c in samp.columns]
    X = samp[[f"k_{k}" for k in event_vals] + controls].dropna()
    y = samp.loc[X.index, "vai"].astype(float)
    try:
        mod = PanelOLS(y, X, entity_effects=True, drop_absorbed=True, check_rank=False)
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        return res.params.get("k_0", np.nan), res.pvalues.get("k_0", np.nan), len(X)
    except Exception:
        return np.nan, np.nan, len(X)


results = []

# Observed baseline (unshifted)
insp["fake_treatment_year"] = insp["first_treatment_year"]
beta, p, n = fit_and_get_k0(df, (2009, 2018))
print(f"Observed (real 2013/2014 treatment):  β(k=0) = {beta:.4f}, p = {p:.4f}, n = {n}")
results.append({"shift_years": 0, "window": "2009-2018", "beta": beta, "p": p, "n": n})

# Pre-era placebo: shift back by various amounts
for shift in [2, 4, 6, 8, 10]:
    insp["fake_treatment_year"] = insp["first_treatment_year"] - shift
    window_lo, window_hi = 2009 - shift, 2018 - shift
    # Ensure window within data range
    window_lo = max(window_lo, 2003)
    window_hi = min(window_hi, 2024)
    if window_hi - window_lo < 5:
        continue
    beta, p, n = fit_and_get_k0(df, (window_lo, window_hi))
    print(f"Placebo (shift -{shift} yr, fake treat {int(insp.first_treatment_year.min())-shift}/{int(insp.first_treatment_year.max())-shift}): "
          f"β(k=0) = {beta:.4f}, p = {p:.4f}, n = {n}, window = [{window_lo},{window_hi}]")
    results.append({"shift_years": -shift, "window": f"{window_lo}-{window_hi}",
                    "beta": beta, "p": p, "n": n})

# Post-era placebo: shift forward (if data available)
for shift in [2, 4, 6]:
    insp["fake_treatment_year"] = insp["first_treatment_year"] + shift
    window_lo, window_hi = 2009 + shift, 2018 + shift
    window_hi = min(window_hi, 2024)
    if window_hi - window_lo < 5:
        continue
    beta, p, n = fit_and_get_k0(df, (window_lo, window_hi))
    print(f"Placebo (shift +{shift} yr, fake treat {int(insp.first_treatment_year.min())+shift}/{int(insp.first_treatment_year.max())+shift}): "
          f"β(k=0) = {beta:.4f}, p = {p:.4f}, n = {n}, window = [{window_lo},{window_hi}]")
    results.append({"shift_years": +shift, "window": f"{window_lo}-{window_hi}",
                    "beta": beta, "p": p, "n": n})

pd.DataFrame(results).to_csv(f"{OUT}/placebo_preera.csv", index=False)
print(f"\nSaved: {OUT}/placebo_preera.csv")

# Figure
fig, ax = plt.subplots(figsize=(7.5, 4.5))
df_r = pd.DataFrame(results)
df_r["label"] = df_r.apply(lambda r: f"Real" if r["shift_years"] == 0 else f"{r['shift_years']:+d}y", axis=1)
colors = ["#d62728" if s == 0 else "#999999" for s in df_r["shift_years"]]
ax.bar(df_r["label"], df_r["beta"], color=colors, edgecolor="black", lw=0.5)
for i, row in df_r.iterrows():
    star = "*" if row["p"] < 0.05 else ""
    ax.text(i, row["beta"] + (0.005 if row["beta"] > 0 else -0.012),
            f"{row['beta']:.3f}{star}", ha="center", fontsize=9)
ax.axhline(0, color="grey", lw=0.6, ls="-")
ax.axhline(-0.02, color="red", lw=0.5, ls=":", alpha=0.5)
ax.set_xlabel("Treatment-year shift from actual (years)")
ax.set_ylabel("β(k=0)")
ax.set_title("Pre-/post-era placebo: β(k=0) under shifted treatment years")
ax.grid(True, alpha=0.3, axis="y")
fig.tight_layout()
fig.savefig(f"{FIG}/phase-B-placebo-preera.pdf")
fig.savefig(f"{FIG}/phase-B-placebo-preera.png", dpi=200)
print(f"Saved: {FIG}/phase-B-placebo-preera.pdf / .png")
