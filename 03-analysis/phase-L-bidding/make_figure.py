# -*- coding: utf-8 -*-
"""Supplementary figure for §4.3: Zhejiang procurement visible:functional ratio across localities.
Panel A = distribution over all 109 localities (median + parity lines); Panel B = top localities by
volume. Reads by_city.csv. Outputs fig_bidding_by_city.{pdf,png}."""
import csv, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

rows=[r for r in csv.DictReader(open("by_city.csv")) if r["vf_ratio"]!="None"]
ratios=np.array([float(r["vf_ratio"]) for r in rows])
n=len(ratios); n_gt1=int((ratios>1).sum()); med=float(np.median(ratios))

PINYIN={'省本级':'Provincial','杭州市':'Hangzhou','义乌市':'Yiwu','宁波市':'Ningbo','台州市':'Taizhou',
'绍兴市':'Shaoxing','嘉兴市':'Jiaxing','安吉县':'Anji','龙湾区':'Longwan','柯桥区':'Keqiao',
'余杭区':'Yuhang','上虞区':'Shangyu','长兴县':'Changxing','衢州市':'Quzhou','鄞州区':'Yinzhou'}
byvol=sorted(rows,key=lambda r:-int(r["vf_total"]))
top=[r for r in byvol if r["city"] in PINYIN][:15]

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(11,4.3))

# Panel A: distribution (log-x histogram)
bins=np.logspace(np.log10(max(ratios.min(),0.4)),np.log10(ratios.max()*1.05),22)
ax1.hist(ratios,bins=bins,color="#4878a8",edgecolor="white",linewidth=.6)
ax1.set_xscale("log")
ax1.axvline(1.0,color="#c0392b",ls="--",lw=1.6,label="parity (1:1)")
ax1.axvline(med,color="#27ae60",ls="-",lw=1.8,label=f"median = {med:.1f}")
ax1.set_xlabel("visible : functional project-count ratio (log scale)")
ax1.set_ylabel("number of localities")
ax1.set_title("(A) Distribution across 109 Zhejiang localities",fontsize=11)
ax1.legend(frameon=False,fontsize=9,loc="upper right")
ax1.text(0.97,0.62,f"{n_gt1} of {n} localities:\nvisible > functional",transform=ax1.transAxes,
         ha="right",va="top",fontsize=9.5,color="#1a5276",
         bbox=dict(boxstyle="round,pad=0.4",fc="#eaf2f8",ec="#aac"))
ax1.set_xticks([0.5,1,2,3,5,10,20]); ax1.set_xticklabels([0.5,1,2,3,5,10,20])

# Panel B: top localities by volume
names=[PINYIN[r["city"]] for r in top][::-1]
vals=[float(r["vf_ratio"]) for r in top][::-1]
cols=["#27ae60" if v>1 else "#c0392b" for v in vals]
y=np.arange(len(names))
ax2.barh(y,vals,color=cols,edgecolor="white")
ax2.set_yticks(y); ax2.set_yticklabels(names,fontsize=9)
ax2.axvline(1.0,color="#c0392b",ls="--",lw=1.4)
ax2.set_xscale("log"); ax2.set_xlabel("visible : functional ratio (log scale)")
ax2.set_title("(B) Top 15 localities by procurement volume",fontsize=11)
ax2.set_xticks([1,2,3,5,8]); ax2.set_xticklabels([1,2,3,5,8])
for yi,v in zip(y,vals): ax2.text(v*1.04,yi,f"{v:.1f}",va="center",fontsize=8,color="#333")

fig.suptitle("Zhejiang public procurement (2.96M records, 2019–2026): visible-type construction projects predominate",
             fontsize=11.5,y=1.0)
fig.tight_layout(rect=[0,0,1,0.96])
for ext in ("pdf","png"):
    fig.savefig(f"fig_bidding_by_city.{ext}",dpi=200,bbox_inches="tight")
print(f"wrote fig_bidding_by_city.pdf/.png | n={n}, {n_gt1}/{n}>1, median={med:.2f}")
