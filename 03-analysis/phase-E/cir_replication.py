"""
Phase E Part 2 — replicate CIR ~ VAI with independently-constructed VAI_ext.

OSF H4 (partial): a VAI built from an independent keyword set should predict
CIR with β > 0 at the 5% level in the same direction as the primary VAI.

We already established r(VAI_primary, VAI_ext) = 0.93. This test asks the
stronger question: does the signal in the independent dictionary, AFTER
controlling for the same covariates, give the same sign and comparable
magnitude of the VAI→CIR link?
"""
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
import warnings; warnings.filterwarnings("ignore")

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
# Use yearbook panel — it has CIR for 2005-2015 (N=2762 after controls)
# Main panel only has CIR for 2015 (N=13)
PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/yearbook_vai_panel.csv"
EXT = f"{PROJ}/03-analysis/phase-E/vai_orig_vs_ext.csv"

panel = pd.read_csv(PANEL).rename(columns={"industry_share": "ind2_share"})
ext = pd.read_csv(EXT, usecols=["city_std", "year", "vai_orig", "vai_ext"])

# Deduplicate ext (in case same city-year appears multiple times)
ext = ext.drop_duplicates(["city_std", "year"])
panel = panel.drop_duplicates(["city_std", "year"])

# Merge
m = panel.merge(ext, on=["city_std", "year"], how="inner")
print(f"Merged sample: {len(m)} city-years (unique city-years: {m.drop_duplicates(['city_std','year']).shape[0]})")

# Primary regression: CIR ~ VAI_v1 + controls + city FE + year FE
m = m.dropna(subset=["cir", "vai", "vai_ext", "ln_gdppc", "ln_pop", "ind2_share"]).drop_duplicates(["city_std","year"])
m_ix = m.set_index(["city_std", "year"])

controls = ["ln_gdppc", "ln_pop", "ind2_share"]

year_dummies = pd.get_dummies(m_ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(int)
year_dummies.index = m_ix.index

def run(vai_col, label):
    X = m_ix[[vai_col] + controls].join(year_dummies)
    y = m_ix["cir"].astype(float)
    mod = PanelOLS(y, X, entity_effects=True, drop_absorbed=True, check_rank=False)
    r = mod.fit(cov_type="clustered", cluster_entity=True)
    b = r.params.get(vai_col, np.nan)
    se = r.std_errors.get(vai_col, np.nan)
    p = r.pvalues.get(vai_col, np.nan)
    ci = r.conf_int().loc[vai_col]
    n = int(r.nobs)
    print(f"  {label:30s} β={b:+.4f}  SE={se:.4f}  p={p:.4f}  "
          f"95% CI=[{ci.iloc[0]:+.3f}, {ci.iloc[1]:+.3f}]  N={n:,}")
    return b, se, p

print("\nCIR ~ VAI + controls, city + year FE, clustered by city")
b1, se1, p1 = run("vai", "Primary VAI (v1)")
b2, se2, p2 = run("vai_orig", "Reconstructed V_ORIG (this session)")
b3, se3, p3 = run("vai_ext", "Expanded independent VAI_ext")

# Horse race: include both
print("\nHorse race: CIR ~ VAI_primary + VAI_ext_residual")
# Residualize VAI_ext against VAI_primary to isolate the independent component
m["vai_ext_resid"] = m.vai_ext - m.vai * (m[["vai", "vai_ext"]].cov().iloc[0, 1] / m["vai"].var())
m_ix = m.set_index(["city_std", "year"])
year_dummies2 = pd.get_dummies(m_ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(int)
year_dummies2.index = m_ix.index
X = m_ix[["vai", "vai_ext_resid"] + controls].join(year_dummies2)
y = m_ix["cir"].astype(float)
mod = PanelOLS(y, X, entity_effects=True, drop_absorbed=True, check_rank=False)
r = mod.fit(cov_type="clustered", cluster_entity=True)
for name in ["vai", "vai_ext_resid"]:
    b = r.params.get(name)
    p = r.pvalues.get(name)
    print(f"  {name:20s} β={b:+.4f}  p={p:.4f}")

out = pd.DataFrame({
    "model": ["Primary v1", "V_ORIG reconstructed", "V_EXT independent"],
    "beta": [b1, b2, b3], "se": [se1, se2, se3], "p": [p1, p2, p3],
})
out.to_csv(f"{PROJ}/03-analysis/phase-E/cir_replication.csv", index=False)
print(f"\nSaved: {PROJ}/03-analysis/phase-E/cir_replication.csv")
