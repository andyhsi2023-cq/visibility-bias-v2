# -*- coding: utf-8 -*-
"""DeepSeek-4.0 (deepseek-v4-pro) draft adjudication of the bidding lexicon for Liu Can to review.
For each visible/functional keyword: is it a reliable cue for that class in Chinese public-procurement
PROJECT TITLES? decision in {keep, move_to_functional, move_to_visible, drop, context_gate}.
Output is a DRAFT — the human co-author (Liu Can, urban & rural planning) owns the final call.
"""
import os, csv, json, re
from pathlib import Path
for ln in Path("/Users/andy/Desktop/Research/_meta/scripts/.env").read_text().splitlines():
    if ln.strip() and not ln.startswith("#") and "=" in ln:
        k,_,v=ln.partition("="); os.environ.setdefault(k.strip(),v.strip().strip('"').strip("'"))
from openai import OpenAI
cli=OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url=os.environ.get("DEEPSEEK_BASE_URL","https://api.deepseek.com/v1"), timeout=180, max_retries=2)

rows=list(csv.DictReader(open("lexicon_adjudication.csv",encoding="utf-8-sig")))
items=[{"term":r["term"],"current_class":r["current_class"],"est_matches":r["est_total"],
        "example":r["example_1"],"flag":r["notes"]} for r in rows]

SYS=("你是城乡规划领域专家,正在审定一套关键词词表。该词表用于把中国公共资源交易平台的**工程招标项目标题**"
     "二分类为:\n"
     "• visible(面子/政绩工程):对评估受众(上级/巡视/媒体/市民)显著可见的地表景观与市政美化——"
     "绿化、公园、广场、道路、桥梁、地铁/轨道交通、地标、亮化、景观等;\n"
     "• functional(里子/民生隐蔽):平时看不见、仅失效时被注意的地下管网与给排水防洪——"
     "排水、管网、污水、供水、防洪、供热、燃气等。\n"
     "对每个关键词,判断它在**项目标题**里作为该类别线索是否可靠。注意多义/误命中(如:道路出现在地址、"
     "景观出现在机构名'市容景观发展中心'、花园出现在楼盘名、地标是'基地标准'的子串)。\n"
     "为每个词给出 decision ∈ {keep(归类正确且可靠), move_to_functional, move_to_visible, "
     "drop(太杂应删除), context_gate(保留但需加上下文限定)},一句话 reason,若 context_gate 给出 gate 规则。\n"
     '只输出 JSON 数组:[{"term":"...","decision":"...","reason":"...","gate":"..."}]。')

USER="待审定词表(current_class / 估计命中次数 / 示例标题 / 我方预标风险):\n"+json.dumps(items,ensure_ascii=False,indent=1)

r=cli.chat.completions.create(model="deepseek-v4-pro",
    messages=[{"role":"system","content":SYS},{"role":"user","content":USER}],
    temperature=0, response_format={"type":"json_object"}, max_tokens=8000)
txt=r.choices[0].message.content or ""
print("raw len:",len(txt))
m=re.search(r"\[.*\]",txt,re.S) or re.search(r"\{.*\}",txt,re.S)
data=json.loads(m.group(0) if m else txt)
if isinstance(data,dict):
    data=data.get("result") or data.get("adjudication") or next((v for v in data.values() if isinstance(v,list)),[])
dec={d["term"]:d for d in data}
# merge into output CSV
out=[]
for r0 in rows:
    d=dec.get(r0["term"],{})
    out.append({**r0,
        "deepseek_decision":d.get("decision",""),
        "deepseek_reason":d.get("reason",""),
        "deepseek_gate":d.get("gate","")})
cols=list(rows[0].keys())+["deepseek_decision","deepseek_reason","deepseek_gate"]
with open("lexicon_adjudication_deepseek.csv","w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(out)
print(f"wrote lexicon_adjudication_deepseek.csv ({len(out)} terms)")
from collections import Counter
print("decision counts:",dict(Counter(o["deepseek_decision"] for o in out)))
print("\nnon-keep decisions (DeepSeek flags):")
for o in out:
    if o["deepseek_decision"] and o["deepseek_decision"]!="keep":
        print(f"  [{o['current_class']}] {o['term']}: {o['deepseek_decision']} — {o['deepseek_reason'][:70]}")
