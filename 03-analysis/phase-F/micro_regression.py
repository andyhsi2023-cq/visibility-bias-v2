"""
Phase F micro-foundation analysis (OSF H5, with data-availability deviation).

Pre-registered H5 called for dual-outcome test: amenity-category-specific satisfaction
(visible: parks/roads vs functional: water/heating). Public CFPS cleaned panel
(2010-2022) does not contain amenity-category items.

Deviation (documented in §Deviation log below): we substitute a three-outcome
visibility-bias signature test that is tighter to the model's mechanism:
  Y1 = qn1101  (对本县市政府评价, 1-5) — perception outcome
  Y2 = qn12012 (对自己生活满意度, 1-5) — direct welfare outcome
  Y3 = health  (1-5, recoded)            — functional welfare outcome

Visibility-bias prediction:
  β(VAI → Y1) > 0   (visible investments buy political approval)
  β(VAI → Y2) ≈ 0   (no net welfare gain)
  β(VAI → Y3) ≤ 0   (crowd-out of functional investments should weakly hurt health)

Identifying signature: β1 > β2 with statistically distinguishable difference.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from linearmodels.panel import PanelOLS
import warnings
warnings.filterwarnings("ignore")

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
CFPS_DTA = "/Volumes/P1/城市研究/CFPS2010-2022清洗好数据/2010-2022cfps非平衡面板数据(stata_推荐使用）.dta"
V1_CFPS = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/cfps_vai_panel.csv"
OUT_DIR = f"{PROJ}/03-analysis/phase-F"
FIG_DIR = f"{PROJ}/04-figures"

# ============================================================
# 1. Load full CFPS (204 cols) + existing city_std mapping
# ============================================================
print("Loading CFPS 204-col panel ...")
cfps = pd.read_stata(CFPS_DTA, convert_categoricals=False)
print(f"  CFPS shape: {cfps.shape}")

print("Loading v1 city_std mapping ...")
vm = pd.read_csv(V1_CFPS, usecols=["pid", "year", "city_std", "vai", "v_count", "f_count",
                                    "income_p", "人均GDP", "城镇化水平", "female",
                                    "urban_dummy", "edu_ord"])
print(f"  v1 cfps_vai_panel shape: {vm.shape}")

# Merge on pid+year; many-to-one
cfps["pid"] = cfps["pid"].astype(float)
merged = cfps.merge(vm[["pid", "year", "city_std", "vai", "v_count", "f_count"]],
                    on=["pid", "year"], how="inner")
print(f"  After merge shape: {merged.shape}")

# Drop implausible survey codes
for c in ["qn1101", "qn12012", "health"]:
    merged[c] = merged[c].where((merged[c] >= 1) & (merged[c] <= 5))

print(f"  Non-null counts post-clean: "
      f"qn1101={merged['qn1101'].notna().sum()}, "
      f"qn12012={merged['qn12012'].notna().sum()}, "
      f"health={merged['health'].notna().sum()}, "
      f"vai={merged['vai'].notna().sum()}")

# ============================================================
# 2. Build city-year panel (collapse to city-year means)
# ============================================================
# Decision: run *individual-level* regressions clustered by city_std, with
# city+year FE via PanelOLS. VAI varies at city-year only; treat city as
# panel entity, year as time, and use demeaning on individual covariates.
# But individuals rotate — can't use PanelOLS with (pid, year) directly since
# entity is city, not pid.

# Implementation: rename to use (city_std, year) as multi-index with row index
merged = merged.dropna(subset=["city_std", "vai"])
merged["row_id"] = np.arange(len(merged))

# Controls (individual-level)
merged["ln_income_p"] = np.log1p(merged["income_p"].clip(lower=0))
merged["female"] = (merged["gender"].astype(float) == 0).astype(int) if "gender" in merged.columns else np.nan
merged["age"] = merged["age"].astype(float)
merged["age2"] = merged["age"] ** 2
merged["edu_yr"] = merged["eduy"].astype(float) if "eduy" in merged.columns else np.nan

indiv_controls = ["ln_income_p", "age", "age2", "edu_yr"]

# Standardize VAI for effect-size interpretation
merged["vai_z"] = (merged["vai"] - merged["vai"].mean()) / merged["vai"].std()

# ============================================================
# 3. Individual-level regression with city + year FE
# ============================================================
def run_reg(outcome, label):
    """OLS with city+year FE via PanelOLS; city = entity."""
    cols = [outcome, "vai_z", "city_std", "year"] + indiv_controls
    d = merged[cols].dropna().copy()
    # Need unique (entity, time) for PanelOLS? PanelOLS entity_effects works with
    # repeated obs in same entity-time; but index must be unique. Use a synthetic key.
    d["unit"] = d["city_std"].astype(str) + "_" + np.arange(len(d)).astype(str)
    d = d.set_index(["city_std", "year"])
    # Since same city-year has many individuals, index repeats — OK for PanelOLS
    # with entity_effects but we need .set_index with unique — use row_id.
    d = d.reset_index()
    d["row"] = np.arange(len(d))
    d = d.set_index(["city_std", "row"])  # city as entity, row as "time"
    # But we want year FE too. Add year dummies manually.
    year_dummies = pd.get_dummies(d["year"], prefix="y", drop_first=True).astype(int)
    X_base = d[["vai_z"] + indiv_controls].join(year_dummies)
    y = d[outcome].astype(float)
    mod = PanelOLS(y, X_base, entity_effects=True, drop_absorbed=True, check_rank=False)
    res = mod.fit(cov_type="clustered", cluster_entity=True)
    beta = res.params.get("vai_z", np.nan)
    se = res.std_errors.get("vai_z", np.nan)
    p = res.pvalues.get("vai_z", np.nan)
    ci = res.conf_int().loc["vai_z"] if "vai_z" in res.conf_int().index else [np.nan, np.nan]
    n = int(res.nobs)
    # Cohen's d-ish: β × 1 SD of VAI / SD of outcome
    y_sd = y.std()
    cohen_d = beta / y_sd if y_sd > 0 else np.nan
    print(f"  {label:30s} β={beta:+.4f}  SE={se:.4f}  p={p:.4f}  n={n:,}  d={cohen_d:+.3f}")
    return {"outcome": outcome, "label": label, "beta": beta, "se": se, "p": p,
            "ci_lo": ci[0] if len(ci) > 0 else np.nan,
            "ci_hi": ci[1] if len(ci) > 1 else np.nan,
            "n": n, "cohen_d": cohen_d, "y_sd": y_sd}


print("\n=== Phase F main regressions (individual-level, city+year FE, clustered by city) ===")
print(f"{'Outcome':30s}  {'β(VAI_z)':10s}  SE      p       N          d")
results = []
for outcome, label in [
    ("qn1101", "County govt eval (1-5)"),
    ("qn12012", "Life satisfaction (1-5)"),
    ("health", "Self-rated health (1-5)"),
]:
    res = run_reg(outcome, label)
    results.append(res)

df_res = pd.DataFrame(results)
df_res.to_csv(f"{OUT_DIR}/micro_main.csv", index=False)

# ============================================================
# 4. Differential test: β(qn1101) ≠ β(qn12012)?
# ============================================================
# Bootstrap over city_std clusters to get variance of difference
print("\n=== Bootstrap test: β(govt eval) - β(life sat) ===")
np.random.seed(20260414)
B = 300
diffs = []
cities = merged["city_std"].dropna().unique()

# Pre-extract required columns for speed
def reg_beta(sub, outcome):
    sub2 = sub[[outcome, "vai_z", "city_std", "year"] + indiv_controls].dropna().copy()
    if len(sub2) < 500 or sub2["city_std"].nunique() < 10:
        return np.nan
    sub2["row"] = np.arange(len(sub2))
    sub2 = sub2.set_index(["city_std", "row"])
    year_dummies = pd.get_dummies(sub2["year"], prefix="y", drop_first=True).astype(int)
    X = sub2[["vai_z"] + indiv_controls].join(year_dummies)
    y = sub2[outcome].astype(float)
    try:
        mod = PanelOLS(y, X, entity_effects=True, drop_absorbed=True, check_rank=False)
        r = mod.fit()
        return r.params.get("vai_z", np.nan)
    except Exception:
        return np.nan


for b in range(B):
    # Block bootstrap over city clusters
    sel = np.random.choice(cities, size=len(cities), replace=True)
    parts = []
    for c in sel:
        parts.append(merged[merged["city_std"] == c])
    boot = pd.concat(parts, ignore_index=True)
    b1 = reg_beta(boot, "qn1101")
    b2 = reg_beta(boot, "qn12012")
    if np.isfinite(b1) and np.isfinite(b2):
        diffs.append(b1 - b2)
    if (b + 1) % 50 == 0:
        print(f"  bootstrap {b+1}/{B} done ({len(diffs)} finite)")

diffs = np.array(diffs)
obs_diff = df_res.loc[df_res.outcome == "qn1101", "beta"].values[0] - \
           df_res.loc[df_res.outcome == "qn12012", "beta"].values[0]
print(f"\nObserved β(govt) - β(life) = {obs_diff:+.4f}")
print(f"Bootstrap SE of difference: {diffs.std():.4f}")
print(f"95% bootstrap CI: [{np.percentile(diffs, 2.5):+.4f}, {np.percentile(diffs, 97.5):+.4f}]")
print(f"Bootstrap p (|diff| ≥ 0 test): "
      f"p = {2 * min(np.mean(diffs >= 0), np.mean(diffs <= 0)):.4f}")

# Save bootstrap
pd.DataFrame({"diff": diffs}).to_csv(f"{OUT_DIR}/diff_bootstrap.csv", index=False)

# ============================================================
# 5. Figure
# ============================================================
fig, ax = plt.subplots(figsize=(6.5, 4.0))
labels = [r["label"] for r in results]
betas = [r["beta"] for r in results]
ses = [r["se"] for r in results]
colors = ["#d62728", "#ff7f0e", "#1f77b4"]
y_pos = np.arange(len(labels))
ax.errorbar(betas, y_pos, xerr=[1.96 * s for s in ses], fmt="o", capsize=5,
            color="black", ecolor="grey", lw=1.5, markersize=7)
for i, (b, c) in enumerate(zip(betas, colors)):
    ax.scatter(b, i, color=c, s=80, zorder=5)
ax.axvline(0, color="grey", lw=0.6, ls="--")
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel("β on standardized VAI (individual-level, city+year FE)")
ax.set_title("Phase F: Visibility bias signature in CFPS 2010–2022")
ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis="x")
fig.tight_layout()
fig.savefig(f"{FIG_DIR}/phase-F-micro.pdf")
fig.savefig(f"{FIG_DIR}/phase-F-micro.png", dpi=200)
print(f"\nSaved: {FIG_DIR}/phase-F-micro.pdf / .png")
print(f"Saved: {OUT_DIR}/micro_main.csv")
print(f"Saved: {OUT_DIR}/diff_bootstrap.csv")
