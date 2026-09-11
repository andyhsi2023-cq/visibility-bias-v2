# -*- coding: utf-8 -*-
"""R2 Appendix B.2 — horse races against alternative explanations, recommended measure."""
import numpy as np, pandas as pd
from linearmodels.panel import PanelOLS
import warnings; warnings.filterwarnings("ignore")

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
m = pd.read_csv(f"{PROJ}/02-data/processed/master_2002_2024.csv")
m = m.drop_duplicates(["city4","year"])
m["ln_gdp_pc"], m["ln_pop"] = np.log(m["l_gdp_pc"]), np.log(m["l_pop"])
m["ind2_share"] = m["sec_share"]
m = m.sort_values(["city4","year"])
m["g_gdp"] = m.groupby("city4")["l_gdp"].transform(lambda s: s.diff())

base_ctrl = ["ln_gdp_pc","ln_pop","ind2_share"]
sub = m[(m.cir.notna()) & (m.wr_visibility.notna()) &
        (m[base_ctrl].notna().all(axis=1)) & (m.year.between(2005,2015))].copy()

def run(label, extra=None):
    d = sub.copy()
    if extra:
        d = d[d[extra].notna().all(axis=1)]
    ix = d.set_index(["city4","year"])
    X = ix[["wr_visibility"] + base_ctrl + (extra or [])].copy()
    yd = pd.get_dummies(ix.index.get_level_values("year"), prefix="y", drop_first=True).astype(float); yd.index=ix.index
    X = X.join(yd)
    r = PanelOLS(ix["cir"], X, entity_effects=True, drop_absorbed=True, check_rank=False)\
        .fit(cov_type="clustered", cluster_entity=True)
    b, se, p = r.params["wr_visibility"], r.std_errors["wr_visibility"], r.pvalues["wr_visibility"]
    print(f"{label:44s} b={b:+.4f}  SE={se:.4f}  p={p:.4f}  N={int(r.nobs)}")

run("(0) baseline")
run("(1) + tertiary share (ter_share)", ["ter_share"])
run("(2) + leader tenure (tennu, age_sec)", ["tennu","age_sec"])
run("(3) + GDP growth (g_gdp)", ["g_gdp"])
run("(4) + inspection pressure (cum_all)", ["cum_all"])
run("(5) + all", ["ter_share","tennu","age_sec","g_gdp","cum_all"])
