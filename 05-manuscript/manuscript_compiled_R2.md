# Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation

*Hongyang Xi¹†\* · Liu Can²† · Zhihui Li¹*
*¹ Chongqing Survey Institute Co., Ltd., Chongqing, China · ² Urban and Rural Planning, Guangzhou College of Applied Science and Technology, Guangzhou, China*
*† co-first authors (equal contribution) · \* corresponding author: 26708155@alu.cqu.edu.cn*

---

# Abstract

We introduce the Visibility Attention Index (VAI), a pre-registered text instrument measuring the share of *visible* versus *functional* infrastructure language in bureaucratic documents, applied to 6,294 Chinese municipal government work reports (282 prefectures, 2002–2024). VAI is motivated by a cadre-attention model. We separate what it measures, visible-versus-functional language, from the stronger claim of strategic visibility bias. We validate VAI at the passage level against human coding (two coders, Cohen κ = 0.70) and report its limits plainly. A naive appearance-word dictionary reaches only 0.10 precision, because polysemous image terms (形象 *xíngxiàng* "image"; 示范 *shìfàn* "model") fire outside infrastructure. A concrete, salience-based lexicon reaches 0.50–0.60 but meets a polysemy ceiling, above which only an LLM ensemble attains high precision (0.84 accuracy; inter-model Fleiss κ = 0.835). We then add a behavioral criterion-validity test. Under quasi-exogenous, retirement-driven secretary turnover, the concrete VAI co-moves with real cosmetic investment (+0.010, p = 0.01; clean pre-trends) while the naive measure does not (+0.002); the valid measure tracks strategic attention, not genre. Descriptively, within-city VAI tracks the Cosmetic Investment Ratio (β = +0.111), and an independent procurement corpus (≈2.96M Zhejiang records) corroborates the tilt, with visible projects running about 2-to-1 over functional in 97 of 108 localities. A failed third-party Wikipedia test (r = −0.15), an inspection event study, a CFPS micro-foundation, and a welfare calibration are reported transparently and demoted. The contribution is methodological: a pre-registered, passage-validated, behaviorally-anchored instrument, with an honest map of where the dictionary stops and an LLM alternative begins.

**Keywords**: text-as-data, policy attention, construct validity, criterion validity, pre-registration, China

**Pre-registration**: OSF DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5). **Replication archive**: Zenodo DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978).


# 1. Introduction

Measuring bureaucratic attention from text is a central challenge in political methodology. Political agents produce corpora of formal documents (legislative speeches, agency reports, municipal plans) whose lexical structure reveals *what they attend to* and, by inference, *what matters to them*. Methodological advances over the past decade have moved from manual content analysis [1] to supervised topic models [2, 3], semi-supervised scaling [4], and large-language-model-assisted classification [5]. Yet most existing instruments are monolingual (English-dominated), aim at *ideological* rather than *compositional* attention, and are rarely pre-registered or subjected to the explicit construct-validity scrutiny standard in psychometrics [6, 7].

This paper contributes a pre-registered text-measurement instrument for a specific form of compositional policy attention: the rhetorical share of visible versus functional infrastructure language in the Chinese municipal government work report (GWR). We are deliberate about the interpretive ladder. The Visibility Attention Index (VAI) measures *language*. The hypothesis that this language reflects strategic visibility bias, namely preferential attention to observationally-salient categories over less-salient but functionally-equivalent ones, is what *motivates* the instrument. Whether a city's visible-infrastructure language reflects strategic signaling, genuine construction, central campaigns, fiscal capacity, or template convention is a question the measure enables. In this revision we go one step further than language alone and test, behaviorally, whether the valid measure moves with real money under an exogenous incentive shock (§3.2.7). The setting makes the strategic interpretation institutionally plausible. Prefecture officials prepare annual work reports within the target-responsibility evaluation system, addressed primarily to superior authorities whose observability over functional categories is limited, a consequentiality we document rather than assert (§3.1.0).

We proceed in three moves.

First, we formalize the compositional-attention problem as a cadre-attention model with an observability-asymmetry assumption (§2). An official allocates a fixed budget between visible and functional categories; the supervisor observes both with Gaussian noise, but the noise on functional categories is strictly larger (a finished boulevard is photographable; a replaced sewer main is not). The model yields the substantive motivation for the instrument and specifies what a *valid* measure of compositional attention should look like.

