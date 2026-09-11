# -*- coding: utf-8 -*-
"""Build a fillable lexicon-adjudication sheet for Liu Can (domain expert).
For every visible/functional term: frequency in a 10% systematic sample of procurement titles
(rowid % 10 == 0, ~296k titles) + two example titles, so high-impact terms are reviewed first.
Liu Can fills the `decision` column: keep / ->functional / ->visible / drop / context-gate.
Outputs lexicon_adjudication.csv + lexicon_adjudication.md (preview)."""
import sqlite3, csv, sys
sys.path.insert(0,"/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding")
from bidding_lexicon import VISIBLE, FUNCTIONAL

DB="/Volumes/P1/城市研究/公共资源交易招投标_浙江全量2017-2026/data/ggzy.db"
con=sqlite3.connect(DB); cur=con.cursor()
terms=[(t,"visible") for t in VISIBLE]+[(t,"functional") for t in FUNCTIONAL]
cnt={t:0 for t,_ in terms}; ex={t:[] for t,_ in terms}
N=0
cur.execute("SELECT title FROM announcements WHERE rowid % 10 = 0")
while True:
    batch=cur.fetchmany(100_000)
    if not batch: break
    for (title,) in batch:
        N+=1; t=title or ""
        for term,_ in terms:
            if term in t:
                cnt[term]+=1
                if len(ex[term])<2 and 8<=len(t)<=60: ex[term].append(t)
con.close()

# pre-filled flags for false-positive patterns spotted in the examples (to speed Liu Can's review)
FLAG={"道路":"FP risk: fires on addresses (…大道中路…商铺租赁); consider context-gate to 工程/改造/建设",
      "大道":"FP risk: address component (…大道…号…租赁); context-gate",
      "景观":"FP risk: org name 市容景观发展中心 (e.g. buying insurance); context-gate",
      "市容":"FP risk: org name 市容景观发展中心; context-gate",
      "花园":"FP risk: real-estate compound names (玉兰花园…); consider drop or gate",
      "地标":"FP risk: substring of 基地+标准 (创业基地标准厂房); needs boundary/exclude",
      "立面":"check: 外立面 改造 is genuine facade work — likely keep"}
rows=[]
for term,cls in terms:
    rows.append({"current_class":cls,"term":term,"sample_matches":cnt[term],
                 "est_total":cnt[term]*10,"est_share_pct":round(cnt[term]/N*100,3),
                 "example_1":(ex[term][0] if ex[term] else ""),
                 "example_2":(ex[term][1] if len(ex[term])>1 else ""),
                 "decision (keep / ->functional / ->visible / drop / context-gate)":"","notes":FLAG.get(term,"")})
rows.sort(key=lambda r:(r["current_class"],-r["sample_matches"]))
cols=list(rows[0].keys())
with open("lexicon_adjudication.csv","w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rows)

with open("lexicon_adjudication.md","w",encoding="utf-8") as f:
    f.write(f"# Bidding-lexicon adjudication — for Liu Can (co-first, urban & rural planning)\n\n")
    f.write(f"10% systematic sample of titles (n={N:,}; est_total ≈ sample×10). Fill **decision** per term: "
            f"keep / →functional / →visible / drop / context-gate. Edit `bidding_lexicon.py` accordingly.\n\n")
    for cls in ("visible","functional"):
        f.write(f"\n## current class: {cls}\n\n| term | est. matches | share % | example | decision | notes |\n|---|---:|---:|---|---|---|\n")
        for r in [r for r in rows if r["current_class"]==cls]:
            f.write(f"| {r['term']} | {r['est_total']:,} | {r['est_share_pct']} | {r['example_1'][:34]} |  |  |\n")
print(f"DONE n_sample={N:,}. wrote lexicon_adjudication.csv + .md ({len(rows)} terms)")
