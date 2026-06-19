"""
Phase E2-2: compute VAI_3rd from Wikipedia-zh city articles (third-party text)
and test H4 pre-registered correlation + CIR replication.

Because Wikipedia articles describe city CHARACTERISTICS (not year-specific),
we test at the CROSS-SECTIONAL level: does mean city-level VAI_primary
(averaged across 2002-2024 GWRs) correlate with VAI_wikipedia?

Pre-registered H4: r(VAI_primary, VAI_3rd) ∈ [0.3, 0.7]; β(VAI_3rd → CIR) > 0.
"""
import os, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings; warnings.filterwarnings("ignore")

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
WIKI_DIR = f"{PROJ}/02-data/raw/wikipedia_zh"
PRIMARY = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
YEARBOOK = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/yearbook_vai_panel.csv"
OUT = f"{PROJ}/03-analysis/phase-E2"
FIG = f"{PROJ}/04-figures"

# Import V_ORIG / F_ORIG dictionaries from Phase E
exec(open(f"{PROJ}/03-analysis/phase-E/construct_validity.py").read().split("# ============================================================\n# Load all GWR texts")[0])
# Now V_ORIG, F_ORIG, V_EXT, F_EXT defined

def count_hits(text, terms):
    return sum(text.count(t) for t in terms)

# Load Wikipedia articles
wiki_files = glob.glob(f"{WIKI_DIR}/*.txt")
print(f"Wikipedia corpus: {len(wiki_files)} files")

rows = []
for f in wiki_files:
    city = os.path.basename(f).replace(".txt", "")
    with open(f) as fh:
        text = fh.read()
    if len(text) < 500:
        continue
    v = count_hits(text, V_ORIG)
    fn = count_hits(text, F_ORIG)
    v_ext = count_hits(text, V_EXT)
    f_ext_hits = count_hits(text, F_EXT)
    rows.append({
        "city_std": city, "text_len": len(text),
        "v_count_wiki": v, "f_count_wiki": fn,
        "v_ext_wiki": v_ext, "f_ext_wiki": f_ext_hits,
        "vai_wiki": v / (v + fn) if (v + fn) >= 3 else np.nan,
        "vai_wiki_ext": v_ext / (v_ext + f_ext_hits) if (v_ext + f_ext_hits) >= 3 else np.nan,
    })
wiki = pd.DataFrame(rows)
print(f"Wikipedia VAI built: {len(wiki)} cities, mean vai_wiki = {wiki.vai_wiki.mean():.3f}")

# City-level mean VAI from primary GWR panel
prim = pd.read_csv(PRIMARY)
city_means = prim.groupby("city_std").agg(
    vai_primary_mean=("vai", "mean"),
    vai_primary_sd=("vai", "std"),
    n_years=("year", "count"),
    cir_mean=("cir", "mean"),
    ln_gdppc_mean=("ln_gdppc", "mean"),
    ln_pop_mean=("ln_pop", "mean"),
    ind2_share_mean=("ind2_share", "mean"),
).reset_index()

# Merge
m = wiki.merge(city_means, on="city_std", how="inner")
m = m.dropna(subset=["vai_wiki", "vai_primary_mean"])
print(f"\nMatched Wiki × Primary: {len(m)} cities")
print(f"VAI_wiki descr: mean={m.vai_wiki.mean():.3f}, SD={m.vai_wiki.std():.3f}")
print(f"VAI_primary city-mean descr: mean={m.vai_primary_mean.mean():.3f}, "
      f"SD={m.vai_primary_mean.std():.3f}")

# =====================================================================
# H4 Test 1: correlation
# =====================================================================
print("\n=== H4 Test 1: cross-sectional correlation (city-level) ===")
r_pearson = m[["vai_wiki", "vai_primary_mean"]].corr().iloc[0, 1]
r_spearman = m[["vai_wiki", "vai_primary_mean"]].corr(method="spearman").iloc[0, 1]
r_ext = m[["vai_wiki_ext", "vai_primary_mean"]].corr().iloc[0, 1]
print(f"  Pearson  r(VAI_wiki_orig, VAI_primary_mean) = {r_pearson:.4f}")
print(f"  Spearman ρ(VAI_wiki_orig, VAI_primary_mean) = {r_spearman:.4f}")
print(f"  Pearson  r(VAI_wiki_ext,  VAI_primary_mean) = {r_ext:.4f}")

from scipy import stats as st
# 95% CI for Pearson r via Fisher z
def ci_r(r, n):
    z = 0.5 * np.log((1 + r) / (1 - r))
    se = 1 / np.sqrt(n - 3)
    zlo, zhi = z - 1.96 * se, z + 1.96 * se
    return np.tanh(zlo), np.tanh(zhi)

ci_lo, ci_hi = ci_r(r_pearson, len(m))
print(f"  95% CI for Pearson r: [{ci_lo:.3f}, {ci_hi:.3f}]")
in_band = 0.3 <= r_pearson <= 0.7
print(f"  Pre-registered band [0.3, 0.7]: {'✓ IN BAND' if in_band else '✗ OUT OF BAND'}")

# =====================================================================
# H4 Test 2: CIR replication with city-level panel using VAI_wiki
# =====================================================================
# Since VAI_wiki is city-level (no year variation), we test the cross-sectional
# CIR ~ VAI_wiki regression (city-mean CIR ~ VAI_wiki + controls)
print("\n=== H4 Test 2: CIR ~ VAI_wiki (cross-section, city-level) ===")
m_cir = m.dropna(subset=["cir_mean", "vai_wiki", "ln_gdppc_mean",
                          "ln_pop_mean", "ind2_share_mean"])