Second, we construct VAI and validate it. In this revision we lead with the validation the original draft lacked and report each rung honestly (§3.2). (i) Direct passage-level validation against human coding (two independent coders, intercoder κ = 0.70) shows that a *naive* appearance-word dictionary fails: visible-class precision is only **0.10**, because polysemous image terms (形象 *xíngxiàng* "image"; 示范 *shìfàn* "model/demonstration") fire pervasively outside infrastructure. (ii) A concrete, salience-based lexicon, the VAI lexicon we recommend, raises precision to **0.50, and 0.60 after targeted refinement, at 0.79 recall**, but meets a polysemy ceiling near 0.60–0.64 that curation cannot break (道路 *dàolù* "road" also names the *path* of industrialization). (iii) For users who need higher passage precision, an LLM-ensemble classifier attains **0.84 accuracy** (inter-model Fleiss κ = 0.835), above the dictionary ceiling. (iv) A behavioral criterion-validity test (§3.2.7): under quasi-exogenous, retirement-driven secretary turnover, the concrete VAI co-moves with *real* accounting-based cosmetic investment (+0.010, p = 0.01; clean pre-trends), whereas the naive measure does not (+0.002, p = 0.54). Co-movement with money under an exogenous shock is what separates a strategic-attention measure from a genre artifact. We complement these with reliability and external checks, each labelled for what it shows: an independent-lexicon replication (*reliability*, r = 0.93), the MOHURD cross-source correlation (modest external anchor, r = 0.24), a within-document review-vs-plan differential (suggestive; may reflect genre), and a pre-registered third-party Wikipedia test that fails (r = −0.15) and is reported plainly as bounding the instrument's domain.

Third, we present descriptive applications of VAI (§4). One is a within-city association between VAI and the accounting-based Cosmetic Investment Ratio (β = +0.111, p = 0.002), reported as compositional substitution rather than a causal effect. The other, new in this revision, is an independent public-procurement corpus (≈2.96M Zhejiang bidding records) in which visible-type construction projects outnumber functional ones ≈2-to-1 (in 97 of 108 localities), corroborating the compositional tilt in an entirely separate, large-scale data source. Three exercises a previous draft foregrounded are demoted to the appendix and reported transparently as failed or assumption-dependent: a central-inspection event study that does not survive heterogeneity-robust estimation, a CFPS micro-foundation test that detects no effect above |d| = 0.011, and a structural welfare calibration too assumption-dependent to headline.

## 1.1 Contribution

Our contribution is **methodological**: a pre-registered, replicable instrument for measuring the visible-versus-functional composition of infrastructure language in bureaucratic text, with direct passage-level validation, a behavioral criterion-validity anchor, an LLM alternative where the dictionary ceiling binds, explicit domain-scope documentation, and transparent null-reporting. We position it as a *domain-specific measurement application* within the established text-as-data tradition, not a departure from it.

- **Text-as-data in political methodology.** A large literature measures political *attention* and *expressed agendas* from text, including expressed priorities in legislative communication, agenda-setting, audience-targeting, and cross-domain priority classification [2, 3, 4, 8, 18, 19]. VAI is a domain-specific instance: an interpretable, expert-coded measure of *compositional* (visible-vs-functional) attention in Chinese municipal reports.

- **Validation honestly bounded, then behaviorally anchored.** Rather than defend a dictionary by face validity and an aggregate correlation, we report its passage-level precision ceiling and supply an LLM route past it. The central result is that the *valid* measure co-moves with real investment under an exogenous shock while the naive one does not. This validation discipline, not the keyword list, is the transferable core.

- **Pre-registration and transparent null-reporting.** We pre-register the instrument and its validity tests at OSF (DOI 10.17605/OSF.IO/ZMJY5) and report all null and failed results transparently [9, 10]. These include a failed third-party validation, a non-robust causal event study, and a null micro-foundation test.

We deliberately refrain from causal and welfare claims as headline contributions: the strategic-bias interpretation is anchored behaviorally (§3.2.7) but not structurally identified, and the Cobb-Douglas welfare calibration is an assumption-dependent appendix illustration.

## 1.2 Roadmap

Section 2 develops the cadre-attention model as motivation. Section 3 describes VAI construction (§3.1) and its validation (§3.2), led by the passage-level human validation and the behavioral criterion-validity test. Section 4 presents the descriptive application (VAI vs accounting-based investment composition), the independent procurement corroboration, and, demoted to supporting material, the exercises that do not support causal or welfare claims. Section 5 discusses scope, portability, and limitations; Section 6 concludes. Five deviations from the pre-registration are logged in Appendix D with reasons and effect-on-sign-and-significance; the replication archive is at Zenodo (DOI 10.5281/zenodo.19569978) and pre-registration at OSF (DOI 10.17605/OSF.IO/ZMJY5).


# 2. Theoretical Motivation

This section states, in light form, why we expect compositional text-rhetoric to carry information about visibility bias, and what that implies for validation. Its purpose is to *motivate the measurement problem and define the construct* rather than to identify structural parameters. A fuller formal treatment, an official's allocation problem under precision-weighted evaluation with closed-form comparative statics, is in Online Appendix A. Nothing in the paper's evidence depends on it, and we no longer headline the welfare expression it yields (§4.4, §5).

## 2.1 Observability asymmetry and the salience definition of "visible"

A municipal official allocates a finite urban-infrastructure budget across asset classes that differ in how *observable* their output is to the audience that evaluates the official. That audience is primarily the superior (provincial) authority controlling promotion, and secondarily inspectors, media, and citizens. We define **visible** capital by observability and salience to that audience rather than by physical surface:

