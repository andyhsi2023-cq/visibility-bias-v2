# V2 Evidence Core — honest measurement thesis (2026-06-19)

**Thesis**: Measuring visibility bias in Chinese bureaucratic text — naive dictionaries fail; even a clean concrete dictionary hits a **polysemy precision ceiling**; LLM-ensemble classification is the high-precision route; and the construct's validity is anchored **behaviorally** (the right text measure co-moves with real cosmetic investment under a quasi-exogenous incentive shock).

## 1. Passage validity (visible class) — human gold (n=120) + 3-model ensemble (n≈499)
| lexicon | human precision | human recall | ensemble precision |
|---|---:|---:|---:|
| naive (42 terms; appearance/image + concrete) | **0.10** | 0.43 | 0.37 |
| concrete v3a (20 terms; Wu-Zhou-aligned) | **0.50** | 0.79 | 0.79 |
| concrete v3b (iterated: −园林; +供热/供气/燃气/管线/饮水/水系) | **0.60** | 0.79 | — |

v3b overall accuracy 0.74; functional 0.60 / mixed 0.82 / irrelevant 0.91. Human↔ensemble Cohen κ = 0.66.
**Ceiling cause** (irreducible by term curation): residual polysemy/metaphor — 道路 ("新型工业化**道路**"), 轨道 ("**轨道**交通产业集群"), 园林 ("国家**园林**城市" award). These are genuine infrastructure in the majority of uses, so removing them destroys recall.

## 2. High-precision alternative: LLM-ensemble classification
3 independent families (Gemini 3.1 Pro / ChatGPT 5.5 / DeepSeek): overall accuracy **0.84**, inter-model Fleiss κ = **0.835**. → For high passage precision, LLM classification > dictionary.

## 3. Behavioral / criterion validity (two-way city+year FE, city-clustered SE; officials-turnover panel 2002-2024)
Under retirement-exogenous (age≥57) secretary turnover:
| outcome | turnover L1 | lead (pre-trend) | retirement-exog L1 |
|---|---:|---:|---:|
| real cosmetic investment (CIR, 2005-2015) | +0.025, p=0.000 | −0.009, p=0.26 ✓clean | +0.024, p=0.043 |
| concrete text measure (wr_visibility) | +0.0103, p=0.010 | +0.001, p=0.84 ✓clean | +0.0164, p=0.010 |
| naive VAI (vai_composite) | +0.002, p=0.54 ✗ | — | +0.004, p=0.39 ✗ |

→ The **concrete/valid** text measure co-moves with **real** cosmetic investment under an exogenous incentive shock, clean leads; the **naive** measure does not. The construct is real in behavior, and the right text measure tracks it. **This is the decisive answer to reviewer C1 (rhetoric ≠ strategic bias).**

**VERIFIED 2026-06-19** (`phase-J-criterion-validity/verify_comovement_master.py` → `verify_results_master.csv`): all three rows reproduce EXACTLY from `officials-turnover-cn/02-data/processed/master_2002_2024.csv` (the panel that holds **both** `vai_composite` AND `wr_visibility`; cols city4/year/cir/change/retire_driven/vai_composite/wr_visibility). NOTE: the earlier `replicate_comovement.py` read `main_panel.csv`, which contains ONLY the naive `vai_composite` — so it could verify only the naive null, never the concrete pillar. Source of truth for the criterion-validity table is now `master_2002_2024.csv` + `verify_comovement_master.py`. `wr_visibility` = the concrete "Wu–Zhou-2018-aligned" lexicon (20 visible / 16 functional terms; built by `officials-turnover-cn/03-analysis/scripts/build_workreport_text.py`), distinct from naive `vai_composite` and from the final v4 salience lexicon. Replication archive must therefore include `master_2002_2024.csv` + that build script + `verify_comovement_master.py`.

## 4. Honest scope (NOT used / demoted)
- Physical **stocks** (绿化率/管网密度…): ~zero within-city signal (P0) — not an anchor.
- Yearbook-stock "behavioral anchor": failed P0 (within r≈0.05) — dropped.
- Welfare calibration: assumption-driven — demoted (reviewer C4); criterion validity ≠ welfare claim.
- Human **inter**coder κ: pending a 2nd coder; current is human↔ensemble κ=0.66.
- Merge: officials-turnover-cn is **not** published separately; its retirement-exogenous identification + `wr_visibility` measure are **absorbed** into V2 (no double-publication, no citing-the-unpublished).

## 5. Reviewer map
C1 → §behavioral criterion validity. C3 → §passage validation (human + ensemble; ceiling reported honestly). C4 → welfare demoted; turnover used only for criterion validity. C5 → focused text-as-data measurement paper.

## 6b. 续(2026-06-19):地面以上原理 + 招投标频次

**判别第一性原理(Andy,2026-06-19 修正)**:可见 = **对评估受众(上级/巡视/媒体/市民)的可观察性/显著度**,**非**字面"地面以上"。关键边界案例 = **地铁/轨道交通**:隧道在地下,但市民日用、媒体大书、上级一眼可见 → 显著度拉满 = **可见**(政绩工程典型)。功能 = 隐蔽、仅失效时被注意(管网/排水/污水/供热)。要点:测**概念**靠具体名词(公园/广场/道路/地铁/地标),**不能**靠"形象/示范"这类多义标签词(那正是 0.10 的祸首)。

