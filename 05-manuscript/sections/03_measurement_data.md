# 3. Measurement and Validation

## 3.0 Positioning in the text-as-data literature

Before describing the VAI construction, we situate the instrument relative to existing text-based measures of political attention. Table 0 compares VAI across five dimensions against four established instruments.

**Table 0. VAI relative to existing text-based policy-attention instruments**

| Instrument | Measurement target | Construction | Passage-level human validation | Behavioral / criterion validity |
|---|---|---|---|---|
| Slapin–Proksch Wordfish [4] | Ideological position, party manifestos | Latent Poisson scaling | No | Cross-source (expert surveys) |
| Grimmer [2] expressed priorities | Topic attention, U.S. press releases | Bayesian hierarchical topic model | Partial (hand-coding agreement) | No |
| Gentzkow–Shapiro [11] / GST [3] slant | Partisan slant, U.S. news | Supervised phrase frequency | No | Cross-source (vote shares) |
| Shi [12] CCP ideology topics | Ideological positioning, party documents | Structural topic model | Face validity only | No |
| **VAI (this paper)** | **Visible-vs-functional infrastructure rhetoric, Chinese municipal GWRs** | **Expert-coded lexicon, count-ratio (+ LLM-ensemble alternative)** | **Yes — confusion matrix + error taxonomy + reported ceiling** | **Yes — co-movement with real investment under an exogenous shock** |

We position VAI as a domain-specific application within the expressed-agendas tradition rather than a departure from it. Two features distinguish the exercise. First, the target is *compositional*, the share of attention across two substantively-paired asset classes within one policy domain, rather than a position on an ideological continuum. Second, and the focus of this revision, we subject the instrument to two tests applied work usually omits: direct passage-level human validation *with the failure honestly reported*, and behavioral criterion validity against real expenditure (§3.2.7).

## 3.1 The Visibility Attention Index (VAI)

We construct a city-year Visibility Attention Index from the universe of annual *government work reports* (GWRs) delivered at prefecture-level People's Congresses. These reports, typically 20,000–60,000 Chinese characters, are the single most important institutional text a municipal government produces each year. Our corpus covers 6,294 GWRs from 282 prefecture-level cities, 2002–2024, compiled from provincial government portals and the zhengfugongzuobaogao.com repository, each stored as a UTF-8 file indexed by standardized city name and year.

### 3.1.0 Institutional role and consequentiality of government work reports

The paper's premise is that GWRs are *consequential* texts whose composition reflects what officials choose to make salient. We document, rather than assert, the institutional basis.

**Drafting and approval.** A municipal GWR is drafted by the city government's research office under the mayor's direct supervision, revised through successive leadership readings, and formally delivered by the mayor to the annual session of the municipal People's Congress, which reviews and votes to adopt it. It is therefore the government's official, on-the-record statement of the year's work and the coming year's commitments, neither a personal essay nor a press release.

**Link to cadre evaluation.** Under the target-responsibility system and performance-assessment regime, the commitments enumerated in the GWR feed the quantified targets against which the prefecture's leadership is subsequently assessed by the superior provincial Party authority. The report is an *input to* the promotion-relevant evaluation process, not merely a record of it.

**Audiences and "visible to whom."** The GWR's audiences include the promotion-controlling superior, the NPC delegates who vote on it, and the public and media to whom it is released. The audience relevant to our construct is the *superior*. The salience criterion is defined relative to this upward principal, which is the channel through which the observability asymmetry of §2.1 operates. The lateral citizen channel is reported as a bounded null (§4.5) rather than asserted as the mechanism.

### 3.1.1 Lexicon construction

The lexicon was built through an iterative expert-coding protocol, seeded from a reading of 50 randomly-sampled reports with terms retained at >85% inter-coder agreement across two coders. A natural first ("naive") lexicon paired 42 visible terms, appearance/image words (形象 *xíngxiàng* "image", 示范 *shìfàn* "model", 面子 *miànzi* "face", 展示 *zhǎnshì* "display") together with concrete construction terms, against 38 functional terms. As the passage-level validation in §3.2.0 shows, this naive lexicon fails: the abstract appearance words are polysemous and fire pervasively outside infrastructure. We therefore refine VAI to a concrete, salience-based lexicon keyed on *observability-bearing referents* rather than appearance words, mirroring the cosmetic-versus-functional split of the MOHURD construction-investment categories (§3.3). The refined version pairs 20 concrete visible terms (绿化 greening, 公园 park, 广场 square, 道路/路网 roads, 桥梁 bridge, 景观 landscape, 亮化 lighting, 地铁/轨道交通 metro/rail, 大道 boulevard, …) with 16 concealed-utility functional terms (排水 drainage, 管网 pipe network, 污水 sewerage, 供水 water supply, 防洪 flood control, 地下管廊 underground utility tunnel, …). The boundary case is metro/rail. It is physically underground yet daily-used, media-celebrated, and unmissable to an evaluating superior, hence maximally *salient* and coded visible (we use the unambiguous 轨道交通/轻轨/城市轨道, not the bare polyseme 轨道). The recommended (concrete) VAI is the `wr_visibility` series; the naive baseline is the `vai_composite` series. Full lexicons and coder statistics are in Online Appendix C.1.

