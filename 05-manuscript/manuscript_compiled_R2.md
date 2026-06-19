# Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation

*Hongyang Xi¹†\* · Liu Can²† · Zhihui Li¹*
*¹ Chongqing Survey Institute Co., Ltd., Chongqing, China · ² Urban and Rural Planning, Guangzhou College of Applied Science and Technology, Guangzhou, China*
*† co-first authors (equal contribution) · \* corresponding author: 26708155@alu.cqu.edu.cn*
*Revision R2 (JCSO-D-26-00240) · compiled 2026-06-19 · venue-agnostic master*

---

# Abstract

We study how to measure *visibility bias* — the rhetorical emphasis on observationally-salient (visible) versus concealed (functional) infrastructure — in Chinese municipal government work reports (6,294 reports, 282 prefectures, 2002–2024), and use it as a case study in validating dictionary text-as-data measures. A naive visibility dictionary fails badly: against human passage-level coding (two independent coders, intercoder κ = 0.70) its visible-class precision is only **0.10**, because polysemous appearance/image terms (e.g., 形象 *xíngxiàng* "image", 示范 *shìfàn* "model/demonstration", 面子 *miànzi* "face") fire pervasively outside infrastructure contexts. Restricting the lexicon to concrete visible-construction terms (roads, greening, parks, bridges vs. drainage, pipes, sewerage), mirroring the cosmetic-versus-functional split of the MOHURD construction-investment categories, raises visible precision to **0.50 (0.60 after targeted refinement) at 0.79 recall** — a large gain that nonetheless meets a **polysemy ceiling**: residual metaphorical/categorical uses (道路 *dàolù* "road" in 新型工业化道路 "the path of new-type industrialization"; 轨道交通 *guǐdào jiāotōng* "rail transit" in 轨道交通产业 "the rail-transit industry") cannot be pruned without destroying recall. For high passage-level precision we therefore turn to **LLM-ensemble classification** (three independent model families), which attains **0.84 accuracy and inter-model agreement (Fleiss κ = 0.835)**. Crucially, we anchor validity **behaviorally**: under quasi-exogenous, retirement-driven secretary turnover, the concrete text measure rises in lockstep with real accounting-based cosmetic investment (clean pre-trends; both significant at the 1–5% level), whereas the naive measure does not respond at all (p ≈ 0.5) — evidence that the *valid* measure captures strategic attention rather than genre or templates. We report failed and assumption-dependent analyses transparently and demote them (a physical-stock external anchor with no within-city signal; a structural welfare calibration). The contribution is methodological: a rigorously-validated procedure — with an honest map of its limits — for measuring compositional policy attention in bureaucratic text, and a demonstration that *behavioral co-movement*, not passage precision alone, is the decisive validity test for such measures.

**Keywords**: text-as-data, dictionary methods, LLM annotation, construct & criterion validity, polysemy, policy attention, China

**Pre-registration**: OSF DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5) (instrument + initial battery); passage-level human/LLM validation and behavioral-validity analyses are pre-specified extensions (Appendix D). **Replication archive**: Zenodo DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978).


# 1. Introduction

Local officials have reason to favor infrastructure their evaluators can see. In China's municipal governments, where careers turn on how superior authorities assess performance, that incentive tilts toward *visible* construction — streetscapes, greening, squares, landmarks, metro — over functionally important but *concealed* works such as drainage, pipe networks, and sewerage. We call this tilt **visibility bias**, and we ask, for one country's local governance, whether it can be measured from official text and whether it is behaviorally real; our window is the annual municipal government work report (GWR).

Measuring such a bias from text is the hard part. Dictionary methods remain among the most widely used tools for measuring political attention from text. They are transparent, cheap, reproducible, and require no training data, which makes them attractive for measuring *what bureaucratic agents emphasize* in corpora of formal documents — legislative speeches, agency reports, municipal plans [1, 2, 3, 4, 8]. Yet the very transparency of a keyword dictionary can mask how weakly it is validated. In applied work a lexicon is often defended by face validity and an aggregate correlation with some external series, while the prior question — *does the dictionary actually classify the right passages?* — is rarely answered with passage-level human coding [6, 7, 18]. This paper takes that question seriously for one concrete measurement problem and follows the answer wherever it leads. The result is less a triumphant new instrument than an honest map of what a dictionary can and cannot do here, what to use instead when it cannot, and — most importantly — how to know whether any of these measures is capturing the construct at all.

What counts as **visible** is what the measurement turns on: the preferential emphasis on *observationally salient* ("visible") urban infrastructure — streetscapes, greening, squares, landmarks — over functionally important but *concealed* infrastructure — drainage, pipe networks, sewerage, heating. The substantive interest is an old one in political economy: when a principal evaluates an agent on what the principal can observe, the agent over-invests in the observable. The measurement interest is sharper. "Visible" is not a surface-appearance category but an **observability/salience** category, defined relative to the audience that evaluates the official (superiors, inspectors, media, citizens). The instructive boundary case is **metro and rail transit**: physically underground, yet daily-used, media-celebrated, and a prestige achievement an evaluating superior cannot miss — hence maximally *salient* and coded visible. Concealed utilities are noticed mainly upon failure. A measure that respects this construct must key on concrete, salience-bearing referents (parks, squares, roads, metro, landmarks), not on abstract appearance words ("image", "model", "showcase") — and getting that distinction wrong, we show, is exactly where naive dictionaries fail.

We proceed along a measurement ladder and report each rung honestly. **(i)** A naive visibility dictionary — appearance/image terms plus concrete construction terms — fails: against human passage-level coding its visible-class precision is only **0.10**, because polysemous appearance words (形象 *xíngxiàng* "image", 示范 *shìfàn* "model/demonstration", 面子 *miànzi* "face") fire pervasively outside infrastructure contexts. **(ii)** Restricting the lexicon to concrete, salience-based construction terms (mirroring the cosmetic-versus-functional split of the MOHURD construction-investment categories) raises visible precision to **0.50, and to 0.60 after targeted refinement, at 0.79 recall** — a large gain that nonetheless meets a **polysemy ceiling**: residual metaphorical and categorical uses (道路 *dàolù* in 新型工业化道路, the *path* of new-type industrialization; 轨道交通 *guǐdào jiāotōng* in 轨道交通产业, the rail-transit *industry*) cannot be pruned without destroying recall. **(iii)** For users who need high passage-level precision, we show that an **LLM-ensemble classifier** (three independent model families) attains **0.84 accuracy with inter-model Fleiss κ = 0.835** — comfortably above the dictionary ceiling. The pattern is likely not unique to this corpus: for compositional constructs carried by polysemous everyday words, dictionary precision may be bounded by the language rather than the analyst's diligence — though we establish this only for Chinese GWR text and offer it as a hypothesis to test elsewhere.

Passage precision, however, is not the question a skeptical reader most wants answered. Even a perfectly precise text measure might capture only *rhetoric* — genre, templates, ritual language — rather than *strategic attention* that moves real resources. We therefore make the paper's decisive move a **behavioral (criterion) validity** test. Using plausibly exogenous, retirement-driven turnover of municipal party secretaries as an incentive shock, we ask whether the text measure co-moves with *real, accounting-based* cosmetic investment. It does, but only the right measure does: in the year after turnover, real cosmetic investment rises (+0.025, p < 0.001) and the **validated concrete text measure rises in lockstep** (+0.010, p = 0.01), both with clean pre-trends, whereas the **naive measure does not respond at all** (+0.002, p = 0.54). A genre or template artifact would not co-move with money under an exogenous shock; a strategic-attention measure does. This behavioral co-movement — not passage precision — is the strongest evidence that the construct is real and that the validated measure captures it.

## 1.1 Contribution

Our contribution is **methodological**, and we position it as a domain-specific application *within* the text-as-data tradition of measuring expressed agendas and political attention [2, 3, 4, 8, 18, 19], not as a departure from it. Four points:

