# -*- coding: utf-8 -*-
"""Structured processing of Zhejiang procurement along Andy's 3 dimensions:
 (1) title + administrative region (county -> prefecture via area.json),
 (2) construction content (visible/functional class) + scale (parsed from title),
 (3) investment amount -- NOT in the index (detail_status=0 for all 2.96M); column left null,
     to be filled only by a detail-page crawl (ggzy.py cmd_details/cmd_extract) or a commercial source.
Outputs structured_projects.csv (visible+functional rows) + by_prefecture.csv.
"""
import sqlite3, json, csv, re, sys
sys.path.insert(0,"/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding")
from bidding_lexicon import classify

D="/Volumes/P1/城市研究/公共资源交易招投标_浙江全量2017-2026"
area=json.load(open(f"{D}/data/area.json",encoding="utf-8"))
ZJ=area.get("330000",[])
code_of={e["name"]:e["id"] for e in ZJ}
name_of={e["id"]:e["name"] for e in ZJ}
def prefecture(city_text):
    code=code_of.get(city_text)
    if not code: return city_text          # 省本级 / unknown -> keep as is
    pref=code[:4]+"00"
    return name_of.get(pref, city_text)

# scale parsed from title (best-effort; coverage partial — true scale needs detail)
SCALE=re.compile(r"(\d[\d,\.]*)\s*(公里|千米|km|万平方米|平方米|㎡|亩|万吨|座|户|栋)")
def scale(t):
    m=SCALE.search(t or "")
    return (m.group(1).replace(",",""), m.group(2)) if m else ("","")

con=sqlite3.connect(f"{D}/data/ggzy.db"); cur=con.cursor()
cur.execute("SELECT city_text,title,category,publish_time,url FROM announcements")
from collections import defaultdict
pref_cnt=defaultdict(lambda: defaultdict(int))
n=0; w=open(f"/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding/structured_projects.csv","w",encoding="utf-8-sig",newline="")
cw=csv.writer(w); cw.writerow(["prefecture","county_text","content_class","scale_value","scale_unit","amount_cny","category","publish_time","title","url"])
while True:
    rows=cur.fetchmany(100_000)
    if not rows: break
    for ct,title,cat,pt,url in rows:
        n+=1
        k=classify(title)
        if k in ("visible","functional"):
            pref=prefecture((ct or "").strip())
            pref_cnt[pref][k]+=1
            sv,su=scale(title)
            cw.writerow([pref,ct,k,sv,su,"",cat,pt,title,url])   # amount blank: index has none
w.close(); con.close()

with open(f"/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding/by_prefecture.csv","w",encoding="utf-8") as f:
    f.write("prefecture,visible,functional,vf_ratio\n")
    out=[]
    for p,d in pref_cnt.items():
        v,fn=d.get("visible",0),d.get("functional",0)
        if v+fn>=100: out.append((p,v,fn,round(v/fn,2) if fn else None))
    out.sort(key=lambda r:-(r[1]+r[2]))
    for r in out: f.write(",".join(str(x) for x in r)+"\n")
print(f"scanned {n:,}; wrote structured_projects.csv + by_prefecture.csv")
print("\n=== visible:functional by Zhejiang PREFECTURE (clean rollup) ===")
for r in out: print(f"  {r[0]:8} visible={r[1]:6} functional={r[2]:6} ratio={r[3]}")
print("all prefectures visible>functional?", all(r[1]>r[2] for r in out))