- **Visible**: output that the evaluating audience readily perceives and attributes to the incumbent: streetscapes, greening, squares, parks, lighting, landmarks, and *metro/rail transit*. Metro is the diagnostic boundary case. Its tunnels are underground, yet it is daily-used, media-celebrated, and an unmistakable prestige achievement, so it is maximally salient and coded visible.
- **Functional**: output that is concealed in normal operation and noticed mainly upon failure: drainage, water and gas pipe networks, sewerage, heating, and structural safety.

The substantive premise is an observability asymmetry. The evaluating audience perceives visible categories with less noise than functional ones ($\omega_V^2 < \omega_F^2$). Three independent proxies for the asymmetry, namely inspection frequency, media-reporting intensity, and the visibility of failures in the accident record, are consistent with it (Online Appendix C.4). The conceptual move that matters here is that "visible to whom" is answered by the *upward* principal; lateral citizen perception is a distinct channel, which our individual-level analysis treats as a bounded null rather than the mechanism (§4.4).

## 2.2 Why composition should leave a textual trace

When evaluation is weighted toward what is observable, an official maximizing a mix of social and career returns tilts attention toward salient categories, and toward *describing* salient categories, because attention to the legible margin yields more perceived performance per yuan. Two implications follow for measurement, and they structure the rest of the paper:

1. A valid text measure of compositional attention should track real visible-investment composition. This is the basis for cross-source and, equally, behavioral validation: the right measure should co-move with accounting-based cosmetic investment, and should do so under exogenous shifts in career incentives (§4).

2. The signal lives in concrete, salience-bearing referents. Because the construct is about *which assets* are emphasized, the measure must key on concrete nouns (parks, squares, roads, metro, landmarks) rather than abstract appearance words ("image", "model", "showcase"). Those abstract words are polysemous and decoupled from infrastructure, which §3 shows is the proximate cause of naive-dictionary failure.

## 2.3 Scope of the theoretical role

The model yields *predictions about what a valid measure should look like and do*. It is not a vehicle for causal identification of incentive parameters. We do not claim to estimate $(\omega_V,\omega_F)$ or a welfare loss as a result; the structural welfare calibration that an earlier draft headlined is demoted to an assumption-dependent illustration (§4.4, Online Appendix A/C.7). A reader interested only in the measurement contribution can proceed directly to §3. We invoke the observability-asymmetry premise again only to interpret the behavioral co-movement in §4.


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

**Audiences and "visible to whom."** The GWR's audiences include the promotion-controlling superior, the NPC delegates who vote on it, and the public and media to whom it is released. The audience relevant to our construct is the *superior*. The salience criterion is defined relative to this upward principal, which is the channel through which the observability asymmetry of §2.1 operates. The lateral citizen channel is reported as a bounded null (§4.4) rather than asserted as the mechanism.

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

The text corpus (§3.1) is combined with five further sources. The **China Urban Construction Statistical Yearbook (Ministry of Construction / MOHURD, 2005–2015)** is the source of the accounting CIR (cosmetic categories ÷ total urban-construction investment) and of the cosmetic/functional split the concrete lexicon mirrors. A city-year control panel covers 282 cities × 2002–2024. A municipal-leader panel gives party-secretary turnover, tenure, and age (the basis for the retirement-driven shock in §3.2.7). The China Family Panel Studies (CFPS, 2010–2022) supplies the bounded individual-level null (§4.4). Zhejiang public-procurement records (≈2,957,789 announcements, predominantly 2019–2026, national `ggzy.gov.cn` platform) provide the independent procurement corroboration (§4.3). The criterion-validity panel (`master_2002_2024.csv`, holding both the naive and concrete text series alongside CIR and turnover) and all code are archived at Zenodo (DOI 10.5281/zenodo.19569978) and pre-registered at OSF (DOI 10.17605/OSF.IO/ZMJY5); provenance and linkage rates are in Online Appendix E.


# 4. Substantive Applications

Section 3 established that the concrete VAI is a validated measure of the visible-versus-functional composition of Chinese municipal governance rhetoric. It was passage-validated against human coding (§3.2.0) and behaviorally anchored to real cosmetic investment under an exogenous incentive shock (§3.2.7). This section presents what the validated instrument *descriptively* reveals: a compositional-substitution association in accounting data (§4.1), a suggestive within-document pattern (§4.2), and an independent large-scale corroboration in public-procurement data (§4.3). Three exercises that a previous draft foregrounded are demoted and reported transparently (§4.4–§4.5). We make no causal claim about *what drives* visibility bias; the criterion-validity evidence (§3.2.7) supports the measure rather than a causal theory.

## 4.1 Application I: Compositional substitution in accounting data (P1)

Our pre-registered H1 holds that within-city variation in VAI positively predicts the accounting-based Cosmetic Investment Ratio (CIR) while leaving total infrastructure investment unchanged. We estimate

$$\text{CIR}_{it} = \beta\,\text{VAI}_{it} + \gamma' X_{it} + \mu_i + \tau_t + \epsilon_{it},$$

