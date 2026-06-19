# -*- coding: utf-8 -*-
"""R2 main-text figures: (1) the lexicon precision ladder + polysemy ceiling + LLM; (2) the
behavioral co-movement (criterion validity). All numbers from verified sources
(phase-K passage validation; phase-J verify_results_master.csv)."""
import csv
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT="/Users/andy/Desktop/Research/visibility-bias-v2/04-figures"

# ---------- Fig 1: precision ladder ----------
labels=["Naive\ndictionary","Concrete\n(Wu–Zhou)","Concrete\nrefined","+ above-ground\nlandmarks","LLM\nensemble"]
prec=[0.10,0.50,0.60,0.64,0.84]
cols=["#c0392b","#e08e0b","#2e86c1","#2e86c1","#27ae60"]
fig,ax=plt.subplots(figsize=(7,4.3))
bars=ax.bar(range(5),prec,color=cols,edgecolor="white",width=0.66)
ax.axhspan(0.60,0.64,color="#5dade2",alpha=0.18)
ax.text(2.5,0.665,"dictionary polysemy ceiling ≈ 0.60–0.64",ha="center",fontsize=8.5,color="#1a5276")
ax.axhline(0.75,ls=":",color="#888",lw=1.2); ax.text(4.4,0.765,"pre-registered 0.75 bar",ha="right",fontsize=8,color="#666")
for i,v in enumerate(prec): ax.text(i,v+0.015,f"{v:.2f}",ha="center",fontsize=10,fontweight="bold")
ax.set_xticks(range(5)); ax.set_xticklabels(labels,fontsize=9)
ax.set_ylabel("visible-class precision (vs human gold, n=120)"); ax.set_ylim(0,0.95)
ax.set_title("Lexicon precision ladder: curation hits a polysemy ceiling; LLM ensemble clears it",fontsize=10.5)
ax.text(0,0.16,"recall 0.43",ha="center",fontsize=7.5,color="#777"); ax.text(1,0.56,"recall 0.79",ha="center",fontsize=7.5,color="#777")
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout()
for e in ("pdf","png"): fig.savefig(f"{OUT}/fig1_precision_ladder.{e}",dpi=200,bbox_inches="tight")
print("wrote fig1_precision_ladder")

# ---------- Fig 2: behavioral co-movement ----------
rows=list(csv.DictReader(open("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-J-criterion-validity/verify_results_master.csv")))
M={"CIR(real invest)":"Real cosmetic\ninvestment (CIR)","wr_visibility(concrete)":"Concrete / valid\ntext measure","vai_composite(naive)":"Naive\ntext measure"}
order=list(M)
def get(out,reg):
    r=next(x for x in rows if x["outcome"]==out and x["regressor"]==reg); return float(r["beta"]),float(r["se"]),float(r["p"])
fig,ax=plt.subplots(figsize=(7,4.0))
y=np.arange(len(order))[::-1]
for i,out in enumerate(order):
    yy=y[i]
    b,se,p=get(out,"turnover L1");
    c="#27ae60" if p<0.05 else "#c0392b"
    ax.errorbar(b,yy+0.13,xerr=1.96*se,fmt="o",color=c,capsize=4,ms=7,label="turnover (t−1)" if i==0 else "")
    ax.text(b,yy+0.30,f"{b:+.3f}{'*' if p<0.05 else ' n.s.'}",ha="center",fontsize=8.5,color=c)
    bl,sel,pl=get(out,"turnover LEAD")
    ax.errorbar(bl,yy-0.13,xerr=1.96*sel,fmt="s",color="#888",mfc="white",capsize=4,ms=6,label="future turnover (pre-trend placebo)" if i==0 else "")
ax.axvline(0,color="#333",lw=1)
ax.set_yticks(y); ax.set_yticklabels([M[o] for o in order],fontsize=9.5)
ax.set_xlabel("effect on outcome (two-way FE, city-clustered 95% CI)")
ax.set_title("Behavioral criterion validity: the valid measure co-moves with real investment;\nthe naive measure does not (clean pre-trends)",fontsize=10.5)
ax.legend(frameon=False,fontsize=8.5,loc="lower right")
ax.spines[["top","right"]].set_visible(False); ax.set_ylim(-0.6,2.6)
fig.tight_layout()
for e in ("pdf","png"): fig.savefig(f"{OUT}/fig2_comovement.{e}",dpi=200,bbox_inches="tight")
print("wrote fig2_comovement")
