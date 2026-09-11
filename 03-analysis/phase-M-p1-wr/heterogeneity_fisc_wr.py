# -*- coding: utf-8 -*-
"""R2 Appendix B.6 rerun — heterogeneity by fiscal capacity, recommended measure."""
import numpy as np, pandas as pd
from linearmodels.panel import PanelOLS
import warnings; warnings.filterwarnings("ignore")

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
m = pd.read_csv(f"{PROJ}/02-data/processed/master_2002_2024.csv").drop_duplicates(["city4","year"])
m["ln_gdp_pc"], m["ln_pop"] = np.log(m["l_gdp_pc"]), np.log(m["l_pop"])
m["ind2_share"] = m["sec_share"]
m["fisc_pc"] = m["l_fisc_exp"] - m["l_pop"]  # ln per-capita fiscal expenditure

ctrl = ["ln_gdp_pc","ln_pop","ind2_share"]
sub = m[(m.cir.notna()) & (m.wr_visibility.notna()) & (m.fisc_pc.notna()) &
        (m[ctrl].notna().all(axis=1)) & (m.year.between(2005,2015))].copy()
med = sub["fisc_pc"].median()
sub["above"] = (sub["fisc_pc"] > med).astype(float)

def run(d, extra=None, label=""):
    ix = d.set_index(["city4","year"])
    cols = ["wr_visibility"] + ctrl + (extra or [])
    X = ix[cols].copy()
    yd = pd.get_dummies(ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(float); yd.index=ix.index
    X = X.join(yd)
    r = PanelOLS(ix["cir"], X, entity_effects=True, drop_absorbed=True, check_rank=False)\
        .fit(cov_type="clustered", cluster_entity=True)
    b, se, p = r.params["wr_visibility"], r.std_errors["wr_visibility"], r.pvalues["wr_visibility"]
    print(f"{label:40s} b={b:+.4f}  SE={se:.4f}  p={p:.4f}  N={int(r.nobs)}")

print(f"median fisc_pc = {med:.3f}")
run(sub[sub.above==1], label="above-median fiscal capacity")
run(sub[sub.above==0], label="below-median fiscal capacity")
run(sub, extra=["above"], label="interaction (above x VAI)")