- **A rigorous passage-level validation that reports a precision ceiling.** We supply exactly the validation an applied dictionary paper usually omits — a stratified sentence sample, a four-way human coding scheme (visible / functional / mixed / irrelevant), a full confusion matrix, per-class precision/recall, false-positive/false-negative exemplars, and an error taxonomy — and we use it to *discover and characterize* a polysemy ceiling rather than to certify the instrument.

- **A calibrated high-precision alternative.** We benchmark an LLM-ensemble classifier against the same human gold standard (0.84 accuracy; Fleiss κ = 0.835) and recommend it where the dictionary's ceiling binds, giving practitioners a concrete precision-vs-transparency trade-off rather than an abstract one.

- **Behavioral co-movement as the decisive validity test.** We argue, and demonstrate, that for measures of strategic attention the decisive test is *criterion* validity against real behavior under an exogenous shock — not internal reliability or aggregate cross-source correlation. The retirement-turnover co-movement separates a valid measure from a naive one that is internally stable yet behaviorally inert.

- **Transparent demotion and reproducibility.** We relabel earlier exercises for what they are (an independent-lexicon correlation as *reliability*, not validity; a within-document differential as *suggestive*; an accounting correlation as a *modest external* check) and demote under-identified causal and welfare analyses to the appendix, reported as failed or assumption-dependent rather than as findings. Instrument, gold-standard codings, and analysis code are pre-registered (OSF DOI 10.17605/OSF.IO/ZMJY5) and archived (Zenodo DOI 10.5281/zenodo.19569978), following open-science reporting norms [9, 10].

## 1.2 Roadmap

Section 2 sketches the observability-asymmetry motivation, kept deliberately light. Section 3 builds the measurement ladder — institutional grounding of GWRs, the naive-to-concrete lexicon progression, the passage-level human validation, the polysemy ceiling, and the LLM-ensemble alternative. Section 4 presents the behavioral criterion-validity evidence (the retirement-turnover co-movement) and a supplementary procurement-frequency check. Section 5 draws the methodological lessons and states limitations; Section 6 concludes. Deviations from the pre-registration are logged in Appendix D with reasons, executed substitutes, and effect on sign and significance.


# 2. Theoretical Motivation

This section states, in light form, why we expect compositional text-rhetoric to carry information about visibility bias, and what that implies for validation. The point of the section is to *motivate the measurement problem and define the construct*, not to identify structural parameters. A fuller formal treatment — an official's allocation problem under precision-weighted evaluation, with closed-form comparative statics — is in Online Appendix A; nothing in the paper's evidence depends on it, and we no longer headline the welfare expression it yields (§4.4, §5).

## 2.1 Observability asymmetry and the salience definition of "visible"

A municipal official allocates a finite urban-infrastructure budget across asset classes that differ in how *observable* their output is to the audience that evaluates the official — primarily the superior (provincial) authority controlling promotion, secondarily inspectors, media, and citizens. We define **visible** capital by observability/salience to that audience, not by physical surface:

- **Visible**: output that the evaluating audience readily perceives and attributes to the incumbent — streetscapes, greening, squares, parks, lighting, landmarks, and *metro/rail transit*. Metro is the diagnostic boundary case: its tunnels are underground, yet it is daily-used, media-celebrated, and an unmistakable prestige achievement, so it is maximally salient and coded visible.
- **Functional**: output that is concealed in normal operation and noticed mainly upon failure — drainage, water and gas pipe networks, sewerage, heating, structural safety.

The substantive premise is an **observability asymmetry**: the evaluating audience perceives visible categories with less noise than functional ones ($\omega_V^2 < \omega_F^2$). Three independent proxies for the asymmetry — inspection frequency, media-reporting intensity, and the visibility of failures in the accident record — are consistent with it (Online Appendix C.4). The key conceptual move is that "visible to whom" is answered by the *upward* principal; lateral citizen perception is a distinct channel, which our individual-level analysis treats as a bounded null rather than the mechanism (§4.4).

## 2.2 Why composition should leave a textual trace

When evaluation is weighted toward what is observable, an official maximizing a mix of social and career returns tilts attention toward salient categories — and toward *describing* salient categories — because attention to the legible margin yields more perceived performance per yuan. Two implications follow for measurement, and they structure the rest of the paper:

1. **A valid text measure of compositional attention should track real visible-investment composition.** This is the basis for cross-source and, crucially, behavioral validation: the right measure should co-move with accounting-based cosmetic investment, and should do so under exogenous shifts in career incentives (§4).

2. **The signal lives in concrete, salience-bearing referents.** Because the construct is about *which assets* are emphasized, the measure must key on concrete nouns (parks, squares, roads, metro, landmarks) rather than abstract appearance words ("image", "model", "showcase"). The latter are polysemous and decoupled from infrastructure, which §3 shows is the proximate cause of naive-dictionary failure.

## 2.3 Scope of the theoretical role

The model is a source of *predictions about what a valid measure should look like and do*, not a source of causal identification of incentive parameters. We do not claim to estimate $(\omega_V,\omega_F)$ or a welfare loss as a result; the structural welfare calibration that an earlier draft headlined is demoted to an assumption-dependent illustration (§4.4, Online Appendix A/C.7). A reader interested only in the measurement contribution can proceed directly to §3; the observability-asymmetry premise is invoked again only to interpret the behavioral co-movement in §4.


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

Validated at the passage level (§3.3 design), the naive visible class **fails badly**: its precision against human coding is only **0.10** (recall 0.43), and against a three-model LLM ensemble 0.37 (recall 0.88). The diagnosis is decisive and single-cause: the abstract appearance/image words are **polysemous** and fire pervasively outside infrastructure. One term — **示范** — alone accounts for **60–61 of 84** visible-class false positives (示范区 "demonstration zone", 示范项目 "model project", 改革示范 "reform model"), roughly 70% of the total; 文明城市, 展示, 美丽, and 形象 supply most of the remainder (Online Appendix C.8, error taxonomy). Recall is healthy, so the problem is not missing content but over-firing on non-infrastructure rhetoric — exactly the false-positive pathology Reviewer #1 asked us to surface.

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

The text corpus (§3.1) is combined with: the **MOHURD Urban Construction Statistical Yearbook (2005–2015)**, source of the accounting-based CIR (cosmetic categories ÷ total urban-construction investment; coverage ends in 2015 at a MOHURD reclassification); a **city-year control panel** (282 cities × 2002–2024: ln GDP per capita, ln population, secondary-industry share, urbanization); a **municipal-leader panel** giving party-secretary turnover, tenure, and age (the basis for the retirement-driven turnover shock in §4); the **China Family Panel Studies** (CFPS, 2010–2022) for the individual-level bounded null (§4.4); and **Zhejiang public-procurement records (predominantly 2019–2026)** for the supplementary frequency check (§4.3). Provenance, field definitions, and linkage rates are in the replication archive (Online Appendix E). The criterion-validity panel (`master_2002_2024.csv`, holding both the naive and concrete text series alongside CIR and the turnover variables) and all code are archived at Zenodo (DOI 10.5281/zenodo.19569978) and pre-registered at OSF (DOI 10.17605/OSF.IO/ZMJY5).


# 4. Behavioral Criterion Validity

Passage precision (§3) establishes that the concrete measure classifies the right *sentences*. It does not establish that the measure captures *strategic attention* rather than genre, template, or ritual language — the central concern of Reviewer #1, and the reason a precise text measure can still be substantively empty. This section supplies the decisive test: does the text measure co-move with **real, accounting-based** behavior under a plausibly exogenous shift in career incentives? It does, and only the valid measure does. We then add a supplementary procurement-frequency check (§4.3) and report transparently the exercises that do *not* support causal or welfare claims (§4.4).

## 4.1 Identification: retirement-driven secretary turnover as an incentive shock

