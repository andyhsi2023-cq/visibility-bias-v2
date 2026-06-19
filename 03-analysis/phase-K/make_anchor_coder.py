#!/usr/bin/env python3
"""make_anchor_coder.py — build a BLIND human coding page for the ~120-sentence anchor.

Selects 30 sentences per dictionary hit-type (stratified, seeded, shuffled) from the
ensemble sheet, then writes a self-contained `human_coder.html` (shows ONLY the sentence —
no dictionary or model labels, so the human is independent) plus a hidden `anchor_key.csv`
used later for scoring.

    python3 make_anchor_coder.py
"""
import csv, json, random
from pathlib import Path

SRC = Path("passage_coding_sheet_ensemble.csv")
PER, SEED = 30, 20260618
LABELS = ["visible", "functional", "mixed", "irrelevant"]

HTML = r"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>VAI 句段盲编码(具体词表v3)</title>
<style>
 body{font-family:-apple-system,"PingFang SC",sans-serif;max-width:760px;margin:24px auto;padding:0 16px;color:#222}
 #bar{height:8px;background:#eee;border-radius:4px;overflow:hidden;margin:8px 0 16px}
 #fill{height:100%;background:#3b82f6;width:0}
 #sent{font-size:24px;line-height:1.7;background:#f7f7f8;border:1px solid #e5e7eb;border-radius:10px;padding:24px;min-height:120px}
 .btns{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0}
 button.lab{font-size:17px;padding:16px;border:1px solid #d1d5db;border-radius:10px;background:#fff;cursor:pointer}
 button.lab:hover{background:#eff6ff;border-color:#3b82f6}
 button.lab b{color:#3b82f6}
 .row{display:flex;gap:8px;align-items:center;justify-content:space-between;margin-top:10px}
 .mut{color:#888;font-size:14px}
 #exp{padding:10px 18px;font-size:15px;border-radius:8px;border:1px solid #16a34a;background:#16a34a;color:#fff;cursor:pointer}
 #exp:disabled{opacity:.4;cursor:default}
 details{margin:10px 0;font-size:14px;color:#444} summary{cursor:pointer;color:#3b82f6}
 code{background:#eef;padding:1px 5px;border-radius:4px}
</style></head><body>
<h3>VAI 句段盲编码(具体词表v3) <span class="mut" id="prog"></span></h3>
<div id="bar"><div id="fill"></div></div>
<details><summary>编码规则(点开)</summary>
 <p><b>可见 (1)</b>:外部可观察的基建——道路、绿化、亮化、立面/外观、景观、广场、市容、形象展示。<br>
 <b>功能 (2)</b>:隐蔽/民生基建——管网/排水、供水供气供暖、结构安全/抗震、防洪排涝、无障碍。<br>
 <b>混合 (3)</b>:同句明确兼有可见与功能(如"道路与地下管网")。<br>
 <b>无关 (4)</b>:不涉及实体基建(财政、人事、口号、社会政策等)。</p>
 <p class="mut">判主导基建指向;比喻义("打造高地")无实体=无关;只有数字无类别=无关。键盘 <code>1/2/3/4</code> 打标,<code>←</code> 或 <code>u</code> 撤销上一句。</p>
</details>
<div id="sent"></div>
<div class="btns">
 <button class="lab" data-l="visible"><b>1</b> 可见 visible</button>
 <button class="lab" data-l="functional"><b>2</b> 功能 functional</button>
 <button class="lab" data-l="mixed"><b>3</b> 混合 mixed</button>
 <button class="lab" data-l="irrelevant"><b>4</b> 无关 irrelevant</button>
</div>
<div class="row">
 <button class="lab" id="undo" style="font-size:14px;padding:8px 14px">← 撤销上一句</button>
 <button id="exp" disabled>导出 CSV ↓</button>
</div>
<p class="mut" id="msg"></p>
<script>
const ITEMS=__ITEMS__;
const KEY="vai_anchor_concrete_v3";
let ans=JSON.parse(localStorage.getItem(KEY)||"{}");
const $=s=>document.querySelector(s);
function idx(){for(let i=0;i<ITEMS.length;i++)if(!(ITEMS[i].id in ans))return i;return ITEMS.length}
function render(){
 const n=Object.keys(ans).length, i=idx();
 $("#fill").style.width=(100*n/ITEMS.length)+"%";
 $("#prog").textContent=`已编码 ${n} / ${ITEMS.length}`;
 $("#exp").disabled=n<ITEMS.length;
 if(i>=ITEMS.length){$("#sent").innerHTML="✅ 全部完成,点「导出 CSV」。";return}
 $("#sent").textContent=ITEMS[i].s;
}
function set(l){const i=idx();if(i>=ITEMS.length)return;ans[ITEMS[i].id]=l;localStorage.setItem(KEY,JSON.stringify(ans));render();}
function undo(){const i=idx();const j=i-1;if(j<0)return;delete ans[ITEMS[j].id];localStorage.setItem(KEY,JSON.stringify(ans));render();}
document.querySelectorAll("button.lab[data-l]").forEach(b=>b.onclick=()=>set(b.dataset.l));
$("#undo").onclick=undo;
document.onkeydown=e=>{const m={"1":"visible","2":"functional","3":"mixed","4":"irrelevant"};
 if(e.key in m)set(m[e.key]); else if(e.key==="u"||e.key==="Backspace"||e.key==="ArrowLeft"){e.preventDefault();undo();}};
$("#exp").onclick=()=>{
 let csv="sample_id,human_label\n";
 ITEMS.forEach(it=>{csv+=it.id+","+(ans[it.id]||"")+"\n";});
 const a=document.createElement("a");
 a.href=URL.createObjectURL(new Blob([csv],{type:"text/csv"}));
 a.download="anchor_human_labels.csv";a.click();
 $("#msg").textContent="已下载 anchor_human_labels.csv —— 放回 phase-G/ 后运行 score_anchor.py";
};
render();
</script></body></html>
"""


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
    rng = random.Random(SEED)
    by = {}
    for r in rows:
        by.setdefault(r["dict_label"], []).append(r)
    sel = []
    for lab in LABELS:
        pool = by.get(lab, [])[:]
        rng.shuffle(pool)
        sel += pool[:PER]
    rng.shuffle(sel)

    with open("anchor_key.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["sample_id", "sentence", "dict_label", "ensemble_majority"])
        for r in sel:
            w.writerow([r["sample_id"], r["sentence"], r["dict_label"], r["ensemble_majority"]])

    items = [{"id": r["sample_id"], "s": r["sentence"]} for r in sel]
    Path("human_coder.html").write_text(
        HTML.replace("__ITEMS__", json.dumps(items, ensure_ascii=False)), encoding="utf-8")
    print(f"{len(sel)} sentences -> human_coder.html  (+ hidden anchor_key.csv)")


if __name__ == "__main__":
    main()
