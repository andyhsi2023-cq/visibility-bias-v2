"""
Phase B2-extended — Event study with CCDI Rounds 1-9 (first treatment + huitoukan re-inspection + additional rounds).

Design insight: Rounds 6-9 extend the treatment timeline from 2013-2014 (narrow
1.5-year window) to 2013-2017 (4.5-year window). All 31 provinces treated by
Round 5; Rounds 6-9 are re-treatments (huitoukan) for 23 provinces.

Two analysis strategies:

  A. **Recent-inspection indicator**: bin each city-year by whether any
     inspection (first or huitoukan) occurred within the last 2 years. This
     treats the inspection regime as a continuously-refreshed treatment and
     leverages the repeated-treatment structure.

  B. **Multi-event study**: treat huitoukan as a SECOND treatment event; estimate
     dynamics around each event separately. Test whether the huitoukan effect is
     as large as the first-treatment effect.

  C. **Sun-Abraham with expanded cohorts**: now 9 cohorts (5 first + 4 re-treat)
     span 2013-2017. Heterogeneity-robust estimator should have better power.

We run C primarily and report A as robustness.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys, os

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
VAI = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
INSP_EXT = f"{PROJ}/02-data/processed/ccdi_inspection_rounds_extended.csv"
OUT = f"{PROJ}/03-analysis/phase-B2"
FIG = f"{PROJ}/04-figures"

# Reuse city→province mapping — inline extract from event_study.py without triggering linearmodels import
import re
with open(f"{PROJ}/03-analysis/phase-B/event_study.py") as f:
    src = f.read()
# Find the mapping dict — assumes it starts with "city_to_province = {"
m = re.search(r"city_to_province = \{.*?\}", src, re.DOTALL)
if m:
    mapping_code = m.group(0)
    exec(mapping_code)
else:
    raise RuntimeError("Could not locate city_to_province mapping")
df = pd.read_csv(VAI)
df["province_code"] = df["city_std"].map(city_to_province)

insp = pd.read_csv(INSP_EXT)
insp["treat_frac_year"] = insp["treatment_year"] + (insp["start_month"] - 1) / 12.0

# Get earliest inspection per province (this is still the first-treatment timing)
first_treat = insp[insp.treatment_type == "first"][["province_code", "treat_frac_year"]].rename(
    columns={"treat_frac_year": "first_treat_year"})
df = df.merge(first_treat, on="province_code", how="left")

# ============================================================
# STRATEGY A: Recent-inspection indicator
# ============================================================
# For each city-year, count how many inspections occurred in the last 2 calendar years
def count_recent_insp(row, insp_data, window=2):
    prov = row["province_code"]
    year = row["year"]
    events = insp_data[insp_data.province_code == prov]["treat_frac_year"].values
    n = sum((events >= year - window) & (events <= year))
    return n

df["n_recent_insp"] = df.apply(lambda r: count_recent_insp(r, insp), axis=1)
df["any_recent_insp"] = (df["n_recent_insp"] > 0).astype(int)
df["first_post"] = (df["year"] >= df["first_treat_year"].fillna(9999)).astype(int)

print("=" * 60)
print("STRATEGY A: Recent-inspection indicator regression")
print("=" * 60)
import statsmodels.api as sm
samp = df[df.vai.notna() & df.year.between(2009, 2020) & df.province_code.notna()].copy()
for ctrl in ["ln_gdppc", "ln_pop", "ind2_share"]:
    if ctrl in samp.columns:
        samp[ctrl] = samp[ctrl].fillna(samp.groupby("city_std")[ctrl].transform("mean"))

# city FE via dummies, year FE via dummies
city_dum = pd.get_dummies(samp["city_std"], prefix="c", drop_first=True).astype(int)
year_dum = pd.get_dummies(samp["year"], prefix="y", drop_first=True).astype(int)

X_cols = ["any_recent_insp"] + [c for c in ["ln_gdppc","ln_pop","ind2_share"] if c in samp.columns]
X = pd.concat([samp[X_cols].astype(float), city_dum, year_dum], axis=1).dropna()
y = samp.loc[X.index, "vai"].astype(float)
# Cluster SE by city
city_group = samp.loc[X.index, "city_std"]
res = sm.OLS(y, sm.add_constant(X)).fit(cov_type="cluster", cov_kwds={"groups": city_group})
print(f"  β(any_recent_insp)  = {res.params['any_recent_insp']:+.4f}  "
      f"SE = {res.bse['any_recent_insp']:.4f}  p = {res.pvalues['any_recent_insp']:.4f}")
print(f"  N = {len(X):,}, 95% CI: [{res.conf_int().loc['any_recent_insp', 0]:+.3f}, "
      f"{res.conf_int().loc['any_recent_insp', 1]:+.3f}]")

# Dose-response: β(n_recent_insp)
X_cols2 = ["n_recent_insp"] + [c for c in ["ln_gdppc","ln_pop","ind2_share"] if c in samp.columns]
X2 = pd.concat([samp[X_cols2].astype(float), city_dum, year_dum], axis=1).dropna()
y2 = samp.loc[X2.index, "vai"].astype(float)
city_group2 = samp.loc[X2.index, "city_std"]
res2 = sm.OLS(y2, sm.add_constant(X2)).fit(cov_type="cluster", cov_kwds={"groups": city_group2})
print(f"  β(n_recent_insp)    = {res2.params['n_recent_insp']:+.4f}  "
      f"SE = {res2.bse['n_recent_insp']:.4f}  p = {res2.pvalues['n_recent_insp']:.4f}")

# Also: first_post indicator
X_cols3 = ["first_post"] + [c for c in ["ln_gdppc","ln_pop","ind2_share"] if c in samp.columns]
X3 = pd.concat([samp[X_cols3].astype(float), city_dum, year_dum], axis=1).dropna()
y3 = samp.loc[X3.index, "vai"].astype(float)
city_group3 = samp.loc[X3.index, "city_std"]
res3 = sm.OLS(y3, sm.add_constant(X3)).fit(cov_type="cluster", cov_kwds={"groups": city_group3})
print(f"  β(first_post)       = {res3.params['first_post']:+.4f}  "
      f"SE = {res3.bse['first_post']:.4f}  p = {res3.pvalues['first_post']:.4f}  "
      f"(includes 2009-2020 window)")

# ============================================================
# STRATEGY C: Sun-Abraham with all 9 cohorts
# ============================================================
print("\n" + "=" * 60)
print("STRATEGY C: Expanded Sun-Abraham with 9 treatment events (1-5 first + 6-9 huitoukan/additional)")
print("=" * 60)

# Each treatment event is a (province, cohort_id) tuple. For event-time analysis,
# use the NEAREST inspection in each (city, year) — i.e., event_time = year - nearest_inspection_year
# where "nearest" prefers post-treatment years (k ≥ 0) if multiple events bracket the year.
def nearest_event(year, events):
    """Return the event with smallest absolute distance to year."""
    if len(events) == 0:
        return np.nan
    diffs = events - year
    idx = np.argmin(np.abs(diffs))
    return events[idx]

# Build per-province event list
events_by_prov = insp.groupby("province_code")["treat_frac_year"].apply(list).to_dict()
df["nearest_event"] = df.apply(
    lambda r: nearest_event(r["year"], np.array(events_by_prov.get(r["province_code"], []))),
    axis=1
)
df["event_time"] = df["year"] - df["nearest_event"]
df["e_bin"] = np.floor(df["event_time"]).clip(-5, 5)

# Per-event cohort: combine (province, round_of_nearest_event) → this creates a
# cohort identifier where the same province has different cohort IDs for different events
def find_round(row):
    prov = row["province_code"]
    nearest = row["nearest_event"]
    if pd.isna(nearest):
        return np.nan
    evs = insp[insp.province_code == prov]
    idx = (evs["treat_frac_year"] - nearest).abs().argmin()
    return evs.iloc[idx]["round"]

df["cohort_nearest"] = df.apply(find_round, axis=1)

# Restrict sample: 2009-2020 window, cohort known
samp = df[df.vai.notna() & df.year.between(2009, 2020) & df.cohort_nearest.notna()].copy()
for ctrl in ["ln_gdppc","ln_pop","ind2_share"]:
    if ctrl in samp.columns:
        samp[ctrl] = samp[ctrl].fillna(samp.groupby("city_std")[ctrl].transform("mean"))

print(f"\nAnalysis sample: {len(samp)} city-years")
print(f"Cohort_nearest distribution: {samp.cohort_nearest.value_counts().sort_index().to_dict()}")
print(f"e_bin distribution: {samp.e_bin.astype(int).value_counts().sort_index().to_dict()}")

# Cohort-specific event-study, then aggregate
from scipy import stats as stx
catt = []
cohorts = sorted(samp.cohort_nearest.dropna().unique().astype(int))
for c in cohorts:
    trt = samp[samp.cohort_nearest == c].copy()
    # Controls: other cohorts' observations where they are NOT yet treated or are far pre
    # Simplified: use other-cohort obs with e_bin <= -2 as pre controls
    ctrl = samp[(samp.cohort_nearest != c) & (samp.e_bin <= -2)].copy()
    # Also concatenate own cohort's pre-period
    work = pd.concat([trt, ctrl], ignore_index=True)

    # Design: event-time dummies for own cohort; control obs have e_bin_eff = nan
    for k in [-3, -2, 0, 1, 2, 3]:
        work[f"k_{k}"] = ((work.cohort_nearest == c) & (work.e_bin == k)).astype(int)

    city_d = pd.get_dummies(work.city_std, prefix="c", drop_first=True).astype(int)
    year_d = pd.get_dummies(work.year, prefix="y", drop_first=True).astype(int)
    kcols = [f"k_{k}" for k in [-3, -2, 0, 1, 2, 3] if work[f"k_{k}"].sum() >= 5]
    if not kcols:
        continue
    ctrl_cols = [c0 for c0 in ["ln_gdppc","ln_pop","ind2_share"] if c0 in work.columns]
    X = pd.concat([work[kcols + ctrl_cols].astype(float), city_d, year_d], axis=1).dropna()
    y = work.loc[X.index, "vai"].astype(float)
    group = work.loc[X.index, "city_std"]
    try:
        r = sm.OLS(y, sm.add_constant(X)).fit(cov_type="cluster", cov_kwds={"groups": group})
        for k in [-3, -2, 0, 1, 2, 3]:
            col = f"k_{k}"
            if col in r.params.index:
                catt.append({"cohort": c, "event_time": k,
                             "beta": r.params[col], "se": r.bse[col],
                             "p": r.pvalues[col],
                             "n_treated": (work.cohort_nearest == c).sum(),
                             "n_control": (work.cohort_nearest != c).sum()})
    except Exception as e:
        print(f"  cohort {c}: failed ({type(e).__name__})")

catt_df = pd.DataFrame(catt)
if len(catt_df) > 0:
    print("\nCATT(c, e) — cohort-specific event-study betas:")
    print(catt_df.pivot(index="event_time", columns="cohort", values="beta").round(3).to_string())

    # Size weights
    cohort_sizes = samp.drop_duplicates("city_std").groupby("cohort_nearest")["city_std"].count()
    cohort_weights = cohort_sizes / cohort_sizes.sum()

    agg = []
    for k in [-3, -2, 0, 1, 2, 3]:
        sub = catt_df[catt_df.event_time == k]
        if len(sub) == 0: continue
        ws = cohort_weights.reindex(sub.cohort).fillna(0).values
        ws = ws / ws.sum() if ws.sum() > 0 else ws
        beta_bar = np.sum(ws * sub.beta.values)
        se_bar = np.sqrt(np.sum((ws * sub.se.values) ** 2))
        z = beta_bar / se_bar if se_bar > 0 else np.nan
        p = 2 * (1 - stx.norm.cdf(abs(z))) if np.isfinite(z) else np.nan
        agg.append({"event_time": k, "beta": beta_bar, "se": se_bar, "p": p})

    agg_df = pd.DataFrame(agg)
    agg_df.loc[len(agg_df)] = {"event_time": -1, "beta": 0, "se": 0, "p": np.nan}
    agg_df = agg_df.sort_values("event_time")
    print("\n=== Expanded Sun-Abraham ATT_bar(e) ===")
    print(agg_df.round(4).to_string(index=False))

    agg_df.to_csv(f"{OUT}/extended_sun_abraham.csv", index=False)
    catt_df.to_csv(f"{OUT}/extended_catt.csv", index=False)

    # Summary at k=0
    if (agg_df.event_time == 0).any():
        b0 = agg_df[agg_df.event_time == 0].iloc[0]
        print(f"\n*** β(k=0) = {b0.beta:+.4f}  SE = {b0.se:.4f}  p = {b0.p:.4f} ***")

    # Figure
    fig, ax = plt.subplots(figsize=(8, 5))
    sa_orig = pd.read_csv(f"{OUT}/sun_abraham_event_study.csv")
    twfe = pd.read_csv(f"{PROJ}/03-analysis/phase-B/event_study_vai.csv")
    ax.errorbar(agg_df.event_time, agg_df.beta,
                yerr=1.96 * agg_df.se, fmt="D-", capsize=4, lw=1.5,
                color="#ff7f0e", ecolor="#ffb366",
                label="Extended SA (9 cohorts, 2013-2017)")
    ax.errorbar(sa_orig.event_time, sa_orig.att_bar,
                yerr=1.96 * sa_orig.se_bar, fmt="o-", capsize=4, lw=1.0,
                color="#2ca02c", ecolor="#60a060", alpha=0.6,
                label="Original SA (5 cohorts, 2013-2014)")
    ax.errorbar(twfe.event_time, twfe.beta,
                yerr=[twfe.beta - twfe.ci_lo, twfe.ci_hi - twfe.beta],
                fmt="s--", capsize=4, lw=1.0,
                color="#1f3a5f", ecolor="#6090b0", alpha=0.5,
                label="TWFE (Phase B baseline)")
    ax.axhline(0, color="grey", lw=0.6, ls="--")
    ax.axvline(-0.5, color="red", lw=0.8, ls=":", alpha=0.7)
    ax.set_xlabel("Event time (years from nearest inspection)")
    ax.set_ylabel("β on VAI (reference k = -1)")
    ax.set_title("Phase B2-extended: Event study with Rounds 1-9 (2013-2017)")
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{FIG}/phase-B2-extended-event-study.pdf")
    fig.savefig(f"{FIG}/phase-B2-extended-event-study.png", dpi=200)
    print(f"Saved: {FIG}/phase-B2-extended-event-study.pdf")

print("\nDone.")