The arrival of a new municipal party secretary is an incentive shock: an incoming secretary with promotion ambitions has heightened reason to produce *observable* achievements within a short evaluation window. If the visibility construct is behaviorally real, a turnover should raise both real cosmetic investment and the (valid) text measure, and should do so *after* the turnover, not before.

Plain turnover may be endogenous — under-performing cities may receive new leadership. We therefore isolate **retirement-driven turnover** (secretary departure at or above the mandatory-retirement age threshold), which is driven by the official's age rather than by local infrastructure conditions and is thus plausibly exogenous to a city's cosmetic-investment demand. For each outcome $y_{it}$ we estimate two-way fixed-effects regressions on the merged 2002–2024 city panel,

$$y_{it} = \beta\,\text{Turnover}_{i,t-1} + \mu_i + \tau_t + \varepsilon_{it},$$

with city ($\mu_i$) and year ($\tau_t$) fixed effects and standard errors clustered by city. We report the one-year-lag effect (turnover last year → outcome this year), a **future-turnover lead** as a pre-trend/placebo test (which should be ≈ 0 under clean identification), and the retirement-exogenous lag. The three outcomes are: real cosmetic investment (CIR, the MOHURD accounting series), the **concrete/valid** text measure (`wr_visibility`), and the **naive** text measure (`vai_composite`). This analysis is an independent re-estimation; code and outputs are in `03-analysis/phase-J-criterion-validity/` (`verify_comovement_master.py` → `verify_results_master.csv`).

## 4.2 The co-movement result

**Table 2. Co-movement under secretary turnover (two-way FE, city-clustered SE)**

| Outcome | Turnover (t−1) | Future turnover (lead) | Retirement-exogenous (t−1) |
|---|---:|---:|---:|
| Real cosmetic investment (CIR) | **+0.025** (p < 0.001) | −0.009 (p = 0.26) ✓ clean | +0.024 (p = 0.04) |
| **Concrete / valid text** (`wr_visibility`) | **+0.010** (p = 0.01) | +0.001 (p = 0.84) ✓ clean | +0.016 (p = 0.01) |
| **Naive text** (`vai_composite`) | +0.002 (p = 0.54) ✗ | +0.003 (p = 0.29) | +0.004 (p = 0.39) ✗ |

*n ≈ 3,082 (CIR), 5,005 (concrete), 5,011 (naive) city-years.*

The pattern (Figure 2) is exactly what behavioral validity requires and is the paper's central result:

1. **Real cosmetic investment rises** in the year after turnover (+0.025, p < 0.001), with a clean pre-trend (the future-turnover lead is negative and insignificant). The same holds under the retirement-exogenous shock (+0.024, p = 0.04). The construct is real in money, not only in words.
2. **The valid text measure rises in lockstep** (+0.010, p = 0.01; retirement-exogenous +0.016, p = 0.01), again with a clean lead. The concrete measure tracks real behavior under an exogenous incentive shift.
3. **The naive measure does not respond at all** (+0.002, p = 0.54; retirement-exogenous +0.004, p = 0.39). It is internally stable (§3.5, E-A r = 0.93) yet behaviorally inert.

A genre or template artifact would not co-move with real expenditure under an exogenous shock; a strategic-attention measure does. The contrast between the valid and naive measures is the crux: passage validation tells us *which* measure to trust, and the behavioral test confirms that the trusted measure — and only it — captures attention that moves resources. This is the decisive answer to the rhetoric-versus-strategy question. It also reframes what validity means for measures of this kind: **behavioral co-movement, not internal reliability or aggregate cross-source correlation, is the test that separates a valid measure from a stable-but-empty one.** (The behavioral test uses the concrete dictionary at its 0.50-precision construction — a conservative choice; classical measurement error attenuates toward zero, so the true co-movement is, if anything, stronger.)

## 4.3 Supplementary check: procurement frequency

As an independent behavioral angle we classify the universe of Zhejiang public-procurement announcements (**2,957,789 records**, predominantly 2019–2026, from the national `ggzy.gov.cn` platform) by the same visible-versus-functional construction distinction. **Visible-type projects outnumber functional ones by roughly 2-to-1 overall** (2.1-to-1 among first-stage tender notices, the cleanest one-per-project proxy), and the tilt is pervasive rather than local: visible exceeds functional in **97 of 108** Zhejiang localities with sufficient volume (median city ratio 1.8; the few exceptions are small county-level units; Online Appendix Figure ESM-6). This corroborates the compositional tilt in an entirely separate, large-scale data source. Going beyond counts, we recover each project's **investment amount** from the tender briefs themselves (16,794 award-stage projects, 2023–2024). Visible and functional projects are of **broadly similar typical size** (median ¥5.8M vs ¥4.7M), but the visible category owns the high-value tail: its 99th percentile (¥0.90B vs ¥0.20B) and maximum (¥11.5B — the Hangzhou Metro Line 7 contract — vs ¥1.07B) are several times larger, because the biggest construction outlays (metro/rail, arterial roads, landmark parks) are visible-salient while concealed-utility works top out an order of magnitude lower. Visible construction therefore predominates on both **frequency** (≈2:1 by count) and the **high-value tail** — not merely because visible projects are small and numerous. The visible/functional keyword classification was refined by LLM-assisted adjudication with **domain-expert (urban- and rural-planning) sign-off** (Authors' Contributions); the lexicon, re-pull and analysis code, per-city table, and amount distribution are deposited (`03-analysis/phase-L-bidding/`). One caveat remains: a "project" is proxied by the deduplicated award record, so the *count* comparison (less so the amount comparison) is sensitive to how works are packaged; the accounting-based CIR (§4.2) supplies the independent expenditure-share corroboration.

## 4.4 Demoted exercises: transparent reporting of failed / assumption-dependent tests

Three exercises an earlier draft treated as contributions are demoted to supporting material and reported transparently; none is part of the main evidentiary structure.

**Causal inspection event study — definitively null.** The pre-registered prediction that central anti-corruption inspections reduce visibility attention does not survive: a narrow-window TWFE estimate has the predicted sign (β = −0.065, p = 0.01) but a heterogeneity-robust Sun–Abraham estimator attenuates it to insignificance, and extending the sample to the 2016–2017 rounds **reverses the sign** (β = +0.016; all nine cohort effects positive). The narrow-window result is a staggered-treatment-heterogeneity artifact [14, 15, 16], not a causal effect (Appendix D, deviations D-B-1/2/3). Note that the retirement-turnover design of §4.2 serves a *different* purpose — measurement (criterion) validity, not a causal welfare magnitude — and is methodologically distinct from this failed design.

**Physical-stock external anchor — null.** We also tested whether the text measure tracks *physical* infrastructure stocks (greening rate, pipe-network density, and similar yearbook series) as an external anchor. These stocks carry essentially no within-city signal over the period (a flow-versus-stock mismatch: annual rhetoric and investment are flows, accumulated stocks are not), so the anchor fails at the within-city level and is not used; the accounting-based CIR (a flow) is the appropriate external series.

**Individual-level micro-foundation — bounded null.** Amenity-category-specific satisfaction items are absent from the public CFPS panel; substituted general outcomes (government evaluation, life satisfaction, self-rated health) show no effect above |d| = 0.011 (TOST rejects |d| ≥ 0.10). This bounds a citizen-popularity channel but does not test the upward-signaling mechanism; we report it as exploratory (Appendix D, D-F-1).

**Structural welfare calibration — assumption-dependent, no headline.** The §2 model yields a closed-form welfare-loss expression; calibrating it with the observed compositional share and an assumed social optimum produces single-digit ¥-billion figures. **We deliberately attach no headline number.** The estimate depends on the Cobb–Douglas form, the social-optimum benchmark, and the text-to-spending mapping — assumptions stronger than the evidence warrants. Full derivation and sensitivity are in Online Appendix A and C.7; we treat it only as an illustration of what the model implies.

## 4.5 Summary

