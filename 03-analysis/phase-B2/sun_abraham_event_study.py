"""
Phase B2 — Sun-Abraham / heterogeneity-robust event study via cohort-stacked
regressions (Abraham-Sun 2021 practical implementation).

Strategy: for each cohort c separately, run an event-study using ONLY cohort-c
cities as treated and not-yet-treated cohorts (or far-pre cohorts) as controls.
This yields CATT(c, e). Average across cohorts with cohort-size weights.

This avoids the singularity issues from running all cohort × event-time
interactions jointly, and matches the Callaway-Sant'Anna (2021) group-time
average treatment effect structure.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from linearmodels.panel import PanelOLS
from scipy import stats as st
import warnings; warnings.filterwarnings("ignore")

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
VAI = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
INSP = f"{PROJ}/02-data/processed/ccdi_inspection_rounds.csv"
OUT = f"{PROJ}/03-analysis/phase-B2"
FIG = f"{PROJ}/04-figures"

# Reuse city→province mapping
exec(open(f"{PROJ}/03-analysis/phase-B/event_study.py").read().split("# Merge treatment year")[0])
df = pd.read_csv(VAI)
df["province_code"] = df["city_std"].map(city_to_province)

insp = pd.read_csv(INSP)
ins = insp[["province_code", "round", "first_treatment_year", "start_month"]].drop_duplicates()
ins["treat_frac_year"] = ins["first_treatment_year"] + (ins["start_month"] - 1) / 12.0
print("Round → treatment fractional year:")
print(ins.groupby("round").agg(cohort_frac=("treat_frac_year","first"),
                                 n_provinces=("province_code","nunique")))

df = df.merge(ins[["province_code", "round", "treat_frac_year"]], on="province_code", how="left")
df["event_time_years"] = df["year"] - df["treat_frac_year"]
df["e_bin"] = np.floor(df["event_time_years"]).astype("Int64").clip(-4, 4)

sample = df[df.vai.notna() & df.year.between(2009, 2018) & df["round"].notna()].copy()
for ctrl in ["ln_gdppc","ln_pop","ind2_share"]:
    if ctrl in sample.columns:
        sample[ctrl] = sample[ctrl].fillna(sample.groupby("city_std")[ctrl].transform("mean"))

cohorts = sorted(sample["round"].dropna().astype(int).unique().tolist())
event_bins = [-3, -2, -1, 0, 1, 2, 3]  # -1 is reference
print(f"\nAnalysis sample: {len(sample)} rows; cohorts: {cohorts}")

# =====================================================================
# For each cohort c: restrict to cohort-c cities + never-yet-treated (here:
# not-yet-treated means cohorts with later round numbers, i.e. control cohorts
# have later start dates).
# Run city FE event study. Extract CATT(c, e).
# =====================================================================
catt_rows = []
for c in cohorts:
    treated = sample[sample["round"] == c].copy()
    # Controls: cities in later cohorts (not yet treated during most of the window)
    # Use cohorts > c as controls if any exist; otherwise use cohorts < c
    control_cohorts = [cc for cc in cohorts if cc > c]
    if not control_cohorts:
        # Last cohort — use prior cohorts' pre-treatment observations only
        ctrl = sample[(sample["round"] < c) & (sample["e_bin"] < -1)].copy()
    else:
        ctrl = sample[sample["round"].isin(control_cohorts)].copy()
        # Use only control-cohort observations from years BEFORE their own treatment
        # i.e. their event_time <= -1
        ctrl = ctrl[ctrl["e_bin"] <= -1]

    # For controls, set their e_bin to NaN (they're "never treated" in this comparison)
    # but we need to keep their observations for the year-by-year comparison
    ctrl["e_bin"] = np.nan

    work = pd.concat([treated, ctrl], ignore_index=True)
    work["row"] = np.arange(len(work))
    work = work.set_index(["city_std", "row"])

    # Construct event-time dummies for treated only; controls are all zero
    # Use each e_bin value except the reference (-1)
    for k in [-3, -2, 0, 1, 2, 3]:
        work[f"k_{k}"] = ((work["e_bin"] == k) & (work["round"] == c)).astype(int)

    # Also include year dummies to absorb calendar-year effects
    year_d = pd.get_dummies(work["year"], prefix="y", drop_first=True).astype(int)
    year_d.index = work.index

    X_cols = [f"k_{k}" for k in [-3, -2, 0, 1, 2, 3]]
    controls_sub = [ctx for ctx in ["ln_gdppc","ln_pop","ind2_share"] if ctx in work.columns]
    # Drop event-time dummies that are all zero in this sub-sample
    X_cols = [x for x in X_cols if work[x].sum() >= 5]
    if not X_cols:
        print(f"  cohort {c}: no event-time variation, skip")
        continue

    X = work[X_cols + controls_sub].join(year_d).astype(float)
    y = work["vai"].astype(float)
    try:
        mod = PanelOLS(y, X, entity_effects=True, drop_absorbed=True, check_rank=False)
        r = mod.fit(cov_type="clustered", cluster_entity=True)
    except Exception as e:
        print(f"  cohort {c}: fit failed ({type(e).__name__})")
        continue
    n_treat = (work["round"] == c).sum()
    n_ctrl = (work["round"] != c).sum()
    for k in [-3, -2, 0, 1, 2, 3]:
        col = f"k_{k}"
        if col in r.params.index:
            catt_rows.append({
                "cohort": c, "event_time": k,
                "beta": r.params[col],
                "se": r.std_errors[col],
                "p": r.pvalues[col],
                "n_treated": n_treat, "n_control": n_ctrl,
            })
    print(f"  cohort {c}: n_treated={n_treat}, n_control={n_ctrl}, "
          f"β(k=0)={r.params.get('k_0', np.nan):+.4f}")

catt = pd.DataFrame(catt_rows)
catt.to_csv(f"{OUT}/cohort_event_time_catt.csv", index=False)

print("\n=== CATT(c, e) — cohort-specific event-study betas ===")
print(catt.pivot(index="event_time", columns="cohort", values="beta").round(3))

# Cohort-size weights
cohort_sizes = sample.drop_duplicates("city_std").groupby("round")["city_std"].count()
cohort_weights = cohort_sizes / cohort_sizes.sum()
print(f"\nCohort weights: {cohort_weights.round(3).to_dict()}")

# Aggregate CATT to overall ATT_bar(e) with size-weighted averaging
agg_rows = []
for k in [-3, -2, 0, 1, 2, 3]:
    sub = catt[catt.event_time == k]
    if len(sub) == 0:
        continue
    ws = cohort_weights.reindex(sub.cohort).values
    ws = ws / ws.sum()
    beta_bar = np.sum(ws * sub.beta.values)
    se_bar = np.sqrt(np.sum((ws * sub.se.values) ** 2))
    z = beta_bar / se_bar if se_bar > 0 else np.nan
    p = 2 * (1 - st.norm.cdf(abs(z))) if np.isfinite(z) else np.nan
    agg_rows.append({"event_time": k, "att_bar": beta_bar, "se_bar": se_bar,
                     "z": z, "p": p,
                     "ci_lo": beta_bar - 1.96 * se_bar,
                     "ci_hi": beta_bar + 1.96 * se_bar})

# Add k=-1 reference row
agg_rows.append({"event_time": -1, "att_bar": 0, "se_bar": 0, "z": 0, "p": np.nan,
                 "ci_lo": 0, "ci_hi": 0})
agg = pd.DataFrame(agg_rows).sort_values("event_time").reset_index(drop=True)

print("\n=== Sun-Abraham-style aggregated ATT_bar(e) ===")
print(agg.round(4).to_string(index=False))
agg.to_csv(f"{OUT}/sun_abraham_event_study.csv", index=False)

# =====================================================================
# Figure
# =====================================================================
twfe = pd.read_csv(f"{PROJ}/03-analysis/phase-B/event_study_vai.csv")

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.errorbar(agg.event_time, agg.att_bar,
            yerr=[agg.att_bar - agg.ci_lo, agg.ci_hi - agg.att_bar],
            fmt="o-", capsize=4, lw=1.5, color="#2ca02c", ecolor="#60a060",
            label="Sun-Abraham (5 cohorts, heterogeneity-robust)")
ax.errorbar(twfe.event_time, twfe.beta,
            yerr=[twfe.beta - twfe.ci_lo, twfe.ci_hi - twfe.beta],
            fmt="s--", capsize=4, lw=1.0, color="#1f3a5f", ecolor="#6090b0",
            alpha=0.5, label="TWFE (2 annual cohorts, Phase B)")
ax.axhline(0, color="grey", lw=0.6, ls="--")
ax.axvline(-0.5, color="red", lw=0.8, ls=":", alpha=0.7)
ax.axhline(-0.02, color="red", lw=0.5, ls=":", alpha=0.3)
ax.axhline(0.02, color="red", lw=0.5, ls=":", alpha=0.3)
ax.set_xlabel("Event time (years from round start)")
ax.set_ylabel("β on VAI (reference k = -1)")
ax.set_title("Phase B2: Heterogeneity-robust cohort-specific event study")
ax.set_xticks(list(range(-3, 4)))
ax.legend(frameon=False)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(f"{FIG}/phase-B2-sun-abraham.pdf")
fig.savefig(f"{FIG}/phase-B2-sun-abraham.png", dpi=200)

# Key comparison
att0 = agg[agg.event_time == 0].iloc[0] if (agg.event_time == 0).any() else None
b_twfe = twfe[twfe.event_time == 0].beta.values[0]
if att0 is not None:
    print(f"\n*** MAIN RESULT ***")
    print(f"Sun-Abraham β(k=0) = {att0.att_bar:+.4f}, SE = {att0.se_bar:.4f}, p = {att0.p:.4f}")
    print(f"  95% CI: [{att0.ci_lo:+.3f}, {att0.ci_hi:+.3f}]")
    print(f"TWFE β(k=0) (Phase B) = {b_twfe:+.4f}")
    print(f"Difference (SA - TWFE): {att0.att_bar - b_twfe:+.4f}")