**精度阶梯(人工金标,可见类)**:naive 0.10 → 具体 0.50 → 迭代(−园林,+供热/燃气/管线/饮水) 0.60 → 含地面地标 0.64 → **v4 显著度原理(含地铁/轨道交通) precision 0.60 / recall 0.79**。→ **词典多义天花板 ≈ 0.60–0.64,词表 curation 破不了**(道路="新型工业化道路"、轨道交通="产业集群" 等隐喻);**含地铁是构念正确选择(召回↑),精度仍封顶**。高精度需 LLM(集成 0.84/κ=0.835)。最终推荐词表:`02-data/processed/lexicon_visible_v4_salience.txt`(33 可见词)+ `lexicon_functional_concrete.txt`(+供热/供气/燃气/管线/饮水/水系)。

**招投标频次验证(浙江全量 2.96M 记录,主体 2019-2026,ggzy.gov.cn)— 2026-06-19 复算落盘**:可见 vs 功能 **项目数比 = 2.31(全 2,957,789 条公告)/ 2.66(发标公告=单项目代理)/ 2.36(2019-24 窗)**;**103/109 地市县 可见>功能**(中位 2.2,范围 0.58-21.49;少数例外为小县:长兴/江山/定海/莲都/天台/嵊泗)。"形象工程项目多"✓ 且跨地市稳健。**金额取不到**(f_budget/f_win_amount 全空)→ "投资额大"维度由 CIR 覆盖,招投标只补"频次"。脚本+词表+逐市表 `phase-L-bidding/`(classify_bidding.py / bidding_lexicon.py / by_city.csv / RESULTS.md;原始库 ggzy.db 2.5GB 在 P1)。⚠️**更正**:旧稿 2.97 /"10 城无一例外"/ 柯桥13.9 **不可复现**(当时无脚本),已纠正为上述可复现值(柯桥实为 2.5、台州 3.7、杭州 7.1)。刘灿(共同一作,城乡规划)负责该验证的分类与领域判断。

**金额维度(2026-06-19 补,Andy 提示"简介里有信息"——对)**:原爬虫 `cl:200` 把招标简介截断至 203 字、丢了投资额;省级 inteligentsearch 改 `cl:3000` 即返回完整简介含金额(无需爬 PDF,`repull_amounts.py`)。重拉 2023-2024 → **18,406 个去重项目金额**(可见 13,818 / 功能 4,588):中位 ¥489万 vs ¥471万(**典型项目等大**,median 比 1.04),但**可见独占高额长尾**(P99 ¥8.66亿 vs ¥2.02亿,比 4.29;max ¥114.57亿杭州地铁7号线 vs ¥10.68亿)。即可见在**频次(3:1)+大额头部**双维度都占优,非"小而多"。raw sum 比 7.67 弃用(长尾+去重残差敏感)。`amounts_2023_2024.csv` / `amount_summary.json`。

**v2 终值(DeepSeek-4.0 审定 + 刘灿签字,2026-06-19)**:词表精修(drop 花园/地标;context-gate 道路/大道/景观/市容/步行街 = 须含施工词、排除地址/租赁/机构名)。重跑后**频次 2.02(全)/2.12(发标公告)/2.08(2019-24),97/108 地市县可见>功能(中位 1.8)**;**金额(16,794 项)中位 ¥578万 vs ¥471万(1.23)、P99 8.99亿 vs 2.02亿(4.45)、max 114.57亿地铁**。结论不变:可见在频次(~2:1)+大额头部双占优。词表 `bidding_lexicon.py` v2;审定 `lexicon_adjudication_deepseek.csv` + `liucan_review.html`。

## 7. 重写蓝图(section → 内容 → 审稿人)
- **摘要**:✓ 已重写(测量验证案例:naive 败→具体撞天花板→LLM 高精→行为效度决定性)。
- **§1 引言**:论点=政务文本测量的 dictionary 验证案例;构念=地面以上可观察;贡献四点;text-as-data 定位。→ C5
- **§2 理论**:可观察性不对称(地面 vs 隐蔽)作动机,轻。→ C1 动机
- **§3 测量**:词表(naive→具体→地面以上原理)+ 多义诊断(示范/形象/道路)+ 段级验证(人工120+3模型集成)+ 精度阶梯0.10→0.64+天花板 + LLM 集成 0.84/κ0.835。→ C3
- **§4 行为效度(中心)**:退休外生更替→具体文本&CIR 同步(lead 干净)、naive 不动;招投标频次 3:1 补充。→ **C1 决定性**
- **§5 讨论**:多义天花板/LLM 推荐/行为同步=决定性效度;局限(浙江招投标、人工 intercoder 待补第二人、无福利)。→ C4
- **§6 结论**;**response letter**:C1→§4 / C3→§3 / C4→降级 / C5→聚焦。

## 6. Artifacts
naive/concrete human anchors + ensemble: `phase-G/`, `phase-K/`. Criterion validity: `phase-J-criterion-validity/`. Lexicons: `02-data/processed/lexicon_visible_concrete.txt` (+ functional). Audited twin source: `officials-turnover-cn/02-data/processed/{main_panel,master_2002_2024}.csv`.