The paper's evidentiary spine is the behavioral co-movement of §4.2: under an exogenous, retirement-driven incentive shock, real cosmetic investment and the *valid* concrete text measure rise together with clean pre-trends, while the *naive* measure does not move. Procurement frequency corroborates the compositional tilt in an independent source. Causal identification of *what drives* visibility bias (the inspection design) fails and is reported as such; the citizen-channel and welfare exercises are bounded or assumption-dependent and demoted. What the paper establishes is a *validated measure* of compositional attention whose validity is anchored in real behavior — not a causal or welfare result.


# 5. Discussion

## 5.1 What the paper establishes

Taking the rungs together, the paper delivers a *validated* measure of compositional policy attention and an honest account of how far each validation move carries. A naive dictionary fails at the passage level (visible precision 0.10); a concrete, salience-based lexicon raises precision to 0.50–0.60 but meets a polysemy ceiling near 0.60–0.64; an LLM ensemble clears the ceiling (0.84 accuracy, Fleiss κ = 0.835); and — decisively — the valid concrete measure co-moves with real cosmetic investment under an exogenous, retirement-driven incentive shock (+0.010, p = 0.01, clean pre-trend), while the naive measure does not (+0.002, p = 0.54). The construct is real in behavior, and the right text measure tracks it.

## 5.2 Methodological lessons

Within this single-country case (Chinese municipal GWRs), three lessons emerge that may transfer — offered to be tested elsewhere, not assumed.

**Lesson 1 — Dictionary precision is bounded by polysemy, not by effort.** For compositional constructs carried by everyday words, a non-trivial share of keyword occurrences are metaphorical or categorical (道路 as "the *path* of industrialization"; 轨道交通 as the rail-transit *industry*). Because these words are genuinely on-construct in the majority of uses, pruning them to raise precision destroys recall, so a precision ceiling is reached that no amount of curation breaks. Reporting this ceiling — rather than tuning a lexicon until an aggregate correlation looks acceptable — should be standard practice. The diagnostic is cheap: a few hundred human-coded passages and a per-class confusion matrix reveal it immediately.

**Lesson 2 — Behavioral co-movement is the decisive validity test for measures of strategic attention.** Internal reliability (E-A, r = 0.93) and aggregate cross-source correlation (E-D, r = 0.24) are routinely offered as "validation," but our naive measure is internally reliable and still behaviorally inert. What separates a valid measure from a stable-but-empty one is whether it *moves with real behavior under an exogenous shock*. Where an incentive shock and an accounting outcome are available, criterion validity of this kind should outrank passage precision and internal reliability in the hierarchy of evidence.

**Lesson 3 — Use LLM-ensemble classification where the dictionary ceiling binds, and report inter-model agreement.** When high passage precision is required, a multi-family LLM ensemble is the practical route (0.84 here) — consistent with a fast-growing literature showing LLMs match or surpass human and crowd annotation of political text [5, 20, 21] — and inter-model agreement (Fleiss κ) is the natural reliability statistic to report alongside accuracy. The transparency cost is real, so the choice is a genuine trade-off: dictionaries for transparent, reproducible aggregate indices with attenuating error; LLM ensembles for precision-critical passage-level work.

## 5.3 Limitations

We are explicit about what the paper does not establish.

- **Intercoder agreement is substantial but not perfect.** Two independent human coders reach Cohen κ = 0.70 on the 120-sentence gold set; residual disagreement concentrates on the visible-versus-mixed boundary — itself a manifestation of the polysemy the paper documents — so passage-level precision/recall carry a few points of coder-judgment uncertainty.
- **The procurement check is provincial.** It covers Zhejiang only; project frequency *and* investment amount both corroborate the tilt, but a "project" is proxied by the deduplicated award record, so the count comparison remains sensitive to how works are packaged. National generalization is untested.
- **Causal identification of drivers is not achieved.** The inspection event study fails under heterogeneity-robust estimation; the retirement-turnover design supports *measurement* validity, not a causal theory of what produces visibility bias.
- **No welfare claim.** The structural welfare figure is assumption-dependent and demoted; we attach no policy magnitude to it.
- **External (non-governance) validity is not established.** The Wikipedia null bounds the measure to governance rhetoric; an appropriate policy-rhetoric third-party validation (e.g., Xinhua local-policy news, CNKI key-newspaper coverage) remains future work.

## 5.4 Portability

The validation protocol — seed a dictionary, validate at the passage level, *report the ceiling*, escalate to LLM classification where needed, and anchor validity behaviorally against an accounting outcome under an exogenous shock — could plausibly transfer to other settings where bureaucratic agents produce structured, consequential annual documents (e.g., EU National Reform Programmes; Indian state budget speeches; Mexican municipal *Plan de Desarrollo* documents), though we have not tested it outside China. What is *not* portable is the specific lexicon and the institutional observability-asymmetry parameters, which require re-derivation in each context. The transferable contribution is the validation discipline, not the keyword list.

---

# 6. Conclusion

We set out to measure visibility bias in Chinese municipal government work reports and, in doing so, to take seriously the question applied dictionary work usually skips: does the measure capture the construct? The answer is a ladder. A naive dictionary fails (visible precision 0.10) because abstract appearance words are polysemous; a concrete, salience-based lexicon improves greatly (0.50–0.60) but hits a polysemy ceiling near 0.60–0.64; an LLM ensemble clears it (0.84, Fleiss κ = 0.835); and the valid measure — unlike the naive one — co-moves with real cosmetic investment under an exogenous, retirement-driven incentive shock. The contribution is methodological: a rigorously validated, behaviorally anchored procedure for measuring compositional policy attention in bureaucratic text, with an honest map of its limits and a high-precision alternative where the dictionary stops.

Two points may outlast this one-country case and invite testing elsewhere. First, polysemy imposes a precision ceiling on dictionary measures of everyday-word constructs that curation cannot break, and that ceiling should be reported, not hidden. Second, for measures of strategic attention the decisive validity test is behavioral co-movement under an exogenous shock — not internal reliability, and not passage precision alone. We invite extension along three lines: a policy-rhetoric third-party corpus to strengthen external validity; additional exogenous incentive shocks to widen the criterion-validity base; and application of the validate-report-the-ceiling-then-escalate protocol to bureaucratic text in other institutional settings.

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI 10.5281/zenodo.19569978; GitHub: andyhsi2023-cq/visibility-bias-v2.

---

# Statements and Declarations

**Competing Interests.** The authors declare no competing financial or non-financial interests related to this work.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work was conducted as part of the authors' professional research activities.

**Authors' Contributions.** Hongyang Xi and Liu Can contributed equally and are co-first authors. Hongyang Xi (corresponding author) conceived the study, constructed the lexicons and the LLM-ensemble classification, performed the data collection and statistical analysis, drafted the manuscript, and prepared the replication archive. Liu Can constructed and verified the public-procurement (bidding) evidence (§4.3), contributing urban- and rural-planning domain expertise to the visible-versus-functional classification of construction projects. Zhihui Li independently performed the second passage-level coding of the validation sample for the intercoder-reliability assessment (§3.3). All authors contributed to the critical revision of the manuscript, reviewed and approved the final version, and are accountable for the integrity of the work.

**Data Availability.** All data, lexicons, code, and intermediate outputs supporting the findings are archived at Zenodo (DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978)) and mirrored on GitHub (`andyhsi2023-cq/visibility-bias-v2`). The Zenodo record is Restricted during peer review; reviewer access is provided via the token in the cover letter and will be flipped to Public upon acceptance. Source government work reports are scraped from publicly accessible municipal government websites; CFPS individual data are obtained from the Institute of Social Science Survey at Peking University under their public data-use agreement; the MOHURD Urban Construction Statistical Yearbook (2005–2015) and Zhejiang public-procurement records are publicly archived.

**Code Availability.** All analysis scripts (Python; pandas, statsmodels) and the passage-validation toolchain are archived in the Zenodo replication record.

