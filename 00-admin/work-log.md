# Visibility Bias v2 — Project Work Log

**Authors** (co-first: Xi + Liu Can; corresponding: Xi):
- **Hongyang Xi** (奚红洋) — Chongqing Survey Institute Co., Ltd.; co-first & corresponding; ORCID 0009-0007-6911-2309; 26708155@alu.cqu.edu.cn
- **Liu Can** (刘灿) — Urban & Rural Planning, Guangzhou College of Applied Science and Technology; Lecturer; co-first; **procurement/bidding-evidence verification** (owns the §4.3 / phase-L work); ORCID 0009-0009-0794-7671; 346584701@qq.com
- **Zhihui Li** (李志辉) — Chongqing Survey Institute Co., Ltd.; second author & **second passage-coder** (intercoder κ); ORCID 0009-0009-5486-8490; 303841718@qq.com
- (info source: `~/Desktop/Research/本地信息.rtf`; Liu Can English info added there 2026-06-19)
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication archive**: Zenodo DOI 10.5281/zenodo.19569979

---

## Project Identity

**Title**: *Measuring Visibility Bias in Bureaucratic Text: A Validated Instrument with Evidence from Chinese Municipal Government Work Reports*

**Type**: Text-as-data measurement-methodology paper

**Final target**: *Journal of Computational Social Science* (Springer Nature, ISSN 2432-2725) — Second-Tier methodology venue

---

## Submission

| Item | Value |
|---|---|
| **Journal** | Journal of Computational Social Science |
| **Editorial Manager portal** | https://www.editorialmanager.com/jcso/ |
| **Article type** | Research Article |
| **Submission date** | 2026-04-14 (~22:30 UTC+8) |
| **Temporary submission ID** | JCSO-S-26-00292 |
| **Status at submission** | Approved by author → forwarded to editorial office |
| **Suggested handling editor** | Robert Ackland (Associate Editor, text-as-data) |
| **Suggested reviewers** | Daniel Mattingly (Yale); Jennifer Pan (Stanford); Yuhua Wang (Harvard) |
| **Cover letter** | Pasted into Comments tab; full text mirrors `submission/cover_letter_jcss.md` |
| **Compliance audit** | 23/24 hard requirements ✓; 1 deferred (Google Scholar URL) — alternative ORCID/OSF/Zenodo identity provided |

---

## Timeline

| Date | Milestone |
|---|---|
| 2026-04-06 | Predecessor manuscript ("Seeing Is Governing", urban-economics framing) submitted to *Habitat International* (HABITATINT-D-26-01417) |
| 2026-04-13 | Habitat International desk reject (Editor Eddie C.M. Hui, "lack of sufficient novelty") |
| 2026-04-14 morning | A-Gate audit fails → α-min upgrade plan executed |
| 2026-04-14 noon | OSF pre-registration formally minted (DOI 10.17605/OSF.IO/ZMJY5) |
| 2026-04-14 afternoon | Phase B (TWFE event study), Phase E (5-test construct validity), Phase F (CFPS micro null) executed; Phase B2 (Sun-Abraham extension) and Phase E2 (Wikipedia third-party validation) added |
| 2026-04-14 evening | Track 1 CCDI extension (Rounds 6–9) discovered P2 sign reversal under heterogeneity-robust estimation → α' methodology repositioning |
| 2026-04-14 night | Manuscript v3 (10,400 words, methodology framing) compiled; Zenodo replication archive minted with reviewer token; cover letter rewritten for JCSS |
| 2026-04-14 22:08–22:18 | Cold outreach: 4 emails sent via CQU alumni mail to Mattingly (Yale, ✓), Pan (Stanford, ✓ wrong subject), Wang (Harvard, ✓), Jiang (NUS, ❌ bounce) |
| 2026-04-14 22:30 | JCSS Editorial Manager submission — manuscript + 4 figs + ESM + cover letter (in Comments) + 3 reviewers + Robert Ackland as suggested editor |
| 2026-04-14 ~23:30 | Submission Approved by author; status: forwarded to editorial office |

---

## What was built