with city ($\mu_i$) and year ($\tau_t$) fixed effects, controls $X_{it}=\{\ln\text{GDPpc}, \ln\text{pop}, \text{ind2-share}\}$, and city-clustered SE; sample 2,751 city-years across 261 cities, 2005–2015 (MOHURD CIR coverage).

**Table 2. P1 — Compositional substitution (CIR ~ VAI)**

| Specification | β(VAI) | SE | p | N |
|---|---:|---:|---:|---:|
| (1) Primary VAI | **+0.113** | 0.037 | **0.002** | 2,751 |
| (2) Reconstructed lexicon (robustness) | +0.111 | 0.036 | 0.002 | 2,751 |
| (3) Independent lexicon | +0.111 | 0.043 | 0.011 | 2,751 |
| (4) No city FE | +0.089 | 0.042 | 0.035 | 2,751 |
| (5) No year FE | +0.184 | 0.055 | 0.001 | 2,751 |
| (6) IV = VAI(t−1) | +0.142 | 0.051 | 0.005 | 2,489 |

All specifications give β > 0 at conventional significance. The null on total investment (ln total urban-construction investment on VAI: β = −0.008, p = 0.71) is consistent with *composition, not expansion*. Horse races against GDP-growth, urbanization stage, and leader tenure leave β(VAI) essentially unchanged (Online Appendix C.2). A pre-registered 24-permutation specification curve gives median β = +0.107 with 24/24 positive and 22/24 significant (Online Appendix B.1). We read this as a descriptive compositional-substitution association, conditional on the instrument's validity, and stop short of a causal claim.

## 4.2 Application II: The within-document review-vs-plan differential (suggestive)

Exploiting the temporal structure of GWRs (a retrospective past-year review and a prospective next-year plan), we partition each report at the first plan marker after character 2000 and compute VAI on each section (N = 4,330 successful splits).

**Table 3. Within-document retrospective-vs-prospective VAI differential**

| Metric | Value |
|---|---:|
| Mean VAI(review) | 0.615 |
| Mean VAI(plan) | 0.591 |
| Mean Δ (review − plan) | **+0.0245** |
| Paired t | **8.40** |
| Two-tailed p | **6.2 × 10⁻¹⁷** |

The differential is positive and highly significant. It cannot arise from lexicon-selection (same lexicon), from author-style (the same author writes both sections), or from report-length (VAI is a ratio). We nonetheless report it as suggestive corroboration rather than a behavioral signature, since, as in R1, genre differences between retrospective and prospective sections could produce the same pattern (§4.2.1). With the criterion-validity test of §3.2.7 now carrying the behavioral argument, the within-document differential is a secondary, measurement-level fact about how reports are written.

### 4.2.1 What this does and does not tell us

The differential is compatible with the upward-signaling mechanism but is not a unique diagnostic. Downstream-facing rhetoric, lexical-availability bias, and selection on what gets completed-versus-planned would also predict it. Robustness to alternative split markers and to long-document/single-tenure subsamples is in Online Appendix C.3.

## 4.3 Application III: Independent corroboration in public-procurement data (new)

As an entirely separate, large-scale corroboration we classify the universe of Zhejiang public-procurement announcements (≈2,957,789 records, predominantly 2019–2026, national `ggzy.gov.cn` platform) by the same visible-versus-functional construction distinction. Visible-type projects outnumber functional ones by roughly 2-to-1 overall (2.1-to-1 among first-stage tender notices, the cleanest one-per-project proxy), and the tilt is pervasive rather than local: visible exceeds functional in 97 of 108 localities with sufficient volume (median city ratio 1.8; the exceptions are small county-level units; Online Appendix Figure ESM-6). Going beyond counts, we recover each project's investment amount from the tender briefs (16,794 award-stage projects, 2023–2024). Visible and functional projects are of broadly similar typical size (median ¥5.8M vs ¥4.7M), but the visible category owns the high-value tail. Its 99th percentile (¥0.90B vs ¥0.20B) and maximum (¥11.5B, the Hangzhou Metro Line 7 contract, vs ¥1.07B) are several times larger, because the biggest construction outlays (metro/rail, arterial roads, landmark parks) are visible-salient while concealed-utility works top out an order of magnitude lower. Visible construction thus predominates on both frequency and the high-value tail. The visible/functional classification was refined by LLM-assisted adjudication with domain-expert (urban- and rural-planning) sign-off (Authors' Contributions); the lexicon, re-pull and analysis code, per-city table, and amount distribution are deposited (`03-analysis/phase-L-bidding/`). One caveat is that a "project" is proxied by the deduplicated award record, so the count comparison (less so the amount comparison) is sensitive to how works are packaged; the accounting CIR (§4.1, §3.2.7) supplies the independent expenditure-share corroboration.

## 4.4 Structural welfare calibration (illustrative; demoted)

