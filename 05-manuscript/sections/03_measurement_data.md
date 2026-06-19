# 3. Measurement and Validation

This section builds and validates the text measure along the ladder previewed in §1. We first situate the measurement target in the text-as-data tradition (§3.0) and document why the source corpus is consequential (§3.1). We then construct a naive dictionary and show, against human passage-level coding, that it fails (§3.2.1); refine it to a concrete, salience-based lexicon that improves sharply but meets a polysemy ceiling (§3.2.2–§3.3); and benchmark an LLM-ensemble classifier that clears the ceiling (§3.4). We close by relabeling the reliability and external checks for exactly what they establish (§3.5) and stating the measure's scope and data (§3.6–§3.7).

## 3.0 Positioning in the text-as-data literature

We position the measure as a domain-specific application *within* the literature that measures political attention and expressed agendas from text — not as a new latent-variable method. Table 0 locates it against four established instruments on the dimensions that matter for a measurement-validation paper.

**Table 0. The visibility measure relative to existing text-based policy-attention instruments**

| Instrument | Measurement target | Construction | Passage-level human validation | Behavioral / criterion validity |
|---|---|---|---|---|
| Slapin–Proksch Wordfish [4] | Ideological position, party manifestos | Latent Poisson scaling | No | Cross-source (expert surveys) |
| Grimmer [2] expressed priorities | Topic attention, U.S. press releases | Bayesian hierarchical topic model | Partial (hand-coding agreement) | No |
| Gentzkow–Shapiro [11] / GST [3] slant | Partisan slant, U.S. news | Supervised phrase frequency | No | Cross-source (vote shares) |
| Shi [12] CCP ideology topics | Ideological positioning, party documents | Structural topic model | Face validity only | No |
| **This paper** | **Visible-vs-functional infrastructure attention, Chinese GWRs** | **Dictionary → LLM-ensemble; reported precision ceiling** | **Yes — confusion matrix + error taxonomy + ceiling** | **Yes — co-movement with real investment under an exogenous shock** |

Two features distinguish the exercise. First, the measurement target is *compositional* — the share of attention across two substantively paired asset classes within one policy domain — rather than position on an ideological continuum or emphasis across many topics; this is continuous with the expressed-agendas tradition. Second, and more importantly, we subject the measure to two tests applied work usually omits: direct passage-level human validation *with the failure honestly reported*, and behavioral criterion validity against real expenditure (§4).

## 3.1 The corpus and its institutional standing

We measure visibility attention from the universe of annual prefecture-level **government work reports** (GWRs). Our corpus covers **6,294 GWRs from 282 prefecture-level cities, 2002–2024**, compiled from provincial government portals and the zhengfugongzuobaogao.com repository; each report (typically 20,000–60,000 Chinese characters) is stored as a UTF-8 file indexed by standardized city name and year.

### 3.1.0 Institutional role and consequentiality of government work reports

The paper's premise is that GWRs are *consequential* texts whose composition reflects what officials choose to make salient to their evaluators. We document, rather than assert, the institutional basis.

**Drafting and approval.** A municipal GWR is drafted by the city government's research office under the mayor's direct supervision, revised through successive leadership readings, and formally delivered by the mayor to the annual session of the municipal People's Congress, which reviews and votes to adopt it. It is therefore the government's official, on-the-record statement of the year's work and the coming year's commitments — neither a personal essay nor a press release.

**Link to cadre evaluation.** Under the target-responsibility system and performance-assessment regime, the commitments enumerated in the GWR feed the quantified targets against which the prefecture's leadership is subsequently assessed by the superior provincial Party authority. The report is an *input to* the promotion-relevant evaluation process, not merely a record of it.

**Audiences and "visible to whom."** The GWR's audiences include the superior authority that controls promotion, the NPC delegates who vote on it, and the public and media to whom it is released. The audience relevant to our construct is the *superior*: our salience criterion is defined relative to this upward principal, which is precisely the channel through which the observability asymmetry of §2.1 operates. Lateral citizen approval is a distinct channel, reported as a bounded null (§4.4), not the mechanism.

## 3.2 A lexicon ladder for visibility

### 3.2.1 The naive dictionary and why it fails

A natural first dictionary pairs **42 visible terms** — appearance/image words (形象 "image", 示范 "model/demonstration", 面子 "face", 展示 "display", 美丽 "beautiful", 样板 "template") together with concrete construction terms — against **38 functional terms**. Visibility attention is the count ratio

$$\text{VAI}_{it} = \frac{v_{it}}{v_{it}+f_{it}} \in [0,1],$$

independent of report length; we require $v_{it}+f_{it}\ge 5$. We refer to this construction as the **naive** measure (the `vai_composite` series used in §4).