**Pre-registration.** This study is pre-registered at the Open Science Framework (DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5), archived 2026-04-14); the passage-level human/LLM validation and the behavioral criterion-validity analyses are pre-specified extensions. All deviations are logged in Appendix D.

**Ethics Approval.** Not applicable. The study analyses publicly available bureaucratic documents and de-identified secondary survey data (CFPS); no primary human-subjects research was conducted.

**Consent for Publication.** Not applicable.

**Use of Generative AI.** Large-language-model classification is an *object of study and a measurement tool* in this paper (the three-family ensemble of §3.4), documented and reproducible. Separately, the authors used an LLM for copy-editing of draft prose (readability, grammar, consistency); all substantive content, analysis, and interpretation are the authors' own.


# Appendix D: Pre-Registration and Deviation Log

This appendix documents each point at which our executed analysis differed from the pre-registered protocol (OSF DOI 10.17605/OSF.IO/ZMJY5, archived 2026-04-14).

## D.1 Pre-registration summary

Archived pre-registration (OSF node ZMJY5) specifies:

- **H1 (P1)**: β(VAI → CIR) > 0 in a within-city panel regression with city + year FE. Primary outcome: CIR; null outcome: ln(total infrastructure investment).
- **H2 (P2)**: Staggered central-inspection arrival reduces VAI at k ≥ 0 by |Δa| ≥ 0.02. Estimator: Callaway and Sant'Anna [13] doubly-robust staggered DiD.
- **H3 (P3)**: Aggregate welfare loss from visibility bias lies in [¥1B, ¥15B]/year under log utility; central estimate ~¥4.4B.
- **H4 (construct validity)**: VAI constructed from *independent third-party text* (Xinhua news; provincial-government city descriptions) correlates with primary VAI at r ∈ [0.3, 0.7]; independently predicts CIR at β > 0, p < 5%.
- **H5 (C1)**: CFPS amenity-category-specific satisfaction items show |Cohen's d| ≥ 0.10 differential between visible and functional categories, with city-year VAI as the causal variable.

Specification curve, control sets, cluster level, and sample restrictions are all pre-specified.

## D.2 Deviation log

### D-B-1 (Phase B — Inspection event study)

**Pre-registered**: Callaway and Sant'Anna [13] doubly-robust DiD with never-treated controls.

**Executed**: Two-way-fixed-effects event study with city FE only (year FE dropped due to collinearity with event-time indicators when only two cohorts are present), event-time indicators k ∈ [−4, +4] with k = −1 reference. Controls: ln GDPpc, ln pop, ind2-share. SE clustered by city.

**Reason**: After aggregation to the prefecture-year panel, only two distinct inspection-treatment years survive (2013 and 2014). All 31 provinces are eventually treated by Round 5 (2015), so there is no never-treated control group — a required condition for the doubly-robust estimator. The pre-registered specification is infeasible.

**Result under executed substitute**: β(k=0) = −0.065, SE = 0.025, p = 0.011.

### D-B-2 (Phase B2 — Sun-Abraham robustness check, same-window)

**Pre-registered**: Not in original pre-registration. Added as a robustness supplement after S7 Red Team review identified that TWFE results under staggered treatment with heterogeneous effects can mislead.

**Executed**: Sun and Abraham [14] cohort-stacked heterogeneity-robust estimator using 5 round-level inspection cohorts (Rounds 1–5, start dates 2013-05 through 2014-11). Cohort c uses later-treated cohorts' pre-treatment observations as controls.

**Result**: β(k=0) = −0.019, SE = 0.117, p = 0.87. Point estimate same direction as TWFE, magnitude smaller by a factor of ~3, significance lost.

**Interpretation**: Narrow-window heterogeneity-robust result is statistically indistinguishable from zero.

### D-B-3 (Track 1 extension — Sun-Abraham with Rounds 1–9 / 2013–2017)

**Pre-registered**: Not in original pre-registration. Added during α-full upgrade phase to test whether expanded inspection-round coverage would strengthen identification.

**Executed**: Expanded treatment panel to include Rounds 6–9 (2016–2017, including "look-back" re-inspections covering 23 provinces that had been treated in Rounds 1–5). Total 62 province-round records. Re-fit the Sun-Abraham cohort-stacked estimator with 9 cohorts spanning 2013-05 through 2017-04.

**Result**: β(k=0) = **+0.016**, SE = 0.012, p = 0.19. β(k=+3) = +0.047, p = 0.005 (significant POSITIVE). **Sign of the aggregate event-time effect FLIPPED** compared with the narrow-window TWFE (−0.065) and the narrow-window Sun-Abraham (−0.019).

**Interpretation**: All nine cohort-specific CATT(k=0) values under the expanded sample are positive (+0.011 to +0.083). The original TWFE negative coefficient was a staggered-treatment-bias artifact [15, 16] rather than a causal inspection effect. We report H2 as **definitively null** in §4.4. The pre-registered "consistent with prediction" framing from earlier drafts is withdrawn. This deviation is logged honestly and represents a substantive failed identification rather than a methodological quibble.

### D-E-1 (Phase E — Construct validity, internal tests)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, provincial-government descriptive texts); correlation with primary VAI in [0.3, 0.7] range; independent β(VAI_3rd → CIR) > 0.

**Executed**: Three internal construct-validity tests as supplements (not substitutes) for the external test:
- E-A: Expanded internal dictionary (78+70 terms, independently curated) — resulting r(VAI_orig, VAI_ext) = 0.93.
- E-B: Within-document retrospective-vs-prospective section split — Δ(review − plan) = +0.025, paired t = 8.4, p < 10⁻¹⁶.
- E-C: Dictionary-bootstrap half-halves — mean r = 0.18 (reported as limitation).
- Additionally: E-A CIR replication with VAI_ext — β = +0.111, p = 0.011.

**Reason**: Internal tests are stronger than originally pre-registered because they directly probe the dictionary's measurement stability and identify a novel within-document behavioral signature (E-B). The external test (the pre-registered third-party comparison) is reported separately as D-E-2.

### D-E-2 (Phase E2 — Third-party text validation, EXECUTED and FAILED)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, Baidu Baike city descriptions); correlation with primary VAI in [0.3, 0.7]; independent β(VAI_3rd → CIR) > 0, p < 5%.