X = m_cir[["vai_wiki", "ln_gdppc_mean", "ln_pop_mean", "ind2_share_mean"]]
X = X.assign(const=1).astype(float)
y = m_cir["cir_mean"].astype(float)

# OLS with heteroskedasticity-robust SE
import statsmodels.api as sm
res = sm.OLS(y, X).fit(cov_type="HC3")
print(f"  β(vai_wiki)    = {res.params['vai_wiki']:+.4f}  "
      f"SE = {res.bse['vai_wiki']:.4f}  p = {res.pvalues['vai_wiki']:.4f}")
print(f"  β(ln_gdppc)    = {res.params['ln_gdppc_mean']:+.4f}")
print(f"  β(ln_pop)      = {res.params['ln_pop_mean']:+.4f}")
print(f"  N = {len(m_cir)}, R² = {res.rsquared:.3f}")

# Horse race: include both VAI_wiki and VAI_primary city-mean
print("\n=== Horse race: CIR ~ VAI_primary + VAI_wiki_residual ===")
# Residualize VAI_wiki against VAI_primary_mean
m_cir["vai_wiki_resid"] = m_cir.vai_wiki - m_cir.vai_primary_mean * \
    (m_cir[["vai_primary_mean", "vai_wiki"]].cov().iloc[0, 1] / m_cir.vai_primary_mean.var())
X = m_cir[["vai_primary_mean", "vai_wiki_resid", "ln_gdppc_mean",
           "ln_pop_mean", "ind2_share_mean"]].assign(const=1).astype(float)
res2 = sm.OLS(m_cir["cir_mean"].astype(float), X).fit(cov_type="HC3")
print(f"  β(vai_primary_mean)    = {res2.params['vai_primary_mean']:+.4f}  "
      f"p = {res2.pvalues['vai_primary_mean']:.4f}")
print(f"  β(vai_wiki_residual)   = {res2.params['vai_wiki_resid']:+.4f}  "
      f"p = {res2.pvalues['vai_wiki_resid']:.4f}")

# Save
summary = pd.DataFrame([
    {"test": "H4 cross-sectional correlation", "value": r_pearson,
     "pre_reg_target": "[0.3, 0.7]",
     "met": in_band},
    {"test": "H4 CIR~VAI_wiki cross-section", "value": res.params["vai_wiki"],
     "pre_reg_target": ">0, p<0.05",
     "met": (res.params["vai_wiki"] > 0) & (res.pvalues["vai_wiki"] < 0.05)},
])
summary.to_csv(f"{OUT}/h4_summary.csv", index=False)
m.to_csv(f"{OUT}/vai_wiki_primary_merge.csv", index=False)

# =====================================================================
# Figure
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
ax.scatter(m.vai_primary_mean, m.vai_wiki, s=20, alpha=0.5, color="#1f3a5f")
ax.plot([0, 1], [0, 1], "k--", lw=0.5)
lim = (0.25, 0.85)
ax.set_xlim(*lim); ax.set_ylim(*lim)
ax.set_xlabel("VAI (primary, GWR text, city-mean across 2002-2024)")
ax.set_ylabel("VAI (Wikipedia-zh third-party)")
ax.set_title(f"Cross-sectional third-party validation\nPearson r = {r_pearson:.3f} "
             f"[95% CI {ci_lo:.2f}, {ci_hi:.2f}]")
ax.grid(True, alpha=0.3)
# Shade pre-registered band
ax.text(0.28, 0.80, f"Pre-reg target: r ∈ [0.3, 0.7]\n"
        f"{'✓ met' if in_band else '✗ out of band'}",
        fontsize=9, verticalalignment="top",
        bbox=dict(facecolor="lightyellow", alpha=0.8, edgecolor="grey"))

ax = axes[1]
# Binned scatter CIR vs VAI_wiki
if len(m_cir) > 0:
    ax.scatter(m_cir.vai_wiki, m_cir.cir_mean, s=20, alpha=0.5, color="#d62728")
    # Add fitted line
    xx = np.linspace(m_cir.vai_wiki.min(), m_cir.vai_wiki.max(), 50)
    yy = (res.params["const"] + res.params["vai_wiki"] * xx +
          res.params["ln_gdppc_mean"] * m_cir.ln_gdppc_mean.mean() +
          res.params["ln_pop_mean"] * m_cir.ln_pop_mean.mean() +
          res.params["ind2_share_mean"] * m_cir.ind2_share_mean.mean())
    ax.plot(xx, yy, "b--", lw=1.5, label=f"β = {res.params['vai_wiki']:+.3f}, "
            f"p = {res.pvalues['vai_wiki']:.3f}")
    ax.set_xlabel("VAI (Wikipedia-zh third-party)")
    ax.set_ylabel("CIR (MOHURD yearbook, city-mean)")
    ax.set_title(f"CIR prediction with third-party VAI (N = {len(m_cir)})")
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(f"{FIG}/phase-E2-thirdparty-validation.pdf")
fig.savefig(f"{FIG}/phase-E2-thirdparty-validation.png", dpi=200)

print(f"\nSaved: {OUT}/vai_wiki_primary_merge.csv")
print(f"Saved: {FIG}/phase-E2-thirdparty-validation.pdf")
