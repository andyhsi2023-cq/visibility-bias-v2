"""
Phase B event study — v2 with proper staggered DiD specification.

Switch to de Chaisemartin-D'Haultfoeuille / Sun-Abraham style with
cohort-interaction event-time dummies, or simply city FE (not both-ways)
since year FE are collinear with event-time when there are only 2 cohorts.

Approach: city FE only + event-time dummies (reference: k=-1).
This is the standard approach when year FE would absorb event-time effects.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from linearmodels.panel import PanelOLS

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
VAI_PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
INSP_CSV = f"{PROJ}/02-data/processed/ccdi_inspection_rounds.csv"
OUT_DIR = f"{PROJ}/03-analysis/phase-B"
FIG_DIR = f"{PROJ}/04-figures"
os.makedirs(FIG_DIR, exist_ok=True)

# Load (reuse city→province mapping from v1 file)
exec(open(f"{PROJ}/03-analysis/phase-B/event_study.py").read().split("# Merge treatment year")[0])

# Re-define since the exec pulls df again
df = pd.read_csv(VAI_PANEL)
insp = pd.read_csv(INSP_CSV)
df["province_code"] = df["city_std"].map(city_to_province)
prov_treat = insp[["province_code", "first_treatment_year"]].drop_duplicates()
df = df.merge(prov_treat, on="province_code", how="left")
df["event_time"] = df["year"] - df["first_treatment_year"]

# Binned event-time: [-inf, -4] → -4; [-3, +3] → own; [+4, +inf] → +4
df["event_bin"] = df["event_time"].clip(-4, 4)

# Sample: VAI non-null, year window 2009-2018 (covers k in [-4, +5] for 2013 cohort,
# and [-5, +4] for 2014 cohort)
sample = df[df.vai.notna() & df.year.between(2009, 2018) &
            df.first_treatment_year.notna()].copy()
print(f"Analysis sample: {len(sample)} city-years across {sample.city_std.nunique()} cities")
print(f"Year range: {sample.year.min()}-{sample.year.max()}")
print(f"Cohort sizes: {sample.drop_duplicates('city_std').first_treatment_year.value_counts().to_dict()}")


# =====================================================================
# MODEL 1: City FE only + event-time dummies (no year FE)
# Identifies event-time effects from within-city variation
# =====================================================================
sample2 = sample.copy().set_index(["city_std", "year"])

event_vals = [-4, -3, -2, 0, 1, 2, 3, 4]  # k = -1 is reference
for k in event_vals:
    sample2[f"k_{k}"] = (sample2["event_bin"] == k).astype(int)

dummies = [f"k_{k}" for k in event_vals]
X1 = sample2[dummies]
y1 = sample2["vai"].astype(float)

# City FE only
mod1 = PanelOLS(y1, X1, entity_effects=True, time_effects=False, drop_absorbed=True)
res1 = mod1.fit(cov_type="clustered", cluster_entity=True)
print("\n=== Model 1: VAI on event-time, city FE only ===")
print(res1.summary.tables[1])


# =====================================================================
# MODEL 2: Add controls, still city FE only
# =====================================================================
controls_available = [c for c in ["ln_gdppc", "ln_pop", "ind2_share"] if c in sample2.columns]

# Fill controls with city-specific mean to reduce data loss
for c in controls_available:
    sample2[c] = sample2[c].fillna(sample2.groupby(level="city_std")[c].transform("mean"))

X2 = sample2[dummies + controls_available].dropna()
y2 = sample2.loc[X2.index, "vai"].astype(float)

mod2 = PanelOLS(y2, X2, entity_effects=True, time_effects=False, drop_absorbed=True)
res2 = mod2.fit(cov_type="clustered", cluster_entity=True)
print("\n=== Model 2: VAI on event-time + controls, city FE only ===")
print(res2.summary.tables[1])


# =====================================================================
# MODEL 3: Cohort-by-event-time specification (de Chaisemartin-D'Haultfoeuille style)
# Key insight: with only 2 cohorts, add cohort-specific event-time effects
# =====================================================================
sample2["cohort"] = sample2["first_treatment_year"].astype(int).astype(str)
# For each cohort, create event-time dummies
int_cols = []
for cohort in ["2013", "2014"]:
    for k in event_vals:
        col = f"c{cohort}_k{k}"
        sample2[col] = ((sample2["cohort"] == cohort) & (sample2["event_bin"] == k)).astype(int)
        int_cols.append(col)

# This model with city FE only (not TWFE) — cohort × event-time interactions
X3 = sample2[int_cols + controls_available].dropna()
y3 = sample2.loc[X3.index, "vai"].astype(float)
try:
    mod3 = PanelOLS(y3, X3, entity_effects=True, time_effects=False,
                    drop_absorbed=True, check_rank=False)
    res3 = mod3.fit(cov_type="clustered", cluster_entity=True)
    print("\n=== Model 3: VAI on cohort×event-time interactions, city FE only ===")
    print(res3.summary.tables[1])
except Exception as e:
    print(f"\n=== Model 3 skipped (rank deficient): {type(e).__name__} ===")


# =====================================================================
# Save Model 2 (preferred specification) results
# =====================================================================
rows = [{"event_time": -1, "beta": 0, "se": 0, "p": np.nan, "ci_lo": 0, "ci_hi": 0}]
for k in event_vals:
    col = f"k_{k}"
    if col in res2.params.index:
        rows.append({
            "event_time": k,
            "beta": res2.params[col],
            "se": res2.std_errors[col],
            "p": res2.pvalues[col],
            "ci_lo": res2.conf_int().loc[col].iloc[0],
            "ci_hi": res2.conf_int().loc[col].iloc[1],
        })
results = pd.DataFrame(rows).sort_values("event_time").reset_index(drop=True)
results.to_csv(f"{OUT_DIR}/event_study_vai.csv", index=False)
print(f"\nModel 2 VAI event-study coefficients:")
print(results.round(4).to_string(index=False))


# =====================================================================
# Joint tests
# =====================================================================
from linearmodels.shared.hypotheses import quadratic_form_test

# Pre-trend test: are k=-4, -3, -2 jointly zero?
# Use scipy's linear constraint via wald_test
import scipy.stats as st

def joint_test(result, coef_names):
    """Joint F-test that subset of coefs = 0."""
    k = len(coef_names)
    b = result.params[coef_names].values
    V = result.cov.loc[coef_names, coef_names].values
    try:
        stat = b @ np.linalg.solve(V, b) / k
        p = 1 - st.f.cdf(stat, k, result.df_resid)
        return stat, p
    except np.linalg.LinAlgError:
        return np.nan, np.nan

pre_coefs = [c for c in ["k_-4", "k_-3", "k_-2"] if c in res2.params.index]
post_coefs = [c for c in ["k_0", "k_1", "k_2", "k_3", "k_4"] if c in res2.params.index]

if pre_coefs:
    stat, p = joint_test(res2, pre_coefs)
    print(f"\nPre-trend joint F-test (H0: k in [-4,-3,-2] all zero):")
    print(f"  F = {stat:.3f}, p = {p:.4f}")
    print(f"  {'⚠️ pre-trend violation' if p < 0.10 else '✅ pre-trend not rejected'}")

if post_coefs:
    stat, p = joint_test(res2, post_coefs)
    print(f"\nPost-treatment joint F-test (H0: k in [0,4] all zero):")
    print(f"  F = {stat:.3f}, p = {p:.4f}")
    print(f"  Pre-registered direction: negative")
    print(f"  Observed post-treatment mean β = {res2.params[post_coefs].mean():.4f}")


# =====================================================================
# Figure
# =====================================================================
fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.errorbar(results["event_time"], results["beta"],
            yerr=[results["beta"] - results["ci_lo"], results["ci_hi"] - results["beta"]],
            fmt="o-", capsize=4, lw=1.5, color="#1f3a5f", ecolor="#6090b0")
ax.axhline(0, color="grey", lw=0.6, ls="--")
ax.axvline(-0.5, color="red", lw=0.8, ls=":", alpha=0.7, label="inspection")
ax.set_xlabel("Event time (years since first central inspection)")
ax.set_ylabel("β on VAI (reference k = −1)")
ax.set_title("Phase B event-study: VAI around central inspection assignment")
ax.set_xticks(list(range(-4, 5)))
ax.legend(frameon=False, loc="upper right")
ax.grid(True, alpha=0.3)

# Pre-registered magnitude threshold line (|Δa| ≥ 0.02)
ax.axhline(-0.02, color="red", lw=0.5, ls=":", alpha=0.5)
ax.axhline(0.02, color="red", lw=0.5, ls=":", alpha=0.5)

fig.tight_layout()
fig.savefig(f"{FIG_DIR}/phase-B-event-study.pdf")
fig.savefig(f"{FIG_DIR}/phase-B-event-study.png", dpi=200)
print(f"\nSaved: {FIG_DIR}/phase-B-event-study.pdf / .png")
