"""
Phase B placebo test: randomize treatment-year assignment across provinces,
re-run the event study, and compare the observed t=0 effect vs the placebo distribution.

If the observed β(k=0) = -0.065 is an artifact of incidental correlation rather
than a true inspection effect, we should see similar magnitudes in placebo
randomizations.
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
import importlib.util
spec = importlib.util.spec_from_file_location("es", f"{PROJ}/03-analysis/phase-B/event_study.py")
# We'll just build from scratch with a simpler mapping extracted from event_study_v2.py's own run
# Simpler: re-load the inspection file and match by province_code
df = pd.read_csv(VAI_PANEL)
insp = pd.read_csv(INSP_CSV)

# We need the city→province mapping. Read it from the previous script output or reconstruct
# Given that all 6294 rows matched in the previous run, we can use a smaller approach:
# build province_code from the first treatment assignment by re-running the mapping.
# To avoid duplicating 300+ lines of mapping dict, we'll exec the event_study.py up to
# the mapping definition.
with open(f"{PROJ}/03-analysis/phase-B/event_study.py") as f:
    src = f.read()
# Exec only the mapping setup (up to "df['province_code']" line)
mapping_src = src.split("df[\"province_code\"]")[0]
exec(mapping_src)
df["province_code"] = df["city_std"].map(city_to_province)

prov_treat = insp[["province_code", "first_treatment_year"]].drop_duplicates()
df_real = df.merge(prov_treat, on="province_code", how="left")
df_real["event_time"] = df_real["year"] - df_real["first_treatment_year"]
df_real["event_bin"] = df_real["event_time"].clip(-4, 4)

# Set sample window (same as main)
sample_real = df_real[df_real.vai.notna() & df_real.year.between(2009, 2018) &
                      df_real.first_treatment_year.notna()].copy()


def run_es(sample, cols_to_use):
    """Fit Model 2 (city FE + event-time dummies + controls) and return β(k=0)."""
    s = sample.copy().set_index(["city_std", "year"])
    event_vals = [-4, -3, -2, 0, 1, 2, 3, 4]
    for k in event_vals:
        s[f"k_{k}"] = (s["event_bin"] == k).astype(int)
    for c in ["ln_gdppc", "ln_pop", "ind2_share"]:
        if c in s.columns:
            s[c] = s[c].fillna(s.groupby(level="city_std")[c].transform("mean"))
    dummies = [f"k_{k}" for k in event_vals]
    controls = [c for c in ["ln_gdppc", "ln_pop", "ind2_share"] if c in s.columns]
    X = s[dummies + controls].dropna()
    y = s.loc[X.index, "vai"].astype(float)
    try:
        mod = PanelOLS(y, X, entity_effects=True, time_effects=False,
                       drop_absorbed=True, check_rank=False)
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        return res.params.get("k_0", np.nan)
    except Exception:
        return np.nan


# Observed β(k=0)
beta_observed = run_es(sample_real, None)
print(f"Observed β(k=0) = {beta_observed:.4f}")

# ================================================================
# Placebo: randomly reassign treatment years across provinces
# ================================================================
np.random.seed(20260414)
N_PLACEBO = 500
placebo_betas = []

# Get the treatment-year distribution
treat_year_pool = insp["first_treatment_year"].values.copy()
prov_pool = insp["province_code"].unique()

for b in range(N_PLACEBO):
    # Shuffle treatment-year assignments across provinces
    perm = np.random.permutation(treat_year_pool)
    placebo_prov_treat = pd.DataFrame({
        "province_code": prov_pool,
        "first_treatment_year": perm[:len(prov_pool)],
    })
    # Rebuild
    df_p = df.merge(placebo_prov_treat, on="province_code", how="left")
    df_p["event_time"] = df_p["year"] - df_p["first_treatment_year"]
    df_p["event_bin"] = df_p["event_time"].clip(-4, 4)
    sample_p = df_p[df_p.vai.notna() & df_p.year.between(2009, 2018) &
                    df_p.first_treatment_year.notna()].copy()
    beta_p = run_es(sample_p, None)
    placebo_betas.append(beta_p)
    if (b + 1) % 50 == 0:
        print(f"  Placebo {b+1}/{N_PLACEBO}: last β = {beta_p:.4f}")

placebo_arr = np.array([b for b in placebo_betas if np.isfinite(b)])
print(f"\n{len(placebo_arr)} finite placebo draws")
print(f"Placebo β(k=0) mean:  {placebo_arr.mean():.4f}")
print(f"Placebo β(k=0) SD:    {placebo_arr.std():.4f}")
print(f"Placebo β(k=0) 5-95%: [{np.percentile(placebo_arr, 5):.4f}, {np.percentile(placebo_arr, 95):.4f}]")

# Empirical p-value: proportion of placebo |β| >= |observed β|
p_empirical = np.mean(np.abs(placebo_arr) >= abs(beta_observed))
p_lower = np.mean(placebo_arr <= beta_observed)  # one-tailed (observed is negative)
print(f"\nTwo-tailed empirical p (|placebo| ≥ |observed|): {p_empirical:.4f}")
print(f"One-tailed empirical p (placebo ≤ observed):    {p_lower:.4f}")

# Save
pd.DataFrame({"placebo_beta": placebo_arr}).to_csv(f"{OUT}/placebo_distribution.csv", index=False)

# Figure
fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.hist(placebo_arr, bins=40, color="#cccccc", edgecolor="#888888", alpha=0.8,
        label=f"Placebo distribution (N={len(placebo_arr)})")
ax.axvline(beta_observed, color="#d62728", lw=2,
           label=f"Observed β = {beta_observed:.3f}")
ax.axvline(0, color="grey", lw=0.8, ls=":")
ax.set_xlabel("β(k=0) under placebo randomization")
ax.set_ylabel("Frequency")
ax.set_title(f"Placebo test: observed effect vs randomized-treatment null (two-tailed p = {p_empirical:.3f})")
ax.legend(frameon=False)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(f"{FIG}/phase-B-placebo.pdf")
fig.savefig(f"{FIG}/phase-B-placebo.png", dpi=200)
print(f"\nSaved: {FIG}/phase-B-placebo.pdf / .png")