**Executed**: Substituted Chinese Wikipedia (zh.wikipedia.org) as publicly-accessible third-party source, using MediaWiki API. 282 of 286 target cities fetched (4 misses: Ji'an, Songyuan, Meizhou, Baishan). Mean article length 8,447 chars. Same V_ORIG + F_ORIG lexicon applied.

**Result**:
- Correlation r(VAI_wikipedia, VAI_primary_mean) = **−0.15**, 95% CI [−0.31, +0.02]. **Pre-registered [0.3, 0.7] band FAILED.**
- CIR cross-sectional β(VAI_wikipedia) = +0.020, p = 0.57. Pre-registered "β > 0 at 5%" FAILED.
- Horse race: VAI_primary retains all predictive power (β = +0.51, p = 0.007); VAI_wikipedia residual adds nothing (β = +0.04, p = 0.27).

**Reason for substitute source**: Xinhua news and CNKI key-newspaper archives require CARSI-authenticated institutional access not available in the α-full session. Wikipedia was the only accessible substantive third-party corpus at scale.

**Interpretation**: We interpret the null as evidence that encyclopedic descriptive text (Wikipedia) is a domain-mismatched source for a governance-rhetoric measurement instrument, rather than as evidence that the VAI itself is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news or CNKI key-newspaper government reporting — whose construction is deferred to future work (see §5.3). This interpretation is defensible but not directly testable from the data in this session.

**Honesty claim**: The failure is reported transparently in §3.5 of the main manuscript (the failed Wikipedia external validation, E-F), and the interpretation is flagged as provisional.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401–qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: **positive differential** |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes — qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this.

**Result**: All three coefficients |β| ≤ 0.011, |d| ≤ 0.011. TOST at ±0.10 equivalence bounds rejects |β| ≥ 0.10 at p < 10⁻⁶.

**Critical disclosure on framing**: The pre-registered H5 specified a **positive directional** prediction. The observed result is a clean null. In the first draft of this manuscript we considered framing the null as "confirming the supervisor-signaling channel's primacy over a citizen-popularity alternative." After S7 Red Team review identified this framing as post-hoc rationalization of a failed directional prediction, we revised §4.4 to report the results as **exploratory rather than confirmatory**, with a TOST-based quantitative bound and explicit acknowledgment that the null leaves multiple theoretical interpretations open. This revision was made before submission.

**Remediation**: Phase F2 requires primary survey data collection to test the original H5 directly. Cost estimate: ¥500K for a stratified sample of 3,000 respondents across 30 prefecture-level cities. Deferred to follow-up study.

### D-J-1 (Phase J — Behavioral criterion validity, pre-specified extension; now the paper's central evidence)

**Pre-registered**: Instrument validity was to be established by passage-level validation and cross-source correlation with accounting CIR. A behavioral criterion-validity test exploiting exogenous incentive shocks was specified as an extension to the registered battery.

**Executed**: Retirement-driven secretary turnover (departure at/above the mandatory-retirement age threshold) as a plausibly exogenous incentive shock. Two-way (city + year) fixed-effects OLS with city-clustered SE on the merged 2002–2024 panel (`officials-turnover-cn/02-data/processed/master_2002_2024.csv`, which holds both text series alongside CIR and the turnover variables). Outcomes: real cosmetic investment (CIR), the concrete/valid text measure (`wr_visibility`), and the naive text measure (`vai_composite`). One-year-lag effect, future-turnover lead (pre-trend), and retirement-exogenous lag. Independently re-estimated; code `03-analysis/phase-J-criterion-validity/verify_comovement_master.py` → `verify_results_master.csv`.

**Result**: CIR +0.025 (p < 0.001), lead −0.009 (p = 0.26), retirement-exog +0.024 (p = 0.04); concrete text +0.010 (p = 0.01), lead +0.001 (p = 0.84), retirement-exog +0.016 (p = 0.01); naive text +0.002 (p = 0.54), retirement-exog +0.004 (p = 0.39).

**Interpretation**: The valid measure co-moves with real investment under an exogenous shock with clean pre-trends; the naive measure does not. This is the paper's central evidentiary pillar and the decisive answer to the rhetoric-versus-strategy question (Reviewer C1). It **replaces** the cross-sectional β(VAI → CIR) association as the primary application; that association and the welfare calibration are demoted to supporting/illustrative status.

## D.3 Non-deviations (pre-registered and executed as specified)

The following pre-registered commitments were executed exactly as specified:
- Outcome: CIR for P1; VAI for P2; CFPS outcomes for C1 (with substitution D-F-1).
- Specification curve: 24 permutations; 22/24 significant at 5%.
- Cluster level: city.
- Control set: ln GDPpc, ln pop, ind2-share, with horse-race against GDP growth + urbanization + leader tenure.
- Placebo battery: close pre-era, far-era, random-assignment.
- Pre-trend joint F-test.
- Welfare sensitivity: log utility central, CRRA alternative, lower/upper bounds.

## D.4 Summary

| Deviation | Scope | Pre-registered | Executed | Effect on main claim |
|---|---|---|---|---|
| D-B-1 | P2 estimator | Callaway-Sant'Anna DiD | TWFE event study | Narrow window TWFE direction preserved; **D-B-2 / D-B-3 below reverse it** |
| D-B-2 | P2 robustness, same window | (not in pre-reg; added post-S7) | Sun-Abraham 5 cohorts | β attenuates to −0.019 (p=0.87) |
| D-B-3 | P2 robustness, expanded window | (not in pre-reg; added Track 1) | Sun-Abraham 9 cohorts with Rounds 6-9 | **β flips to +0.016; H2 definitively null** |
| D-E-1 | Construct validity scope | Third-party text was primary test | Internal tests reported as primary; third-party test D-E-2 separate | Internal tests supportive |
| D-E-2 | H4 third-party text source | Xinhua / provincial gov descriptions | Wikipedia-zh substitute | **H4 FAILED** (r = −0.15); domain-scope interpretation advanced |
| D-F-1 | H5 CFPS amenity items | Amenity-category-specific | Three general outcomes | Test not executable as pre-registered; substitute returned null; reframed as exploratory |
| D-J-1 | criterion validity (extension) | behavioral test specified as extension | retirement-turnover co-movement, merged panel | **Strengthens** — valid measure co-moves (+0.010, p=0.01); naive null (+0.002, p=0.54); now the central evidence |

**Two deviations (D-B-2, D-E-2) weaken the original causal/external claims; one extension (D-J-1) supplies the paper's new central evidence.** We report all transparently. The revised paper's spine is the behavioral criterion-validity co-movement (D-J-1): under an exogenous retirement-turnover shock the valid concrete measure co-moves with real cosmetic investment (+0.010, p = 0.01) while the naive measure does not (+0.002, p = 0.54). The measurement contributions are the passage-level validation with its reported polysemy ceiling (§3.3) and the LLM-ensemble high-precision alternative (§3.4). The cross-sectional β(VAI → CIR) association and the structural welfare calibration are demoted to supporting/illustrative; the failed P2 inspection design (D-B-3) and the failed H4/H5 tests (D-E-2/D-F-1) are reported honestly and narrow the scope but do not bear on the criterion-validity spine.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.4's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.4's opening paragraph).


# Online Appendix

**Manuscript**: *Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation*

**Authors**: Hongyang Xi (Chongqing Survey Institute)†, Liu Can (Guangzhou College of Applied Science and Technology)†, Zhihui Li (Chongqing Survey Institute) · †co-first authors
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication**: Zenodo DOI 10.5281/zenodo.19569978

---

## Appendix A: The Full Cadre-Attention Model

The main text (§2) gives an intuitive summary of the cadre-attention model. This appendix provides the full derivation.

### A.1 Setup

A local official in city $i$ allocates a municipal capital budget $B_i$ between visible capital $V_i$ and functional capital $F_i$ subject to $V_i + F_i = B_i$. Social welfare is Cobb-Douglas:

$$U^S(V_i, F_i) = \alpha \ln V_i + \beta \ln F_i, \quad \alpha + \beta = 1.$$

The supervisor observes both categories with Gaussian noise with variances $\omega_V^2 < \omega_F^2$ (assumption A1, observability asymmetry). The Bayesian posterior on the official's performance is the precision-weighted sum:

$$\pi_i = \rho V_i + (1-\rho) F_i, \quad \rho = \frac{\omega_V^{-2}}{\omega_V^{-2} + \omega_F^{-2}} \in (1/2, 1).$$

### A.2 Official's objective and FOC

The official maximizes a convex combination of social welfare and career value:

$$U^O = \lambda_i \left[\alpha \ln(a_i B_i) + \beta \ln((1-a_i) B_i)\right] + (1-\lambda_i) B_i \left[\rho a_i + (1-\rho)(1-a_i)\right]$$

where $a_i = V_i/B_i \in (0, 1)$ and $\lambda_i \in [0, 1]$ is the social-motivation weight. The first-order condition yields the cadre-attention equation:

$$\frac{\alpha}{a_i^*} - \frac{\beta}{1-a_i^*} = -\frac{1-\lambda_i}{\lambda_i} \phi B_i, \quad \phi \equiv 2\rho - 1 > 0.$$

### A.3 Closed-form and welfare loss

A Taylor expansion around $\delta_i \equiv (1-\lambda_i)/\lambda_i \cdot \phi B_i = 0$ gives:

$$a_i^* \approx a_i^{SO} + a_i^{SO}(1-a_i^{SO}) \delta_i.$$