### Manuscript (`05-manuscript/`)
- `manuscript_v3_compiled.md` — full 10,400-word manuscript
- `submission/title_page.{md,docx,pdf}` — author info, ORCID, Scholar deferment statement
- `submission/cover_letter_jcss.{md,docx,pdf}` — JCSS cover letter with Zenodo reviewer token
- `submission/manuscript.{docx,pdf}` — main body for EM upload
- `submission/manuscript_full.docx` — combined title + body (actually uploaded to EM)
- `submission/ESM_1.{docx,pdf}` — Online Resource 1 (Online Appendix A–E)
- `submission/figures/Fig1-Fig4.{pdf,png}` — main-text figures (5 panels via 4 files)
- `submission/figures/ESM_Fig1-5.pdf` — appendix figures
- `submission/suggested_reviewers.md` — 3 reviewers + 1 handling editor + 2 recusals
- `submission/JCSS_compliance_audit.md` — 24-item JCSS guidelines compliance check
- `submission/em-pdf/JCSO-S-26-00292_built.pdf` — Editorial Manager-built PDF (1.78 MB)

### Bibliography (`01-literature/`)
- `references.bib` — 35 entries (APA 7); 17 cited in main text after JCSS numeric-citation conversion
- `05-manuscript/sections/08_references.md` — JCSS-format numbered list (1–17)

### Analysis code (`03-analysis/`)
- `phase-B/` — TWFE event study (placebo + 500-iter random-assignment)
- `phase-B2/` — Sun-Abraham 5-cohort + 9-cohort extended
- `phase-E/` — 5-test construct-validity battery
- `phase-E2/` — Wikipedia third-party validation
- `phase-F/` — CFPS individual-level micro null
- `welfare-sensitivity.py` — Cobb-Douglas + CRRA + BOE replacement-cost calibration

### Data (`02-data/`)
- `processed/ccdi_inspection_rounds_extended.csv` — 62 province-rounds (2013–2017)
- `raw/wikipedia_zh/` — 282 Chinese Wikipedia city-description files

