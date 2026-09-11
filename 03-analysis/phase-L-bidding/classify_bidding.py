# -*- coding: utf-8 -*-
"""Liu Can's procurement-frequency verification (§4.3): classify every Zhejiang public-procurement
project title as visible / functional / mixed / other, and compute the visible:functional count
ratio overall and by city. Single streaming pass over ggzy.db (2.96M announcements); memory-light
(only counters). Reports BOTH all-announcements and a per-project proxy (发标公告 = one tender notice
per project) and a 2019-2024 window, so the ratio's robustness to definition is visible.

Source DB: /Volumes/P1/.../公共资源交易招投标_浙江全量2017-2026/data/ggzy.db
Output: results_summary.json + by_city.csv (this dir).
"""
import sqlite3, json, sys
from collections import defaultdict
sys.path.insert(0, "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding")
from bidding_lexicon import classify

DB = "/Volumes/P1/城市研究/公共资源交易招投标_浙江全量2017-2026/data/ggzy.db"
OUT = "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding"

con = sqlite3.connect(DB)
cur = con.cursor()

# counters: [scope] -> Counter over classes ; and by-city -> {city: {class:n}}
agg = {s: defaultdict(int) for s in ["all", "fb", "win2019_24"]}
city = {s: defaultdict(lambda: defaultdict(int)) for s in ["all", "fb", "win2019_24"]}

cur.execute("SELECT city_text, title, category, publish_time FROM announcements")
n = 0
while True:
    rows = cur.fetchmany(100_000)
    if not rows:
        break
    for ct, title, cat, pt in rows:
        n += 1
        k = classify(title)
        ct = (ct or "未知").strip()
        agg["all"][k] += 1
        city["all"][ct][k] += 1
        if cat == "发标公告":                       # one tender notice per project (project proxy)
            agg["fb"][k] += 1
            city["fb"][ct][k] += 1
        if pt and "2019-01-01" <= pt[:10] <= "2024-12-31":
            agg["win2019_24"][k] += 1
            city["win2019_24"][ct][k] += 1
con.close()

def ratio(d):
    v, f = d.get("visible", 0), d.get("functional", 0)
    return round(v / f, 3) if f else None

summary = {"n_announcements": n}
for s in agg:
    d = dict(agg[s])
    summary[s] = {"counts": d, "visible_functional_ratio": ratio(d)}

# by-city table (use the project-proxy 发标公告 scope; rank by visible+functional volume)
rows_out = []
for ct, d in city["fb"].items():
    v, f = d.get("visible", 0), d.get("functional", 0)
    if v + f >= 50:                                  # enough volume to be meaningful
        rows_out.append((ct, v, f, round(v / f, 3) if f else None, v + f))
rows_out.sort(key=lambda r: -r[4])

with open(f"{OUT}/results_summary.json", "w", encoding="utf-8") as fh:
    json.dump(summary, fh, ensure_ascii=False, indent=2)
with open(f"{OUT}/by_city.csv", "w", encoding="utf-8") as fh:
    fh.write("city,visible,functional,vf_ratio,vf_total\n")
    for r in rows_out:
        fh.write(",".join(str(x) for x in r) + "\n")

print(f"DONE. n={n:,}")
print("OVERALL (all announcements):", summary["all"])
print("PROJECT PROXY (发标公告):   ", summary["fb"])
print("WINDOW 2019-2024:           ", summary["win2019_24"])
print(f"\nby-city (发标公告, vf_total>=50), top 15 of {len(rows_out)} cities, all visible>functional?:",
      all(r[1] > r[2] for r in rows_out))
for r in rows_out[:15]:
    print(f"  {r[0]:10} visible={r[1]:6} functional={r[2]:6} ratio={r[3]}")