Validated at the passage level (§3.3 design), the naive visible class **fails badly**: its precision against human coding is only **0.10** (recall 0.43), and against a three-model LLM ensemble 0.37 (recall 0.88). The diagnosis is decisive and single-cause: the abstract appearance/image words are **polysemous** and fire pervasively outside infrastructure. One term — **示范** — alone accounts for **61 of 84** visible-class false positives (示范区 "demonstration zone", 示范项目 "model project", 改革示范 "reform model"), roughly 70% of the total; 文明城市, 展示, 美丽, and 形象 supply most of the remainder (Online Appendix C.8, error taxonomy). Recall is healthy, so the problem is not missing content but over-firing on non-infrastructure rhetoric — exactly the false-positive pathology Reviewer #1 asked us to surface.

### 3.2.2 A concrete, salience-based lexicon

The fix is surgical, not wholesale: blanket-pruning the thirteen most polysemous terms lifts visible precision to 0.59 but collapses recall to 0.47 (over-correction). Instead we rebuild the visible lexicon on the **salience principle** of §2.1 — keying on *concrete, observability-bearing referents* rather than abstract appearance words — mirroring the cosmetic-versus-functional split of the MOHURD Urban Construction Statistical Yearbook investment categories (§3.7). The concrete visible set comprises **20 terms** (绿化 greening, 公园 park, 广场 square, 道路/路网 roads, 桥梁 bridge, 景观 landscape, 亮化 lighting, 地铁/轨道 metro/rail, 大道 boulevard, …); the concrete functional set comprises **16 concealed-utility terms** (排水 drainage, 管网 pipe network, 污水 sewerage, 供水 water supply, 防洪 flood control, 地下管廊 underground utility tunnel, …). This concrete measure is the `wr_visibility` series validated behaviorally in §4.

Two refinements follow the construct. First, the **metro/rail boundary case** (§2.1): we retain 地铁 and replace the bare polyseme 轨道 ("orbit"/"track"/"industry rail") with the unambiguous 轨道交通 / 轻轨 / 城市轨道, and add above-ground landmarks (地标, 体育馆, 博物馆, 雕塑). Second, we drop 园林, which mostly appears in the award title 国家园林城市 rather than as construction, and add concealed-utility terms to the functional side (供热 heating, 燃气 gas, 管线 pipelines, 饮水 potable water). This salience-refined lexicon (`lexicon_visible_v4_salience.txt` + `lexicon_functional_concrete.txt`) is our recommended dictionary.

## 3.3 Passage-level human validation

**Design.** We draw a stratified random sample of sentences (stratified by dictionary hit-type, city tier, and era) and code each independently as **visible / functional / mixed / irrelevant**. A **human gold standard of 120 sentences** anchors the analysis; a three-model LLM ensemble (§3.4) labels a larger **499-sentence** sample, licensed to scale by its agreement with the human anchor. Against the human labels we report a full confusion matrix, per-class precision/recall/F1, verbatim false-positive/false-negative exemplars, and an error taxonomy. The sampler, four-class coding manual, and pre-set success criteria are pre-registered as an amendment to OSF ZMJY5 (`03-analysis/phase-K/`). The 120-sentence gold standard was independently double-coded by two coders on an identical sentence set, with **substantial human intercoder agreement (Cohen κ = 0.70**; Online Appendix C.8); we also report human↔ensemble agreement (Cohen κ = 0.66, §3.4) as a scaling check.

**Results: a precision ladder.** Curation moves visible-class precision up a clear ladder against the human gold standard (Figure 1):

**Table 1. Visible-class passage validation against human coding (n = 120 gold)**

| Lexicon | Visible precision | Visible recall | Note |
|---|---:|---:|---|
| Naive (42 appearance+concrete terms) | **0.10** | 0.43 | 示范/形象/展示 polysemy |
| Concrete, salience-based (MOHURD-aligned) | **0.50** | 0.79 | verified, `score_anchor.py` |
| Concrete, refined (−园林; +concealed-utility terms) | **0.60** | 0.79 | targeted disambiguation |
| Concrete + above-ground landmarks | **0.64** | — | approaching the ceiling |

The concrete lexicon's overall four-class accuracy is 0.74 (functional precision 0.60, mixed 0.80, irrelevant 0.90; full confusion matrix in Online Appendix C.8). The gain from 0.10 to 0.60 is large and entirely attributable to replacing abstract appearance words with concrete salience-bearing referents.

**The polysemy ceiling.** Curation cannot push visible precision past roughly **0.60–0.64**. The residual errors are **irreducible by term selection** because the offending words are genuinely infrastructure in the *majority* of their uses, so deleting them destroys recall:

- 道路 *dàolù* ("road") is also the metaphor 新型工业化道路 ("the *path* of new-type industrialization");
- 轨道交通 *guǐdào jiāotōng* ("rail transit") also names the 轨道交通产业 ("rail-transit *industry*");
- 园林 *yuánlín* ("garden/landscaping") is also the award 国家园林城市 *guójiā yuánlín chéngshì*.

