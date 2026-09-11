# -*- coding: utf-8 -*-
"""Re-pull Zhejiang procurement briefs with FULL content (cl=3000) to recover the investment
amount the original crawl truncated (it set cl=200). Provincial inteligentsearch endpoint
(ggzy.zj.gov.cn), polite 1.5s interval. For each AWARD/RESULT record (中标/成交/结果) we take the
max ¥ value in the brief as the project amount, classify the title visible/functional, dedup by
title, and accumulate per-class amount sums for the amount-weighted ratio.

Usage: repull_amounts.py SDT EDT OUT.csv   (dates inclusive, YYYY-MM-DD)
"""
import sys, requests, re, time, csv, json
from datetime import datetime, timedelta
sys.path.insert(0, "/Volumes/P1/城市研究/公共资源交易招投标_浙江全量2017-2026")
import config as C
from provincial import ISEARCH, PLATFORMS, _headers
sys.path.insert(0, "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-L-bidding")
from bidding_lexicon import classify

P = PLATFORMS["330000"]; HOST = P["host"]; REF = P["ref"]
SDT, EDT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
RN, CL, INTERVAL = 500, 3000, 1.6
_MONEY = re.compile(r"([\d,]{4,}(?:\.\d+)?)\s*(万元|万|亿元|亿|元)")
AWARD = ("中标", "成交", "结果", "中选")          # award/result announcements carry the amount

def to_yuan(n, u):
    v = float(n.replace(",", ""))
    return v*1e8 if u in ("亿元","亿") else v*1e4 if u in ("万元","万") else v

def amount(content):
    t = re.sub(r"<[^>]+>", " ", content or "")
    vals = [to_yuan(n, u) for n, u in _MONEY.findall(t)]
    vals = [v for v in vals if 1e4 <= v <= 5e10]
    return max(vals) if vals else None

def next_day(d):
    return (datetime.strptime(d, "%Y-%m-%d").date() + timedelta(days=1)).isoformat()

def query(day, pn):
    body = {"token":"","pn":pn,"rn":RN,"sdt":day,"edt":next_day(day),"wd":"","inc_wd":"","exc_wd":"","fields":"",
            "cnum":"001","sort":"{\"webdate\":\"0\"}","ssort":"title","cl":CL,"terminal":"","condition":[],
            "time":[],"highlights":"","statistics":None,"unionCondition":[],"accuracy":"","noParticiple":"1",
            "searchRange":None,"isBusiness":"1"}
    for attempt in range(4):
        try:
            r = requests.post(HOST+ISEARCH, json=body, headers=_headers(HOST,REF), timeout=45)
            res = (r.json() or {}).get("result", {}) or {}
            return res.get("records", []) or [], int(res.get("totalcount", 0) or 0)
        except Exception as e:
            time.sleep(4*(attempt+1))
    return [], 0

def daterange(a, b):
    d = datetime.strptime(a, "%Y-%m-%d").date(); end = datetime.strptime(b, "%Y-%m-%d").date()
    while d <= end:
        yield d.isoformat(); d += timedelta(days=1)

seen = set()
fh = open(OUT, "w", encoding="utf-8-sig", newline=""); w = csv.writer(fh)
w.writerow(["date","class","city","amount_cny","title"]); fh.flush()
n_rec = n_amt = 0
for day in daterange(SDT, EDT):
    pn = 0
    while pn < 10000:
        time.sleep(INTERVAL)
        recs, total = query(day, pn)
        if not recs: break
        for r in recs:
            n_rec += 1
            title = (r.get("title") or "").strip()
            content = r.get("content") or ""
            itt = re.sub(r"<[^>]+>", "", content)[:30]
            if not any(k in itt for k in AWARD):       # only award/result records carry the amount
                continue
            k = classify(title)
            if k not in ("visible","functional"):
                continue
            key = re.sub(r"[\[(（].*$", "", title)[:40]  # dedup by title stem
            if key in seen: continue
            a = amount(content)
            if not a: continue
            seen.add(key); n_amt += 1
            w.writerow([day, k, r.get("infod") or "", int(a), title[:80]])
        fh.flush()
        if pn + RN >= total: break
        pn += RN
    print(f"{day}: cum_records={n_rec} amounts={n_amt}", flush=True)
fh.close()
print(f"DONE {SDT}..{EDT}: scanned {n_rec} records, extracted {n_amt} project amounts -> {OUT}", flush=True)