### Pre-registration & archive (`07-prereg/`)
- OSF DOI 10.17605/OSF.IO/ZMJY5 (https://osf.io/zmjy5/)
- Zenodo DOI 10.5281/zenodo.19569979 (Restricted with reviewer token; flips to Public on acceptance)
- GitHub: `andyhsi2023-cq/visibility-bias-v2`
- `zenodo-dois.md` — token + URL documentation

### Outreach (`00-admin/outreach/`)
- 4 customized cold-outreach emails (Mattingly, Pan, Mattingly, Wang)
- `research_summary_1page.{md,pdf}` — 1-page methodology summary attached to all
- `outreach_log.md` — bounce + delivery status

### S7 four-layer audit reports (`06-review/`)
- `S7-1-format-audit.md`, `S7-2-novelty-audit-v3.md`, `S7-3-red-team-report.md`, `S7-4-editor-simulation.md`
- Phase-level memos: `phase-{B,B2,E,E2,F}-results-memo.md`, `track1-results-memo.md`

---

## Key methodological achievements

1. **Within-document retrospective-vs-prospective behavioral signature** (E-B): Δ = +0.025, paired t = 8.4, p < 10⁻¹⁶ on 4,330 GWRs. To my knowledge novel in the text-as-data literature.
2. **Five-test pre-registered construct-validity battery** (Cronbach-Meehl): 4 pass + 1 scope-bounding null (Wikipedia E-F) reported transparently.
3. **Pre-registered null disclosure**: P2 inspection event study reverses sign under heterogeneity-robust extension (TWFE −0.065 → Sun-Abraham +0.016). Reported in §5.4.1 instead of suppressed.
4. **Structural welfare calibration**: ¥1–15 B/yr defensible range under log utility; ¥4.4 B central; ¥55 B BOE ceiling.
5. **Complete reproducibility chain**: OSF pre-reg → Zenodo replication → GitHub mirror, all DOI-linked.

---

## Known caveats / scope statements

- Causal identification of *what drives* visibility bias is not achieved (P2 null).
- External construct validity not fully established (Wikipedia null is scope-bounding rather than refuting).
- Micro-foundation of citizen-satisfaction channel not detected at |d| > 0.011 in CFPS.
- All applications assume the cadre-attention model is substantively correct; structural welfare numbers are conditional on model + parameters.

---

## Deviations from pre-registration

Five deviations (D-B-1 through D-F-1) logged in `06_appendix_deviations.md`:
- D-B-1: Callaway-Sant'Anna infeasible → TWFE substitute
- D-B-2: Sun-Abraham added post-hoc as heterogeneity-robust check
- D-B-3: Sample extended to 2017 with Rounds 6–9
- D-E2-1: Wikipedia E-F substitute for original third-party text source
- D-F-1: CFPS substituted for original micro-foundation specification

All deviations include reason + executed substitute + effect-on-sign-and-significance.

---

## Concurrent submissions / disclosure

- Predecessor (different framing): Habitat International HABITATINT-D-26-01417 — desk-rejected 2026-04-13
- This submission (methodology framing): not submitted concurrently elsewhere
- Pre-registration: OSF ZMJY5 (open since 2026-04-14)

---

## Outreach status (informal pre-submission engagement)

| Recipient | Institution | Email | Sent | Delivery |
|---|---|---|---|---|
| Daniel Mattingly | Yale | daniel.mattingly@yale.edu | 22:14 | ✅ delivered |
| Jennifer Pan | Stanford | jp1@stanford.edu | 22:10 | ✅ delivered (subject error: shows attachment filename) |
| Yuhua Wang | Harvard | yuhuawang@fas.harvard.edu | 22:18 | ✅ delivered |
| Junyan Jiang | NUS | junyan.jiang@nus.edu.sg | 22:08 | ❌ bounced (address invalid) |

Disclosed transparently to JCSS editor in cover letter.

---

## Next actions

1. **Wait for editorial decision** (EM dashboard at https://www.editorialmanager.com/jcso/)
2. **Track responses** from outreach scholars over next 7–14 days
3. **Identify alternate Junyan Jiang email** for re-attempt
4. **Monitor Research Square dashboard** (consented during submission) for peer-review status updates
5. **On acceptance**: flip Zenodo from Restricted → Public; update title page Scholar URL field

---

## Files / locations cheat-sheet

- Project root: `/Users/andy/Desktop/Research/visibility-bias-v2/`
- Submission package: `05-manuscript/submission/`
- EM-built PDF archive: `05-manuscript/submission/em-pdf/JCSO-S-26-00292_built.pdf`
- Compliance audit: `05-manuscript/submission/JCSS_compliance_audit.md`
- This work log: `00-admin/work-log.md`

---

## 2026-06-18/19 — R1 大修:转向"诚实测量验证"稿 + 与 officials-turnover-cn 合并

**触发**:JCSS(JCSO-D-26-00240)Major Revision。取回审稿 PDF(`06-submission/JCSO_review.pdf`),Reviewer #1 核心 C1 = 测的是话术≠真实分配。

**关键转折(按序)**:
1. **Plan-B 因果可行性裁决**:无干净因果识别可救(CCDI 巡视已死,见 rejection-log)。
2. **词典验证**(人工 120 句 + 3 模型集成,Fleiss κ=0.77/0.835):**朴素 VAI 可见精度仅 0.10(人工金标)**,祸首多义词「示范」(占可见误报 61/84)+ 形象/展示/美丽/样板。
3. **发现并审计双胞胎 `officials-turnover-cn`**(同构念"面子里子"/同语料/建在本项目 VAI 上):审计判其**稳健且诚实**(财政线 CIR 真;文本线语义验证三振=同一弱点)。**决定不单独发表、整体并入 V2**(避免自我重叠/双发)。
4. **测量重建**:具体词表(Wu-Zhou 对齐)→ 精度 0.50→0.60;**显著度原理(Andy:地铁/轨道交通=可见,边界案例)**→ v4 词表;**词典多义天花板 ≈ 0.60–0.64,词表 curation 破不了**(道路="工业化道路"、轨道交通="产业"隐喻);高精度 = **LLM 集成 0.84 / κ=0.835**。
5. **行为标准效度(独立复算)**:退休外生更替下,真实 CIR 面子投资 +0.025(p<0.001)与有效文本 +0.010(p=0.01)**同步上升、lead 干净**;朴素文本不动(p=0.54)。→ **决定性答 C1**。
6. **招投标**(浙江 2019-2024,2.96M 索引):可见/功能**项目数 3:1**(10 城一致);金额本库取不到(只爬索引,detail 0%)→ 由 CIR 覆盖。诚实caveat:频次靠招投标、金额靠 CIR。

**新论点**:政务文本测量的**验证案例**——朴素词典败(0.10)→ 具体撞多义天花板(0.60)→ LLM 高精(0.84)→ **行为同步决定效度**。诚实、有真行为效度、无 overclaim。

**本会话产出(落盘)**:`03-analysis/phase-K/V2-EVIDENCE-CORE.md`(数字+原理+v4词表+逐section重写蓝图+审稿人映射)、`06-submission/response-to-reviewers-R1.md`(答 C1–C5)、`02-data/processed/lexicon_visible_v4_salience.txt`、phase-I/J/K/L 脚本与中间结果、`00-admin/planB-data-menu.md`、`00-admin/NEXT-SESSION-KICKOFF.md`。

**待办**:① 正文六节按蓝图重写(**新会话**,读 NEXT-SESSION-KICKOFF.md);② 第二编码员补人工 intercoder κ;③ OSF/Zenodo 重存并验证链接;④ EM 上传(Word/Tex)。

---

## 2026-06-19 (续) — R2 正文六节重写完成 + 验证决定性数字

**本会话产出**:`05-manuscript/manuscript_compiled_R2.md`(10,772 words);§1–§6 + 标题全部按 V2-EVIDENCE-CORE §7 蓝图重写到收敛论点(测量验证案例:naive 0.10 → 具体撞天花板 0.60 → LLM 0.84 → 行为同步决定效度)。section 文件 00–08 全部更新。

**关键发现 + 修复(高优先)**:决定性数字「具体文本随退休外生更替与真实 CIR 同步 +0.0103/p=0.010」在 V2 **此前不可复现**——`replicate_comovement.py` 读的 `main_panel.csv` 只有 naive `vai_composite`(给出 null +0.0016/p=0.54),**没有 `wr_visibility` 列**;NEXT-SESSION-KICKOFF.md 的数据指针写错了文件。`wr_visibility`(具体 Wu-Zhou 对齐词表,20v/16f)实际在 `officials-turnover-cn/02-data/processed/master_2002_2024.csv`(col 57)。新写 `phase-J-criterion-validity/verify_comovement_master.py` → `verify_results_master.csv`:三条全部**精确复现** V2-EVIDENCE-CORE(CIR +0.0249/p<0.001;concrete +0.0103/p=0.010;naive +0.0016/p=0.54;lead 全干净)。已在 V2-EVIDENCE-CORE.md §3 注明正确文件与脚本。**支柱成立且现在可追溯。**

**写作期独立复核(全部 trace)**:具体词典 visible precision 0.500/recall 0.789(score_anchor.py);human↔ensemble Cohen κ=0.663;ensemble accuracy 0.842(JSON);naive FP 由「示范」主导(61/84,PILOT-FINDINGS)。

**结构决定**:① 横截面 β=+0.111(P1)**不再作头条**(blockers 已记 robustness 行不可追溯;蓝图未列)——降级为 §3.5 的 E-D 跨源弱检验(r=0.24);行为同步(§4)成为主轴。② 福利、物理存量、巡视、CFPS 全部降级到附录并诚实报 null。

**附录一致性修复**:新增 Online Appendix C.8(混淆矩阵 + 示范 FP 误差分类,verified 数字);新增 deviation log D-J-1(criterion-validity 扩展=新主轴)+ 改写 D.4 摘要(原文还在说 β=+0.111/福利"unaffected",已纠正);Appendix E 复现架构补 phase-J/K/L + master panel;修正正文交叉引用(Appendix C→D for deviations;error taxonomy→C.8;data provenance→Appendix E)。

**Andy 待办(我做不了/需人工)**:
- **R-1 引用**:references [20] = Wu & Zhou (2018) 面子投资分类,占位「ANDY TO SUPPLY」(摘要+§3.2.2 已引;build_workreport_text.py 注释作"吴周2018",但全项目无完整引文,我不杜撰)。
- **R-2 第二编码员 intercoder κ — ✅ 已解决(2026-06-19,李志辉编码)**:李志辉用 `second_coder_LOCKED.html` 盲编了**与 gold 同一 120 句**(导出 `coder2_filled.csv` → `phase-K/li_labels.csv`),`score_anchor.py coder2_labels.csv li_labels.csv` 得 **人际 Cohen κ = 0.699(substantial,n=120,120/120 同句)**。已写入摘要/§3.3/附录 C.8/response letter(替换原 pending)。分歧主要在 visible↔mixed 边界(Li 更倾向标 visible:36 vs gold 19),与多义天花板论点一致。**C3 自此完整满足**(段级 P/R/FP/FN/模糊例 + 人际 κ)。

  〔历史记录,2026-06-19 早先〕:Downloads 另两份编码(`anchor_human_labels.csv` 22:39 / `anchor_human_labels-2.csv` 08:10)**不构成有效双编码对**——两人各编 120 句但取自 500 池的**不同子集**(仅 26 句重合),且 26 句上一致仅 6/26(κ=−0.032,≈随机)。HTML 编码器每次发不同批次(为覆盖率,非双编码),`passage_coding_sheet.csv` 的 coder1/coder2 列是空模板。coder2(08:10)= 0.50 精度的 gold;coder1(22:39)像粗糙首遍(把明显可见的大道/公园判 irrelevant)。**没有把 κ=−0.03 写进稿**(那会假称构念不可靠)。**修复已备**:`03-analysis/phase-K/second_coder_sheet_LOCKED.csv`(同一 120 gold 句、空标签、隐藏 dict/ensemble)→ 第二人填 `human_label` → `score_anchor.py coder2_labels.csv <filled>.csv` 出真 κ。**这是 R2 离干净 C3 仅剩的一件实事**(且 gold 的 0.50 精度目前只靠单编码者,双编码若回来仍低则精度本身存疑)。详见 `06-review/R2-responsiveness-audit.md`。
- **R-3 复现归档**:必须把 `master_2002_2024.csv` + `build_workreport_text.py` + `verify_comovement_master.py` 并入 V2 Zenodo 记录(决定性数字依赖 sibling 项目文件);并修 blockers 旧账(phase-A/specification_curve_v2.py 路径不存在、24-vs-96 spec-curve)——但这些已随 β=+0.111 降级,不再承重。
- **R-4 招投标验证 — ✅ 已完成并落盘(2026-06-19,Liu Can 的活儿)**:原 `phase-L-bidding/` 空、3:1 结果无脚本。本会话发现原始库在 P1(`公共资源交易招投标_浙江全量2017-2026/data/ggzy.db`,2.5GB,announcements 表 2,957,789 行),写了 `classify_bidding.py` + `bidding_lexicon.py`,全量复算:可见:功能 = **2.31(全)/ 2.66(发标公告)/ 2.36(2019-24)**,**103/109 地市县可见>功能**(中位 2.2)。⚠️ 旧稿 **2.97 /"10 城无一例外"/ 柯桥13.9 不可复现**(无脚本),已纠正(柯桥实 2.5);正文 §4.3、evidence-core §6b、`phase-L-bidding/RESULTS.md` 全部改为可复现值。**待 Andy/Liu Can**:① Liu Can 审定 `bidding_lexicon.py` 的可见/功能归类(领域判断=其实质贡献);② 归档时把 `by_city.csv`+两脚本并入 Zenodo(raw 2.5GB DB 太大,附数据获取说明)。

**结构化处理 + 金额(2026-06-19,Andy 要求 B 方案爬金额)**:确认结构化抽取从未做(detail/extract 全 0)。已做不需爬虫的维度:`structured_projects.csv`(360,952 可见+功能项目,区域+内容类别+标题规模,amount 空列预留)。**金额爬取实测后判定不可行**:建设类招标(002002/002007/002001=公园/道路/污水)正文在 **JS 注入的 PDF 附件**里(`.pdfurl` 不在静态 HTML),唯一内联金额的政府采购 002011 在可见/功能里仅占 6/200,000≈0%。要拿金额需 headless 渲染→下载 PDF→OCR 解析,几千页、易碎、WAF 限速=数天工程,与"补充性检验"不成比例,**已否决**。~~结论:金额公共源取不到~~。**——此结论已推翻(2026-06-19,Andy 提示"看招标简介")**:中标 PDF 那条路确实不行,但**金额本就在招标简介里**,只是原爬虫 `cl:200` 把简介截断丢了。省级 inteligentsearch 改 `cl:3000` 即返回完整简介含投资额(无需 PDF/headless)。`repull_amounts.py` 重拉 2023-2024 → **18,406 个去重项目金额**(可见 13,818/功能 4,588):中位 ¥489万≈¥471万(典型等大),可见独占高额长尾(P99 8.66亿 vs 2.02亿;max 114.57亿杭州地铁7号线)。频次(3:1)+大额头部双维度可见占优。§4.3 已补金额段;raw sum 比 7.67 弃用(长尾敏感)。详见 `phase-L-bidding/RESULTS.md` + `amount_summary.json`。**R-4 由此从"频次only"升级为"频次+金额"两维,且全部可复现落盘。**

**词表审定定稿(2026-06-19,DeepSeek-4.0 + 刘灿)**:`deepseek_adjudicate.py`(deepseek-v4-pro,温度0)对 59 词判 52 keep/5 gate/2 drop;`liucan_review.html` 给刘灿复核,**刘灿反馈 DeepSeek 判断准确无误、全部采纳**。`bidding_lexicon.py` 升 v2(drop 花园/地标;gate 道路/大道/景观/市容/步行街)。重跑定稿:**频次 2.02/2.12/2.08,97/108 地市县,金额中位 ¥578万 vs ¥471万、P99 比 4.45、max 114.57亿地铁**。§4.3 + RESULTS + evidence-core 全部更新到 v2 终值;图 `fig_bidding_by_city` 重生成(97/108,中位 1.79)。**R-4 完全收口(频次+金额,LLM 辅助审定 + 领域专家签字,全可复现)。** 方法论:§4.3 已写明"LLM 辅助审定 + 领域专家签字",与正文 LLM-ensemble 主题一致。

## 2026-06-19 (续3) — 剩余工作自主执行(response/cover/文献/图/DOCX)

**本会话产出**:
- **Response letter 重写**(`06-submission/response-to-reviewers-R1.md`):加"作者团队"段(Liu Can 招标验证 / Zhihui Li 第二编码,ICMJE);C1–C5 逐条写明**如何修改优化**(行为效度表、段级验证+多义天花板+LLM+人际 κ=0.70、降级、收窄+招标频次+金额);落款三作者。
- **Cover letter 重写**(`submission/cover_letter_jcss.md`):三作者、新标题、收敛论点+新证据、复现声明(链接重存中)。
- **近三年文献**:CrossRef 查证后加 2 篇真引文 — [21] Gilardi et al. 2023 (PNAS, 10.1073/pnas.2305016120)、[22] Heseltine & Clemm von Hohenberg 2024 (Research & Politics, 10.1177/20531680241236239);引于 §3.4/§5.2。Wu&Zhou 2018 CrossRef 查无(CNKI 中文源)→ 仍待 Andy(R-1)。
- **两张主图**(原 Fig1-4 都是被降级内容,正文只剩表):新 **Fig 1 精度阶梯**(0.10→0.60 天花板→LLM 0.84)、**Fig 2 行为同步**(系数图:CIR+0.025*/具体+0.010*/朴素 n.s.,lead 干净)→ `04-figures/fig1_precision_ladder.* / fig2_comovement.*`,引于 §3.3/§4.2;旧 Fig1-4 标记转 ESM(figure_captions.md 已注)。
- **DOCX**(pandoc 3.9):`manuscript_R2.docx`(11,321 词,12 表)、`cover_letter_jcss.docx`、`title_page_R2.docx`、`response-to-reviewers-R2.docx`。
- 最终审计:引文 [1–22] 全有定义、无悬空;无残留旧标题/旧数字/单作者;交叉引用解析正常。

**仍需 Andy/外部(收尾)**:
- **R-1** Wu&Zhou(2018)完整引文([20] 占位;CNKI 查)。
- **R-3** OSF/Zenodo 重存并验证链接可达(含 `master_2002_2024.csv` + phase-J/K/L 脚本数据 + 招标 by_city/amount),发新 reviewer token。
- **EM 上传**(due 2026-07-30):DOCX 已就绪;主图 Fig1/Fig2 PDF 就绪;ESM 重编号按 figure_captions 注。
- (可选)OSF Phase-G/J/L amendment。
- **R-5 标题**:✅ Andy 选定 = *"When Dictionaries Hit a Polysemy Ceiling: Validating a Measure of Visibility Bias with LLMs and Behavioral Evidence"*(已落到 R2 + online appendix;title_page.{md,docx,pdf} 投稿时需同步更新)。
- **R-6 EM 上传**:R2 → DOCX,due 2026-07-30。