The cadre-attention model yields a closed-form welfare-loss expression. Calibrated with the observed compositional share, an assumed social optimum $a^{SO} \in [0.40, 0.50]$, and an aggregate renewal-expenditure base, it produces figures on the order of single-digit ¥ billions per year. We deliberately do not headline this number. It depends on strong assumptions that we have not independently validated: the Cobb-Douglas welfare function, the social-optimum benchmark, and the text-to-spending mapping. The derivation and sensitivity table are in Online Appendix A and C.7, and we attach no policy weight to the magnitude.

## 4.5 Demoted exercises: transparent reporting of failed/null tests

Two pre-registered tests are demoted from the main evidentiary structure (full detail in Appendix C.3 and Appendix D):

**Null 1, central-inspection event study (H2): definitively null.** A narrow-window TWFE specification gave the predicted sign (β(k=0) = −0.065, p = 0.011), but a heterogeneity-robust Sun–Abraham estimator attenuates it to insignificance and, extending to Rounds 6–9 (2016–2017), reverses the sign (β = +0.016). The narrow-window result is a staggered-treatment-heterogeneity artifact [14, 15, 16] rather than a causal inspection effect (deviations D-B-1/2/3).

**Null 2, individual-level CFPS micro-foundation (H5): bounded null.** Amenity-category-specific satisfaction items are absent from the public CFPS panel; substituted general outcomes show no effect above |d| = 0.011 (TOST rejects |d| ≥ 0.10 at p < 10⁻⁶). This bounds a citizen-popularity channel but does not test the pre-registered mechanism, and is reported as exploratory (deviation D-F-1).

## 4.6 Summary

The validated VAI tracks an external accounting measure of investment composition (P1, β = +0.111, with no effect on total investment). It co-moves with real cosmetic investment under an exogenous turnover shock while the naive measure does not (§3.2.7). In an entirely independent procurement corpus it is corroborated by a ≈2:1 visible-over-functional tilt across 97 of 108 localities and a visible-dominated spending tail (§4.3), and it shows a suggestive within-document differential (§4.2). The inspection event study, the CFPS micro-foundation, and the welfare calibration are demoted and reported transparently; they limit, rather than support, the causal and welfare claims the instrument can carry.


# 5. Discussion

## 5.1 What the paper establishes methodologically

The paper's contribution is the Visibility Attention Index, a pre-registered, replicable instrument for the visible-versus-functional composition of infrastructure language. It is now validated more rigorously than in the original draft, and honestly bounded:

- Direct passage-level validation (§3.2.0): the naive appearance-word dictionary fails (visible precision 0.10); the concrete, salience-based VAI reaches 0.50–0.60 but meets a polysemy ceiling near 0.60–0.64; an LLM ensemble clears it (0.84 accuracy, Fleiss κ = 0.835). Human intercoder agreement is Cohen κ = 0.70.
- Behavioral criterion validity (§3.2.7) is the test that does the work. Under an exogenous, retirement-driven turnover shock the concrete VAI co-moves with real cosmetic investment (+0.010, p = 0.01; clean pre-trend), while the naive measure does not (+0.002, p = 0.54). The construct is real in behavior, and the right measure tracks it.
- A cross-source accounting correlation (E-D, r = 0.24) provides independent external evidence, modest in magnitude. An independent-dictionary replication (E-A, r = 0.93) is a reliability check rather than a validation. And an independent procurement corroboration (§4.3) shows a ≈2:1 visible-over-functional tilt in 97 of 108 Zhejiang localities, with a visible-dominated spending tail.

One pre-registered test, applying the lexicon to Chinese Wikipedia, fails (r = −0.15 against a [0.3, 0.7] criterion). We report it plainly as a domain mismatch that bounds the instrument to governance rhetoric.

## 5.2 What substantively follows (conditional on the instrument)

Within cities, VAI tracks the accounting-based Cosmetic Investment Ratio (P1, β = +0.111) with no accompanying change in total investment. The association is therefore compositional rather than expansionary, and under the turnover shock both rise together. We read these as evidence that the measure captures strategic compositional attention. We do not offer a headline welfare figure, because the model-based calibration (§4.4) is too assumption-dependent to support one.

## 5.3 What we cannot establish

- Causal identification of drivers is not achieved. The inspection event study fails under heterogeneity-robust estimation (§4.5); the retirement-turnover design supports *measurement* (criterion) validity, not a causal theory of what produces visibility bias.
- External (non-governance) validity is bounded. The Wikipedia null scopes the measure to governance rhetoric, and an appropriate policy-rhetoric third-party validation (e.g., Xinhua local-policy news, CNKI key-newspaper coverage) remains future work.
- Intercoder agreement is substantial but not perfect. Two human coders reach Cohen κ = 0.70 on the 120-sentence gold set. Residual disagreement concentrates on the visible-versus-mixed boundary, itself a manifestation of the polysemy the paper documents, so passage-level precision/recall carry a few points of coder-judgment uncertainty.
- The procurement corroboration is provincial. It covers Zhejiang, and although frequency and amount both corroborate the tilt, a "project" is proxied by the deduplicated award record, so the count comparison is sensitive to packaging. National generalization is untested.
- No welfare claim. The structural welfare figure is assumption-dependent and demoted, and we attach no policy magnitude to it.