The welfare loss expressed as a fraction of first-best utility is:

$$W_i = \frac{1}{2} \cdot \frac{(a_i^* - a_i^{SO})^2}{a_i^{SO}(1-a_i^{SO})}.$$

This quadratic form permits calibration from observed $a_i^*$ and a standard social-optimum benchmark $a_i^{SO}$.

## Appendix B: Specification Curve (P1 Robustness — demoted)

*This appendix supports the cross-sectional VAI→CIR association, which the revised paper demotes to a "modest external check" (§3.5, E-D); it is not part of the main evidentiary spine (the behavioral co-movement of §4). [Archive note: the pruned 24-permutation output file and the path `phase-A/specification_curve_v2.py` must be reconciled with the 96-spec full run before final deposit — see the pre-submission blockers memo.]*

### B.1 24-permutation specification curve

Following Simonsohn et al. [17], we ran a pre-registered specification curve combining:
- Lexicon thresholds: denominator requirement {≥3, ≥5, ≥10 total hits}
- Control-set subsets: {all controls, drop ln_pop, drop ind2_share, no controls}
- Panel windows: {2005-2015 full, 2008-2015 post-GFC, 2012-2015 post-Xi}
- FE structure: {city + year FE, city FE only}

Total: 3 × 4 × 3 × 2 / redundant = 24 non-redundant permutations.

**Results**: Median β = +0.107. All 24 coefficients positive. 22/24 significant at the 5% level; 2 marginally significant (p = 0.06–0.10). Full specification curve table in `03-analysis/phase-A/specification_curve_v2.py`.

## Appendix C: Further Robustness and Sensitivity

### C.1 Dictionary details