### 3.1.2 VAI formula

For each city-year document we count visible-lexicon frequencies ($v_{it}$) and functional-lexicon frequencies ($f_{it}$) and define

$$\text{VAI}_{it} = \frac{v_{it}}{v_{it} + f_{it}} \in [0,1],$$

a composition share independent of report length; we require $v_{it} + f_{it} \ge 5$.

### 3.1.3 Descriptive statistics

For the concrete VAI, mean ≈ 0.60, with the majority of total variation *within* city over time, which justifies the city and year fixed effects in §4. The within-city time-variation is what the behavioral test in §3.2.7 exploits.

## 3.2 Construct Validity

The central question is whether a text measure captures the construct, the visible-versus-functional composition of infrastructure language, rather than an artifact of lexicon selection or genre. We lead with the most direct evidence, a passage-level comparison against human coding (§3.2.0). We then report a pre-registered battery of indirect checks (E-A–E-F, §3.2.1–§3.2.6), and finally the decisive behavioral criterion-validity test (§3.2.7).

### 3.2.0 Direct passage-level validation against human coding (primary)

We draw a stratified random sample of sentences (by dictionary hit-type, city tier, era) and have them independently coded as visible, functional, mixed, or irrelevant. A human gold standard of 120 sentences, independently double-coded by two coders (dictionary and model labels hidden), anchors the analysis (intercoder Cohen κ = 0.70, substantial; Online Appendix C.8). Against the human labels we report a full confusion matrix, per-class precision/recall, verbatim error exemplars, and an error taxonomy. The findings define a precision ladder (Table 1, Panel A):

- **The naive dictionary fails.** Visible-class precision against human coding is only 0.10 (recall 0.43). The diagnosis is single-cause: one polysemous term, 示范 *shìfàn*, alone produces 60–61 of 84 visible-class false positives (示范区 "demonstration zone", 示范项目 "model project", 改革示范 "reform model"), with 文明城市, 展示, 美丽, and 形象 supplying most of the remainder.
- **The concrete lexicon improves greatly but meets a ceiling.** Restricting to concrete, salience-based terms raises visible precision to 0.50, and to 0.60 after targeted refinement, at 0.79 recall. Curation cannot push past ~0.60–0.64. Residual uses are genuinely metaphorical or categorical (道路 *dàolù* "road" also appears in 新型工业化道路 "the *path* of industrialization"; 轨道交通 *guǐdào jiāotōng* also names the 轨道交通产业 "rail-transit *industry*"), and pruning them destroys recall. This is a polysemy ceiling, not a curation failure.
- **An LLM ensemble clears the ceiling.** Three independent model families (Gemini 3.1 Pro, ChatGPT 5.5, DeepSeek), each given the same four-class definition with the majority label taken, attain 0.84 accuracy against the human gold standard with inter-model Fleiss κ = 0.835. This is the recommended route where high passage precision is required, consistent with recent evidence that LLMs match or surpass human and crowd annotation of political text [5, 20, 21] (the transparency cost is discussed in §5).

The implication for VAI is twofold. The appearance-word naive measure should not be used. The concrete VAI is a usable aggregate index (its errors attenuate in the count ratio), and for passage-critical work an LLM classifier is the high-precision alternative.

### 3.2.1 Replication with an independent dictionary (E-A) — *reliability*

A second concrete lexicon, curated independently from a separate reading of 150 GWRs, yields VAI correlated with the primary at r = 0.93. We report this as internal reliability rather than independent construct validity: both lexicons are drawn from the same governance genre, so overlap is expected.

### 3.2.2 Within-document retrospective-vs-prospective split (E-B) — *suggestive*

Each GWR contains a *retrospective* past-year review and a *prospective* next-year plan; we partition at the first plan marker after character 2000 and compute VAI on each. The model predicts $\text{VAI}_{\text{review}} > \text{VAI}_{\text{plan}}$. We report the differential (§4.2) as a *suggestive* within-document pattern that, as §4.2.2 notes, may partly reflect genre rather than behavior, and it is no longer the lead validity evidence.

### 3.2.3 Dictionary-bootstrap stability (E-C) — *diagnostic*

Random half-lexicon partitions correlate only weakly (mean r = 0.18). Any half is an unstable estimator, so the *full* lexicon is the minimum stable measurement unit. We report this as a transparency limitation.

### 3.2.4 Cross-source correlation (E-D) — *modest external anchor*

VAI correlates with the MOHURD yearbook-derived Cosmetic Investment Ratio (CIR) at r = 0.24 (p < 10⁻³⁰) over the 2005–2015 overlap. This is independent evidence from accounting rather than text, modest in magnitude.