## 5.4 Portability to non-Chinese settings

The construction-and-validation protocol has a fixed shape: seed a dictionary, validate at the passage level, *report the ceiling*, escalate to LLM classification where needed, and anchor validity behaviorally against an accounting outcome under an exogenous shock. In principle this protocol ports to other settings where bureaucratic agents produce structured, consequential annual documents (EU National Reform Programmes; Indian state budget speeches; Mexican municipal *Plan de Desarrollo* documents), though we have not tested it outside China. What is *not* portable is the specific lexicon and the institutional observability-asymmetry parameters, which require re-derivation in each context. What transfers is the validation discipline, not the keyword list.

## 5.5 Policy implications (conditional on the cadre-attention model)

Suppose the cadre-attention model is substantively correct. It is theoretically motivated and now behaviorally supported (§3.2.7), though not cleanly identified causally. Three levers then follow. (1) Increase the observability of functional categories, reducing the legibility asymmetry, through real-time pipe-pressure telemetry, open waterworks dashboards, and mandatory structural-safety reporting. (2) Introduce functional output targets in cadre evaluation, raising the social-motivation weight. (3) Build citizen-audit portals as supplementary, informational pressure, given the §4.5 individual-level null. Because these follow from the model rather than from identified causal estimates, we offer them as model-implied possibilities rather than forecasts, and attach no net-present-value figure.

---

# 6. Conclusion

We set out to measure visibility bias in Chinese municipal government work reports and to take seriously the question applied dictionary work usually skips: does the measure capture the construct? The Visibility Attention Index, built from 6,294 GWRs, is validated directly at the passage level. We report that validation honestly, including the naive dictionary's failure (precision 0.10), the concrete lexicon's polysemy ceiling (~0.60), and an LLM ensemble that clears it (0.84). The behavioral test settles the question: under an exogenous retirement-turnover shock the valid measure co-moves with real cosmetic investment while the naive one does not. Descriptively, VAI tracks the accounting Cosmetic Investment Ratio and is corroborated by an independent procurement corpus, where visible projects run ≈2:1 over functional and own the high-value tail. One pre-registered third-party test failed and is reported plainly. An inspection event study, a CFPS micro-foundation, and a welfare calibration are demoted as non-robust or assumption-dependent.

The contribution is methodological: a pre-registered, passage-validated, behaviorally-anchored instrument for measuring compositional infrastructure rhetoric, with an honest map of its limits and a high-precision LLM alternative where the dictionary stops. Two points may carry beyond this one-country case and invite testing elsewhere. First, polysemy imposes a precision ceiling on dictionary measures of everyday-word constructs that curation cannot break, and that ceiling should be reported rather than hidden. Second, for measures of strategic attention the validity test that decides the matter is behavioral co-movement under an exogenous shock, not internal reliability or passage precision alone. We invite extension via a policy-rhetoric third-party corpus, further exogenous shocks, and application to bureaucratic text in other institutional settings.

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI 10.5281/zenodo.19569978; GitHub: andyhsi2023-cq/visibility-bias-v2.

---

# Statements and Declarations

**Competing Interests.** The authors declare no competing financial or non-financial interests related to this work.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work was conducted as part of the authors' professional research activities.

**Authors' Contributions.** Hongyang Xi and Liu Can contributed equally and are co-first authors. Hongyang Xi (corresponding author) conceived the study, constructed the lexicons and the LLM-ensemble classification, performed the data collection and statistical analysis (including the behavioral criterion-validity test), drafted the manuscript, and prepared the replication archive. Liu Can constructed and verified the public-procurement (bidding) evidence (§4.3), contributing urban- and rural-planning domain expertise to the visible-versus-functional classification of construction projects. Zhihui Li independently performed the second passage-level coding of the validation sample for the intercoder-reliability assessment (§3.2.0). All authors critically revised the manuscript, approved the final version, and are accountable for the integrity of the work.

**Data Availability.** All data, lexicons, code, and intermediate outputs are archived at Zenodo (DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978)) and mirrored on GitHub (`andyhsi2023-cq/visibility-bias-v2`). The Zenodo record is open access (CC-BY-4.0). Source government work reports are scraped from publicly accessible municipal government websites; CFPS individual data are obtained from the Institute of Social Science Survey at Peking University under their public data-use agreement; the China Urban Construction Statistical Yearbook (Ministry of Construction / MOHURD, 2005–2015) and Zhejiang public-procurement records are publicly archived.

**Code Availability.** All analysis scripts (Python; pandas, statsmodels) and the passage-validation and re-pull toolchains are archived in the Zenodo record.

**Pre-registration.** Pre-registered at the Open Science Framework (DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5), archived 2026-04-14); the passage-level human/LLM validation and the behavioral criterion-validity analyses are pre-specified extensions. All deviations are logged in Appendix D.