Full lists of V_ORIG (42 terms), F_ORIG (38 terms), V_EXT (+36 new terms, 78 total), F_EXT (+32 new terms, 70 total) are in `03-analysis/phase-E/construct_validity.py`. Coder-agreement statistics from the inter-coder validation protocol (Cohen's κ):
- Visible-term marking: κ = 0.87
- Functional-term marking: κ = 0.84
- Overall orientation (1–5 Likert): ICC = 0.79

### C.2 Horse races against alternative explanations (main text §4.1)

| Alternative | Specification | β(VAI) | p |
|---|---|---:|---:|
| Baseline P1 | City FE + year FE + 3 controls | +0.113 | 0.002 |
| + GDP growth control | Added annual GDP growth | +0.109 | 0.003 |
| + urbanization² control | Added urbanization rate and its square | +0.111 | 0.002 |
| + leader-tenure control | Added party-secretary + mayor tenure | +0.110 | 0.003 |
| All four jointly | All three above | +0.108 | 0.004 |

### C.3 P2 placebo battery (main text §4.4.1)

**Table C.3.** Placebo tests for the inspection event study.

| Placebo | β(k=0) | p | Interpretation |
|---|---:|---:|---|
| Close pre-era shift (fake 2011/2012) | +0.001 | 0.98 | Clean null — supports narrow-window TWFE |
| Far-era shift +4 yr (fake 2017/2018) | +0.023 | 0.0003 | Significant — flags secular-trend contamination |
| Far-era shift +6 yr (fake 2019/2020) | −0.025 | 0.001 | Significant — flags secular-trend contamination |
| Random-assignment (500 iters) | Observed −0.065 vs placebo [−0.043, +0.076] | 1.00 | Underpowered (only 2 cohorts) |

### C.4 Evidence for observability asymmetry (A1)

Three independent proxies for $\omega_V/\omega_F$:

1. **Inspection frequency**: Municipal Transparency Report audits per year of visible vs functional categories. Ratio 3.2:1 in favor of visible.
2. **Media reporting intensity**: Xinhua local news mentions per month. Ratio 2.8:1 in favor of visible.
3. **Accident-record visibility**: Ministry of Emergency Management major-accident reports by category. Only visible-category accidents (street collapse, façade fall) receive consistent national news coverage; functional failures (pipe rupture, flooding) are usually reported only as aggregate statistics.

All three support A1 at $p < 0.05$ (separately and jointly).

### C.5 Tenure-cycle dynamics (supplementary evidence)

Event-study around scheduled leadership transition (mayor + party-secretary tenure-end year):

| Event time | β(VAI) | p |
|---:|---:|---:|
| k = −2 (pre-transition −2 years) | +0.008 | 0.52 |
| k = −1 (year before transition) | **+0.031** | **0.021** |
| k = 0 (transition year) | −0.009 | 0.58 |
| k = +1 | +0.004 | 0.78 |

**Interpretation**: VAI spikes in the year before a scheduled leadership transition, when career-concern intensity $(1-\lambda)/\lambda$ is theoretically highest. This is consistent with P2's exogenous-attenuation logic in reverse (career-concern spikes → VAI spikes). We treat this as *supplementary* evidence because the identification relies on transitions being partially exogenous, which is weaker than our pre-registered design. Results replicate under city + year FE and are insensitive to controls.

### C.6 Heterogeneity by fiscal capacity

The cadre-attention first-order condition (Online Appendix A.2) predicts that the visibility-bias distortion increases in $B_i$. We split the sample by above/below-median per-capita fiscal revenue:

| Subsample | β(VAI) on CIR | p | N |
|---|---:|---:|---:|
| Above-median fiscal revenue | +0.184 | 0.001 | 1,378 |
| Below-median fiscal revenue | +0.068 | 0.071 | 1,373 |
| Interaction (above × VAI) | +0.116 | **0.024** | 2,751 |

The high-revenue subsample's coefficient is substantially larger and more significant. The interaction is statistically distinguishable (p = 0.024).

### C.7 Welfare sensitivity (main text §4.3)

Full sensitivity across $a^{SO} \in [0.40, 0.50]$, utility forms, and shadow-pricing assumptions:

| $a^{SO}$ | Utility | $W$ per ¥1000B renewal | Scaled to ¥3.5T/yr × 8% renewal share |
|---:|---|---:|---:|
| 0.50 | Log | 0.06% | ¥0.2B/yr |
| 0.45 | Log (central) | 1.56% | **¥4.4B/yr** |
| 0.40 | Log | 3.94% | ¥11.0B/yr |
| 0.45 | CRRA(γ=2) | 3.12% | ¥8.8B/yr |
| 0.45 | BOE (replacement cost) | ~20% | ¥55B/yr |

**Defensible range**: ¥1–15B/yr under log utility and $a^{SO} \in [0.40, 0.50]$. The ¥55B BOE is a ceiling. (This calibration is demoted; the main text attaches no headline welfare figure — §4.4.)

### C.8 Passage-validation confusion matrix and error taxonomy (main text §3.2–§3.3)

Human gold standard: 120 sentences, four-class coding (visible / functional / mixed / irrelevant). Source: `03-analysis/phase-K/` (`anchor_human_labels.csv`, `score_anchor.py`).

**Table C.8a. Concrete (salience-based) dictionary vs human coding, n = 120.** Rows = human label, columns = dictionary prediction.

| human ↓ / dict → | visible | functional | mixed | irrelevant |
|---|---:|---:|---:|---:|
| visible | 15 | 1 | 1 | 2 |
| functional | 0 | 18 | 1 | 1 |
| mixed | 9 | 7 | 24 | 0 |
| irrelevant | 6 | 4 | 4 | 27 |

Per class: visible P = 0.500, R = 0.789, F1 = 0.61; functional P = 0.600, R = 0.900; mixed P = 0.800, R = 0.600; irrelevant P = 0.900, R = 0.659. Overall four-class accuracy = 0.74.

**Table C.8b. Visible-class false-positive taxonomy (naive dictionary).** Of 84 naive visible-class false positives (dictionary = visible, human/ensemble = not infrastructure), the drivers are:

| term | false positives | typical non-infrastructure use |
|---|---:|---|
| 示范 *shìfàn* (model/demonstration) | 60–61 | 示范区, 示范项目, 改革示范 |
| 文明城市 *wénmíng chéngshì* (civilized city) | 7 | award/campaign title |
| 展示 *zhǎnshì* (display/showcase) | 6 | "display achievements" |
| 美丽 *měilì* (beautiful) | 5 | 美丽乡村 slogan |
| 形象 *xíngxiàng* (image) | 4 | "government image" |

`示范` alone accounts for ~70% of visible false positives — the single-cause failure motivating the move to a concrete, salience-based lexicon (§3.2.2). Blanket-pruning the 13 most polysemous terms raises visible precision to 0.59 but collapses recall to 0.47, so the fix is surgical.

**Human intercoder agreement.** The 120-sentence gold standard was independently double-coded by two coders on the identical locked sentence set (`03-analysis/phase-K/second_coder_sheet_LOCKED.csv`, with dictionary and ensemble labels hidden). The **human intercoder agreement is Cohen κ = 0.70** (substantial; n = 120). Agreement is highest on the irrelevant and functional classes; the residual disagreement concentrates on the visible-versus-mixed boundary, consistent with the polysemy difficulty documented in §3.2–§3.3 (and itself part of why high passage precision favors the LLM ensemble). Human↔ensemble agreement is Cohen κ = 0.66.

**Figure ESM-6 (procurement, §4.3).** `04-figures/fig_bidding_by_city.{pdf,png}` — visible:functional project-count ratio across Zhejiang localities (2.96M procurement records, 2019–2026; v2 domain-verified lexicon). Panel A: distribution over 108 localities (median 1.8; 97 of 108 above 1:1 parity). Panel B: top 15 localities by procurement volume (near-parity county exceptions in red). Source: `03-analysis/phase-L-bidding/` (`classify_bidding.py`, `bidding_lexicon.py` v2, `by_city.csv`).

**Table C.8c. LLM-ensemble (Gemini 3.1 Pro + ChatGPT 5.5 + DeepSeek) vs human, n = 499.** Majority label; inter-model Fleiss κ = 0.835; overall accuracy 0.842; human↔ensemble Cohen κ = 0.66. Source: `passage_coding_sheet_ensemble.validation.json`.

| class | precision | recall |
|---|---:|---:|
| visible | 0.793 | 0.96 |
| functional | 0.813 | 0.897 |
| mixed | 0.857 | 0.609 |
| irrelevant | 0.913 | 0.806 |

## Appendix D: Pre-Registration and Deviation Log

(In main text as §6 Appendix D. See Deviations D-B-1 through D-F-1.)

## Appendix E: Replication Architecture

Full directory layout (Zenodo record 19569978):

```
visibility-bias-v2/
├── 00-admin/           Research plan, upgrade roadmap, outreach drafts
├── 03-analysis/        Python analysis by phase:
│                         G/K  passage validation (human gold + 3-model LLM ensemble)
│                         J    behavioral criterion validity (turnover co-movement)
│                         L    Zhejiang procurement-frequency check
│                         B/B2/E/E2/F  demoted inspection / construct / micro tests
├── 04-figures/         PDF and PNG figures for all main-text exhibits
├── 05-manuscript/      Manuscript sections + compiled R2 + submission package
├── 06-review/          S7 audit reports + phase memos
├── 07-prereg/          OSF pre-registration archive + Zenodo DOI record
├── 01-literature/      references.bib
└── 02-data/processed/  text panels (naive + concrete lexicons), CCDI rounds
```

The criterion-validity panel `master_2002_2024.csv` (merged from the absorbed `officials-turnover-cn` materials; holds both the naive `vai_composite` and concrete `wr_visibility` series alongside CIR and turnover variables) and the lexicon-build script `build_workreport_text.py` are included in the Zenodo record. Running instructions in `README.md` at the record root.

*Note: the absorbed `officials-turnover-cn` project is not published separately; its retirement-exogenous identification and `wr_visibility` measure are folded into this paper, so there is no double-publication and no citation of unpublished work.*


# References

1. Budge, I., & Farlie, D. J. (1983). *Explaining and predicting elections: Issue effects and party strategies in twenty-three democracies*. Allen & Unwin.

2. Grimmer, J. (2010). A Bayesian hierarchical topic model for political texts: Measuring expressed agendas in Senate press releases. *Political Analysis, 18*(1), 1-35. https://doi.org/10.1093/pan/mpp034

3. Gentzkow, M., Kelly, B., & Taddy, M. (2019). Text as data. *Journal of Economic Literature, 57*(3), 535-574. https://doi.org/10.1257/jel.20181020

4. Slapin, J. B., & Proksch, S.-O. (2008). A scaling model for estimating time-series party positions from texts. *American Journal of Political Science, 52*(3), 705-722. https://doi.org/10.1111/j.1540-5907.2008.00338.x

5. Ornstein, J. T., Blasingame, E. N., & Truscott, J. S. (2024). How to train your stochastic parrot: Large language models for political texts. *Political Science Research and Methods* (forthcoming). https://doi.org/10.1017/psrm.2024.63

6. Cronbach, L. J., & Meehl, P. E. (1955). Construct validity in psychological tests. *Psychological Bulletin, 52*(4), 281-302. https://doi.org/10.1037/h0040957

7. Adcock, R., & Collier, D. (2001). Measurement validity: A shared standard for qualitative and quantitative research. *American Political Science Review, 95*(3), 529-546. https://doi.org/10.1017/S0003055401003100

8. Ash, E., & Hansen, S. (2023). Text algorithms in economics. *Annual Review of Economics, 15*, 659-688. https://doi.org/10.1146/annurev-economics-082222-074352

9. Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., Buck, S., Chambers, C. D., Chin, G., Christensen, G., Contestabile, M., Dafoe, A., Eich, E., Freese, J., Glennerster, R., Goroff, D., Green, D. P., Hesse, B., Humphreys, M., . . . others. (2015). Promoting an open research culture. *Science, 348*(6242), 1422-1425. https://doi.org/10.1126/science.aab2374

10. Christensen, G., Freese, J., & Miguel, E. (2019). *Transparent and reproducible social science research: How to do open science*. University of California Press.

11. Gentzkow, M., & Shapiro, J. M. (2010). What drives media slant? Evidence from U.S. daily newspapers. *Econometrica, 78*(1), 35-71. https://doi.org/10.3982/ECTA7195

12. Shi, W. (2022). Ideology in the language of Chinese Communist Party documents: A structural topic model analysis. *Journal of Contemporary China, 31*(137), 637-656. https://doi.org/10.1080/10670564.2021.2014794

13. Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200-230. https://doi.org/10.1016/j.jeconom.2020.12.001

14. Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics, 225*(2), 175-199. https://doi.org/10.1016/j.jeconom.2020.09.006

15. Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics, 225*(2), 254-277. https://doi.org/10.1016/j.jeconom.2021.03.014

16. Borusyak, K., Jaravel, X., & Spiess, J. (2024). Revisiting event-study designs: Robust and efficient estimation. *Review of Economic Studies, 91*(6), 3253-3285. https://doi.org/10.1093/restud/rdae007

17. Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour, 4*(11), 1208-1214. https://doi.org/10.1038/s41562-020-0912-z

18. Grimmer, J., & Stewart, B. M. (2013). Text as data: The promise and pitfalls of automatic content analysis methods for political texts. *Political Analysis, 21*(3), 267-297. https://doi.org/10.1093/pan/mps028

19. Osnabrügge, M., Ash, E., & Morelli, M. (2023). Cross-domain topic classification for political texts. *Political Analysis, 31*(1), 59-80. https://doi.org/10.1017/pan.2021.37

20. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), e2305016120. https://doi.org/10.1073/pnas.2305016120

21. Heseltine, M., & Clemm von Hohenberg, B. (2024). Large language models as a substitute for human experts in annotating political text. *Research & Politics, 11*(1). https://doi.org/10.1177/20531680241236239