### 3.2.5 Third-party text validation (E-F) — *failed, reported plainly*

A parallel VAI from Chinese Wikipedia city descriptions does not correlate with the primary (r = −0.15, 95% CI [−0.31, +0.02]); the pre-registered band was [0.3, 0.7]. We report the failure plainly (deviation D-E-2). The most likely cause is a genre mismatch (Wikipedia city articles yield a median of 6 lexicon hits vs 50+ for a GWR), which in hindsight made Wikipedia-zh a poorly-chosen third-party source. It bounds the instrument's domain to governance rhetoric.

### 3.2.6 Results of the indirect battery

**Table 1, Panel B. Pre-registered construct-validity battery**

| Test | Quantity | Value | Interpretation |
|---|---|---:|---|
| E-A independent-lexicon | r(VAI, VAI_ext) | **0.93** | reliability, not validity |
| E-B review-vs-plan | Δ | **+0.025** (t = 8.4) | suggestive (may reflect genre) |
| E-C bootstrap half-halves | mean r | 0.18 | full lexicon is minimum unit |
| E-D yearbook cross-source | r(VAI, CIR) | **0.24** (p < 10⁻³⁰) | modest external anchor |
| E-F Wikipedia third-party | r | **−0.15** | **FAILED** (domain mismatch) |

### 3.2.7 Behavioral criterion validity (new) — *the decisive test*

Passage precision is not the question a skeptical reader most wants answered. Even a precise text measure might capture only *rhetoric* rather than *strategic attention* that moves real resources. We therefore add the criterion-validity test the original draft lacked. Using plausibly exogenous, retirement-driven turnover of municipal party secretaries (departure at/above the mandatory-retirement age threshold) as an incentive shock, we ask whether the text measure co-moves with *real, accounting-based* cosmetic investment (CIR). Two-way (city + year) fixed-effects regressions with city-clustered standard errors on the merged 2002–2024 panel (`master_2002_2024.csv`) give (Table 1, Panel C):

**Table 1, Panel C. Co-movement under secretary turnover (two-way FE; city-clustered)**

| Outcome | turnover (t−1) | future turnover (lead, placebo) | retirement-exogenous (t−1) |
|---|---:|---:|---:|
| Real cosmetic investment (CIR) | **+0.025** (p < 0.001) | −0.009 (p = 0.26) ✓ clean | +0.024 (p = 0.04) |
| Concrete / valid VAI (`wr_visibility`) | **+0.010** (p = 0.01) | +0.001 (p = 0.84) ✓ clean | +0.016 (p = 0.01) |
| Naive VAI (`vai_composite`) | +0.002 (p = 0.54) | +0.003 (p = 0.29) | +0.004 (p = 0.39) |

The pattern is exactly what criterion validity requires. In the year after turnover, real cosmetic investment rises and the concrete VAI rises in lockstep, both with clean pre-trends (the future-turnover placebo is null), while the naive VAI does not respond at all. A genre or template artifact would not co-move with money under an exogenous shock; a strategic-attention measure does. This behavioral co-movement, rather than passage precision, is the strongest evidence that the construct is real and that the *valid* (concrete) measure captures it. It is also what licenses the term "visibility bias" rather than merely "visible-infrastructure rhetoric."

The 2005–2015 window is the coverage of the yearbook's municipal fixed-asset *investment*-by-category table (the CIR source), not a window chosen after the fact. As a check, we re-ran the same turnover test on a longer-span *physical-stock* cosmetic measure available for 2002–2024, the annual increment in built-up green-space coverage, and find a co-movement that is directionally consistent but not statistically significant (+0.20, p = 0.12). The behavioral signal is therefore carried by investment composition, which officials can re-direct within a budget year, rather than by slow-moving physical stocks. A cross-sectional physical-stock measure likewise shows no within-city signal.

## 3.3 Data

The text corpus (§3.1) is combined with five further sources. The **China Urban Construction Statistical Yearbook (Ministry of Construction / MOHURD, 2005–2015)** is the source of the accounting CIR (cosmetic categories ÷ total urban-construction investment) and of the cosmetic/functional split the concrete lexicon mirrors. A city-year control panel covers 282 cities × 2002–2024. A municipal-leader panel gives party-secretary turnover, tenure, and age (the basis for the retirement-driven shock in §3.2.7). The China Family Panel Studies (CFPS, 2010–2022) supplies the bounded individual-level null (§4.5). Zhejiang public-procurement records (≈2,957,789 announcements, predominantly 2019–2026, national `ggzy.gov.cn` platform) provide the independent procurement corroboration (§4.3). The criterion-validity panel (`master_2002_2024.csv`, holding both the naive and concrete text series alongside CIR and turnover) and all code are archived at Zenodo (DOI 10.5281/zenodo.19569978) and pre-registered at OSF (DOI 10.17605/OSF.IO/ZMJY5); provenance and linkage rates are in Online Appendix E.
