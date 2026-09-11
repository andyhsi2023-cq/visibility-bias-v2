# -*- coding: utf-8 -*-
"""R2 Table 3 rerun — P1 compositional substitution with the recommended
wr_visibility measure (FACADE 20 / LIZI 16, validated in phase-K).
Data: 02-data/processed/master_2002_2024.csv (CIR coverage 2005-2015)."""
import numpy as np, pandas as pd
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS
import warnings; warnings.filterwarnings("ignore")

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
m = pd.read_csv(f"{PROJ}/02-data/processed/master_2002_2024.csv")
m = m.drop_duplicates(["city4","year"])
m["ln_gdp_pc"], m["ln_pop"] = np.log(m["l_gdp_pc"]), np.log(m["l_pop"])
m["ind2_share"] = m["sec_share"]

sub = m[(m.cir.notna()) & (m.wr_visibility.notna()) & (m.l_gdp_pc.notna()) &
        (m.l_pop.notna()) & (m.ind2_share.notna()) & (m.year.between(2005,2015))].copy()
print(f"estimation sample: {len(sub)} city-years, {sub.city4.nunique()} cities, {sub.year.min()}-{sub.year.max()}")

def panel_fit(y, Xcols, entity=True, time=True, cluster=True):
    ix = sub.set_index(["city4","year"])
    X = ix[Xcols].copy()
    if time:
        yd = pd.get_dummies(ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(float)
        yd.index = ix.index; X = X.join(yd)
    r = PanelOLS(ix[y], X, entity_effects=entity, drop_absorbed=True, check_rank=False)\
        .fit(cov_type="clustered", cluster_entity=cluster)
    return r

ctrl = ["ln_gdp_pc","ln_pop","ind2_share"]
rows = []
def rep(label, r, key, n=None):
    b, se, p = r.params.get(key,np.nan), r.std_errors.get(key,np.nan), r.pvalues.get(key,np.nan)
    nn = int(r.nobs) if n is None else n
    print(f"{label:42s} b={b:+.4f}  SE={se:.4f}  p={p:.4f}  N={nn}")
    rows.append({"spec":label,"beta":round(b,4),"se":round(se,4),"p":round(p,4),"n":nn})

# (1) primary
r = panel_fit("cir", ["wr_visibility"]+ctrl); rep("(1) wr_visibility (primary)", r, "wr_visibility")
# (2) naive comparison
r = panel_fit("cir", ["vai_composite"]+ctrl); rep("(2) vai_composite (naive)", r, "vai_composite")
# (3) no city FE
r = panel_fit("cir", ["wr_visibility"]+ctrl, entity=False); rep("(3) no city FE", r, "wr_visibility")
# (4) no year FE
r = panel_fit("cir", ["wr_visibility"]+ctrl, time=False); rep("(4) no year FE", r, "wr_visibility")

# (5) IV = Wother_wr_visibility (lagged wr_visibility) instrumenting wr_visibility
ivsub = sub[sub.Wother_wr_visibility.notna()].copy()
ix = ivsub.set_index(["city4","year"])
X = ix[ctrl].copy()
yd = pd.get_dummies(ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(float); yd.index=ix.index
X = X.join(yd)
cd = pd.get_dummies(ix.index.get_level_values("city4"), prefix="c", drop_first=True).astype(float); cd.index=ix.index
X = X.join(cd)
endog = ix[["wr_visibility"]].join(X)
ivr = IV2SLS(ix["cir"], X, endog["wr_visibility"], ix["Wother_wr_visibility"]).fit(cov_type="clustered", clusters=ix.index.get_level_values("city4"))
b,se,p = ivr.params["wr_visibility"], ivr.std_errors["wr_visibility"], ivr.pvalues["wr_visibility"]
print(f"(5) IV = wr_visibility(t-1)                        b={b:+.4f}  SE={se:.4f}  p={p:.4f}  N={ivr.nobs}")
rows.append({"spec":"(5) IV = wr_visibility(t-1)","beta":round(b,4),"se":round(se,4),"p":round(p,4),"n":int(ivr.nobs)})
fstat = ivr.first_stage.diagnostics.get('f.stat')
print(f"    first-stage F = {float(fstat.iloc[0]):.1f}")

# (6) null on total investment
r = panel_fit("l_tot", ["wr_visibility"]+ctrl); rep("(6) null: total investment", r, "wr_visibility")

pd.DataFrame(rows).to_csv(f"{PROJ}/03-analysis/phase-M-p1-wr/table3_wr_results.csv", index=False)
print("\nsaved: 03-analysis/phase-M-p1-wr/table3_wr_results.csv")
