# Procurement-frequency verification (§4.3) — reproducible results

> ## ★ FINAL v2 (DeepSeek-4.0 adjudication + Liu Can sign-off, 2026-06-19) — supersedes draft numbers below
> Lexicon refined: DROP 花园/地标; CONTEXT-GATE 道路/大道/景观/市容/步行街 (require a construction word, exclude address/rental/org). Re-ran count (full 2.96M) + amount (re-classified 2023-24).
> **Count**: visible:functional = **2.02** (all announcements) / **2.12** (发标公告) / **2.08** (2019-24); **97 of 108 localities** visible>functional (median city ratio 1.8).
> **Amount** (16,794 award projects, 2023-24): median ¥5.78M vs ¥4.71M (**1.23**); P99 ¥0.90B vs ¥0.20B (**4.45**); max ¥11.46B (杭州地铁7号线) vs ¥1.07B; trimmed-mean(P99) ratio 2.66. Raw sum ratio discarded (tail-sensitive).
> **Reading unchanged**: visible dominates on frequency (~2:1) AND owns the high-value tail (metro/rail/arterial). Files: `bidding_lexicon.py` (v2), `lexicon_adjudication_deepseek.csv`, `liucan_review.html`, `amounts_final.csv`, `amount_summary.json`, `by_city.csv`, `fig_bidding_by_city.*`.

---


**Date**: 2026-06-19 · **Author of this analysis**: Liu Can (co-first; urban & rural planning) work, executed/scripted here.
**Data**: `/Volumes/P1/城市研究/公共资源交易招投标_浙江全量2017-2026/data/ggzy.db` (SQLite, 2.5 GB), table `announcements` = **2,957,789** records, national `ggzy.gov.cn` platform, Zhejiang slice. Year mass 2019–2026 (2019: 90k → 2024: 757k → 2025: 445k → 2026: 172k; pre-2019 sparse). `f_budget`/`f_win_amount` unpopulated → **counts only, no amounts**.
**Code**: `classify_bidding.py` + `bidding_lexicon.py` (lexicon is the domain-expert classification — Liu Can to own/edit). **Outputs**: `results_summary.json`, `by_city.csv`.

## Headline (reproducible)

Visible-type construction projects outnumber functional ones:

| scope | visible | functional | mixed | ratio v:f |
|---|---:|---:|---:|---:|
| all announcements | 251,859 | 109,093 | 11,456 | **2.31** |
| 发标公告 (tender notice = project proxy) | 63,099 | 23,695 | 2,357 | **2.66** |
| window 2019–2024 | 188,362 | 79,910 | 7,776 | **2.36** |

By city (发标公告, ≥50 visible+functional; 109 localities): **visible > functional in 103 / 109** (median city ratio **2.20**, range 0.58–21.49). The 6 exceptions are small county-level units (长兴县 ~1:1, 江山市, 定海区, 莲都区, 天台县, 嵊泗县). Examples: 杭州市 7.1, 宁波市 4.5, 台州市 3.7, 柯桥区 2.5.

## ⚠️ Correction to prior draft numbers (were not reproducible)

The pre-rewrite manuscript/evidence-core claimed **ratio 2.97 ("≈3:1"), "every one of ten cities", Keqiao 13.9 / Taizhou 6.5 / Hangzhou 5.7**. None of these reproduce (there was no script on disk). The real, reproducible figures are ratio **≈2.3–2.7**, **103/109 localities** (not "every one"), and the specific city numbers differ (Keqiao 2.5, Taizhou 3.7, Hangzhou 7.1). The manuscript and `V2-EVIDENCE-CORE.md` have been corrected to the reproducible values.

## Structured processing along the 3 dimensions (2026-06-19 audit)

The prior project **never ran structured extraction** — `detail_status = 0` and `extract_status = 0` for ALL 2,957,789 rows; `body_text`, `f_budget`, `f_win_amount`, `f_winner`, `fields_json` are 0% populated. Only the **index** (title, region-name, category, date, url) was crawled. Availability by dimension:

| Andy's dimension | available from index? | source |
|---|---|---|
| 1. title + administrative region | ✅ yes | `title`, `city_text` (locality level; clean 11-prefecture rollup deferred — needs a county→prefecture crosswalk, area.json incomplete) |
| 2a. construction content (visible/functional) | ✅ yes | title classification (`bidding_lexicon.py`) |
| 2b. scale (规模, km/㎡/亩…) | ⚠️ ~0.3% only | titles rarely carry it → in detail page |
| 3. investment amount (投资额) | ❌ 0% | **detail page only** (`f_budget`/`f_win_amount` empty) |

`structured_projects.csv` (360,952 visible+functional rows) holds dims 1 + 2a (+ sparse 2b), with an `amount_cny` column **ready to be filled**. The **amount and scale dimensions require crawling detail pages** — the pipeline already exists (`ggzy.py` `detail()` + `extract_fields()` regex for 预算金额/中标金额; `cmd_details`/`cmd_extract`), it was simply never executed (rate-limited: 8 s/request, ≤40/10 min, WAF-ban risk per the dataset README). ### Amount crawl attempted 2026-06-19 — NOT FEASIBLE (definitive)

Live test (IP not blocked, HTTP 200): detail pages for **construction** bids (sub-systems 002002/002007/002001 — the 公园/道路/污水 projects) are **shell pages**; the body holding 中标金额 is loaded from a **PDF attachment whose URL is JS-injected** (`$(".pdfurl")`), not present in the static HTML. The only sub-system that inlines 成交金额 in HTML is 政府采购 (002011) — but it is **6 of 200,000** visible/functional award notices (≈0%; gov-procurement is goods/services, not construction). So a simple detail crawl yields amounts for ~0% of the relevant projects; getting amounts would require a **headless-browser render → PDF download → OCR/parse** pipeline per page, over a WAF-limited site, for thousands of pages (days; fragile). **Rejected as disproportionate** for a supplementary check that MOHURD CIR already covers on the expenditure dimension.

### Amount RECOVERED 2026-06-19 via the tender BRIEF (the actual resolution)

The "not feasible" note above applies only to the **中标 (award) detail PDFs**. The amount is in fact in the **招标简介 (tender brief)** all along — the original crawl set `cl: 200` (content-length cap) in the provincial `inteligentsearch` request, truncating the brief to 203 chars and dropping 建设内容/规模/投资. **Re-querying the same endpoint with `cl: 3000` returns the full brief, including the bid/control-price amount** — no PDF, no headless, provincial site at 1.5 s/req. Script: `repull_amounts.py` (date-sliced, `edt = day+1`; award records only; amount = max ¥ value in brief; classify by title; dedup).

**Re-pull 2023–2024** (`amounts_2023_2024.csv`, 1.38M records scanned → **18,406 deduped project amounts**, 13,818 visible / 4,588 functional; `amount_summary.json`):

| stat | visible | functional |
|---|---:|---:|
| n | 13,818 | 4,588 |
| median | ¥489万 | ¥471万 |
| mean | ¥3,998万 | ¥1,571万 |
| P99 | ¥8.66亿 | ¥2.02亿 |
| max | ¥114.57亿 (杭州地铁7号线) | ¥10.68亿 |

Ratios: **count 3.01 · median 1.04 · P99 4.29 · trimmed-mean(P99) 2.43**. Raw sum ratio 7.67 — **discarded** (heavy visible megaproject tail + residual title-dedup imperfection; not robust). **Reading**: typical visible/functional project equal in size; visible owns the high-value tail (metro/rail/arterial = visible-salient). Visible dominates on frequency (3:1) AND big-ticket spend — answers the reviewer's "counts confounded by packaging". §4.3 updated accordingly. (Amount re-pull covers 2023–2024; the count analysis covers the full 2019–2026.)

## Honest caveats (carried into §4.3)

1. **Counts, not amounts** — budget/award fields unpopulated; the expenditure dimension is carried by the accounting-based CIR (§4.2).
2. **Granularity** — "project" is proxied by tender-notice count; multi-lot/multi-stage packaging differs across project types.
3. **Lexicon = domain judgment** — `bidding_lexicon.py` encodes the visible/functional assignment; it is Liu Can's substantive contribution and should be reviewed/owned by the domain expert.
4. **Raw DB is 2.5 GB on P1** — for the replication archive deposit `by_city.csv` + the two scripts + a data-access note (the raw DB is too large for Zenodo).