**Ethics Approval.** Not applicable. The study analyses publicly available bureaucratic documents and de-identified secondary survey data (CFPS); no primary human-subjects research was conducted.

**Consent for Publication.** Not applicable.

**Use of Generative AI.** Large-language-model classification is an *object of study and a measurement tool* in this paper (the three-family ensemble of §3.2.0), documented and reproducible. Separately, the authors used an LLM for copy-editing of draft prose; all substantive content, analysis, and interpretation are the authors' own.


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

**Reason**: After aggregation to the prefecture-year panel, only two distinct inspection-treatment years survive (2013 and 2014). All 31 provinces are eventually treated by Round 5 (2015), so there is no never-treated control group. Because the doubly-robust estimator requires such a group, the pre-registered specification is infeasible.

**Result under executed substitute**: β(k=0) = −0.065, SE = 0.025, p = 0.011.

### D-B-2 (Phase B2 — Sun-Abraham robustness check, same-window)

**Pre-registered**: Not in original pre-registration. Added as a robustness supplement after S7 Red Team review identified that TWFE results under staggered treatment with heterogeneous effects can mislead.

**Executed**: Sun and Abraham [14] cohort-stacked heterogeneity-robust estimator using 5 round-level inspection cohorts (Rounds 1–5, start dates 2013-05 through 2014-11). Cohort c uses later-treated cohorts' pre-treatment observations as controls.

**Result**: β(k=0) = −0.019, SE = 0.117, p = 0.87. The point estimate runs in the same direction as TWFE, but the magnitude is smaller by a factor of ~3 and significance is lost.

**Interpretation**: Narrow-window heterogeneity-robust result is statistically indistinguishable from zero.

### D-B-3 (Track 1 extension — Sun-Abraham with Rounds 1–9 / 2013–2017)

**Pre-registered**: Not in original pre-registration. Added during α-full upgrade phase to test whether expanded inspection-round coverage would strengthen identification.

**Executed**: Expanded treatment panel to include Rounds 6–9 (2016–2017, including "look-back" re-inspections covering 23 provinces that had been treated in Rounds 1–5). Total 62 province-round records. Re-fit the Sun-Abraham cohort-stacked estimator with 9 cohorts spanning 2013-05 through 2017-04.

**Result**: β(k=0) = **+0.016**, SE = 0.012, p = 0.19. β(k=+3) = +0.047, p = 0.005 (significant POSITIVE). **Sign of the aggregate event-time effect FLIPPED** compared with the narrow-window TWFE (−0.065) and the narrow-window Sun-Abraham (−0.019).

**Interpretation**: All nine cohort-specific CATT(k=0) values under the expanded sample are positive (+0.011 to +0.083). The original TWFE negative coefficient was a staggered-treatment-bias artifact [15, 16], not a causal inspection effect. We report H2 as **definitively null** in §4.5. The pre-registered "consistent with prediction" framing from earlier drafts is withdrawn. We log this deviation honestly; it represents a substantive failed identification, not a methodological quibble.

### D-E-1 (Phase E — Construct validity, internal tests)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, provincial-government descriptive texts); correlation with primary VAI in [0.3, 0.7] range; independent β(VAI_3rd → CIR) > 0.

**Executed**: Three internal construct-validity tests as supplements (not substitutes) for the external test:
- E-A: Expanded internal dictionary (78+70 terms, independently curated), giving r(VAI_orig, VAI_ext) = 0.93.
- E-B: Within-document retrospective-vs-prospective section split, with Δ(review − plan) = +0.025, paired t = 8.4, p < 10⁻¹⁶.
- E-C: Dictionary-bootstrap half-halves, mean r = 0.18 (reported as limitation).
- E-A CIR replication with VAI_ext, a further check, gave β = +0.111, p = 0.011.

**Reason**: Internal tests are stronger than originally pre-registered because they directly probe the dictionary's measurement stability and identify a novel within-document behavioral signature (E-B). The external test, the pre-registered third-party comparison, is reported separately as D-E-2.

### D-E-2 (Phase E2 — Third-party text validation, EXECUTED and FAILED)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, Baidu Baike city descriptions); correlation with primary VAI in [0.3, 0.7]; independent β(VAI_3rd → CIR) > 0, p < 5%.