This is a general property of compositional constructs carried by everyday words: dictionary precision is bounded by the language, not by the analyst's effort. We report the ceiling as a *finding*, not a defect to be hidden.

## 3.4 A high-precision alternative: LLM-ensemble classification

Where the ceiling binds, classification — not a longer dictionary — is the route to high precision; recent work finds LLMs increasingly match or surpass human and crowd annotation of political text [5, 20, 21]. We classify each sampled sentence with **three independent LLM families** (Gemini 3.1 Pro, ChatGPT 5.5, DeepSeek), each given the same four-class definition, and take the majority label. The ensemble attains **0.84 accuracy against the human gold standard**, with **inter-model Fleiss κ = 0.835** (substantial-to-near-perfect agreement) — well above the dictionary ceiling. Per class against human coding: visible precision 0.79 / recall 0.96, functional 0.81 / 0.90, mixed 0.86 / 0.61, irrelevant 0.91 / 0.81 (`passage_coding_sheet_ensemble.validation.json`). Human↔ensemble agreement is Cohen κ = 0.66.

The practical recommendation is therefore a precision-vs-transparency trade-off made explicit: the concrete dictionary is transparent, free, and reproducible but precision-capped near 0.60; the LLM ensemble reaches 0.84 at the cost of API dependence and lower interpretability. For aggregate city-year indices the dictionary's measurement error is largely classical and attenuates rather than biases (and the behavioral test in §4 uses the dictionary measure, conservatively); for passage-level applications that need precision, the ensemble is preferable.

## 3.5 Reliability and external checks (relabeled)

We previously reported a battery of indirect tests as "construct validity." We relabel each for what it actually establishes:

- **Internal reliability, not validity (E-A).** An independently built 148-term lexicon yields a city-year index correlated at **r = 0.93** with the original. Because both lexicons are curated from the same governance-rhetoric genre, this measures *stability within the lexicon family*, not independent validation. (A half-lexicon bootstrap, E-C, confirms the full lexicon is the minimum stable unit: mean split-half r = 0.18.)
- **A modest external check (E-D).** The text measure correlates with the MOHURD yearbook-derived Cosmetic Investment Ratio (CIR) at **r = 0.24** (p < 10⁻³⁰) over the 2005–2015 overlap — independent evidence from a different data source (accounting, not text), but modest in magnitude and cross-sectional. The decisive external evidence is behavioral, not this correlation (§4).
- **A suggestive within-document pattern (E-B).** Retrospective ("past-year") sections are more visibility-loaded than prospective ("next-year plan") sections (Δ = +0.025, paired t = 8.4 on 4,330 GWRs). This is invariant to lexicon and author, but may partly reflect *genre* differences between report sections, so we treat it as suggestive corroboration only.
- **A failed external validation (E-F).** A pre-registered test applying the lexicon to Chinese-Wikipedia city articles **fails**: r = −0.15 against a pre-registered [0.3, 0.7] criterion. We report it plainly, not as a feature. The likely cause is genre mismatch — encyclopedic articles produce few lexicon hits (median 6 vs 50+ per GWR), yielding noisy ratios — which means Wikipedia-zh was a poorly chosen third-party source; an appropriate policy-rhetoric external validation remains to be done. Logged as deviation D-E-2 (Appendix D).

## 3.6 Scope of the measure

On the strength of the passage-level validation and — decisively — the behavioral co-movement of §4, we claim the concrete measure is a validated index of the visible-versus-functional composition of *Chinese municipal governance rhetoric*. We do not claim it measures intrinsic city characteristics, citizen perceptions, or compositional attention in non-governance texts about the same cities; any such use requires separate validation (the Wikipedia null is the cautionary case). And we are explicit that text alone identifies *what is emphasized*; the *strategic* interpretation rests on the behavioral evidence, not on the text in isolation.

## 3.7 Data

The text corpus (§3.1) is combined with: the **MOHURD Urban Construction Statistical Yearbook (2005–2015)**, source of the accounting-based CIR (cosmetic categories ÷ total urban-construction investment; coverage ends in 2015 at a MOHURD reclassification); a **city-year control panel** (282 cities × 2002–2024: ln GDP per capita, ln population, secondary-industry share, urbanization); a **municipal-leader panel** giving party-secretary turnover, tenure, and age (the basis for the retirement-driven turnover shock in §4); the **China Family Panel Studies** (CFPS, 2010–2022) for the individual-level bounded null (§4.4); and **Zhejiang public-procurement records (2019–2024)** for the supplementary frequency check (§4.3). Provenance, field definitions, and linkage rates are in the replication archive (Online Appendix E). The criterion-validity panel (`master_2002_2024.csv`, holding both the naive and concrete text series alongside CIR and the turnover variables) and all code are archived at Zenodo (DOI 10.5281/zenodo.19569978) and pre-registered at OSF (DOI 10.17605/OSF.IO/ZMJY5).
