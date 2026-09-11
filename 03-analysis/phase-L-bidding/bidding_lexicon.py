# -*- coding: utf-8 -*-
"""Visible vs functional construction-project lexicon for Zhejiang public-procurement titles.
v2 (2026-06-19): refined by DeepSeek-4.0 adjudication + Liu Can (co-first, urban & rural planning)
sign-off. Changes vs v1: DROP 花园 (楼盘名) & 地标 ("基地标准" substring); CONTEXT-GATE 道路/大道/景观/
市容/步行街 (count as visible only inside a construction phrase, excluding addresses/org-names/rentals).
52 other terms confirmed keep. Adjudication: lexicon_adjudication_deepseek.csv + liucan sign-off.
"""
import re

# always-visible (unambiguous in procurement titles); 花园/地标 dropped, 5 gated terms removed to GATED
VISIBLE_PLAIN = [
    "绿化", "公园", "广场", "路网", "桥梁", "立交", "亮化", "绿道", "街景", "园林",
    "美化", "景观带", "地铁", "轨道交通", "轻轨", "有轨电车", "雕塑", "风貌", "喷泉",
    "立面", "体育公园", "口袋公园", "绿廊", "彩化", "靓化", "夜景",
]
# concealed-utility (functional) — unchanged
FUNCTIONAL = [
    "排水", "排涝", "管网", "污水", "供水", "防洪", "管廊", "内涝", "下水道",
    "排污", "给排水", "防汛", "雨水", "供热", "燃气", "供气", "管线", "饮水",
    "截污", "雨污", "泵站", "海绵", "自来水", "供排水", "二次供水", "中水",
]
# context-gated visible: term counts as visible only when a construction word is present somewhere
# (real works almost always carry one) AND no exclusion pattern (address/rental/org-name/contract).
GATED_TERMS = ["道路", "大道", "景观", "市容", "步行街"]
_WORK = re.compile(r"工程|建设|建造|修建|改造|改建|新建|扩建|施工|整治|提升|拓宽|拓展|维修|养护|"
                   r"硬化|白改黑|修复|设计|绿化|亮化|延伸|配套|贯通|畅通|综合|监理")
_EXCL = re.compile(r"租赁|出租|商铺|铺位|售货|摊位|拍卖|发展中心|管理中心|保险|采购合同|物业|"
                   r"餐饮|食堂|保洁|交叉口|号楼|房产|资产|车位|广告")
# for importers/back-compat (display only): the full visible vocabulary
VISIBLE = VISIBLE_PLAIN + GATED_TERMS

def _is_visible(t):
    if any(w in t for w in VISIBLE_PLAIN):
        return True
    if any(g in t for g in GATED_TERMS):
        return bool(_WORK.search(t)) and not _EXCL.search(t)
    return False

def classify(title):
    """Return 'visible' / 'functional' / 'mixed' / 'other' for a project title."""
    t = title or ""
    f = any(w in t for w in FUNCTIONAL)
    v = _is_visible(t)
    if v and f:
        return "mixed"
    if v:
        return "visible"
    if f:
        return "functional"
    return "other"