**Executed**: Substituted Chinese Wikipedia (zh.wikipedia.org) as a publicly-accessible third-party source, fetched via the MediaWiki API. 282 of 286 target cities fetched (4 misses: Ji'an, Songyuan, Meizhou, Baishan). Mean article length 8,447 chars. Same V_ORIG + F_ORIG lexicon applied.

**Result**:
- Correlation r(VAI_wikipedia, VAI_primary_mean) = **−0.15**, 95% CI [−0.31, +0.02]. **Pre-registered [0.3, 0.7] band FAILED.**
- CIR cross-sectional β(VAI_wikipedia) = +0.020, p = 0.57. Pre-registered "β > 0 at 5%" FAILED.
- Horse race: VAI_primary retains all predictive power (β = +0.51, p = 0.007); VAI_wikipedia residual adds nothing (β = +0.04, p = 0.27).

**Reason for substitute source**: Xinhua news and CNKI key-newspaper archives require CARSI-authenticated institutional access that was not available in the α-full session. Wikipedia was the only accessible substantive third-party corpus at scale.

**Interpretation**: We read the null as evidence that encyclopedic descriptive text (Wikipedia) is a domain-mismatched source for a governance-rhetoric measurement instrument, rather than as evidence that the VAI itself is invalid. The appropriate third-party source is *policy-rhetoric* text (Xinhua local-policy news or CNKI key-newspaper government reporting), whose construction is deferred to future work (see §5.3). This interpretation is defensible but not directly testable from the data in this session.

**Honesty claim**: The failure is reported transparently in §3.2.5 of the main manuscript (the failed Wikipedia external validation, E-F), and the interpretation is flagged as provisional.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401–qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: **positive differential** |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes: qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this.

**Result**: All three coefficients |β| ≤ 0.011, |d| ≤ 0.011. TOST at ±0.10 equivalence bounds rejects |β| ≥ 0.10 at p < 10⁻⁶.

**Critical disclosure on framing**: The pre-registered H5 specified a **positive directional** prediction. The observed result is a clean null. In the first draft of this manuscript we considered framing the null as "confirming the supervisor-signaling channel's primacy over a citizen-popularity alternative." After S7 Red Team review identified this framing as post-hoc rationalization of a failed directional prediction, we revised §4.5 to report the results as **exploratory rather than confirmatory**, with a TOST-based quantitative bound and explicit acknowledgment that the null leaves multiple theoretical interpretations open. This revision was made before submission.

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

**Two deviations (D-B-2, D-E-2) weaken the original causal/external claims; one extension (D-J-1) supplies the paper's new central evidence.** We report all transparently. The revised paper's spine is the behavioral criterion-validity co-movement (D-J-1): under an exogenous retirement-turnover shock the valid concrete measure co-moves with real cosmetic investment (+0.010, p = 0.01) while the naive measure does not (+0.002, p = 0.54). The measurement contributions are the passage-level validation with its reported polysemy ceiling and the LLM-ensemble high-precision alternative (both §3.2.0). The cross-sectional β(VAI → CIR) association and the structural welfare calibration are demoted to supporting/illustrative. The failed P2 inspection design (D-B-3) and the failed H4/H5 tests (D-E-2/D-F-1) are reported honestly. They narrow the scope but do not bear on the criterion-validity spine.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.5's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.4's opening paragraph).


# Online Appendix

**Manuscript**: *Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation*

**Authors**: Hongyang Xi (Chongqing Survey Institute)†, Liu Can (Guangzhou College of Applied Science and Technology)†, Zhihui Li (Chongqing Survey Institute) · †co-first authors
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication**: Zenodo DOI 10.5281/zenodo.19569978

---

## Appendix A: The Full Cadre-Attention Model

The main text (§2) gives an intuitive summary of the cadre-attention model. The full derivation follows.

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

This quadratic form allows calibration from observed $a_i^*$ together with a standard social-optimum benchmark $a_i^{SO}$.

## Appendix B: Specification Curve (P1 Robustness — demoted)

*This appendix supports the cross-sectional VAI→CIR association (§4.1), a modest external check (E-D, §3.2.4). It is not part of the main evidentiary spine, which rests on the behavioral criterion-validity co-movement of §3.2.7.*

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

### C.3 P2 placebo battery (main text §4.5)

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
3. **Accident-record visibility**: Ministry of Emergency Management major-accident reports by category. Only visible-category accidents (street collapse, façade fall) receive consistent national news coverage. Functional failures (pipe rupture, flooding) are usually reported only as aggregate statistics.

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

**Defensible range**: ¥1–15B/yr under log utility and $a^{SO} \in [0.40, 0.50]$. The ¥55B BOE is a ceiling. (This calibration is demoted; the main text attaches no headline welfare figure. See §4.4.)

### C.8 Passage-validation confusion matrix and error taxonomy (main text §3.2.0)

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

`示范` alone accounts for ~70% of visible false positives. This single-cause failure motivated the move to a concrete, salience-based lexicon (§3.2.2). Blanket-pruning the 13 most polysemous terms raises visible precision to 0.59 but collapses recall to 0.47, so the fix is surgical.

**Human intercoder agreement.** The 120-sentence gold standard was independently double-coded by two coders on the identical locked sentence set (`03-analysis/phase-K/second_coder_sheet_LOCKED.csv`, with dictionary and ensemble labels hidden). The **human intercoder agreement is Cohen κ = 0.70** (substantial; n = 120). Agreement is highest on the irrelevant and functional classes. The residual disagreement concentrates on the visible-versus-mixed boundary, consistent with the polysemy difficulty documented in §3.2.0, which is itself part of why high passage precision favors the LLM ensemble. Human↔ensemble agreement is Cohen κ = 0.66.

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


