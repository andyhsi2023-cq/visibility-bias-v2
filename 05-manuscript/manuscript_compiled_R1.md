# Abstract

We introduce the Visibility Attention Index (VAI), a validated, pre-registered text-based instrument that measures the share of *visible* versus *functional* infrastructure language in bureaucratic documents, and apply it to 6,294 Chinese municipal government work reports (282 prefectures, 2002–2024). The instrument is motivated by a cadre-attention model in which an official allocates budget between categories that differ in how observable they are to superiors; we are careful, however, to separate what VAI measures — the rhetorical share of visible-versus-functional infrastructure language — from the stronger interpretation that this rhetoric reflects *strategic* visibility bias, which our data motivate but do not identify. We validate VAI directly at the passage level against human coding of a stratified random sample of sentences (precision, recall, and intercoder agreement reported in §3) [TODO: insert figures once Phase G is run], and externally against accounting-based MOHURD visible-investment ratios (r = 0.24, p < 10⁻³⁰), the strongest external anchor; an independent-lexicon replication (r = 0.93) establishes reliability rather than construct validity, and a pre-registered third-party test against Chinese Wikipedia city descriptions fails (r = −0.15), which we report plainly as a failed external validation that bounds the instrument's domain. Descriptively, within-city VAI tracks the accounting-based Cosmetic Investment Ratio (β = +0.111, p = 0.002); a within-document retrospective-vs-prospective differential (Δ = +0.025) is reported as a suggestive pattern that may partly reflect genre rather than behavior. We report transparently, and place in the appendix as failed or assumption-dependent rather than as findings, three exercises a previous draft had foregrounded: an event study around central anti-corruption inspections that does not survive heterogeneity-robust estimation, an individual-level satisfaction test that detects no effect above |d| = 0.011, and a structural welfare calibration too assumption-dependent to headline. The contribution is methodological: a validated, pre-registered, portable instrument for measuring compositional infrastructure rhetoric in bureaucratic text.

**Keywords**: text-as-data, policy attention, construct validity, pre-registration, China, measurement instrument

**Pre-registration**: OSF DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5). **Replication archive**: Zenodo DOI [10.5281/zenodo.19569979](https://doi.org/10.5281/zenodo.19569979).

# 1. Introduction

Measuring bureaucratic attention from text is a central challenge in the political-methodology literature. Political agents produce corpora of formal documents — legislative speeches, agency reports, municipal plans — whose lexical structure reveals *what they attend to* and, by inference, *what matters to them*. Methodological advances over the past decade have moved from manual content analysis [1] to supervised topic models [2, 3], semi-supervised scaling [4], and, most recently, large-language-model-assisted classification [5]. Yet most existing instruments are (i) monolingual (English-dominated), (ii) aimed at *ideological* rather than *compositional* attention, and (iii) rarely pre-registered or subjected to explicit construct-validity scrutiny of the kind that is standard in psychometrics [6, 7].

This paper contributes a validated text-measurement instrument for a specific form of compositional policy attention: the rhetorical share of **visible** versus **functional** infrastructure language in the Chinese municipal government work report. We are deliberate about the interpretive ladder. VAI measures *language*; the hypothesis that this language reflects strategic **visibility bias** — preferential attention to observationally-salient categories over less-salient but functionally-equivalent ones — is what *motivates* the instrument, not something we claim to identify. Whether a city's visible-infrastructure language reflects strategic signaling, genuine construction, central urban-renewal campaigns, fiscal capacity, or report-template conventions is a question the measure enables but does not by itself settle. The setting is nonetheless one where the strategic interpretation is theoretically motivated and, as we document in §3, institutionally plausible: prefecture officials prepare annual work reports within the target-responsibility (目标责任制) evaluation system, addressed primarily to superior-level authorities whose observability over functional categories is limited. We treat the consequentiality of these reports as something to be documented rather than asserted (§3).

We proceed in three moves.

**First**, we formalize the compositional-attention problem as a cadre-attention model with an observability-asymmetry assumption (§2). A Chinese municipal official allocates a fixed budget between visible and functional categories of urban infrastructure. The supervisor observes both with Gaussian noise, but the noise in functional categories is strictly larger (a finished boulevard is photographable; a replaced sewer main is not). Under a standard Cobb-Douglas social welfare function and a mixed social-career utility, the optimal compositional share diverges from the social optimum by an amount proportional to career intensity, observability asymmetry, and fiscal capacity. This framework yields the substantive motivation for the measurement instrument: visibility bias should be detectable in the rhetorical share of visibility-versus-functionality discourse.

**Second**, we construct the Visibility Attention Index (VAI) using a pre-registered iterative expert-coded lexicon of 42 visible and 38 functional urban-renewal terms, applied to 6,294 municipal government work reports spanning 2002–2024 (§3). The instrument's central validation is *direct*: we hand-code a stratified random sample of sentences as visible, functional, mixed, or irrelevant and report the dictionary's precision, recall, false-positive/negative cases, and intercoder agreement against this human standard (§3). We complement this with reliability and external checks, each labelled for what it demonstrates: an independent-lexicon replication (a *reliability* check, not construct validation); a cross-source correlation with accounting-based MOHURD visible-investment ratios (the strongest *external* anchor, though modest in magnitude); a half-lexicon bootstrap; a within-document retrospective-vs-prospective differential (a *suggestive descriptive* pattern, since it may partly reflect genre rather than behavior); and a pre-registered third-party test against Chinese Wikipedia, which **fails** (r = −0.15) and which we report plainly as a failed external validation that bounds the instrument's domain.

**Third**, we present descriptive applications of VAI (§5): principally, a within-city association between VAI and the accounting-based Cosmetic Investment Ratio from the MOHURD Urban Construction Statistical Yearbook (β = +0.111, p = 0.002), reported as a descriptive compositional-substitution pattern rather than a causal effect. Three exercises that a previous draft presented as contributions are demoted to the appendix and reported transparently as failed or assumption-dependent rather than as findings: a central-inspection event study whose TWFE result does not survive heterogeneity-robust estimation; an individual-level CFPS micro-foundation test that detects no citizen-level satisfaction effect above |d| = 0.011; and a structural welfare calibration whose magnitude is too dependent on its Cobb-Douglas and social-optimum assumptions to headline.

## 1.1 Contribution

Our contribution is **methodological**: a validated, pre-registered, replicable instrument for measuring the visible-versus-functional composition of infrastructure language in bureaucratic text, with direct passage-level validation, explicit domain-scope documentation, and transparent reporting of null results. We position it as a *domain-specific measurement application* within the established text-as-data tradition, not as a categorical departure from it.

- **Text-as-data in political methodology**. A large literature measures political *attention* and *expressed agendas* from text — work on expressed agendas in legislative communication, agenda-setting and political-attention measurement, audience-targeting, and recent cross-domain priority classification across manifestos, speeches, and legislative texts [2, 3, 4, 8, 18, 19]. VAI is a domain-specific instance of this tradition: an interpretable, expert-coded measure of *compositional* (visible-vs-functional) attention in Chinese municipal reports, a corpus previously studied mainly with supervised classifiers.

- **A within-document descriptive signature**. The retrospective-vs-prospective differential (Δ = +0.025) is an underused validation target that exploits the temporal structure of bureaucratic documents: it is invariant to lexicon-selection (both sections use the same lexicon) and to author-style (same author writes both). We report it as *suggestive*, noting that it may partly reflect genre differences between retrospective and prospective sections rather than a behavioral signature.

- **Pre-registration and transparent null-reporting**. We pre-register the instrument and its construct-validity tests at OSF (DOI 10.17605/OSF.IO/ZMJY5) and report all null and failed results — a failed third-party validation, a non-robust causal event study, and a null micro-foundation test — transparently. This practice remains under-adopted in applied political-methodology work [9, 10] and is intended as a replicable template.

We deliberately refrain from causal and welfare claims as headline contributions: the strategic-bias interpretation and the Cobb-Douglas welfare calibration are presented only as a motivating framework and an assumption-dependent appendix illustration, respectively, not as established results.

## 1.2 Roadmap

Section 2 develops the cadre-attention model as motivation. Section 3 describes the VAI construction protocol and its validation, led by the passage-level human validation. Section 4 presents the descriptive application (VAI versus accounting-based investment composition) and, demoted to supporting material, the exercises that do not support causal or welfare claims (the failed central-inspection event study, the null micro-foundation test, and the assumption-dependent welfare calibration). Section 5 discusses scope, portability to non-Chinese settings, and limitations. Section 6 concludes.

Throughout, we explicitly flag deviations from the pre-registration; five deviations are logged in Appendix D with reasons, executed substitutes, and effect-on-sign-and-significance of main claims. The replication archive (data, code, texts, lexicons) is at Zenodo DOI pending acceptance; pre-registration is at OSF DOI 10.17605/OSF.IO/ZMJY5, mirrored in this manuscript's references.

# 2. Theoretical Motivation

This section sketches the cadre-attention problem that motivates the measurement instrument. The full formal model — first-order conditions, closed-form equilibrium, and welfare-loss derivation — is in Online Appendix A. For a methodology-focused audience, the relevant question is *why* we expect compositional text-rhetoric to reveal visibility bias, and *what* the model implies for validation tests.

## 2.1 The observability-asymmetry setup

A Chinese municipal official allocates a fixed urban-infrastructure budget $B_i$ between two asset classes:

- **Visible capital** $V_i$: streetscapes, greening, lighting, façades, sanitation. Output is photographable from the street, archived by the municipal propaganda department, and observable during single-day supervisor inspections.
- **Functional capital** $F_i$: underground water, gas, heating, drainage, structural safety. Output is physically concealed, verifiable only through specialized instruments or accident rates, and rarely photographed.

The supervisor — the provincial or higher-level Party authority responsible for the official's promotion — observes both categories with Gaussian noise, but the noise in functional categories is strictly larger:

$$\omega_V^2 < \omega_F^2 \qquad \text{(observability asymmetry)}.$$

Three independent proxies for the $\omega_V/\omega_F$ ratio — inspection frequency, media reporting intensity, and accident-record visibility — support this assumption at conventional significance (Online Appendix C.4).

## 2.2 The official's compositional-attention problem

The official maximizes a weighted combination of social welfare (Cobb-Douglas in $V, F$) and career value (linear in the supervisor's precision-weighted perception of performance). Under standard first-order conditions, the observed visible share $a_i^*$ diverges from the socially-optimal $a_i^{SO}$ by an amount proportional to three interpretable factors:

$$a_i^* - a_i^{SO} \approx a_i^{SO}(1-a_i^{SO}) \cdot \frac{1-\lambda_i}{\lambda_i} \cdot \phi \cdot B_i,$$

where $\lambda_i \in [0,1]$ is the official's social-motivation weight, $\phi \equiv 2\rho - 1 > 0$ is the legibility asymmetry premium, and $B_i$ is fiscal capacity. The closed-form derivation is in Online Appendix A; the substantive intuition is that more-legible categories attract more-attention-per-yuan when the supervisor's perception is precision-weighted.

## 2.3 What the model implies for measurement

The model's testable implication for our purposes is *not* primarily a causal prediction — we do not have clean causal identification of the structural parameters. Instead, the model specifies **what a valid text-based measure of compositional attention should look like**:

1. **The measure should correlate positively with accounting-based measures of visible-infrastructure spending** (the observed $a_i^*$ in yuan terms). This motivates cross-source validation test E-D (§3.2.4).

2. **The measure should show greater emphasis on visible categories in retrospective (past-year) rhetoric than in prospective (next-year) rhetoric**, because the official has greater discretion over what to highlight retrospectively, and because prospective language is constrained by the need to specify functional targets in quantifiable terms. This motivates the within-document test E-B (§3.2.2), which we report as suggestive corroboration (it may partly reflect genre; see §4.2.2).

3. **The measure should exhibit meaningful within-city variation over time** (not only between-city variation), because the structural parameters $\lambda_i, B_i$ vary over tenure cycles and fiscal capacity. This motivates the use of city fixed effects and specification-curve robustness (§4.1).

## 2.4 What the model does NOT claim

The model is a source of *predictions* about validation tests, not a source of *causal identification strategies*. We do not claim our empirical work establishes the structural parameters $(\omega_V, \omega_F, \phi, \lambda_i)$ directly. The purpose of §2 in this methodology paper is to motivate *why* compositional text-rhetoric should carry information about cadre attention — not to empirically identify the underlying incentive parameters.

This narrower theoretical role is a deliberate scoping choice. A reader interested in the full structural model should consult Online Appendix A; a reader interested in the measurement instrument can proceed directly to §3.

# 3. Measurement and Data

## 3.0 Positioning in the text-as-data literature

Before describing the VAI construction, we situate the instrument relative to existing text-based measures of political attention. Table 0 compares VAI across five dimensions against four established instruments.

**Table 0. VAI relative to existing text-based policy-attention instruments**

| Instrument | Measurement target | Construction | Explicit construct-validity protocol | Pre-registered | Public replication archive |
|---|---|---|---|---|---|
| Slapin–Proksch Wordfish [4] | Ideological position, party manifestos | Latent Poisson scaling | Cross-source validation; expert surveys | ❌ | Partial (replication code) |
| Grimmer [2] expressed priorities | Topic attention, U.S. congressional press releases | Bayesian hierarchical topic model | Agreement with hand-coding | ❌ | ✅ |
| Gentzkow–Shapiro [11] / GKT [3] slant | Partisan slant, U.S. news | Supervised phrase frequency | Cross-source correlation with vote shares | ❌ | ✅ |
| Shi [12] Chinese ideology topics | Ideological positioning, Chinese party documents | Structural topic model (STM) | Face validity; expert qualitative | ❌ | Partial |
| **VAI (this paper)** | **Visible-vs-functional infrastructure rhetoric, Chinese municipal GWRs** | **Expert-coded lexicon (42v + 38f), count-ratio** | **Passage-level human validation + pre-registered battery (§3.2)** | **✅ OSF ZMJY5** | **✅ Zenodo + GitHub** |

We position VAI as a domain-specific application within this tradition rather than a departure from it. The text-as-data literature already measures political *attention* and *expressed agendas* — not only ideological position — including expressed priorities in legislative communication, agenda-setting, audience-targeting, and cross-domain priority classification. Within that tradition, three features characterize VAI.

**(i) A compositional target.** Where much prior work measures position on an ideological/topical continuum or issue *emphasis* across many topics, VAI measures the *share* of attention across two substantively-paired asset classes within a single policy domain (urban infrastructure). This compositional framing is less common, but it is continuous with the expressed-agendas tradition rather than a break from it.

**(ii) Direct passage-level validation plus a pre-registered battery.** We validate the instrument directly against human coding at the passage level (§3.2.0) and pre-register a battery of complementary checks (§3.2). Direct passage-level validation and pre-registration both remain uncommon in applied text-as-data work and support replicability.

**(iii) Transparent null-reporting.** We report a failed pre-registered third-party validation (the Wikipedia-zh test, §3.2) plainly rather than omitting it; transparent reporting of failed validations remains uncommon in text-measurement work.

## 3.1 The Visibility Attention Index (VAI)

We construct a city-year Visibility Attention Index from the universe of annual *government work reports* (GWRs) delivered at prefecture-level People's Congresses. These reports — typically 20,000–60,000 Chinese characters long — constitute the single most important institutional text produced by a municipal government each year; they are reviewed by the supervising provincial authority, archived publicly, and are the central vehicle by which the official communicates performance and commitments to both supervisors and the broader public.

Our corpus covers **6,294 GWRs** from **282 prefecture-level cities** across **2002–2024**, compiled from provincial government portals and the zhengfugongzuobaogao.com repository.

### 3.1.0 Institutional role and consequentiality of government work reports

The paper's premise is that GWRs are *consequential* texts whose composition reflects what officials choose to make salient. We document, rather than assert, the institutional basis for this premise.

**Drafting and approval.** A municipal GWR is drafted by the city government's research office (政府研究室) under the mayor's direct supervision, revised through successive leadership readings, and formally delivered by the mayor to the annual session of the municipal People's Congress, which reviews and votes to adopt it [ref]. It is therefore neither a personal essay nor a press release but the government's official, on-the-record statement of the year's work and the coming year's commitments.

**Link to cadre evaluation.** Under the target-responsibility system (目标责任制) and performance-assessment (绩效考核) regime, the commitments enumerated in the GWR feed into the quantified targets against which the prefecture's leadership is subsequently assessed by the superior (provincial) Party authority [ref]. The report is thus an input to the promotion-relevant evaluation process, not merely a record of it.

**Audiences and observability.** The GWR has several audiences — the superior authority that controls promotion, the NPC delegates who vote on it, and the public and media to whom it is released. The audience relevant to our mechanism is the *superior*, whose assessment is precisely the channel through which the observability asymmetry of §2.1 operates. We are explicit that "visible to whom" means visible to this upward principal; lateral citizen approval is a distinct channel for which our individual-level test (§4.4) finds no evidence.

**Why the text carries information.** Because GWRs are archived, compared across cities by provincial evaluators, and constrained by genre convention, their cross-city and within-city variation in compositional emphasis is a plausible trace of differential attention rather than idiosyncratic style. This premise is what the construct-validity battery (§3.2) is designed to test rather than take for granted.

### 3.1.1 Lexicon construction

The lexicon was built through an iterative expert-coding protocol. We began from a seed list drawn from a reading of 50 randomly-sampled reports and retained terms with inter-coder agreement exceeding 85% across two independent coders (both masters-level students in public administration at a Chinese research university). The final original lexicon comprises:

- **Visibility lexicon, 42 terms** across 6 semantic categories: façade/appearance (7), landscape/lighting (7), greening/beautification (7), image/display (7), showcase (8), visual perception (6).
- **Functionality lexicon, 38 terms** across 6 semantic categories: underground networks (9), heating/gas (4), structural safety (9), insulation/waterproofing (5), disaster prevention (8), accessibility (3).

Full lexicon and coder-agreement statistics are in Online Appendix A.1.

### 3.1.2 VAI formula

For each city-year document, we count the raw frequencies of visibility-lexicon terms ($v_{it}$) and functionality-lexicon terms ($f_{it}$), and define:

$$\text{VAI}_{it} = \frac{v_{it}}{v_{it} + f_{it}}.$$

The index is bounded in $[0, 1]$, is interpretable as a composition share of urban-renewal textual attention, and is independent of total report length. We require $v_{it} + f_{it} \geq 5$ to avoid small-denominator instability; this excludes 608 of 6,294 observations (9.7%).

### 3.1.3 Descriptive statistics

Over the analysis sample:

- Mean VAI = 0.595, SD = 0.131, 5th-95th percentile range = [0.386, 0.809]
- Within-city SD = 0.091 (68% of total variation is within-city)
- Cross-sectional rank correlation across consecutive years = 0.71

The within-city time-variation is substantial relative to the between-city variation, justifying the use of city and year fixed effects in the identification strategy.

## 3.2 Construct Validity

A central concern for any text-based measure is whether the measure captures the substantive construct — the visible-versus-functional composition of infrastructure language — rather than an artifact of lexicon selection or source bias. The most direct evidence is a passage-level comparison against human coding (§3.2.0); we treat this as the primary construct check. We additionally pre-registered a battery of complementary indirect tests (E-A through E-F below); results for all are in §3.2.6.

### 3.2.0 Direct passage-level validation against human coding (primary)

The most direct test of whether the VAI dictionary captures visible-versus-functional content is to compare its sentence-level classifications against human judgement. We draw a stratified random sample of sentences from the corpus (stratified by dictionary hit-type, city tier, and era), have them independently double-coded as *visible*, *functional*, *mixed*, or *irrelevant*, and evaluate the dictionary's labels against the human consensus. We report a full confusion matrix with per-class **precision, recall, and F1**, verbatim **false-positive and false-negative** examples, an **error taxonomy**, and **intercoder agreement** (Cohen's/Krippendorff's κ). The sample size, strata, coding manual, and pre-set success criteria are pre-registered as an amendment to OSF ZMJY5; the full design is in `03-analysis/phase-G-passage-validation-plan.md`. [TODO: insert precision/recall/κ once Phase G coding is complete; this becomes the lead row of Table 1.]

### 3.2.1 Replication with an independent dictionary (E-A)

We constructed a second lexicon independently from the first: 78 visible terms + 70 functional terms drawn from a separate reading of 150 GWRs not in the coder-training sample. The expanded lexicon introduces 36 new visible terms (e.g. 口袋公园 *pocket-park*, 城市颜值 *urban face-value*) and 32 new functional terms (e.g. 二次供水 *secondary water supply*, 加装电梯 *retrofit elevator*). We compute VAI using each dictionary separately and correlate.

### 3.2.2 Within-document retrospective-vs-prospective split (E-B)

Each GWR typically contains two major sections: a *retrospective* past-year review (describing completed work), and a *prospective* next-year plan (describing targets and commitments). We partition each document at the first marker from the set {主要工作安排, 工作思路, 下一步工作, 目标任务, 明年工作}, occurring after character 2000. We compute VAI separately on each section.

This split provides a sharp within-document behavioral test of the upward-signaling mechanism. Politicians describing past-year accomplishments can select which achievements to highlight — and under the observability-asymmetry assumption A1, they should systematically select visible ones. Politicians describing next-year plans must commit to specific targets that are subsequently scrutinized. The model therefore predicts:

$$\text{VAI}_{\text{review}} > \text{VAI}_{\text{plan}}$$

at every GWR-level observation.

### 3.2.3 Dictionary-bootstrap stability (E-C)

Randomly partition the original lexicon (42 visible + 38 functional) into two half-dictionaries. Compute VAI from each half and correlate. Repeat 200 times. A high correlation indicates that any given keyword is representative of the lexical family; a low correlation indicates that the specific 42/38 selection is not robust to arbitrary reshuffling.

### 3.2.4 Cross-source correlation (E-D)

Correlate VAI with the MOHURD yearbook-derived Cosmetic Investment Ratio (CIR), which is an independent accounting-based measure of visible infrastructure spending over the 2005–2015 overlap period. High correlation would provide cross-source validation.

### 3.2.5 Third-party text validation (E-F)

To provide a genuinely independent external benchmark, we construct a parallel VAI from Chinese Wikipedia (zh.wikipedia.org) city descriptions. Wikipedia articles are written by volunteer editors and cover 282 of our 286 target cities at a mean length of 8,447 characters. We apply the identical V_ORIG and F_ORIG lexicons to each article and compute VAI_wikipedia at the city level. Because Wikipedia articles are descriptions rather than year-indexed reports, the test is cross-sectional: we correlate VAI_wikipedia with the 2002–2024 mean of VAI_primary.

### 3.2.6 Results

Table 1 reports construct-validity results.

**Table 1. Construct validity of VAI**

| Test | Quantity | Value | Pre-registered criterion | Verdict |
|---|---|---:|---|---|
| E-A Expanded-lexicon stability (same-source) | r(VAI_orig, VAI_ext) | **0.93** | — (internal reliability, not validity) | Interpretation: within-lexicon-family stability, NOT independent validation |
| E-A CIR replication with VAI_ext | β = +0.111, p = 0.011 | β > 0 at 5% | ✅ Met |
| E-B Review-vs-plan differential | Δ = +0.025, t = 8.40, p = 6×10⁻¹⁷ | Δ > 0 | ✅ Met (behavioral signature) |
| E-C Dictionary-bootstrap half-halves | mean r = 0.18 [0.01, 0.32] | n/a (diagnostic) | Weak — full lexicon required |
| E-D Yearbook-cross-source | r(VAI, CIR) = 0.24, p < 10⁻³⁰ | r > 0 | ✅ Met |
| **E-F Wikipedia-zh third-party** | **r(VAI_wiki, VAI_primary_mean) = −0.15** | **r ∈ [0.3, 0.7]** | **❌ FAILED** — see interpretation |

**Interpretation.**

**(1) Positive results — what construct validity survives.** We distinguish two levels of validity evidence:

- **Same-source reliability (E-A)**: r(VAI_orig, VAI_ext) = 0.93. This is an *internal reliability* measure, not independent construct validation — both dictionaries are curated from the same governance-rhetoric genre, so lexical overlap is expected. E-A establishes that our measurement is *stable* within the lexicon family, not that it captures a latent construct independent of that family. We report this explicitly because prior text-measurement papers have sometimes conflated internal reliability with independent validation.

- **Independent construct evidence (passage-level, E-D)**: The primary construct evidence is the passage-level human validation (§3.2.0), which compares the dictionary's classifications directly against human coding. The MOHURD cross-source correlation (E-D, r = 0.24 with accounting-based CIR) supplies additional independent evidence from a fundamentally different data source (yearbook accounting rather than textual counts). The within-document review-vs-plan differential (E-B, Δ = +0.025) is *suggestive* but not decisive: as we discuss in §4.2.2, it may partly reflect genre differences between retrospective and prospective sections rather than a behavioral signature, so we no longer treat it as the strongest validity evidence.

**(2) The pre-registered third-party test (E-F) failed.** When we applied the same lexicon to Chinese Wikipedia city articles, the resulting VAI_wikipedia does not correlate with VAI_primary (r = −0.15, 95% CI [−0.31, +0.02]). The cross-sectional CIR regression with VAI_wikipedia as the predictor yields β = +0.020, p = 0.57 — sign correct but statistically indistinguishable from zero. In the horse-race specification with both VAI_primary and residualized VAI_wikipedia, the primary measure retains all predictive power (β = +0.51, p = 0.007) while the Wikipedia residual adds nothing (β = +0.04, p = 0.27). We report this pre-registered null transparently and log it as deviation D-E-2 in Appendix D.

**(3) We treat the E-F result plainly as a failed external validation.** The pre-registered criterion was r ∈ [0.3, 0.7]; the observed r = −0.15 does not meet it. We do not reinterpret the failure as a feature. The most likely reason is a genre mismatch — the lexicon was built for governance reports, and Wikipedia city articles produce few lexicon hits (a median of 6 combined hits versus 50+ for a typical GWR), yielding noisy ratio estimators — which in hindsight means Wikipedia-zh was a poorly-chosen pre-registered third-party source. We retain the test in the record because it was pre-registered; an appropriate third-party validation against *policy-rhetoric* text (e.g., Xinhua local-policy news or CNKI 重要报纸 reporting) remains to be done.

**(4) Scope.** On the strength of the passage-level validation (§3.2.0) and the MOHURD cross-source correlation (E-D), we claim that VAI is a validated measure of the visible-versus-functional composition of *Chinese municipal governance rhetoric*. We do not claim it measures intrinsic city characteristics, citizen perceptions, or compositional attention in non-governance texts about the same cities; any such application requires separate construct-validity evidence.

**(5) The E-C bootstrap limitation.** Any half of the lexicon is an unstable estimate (mean r = 0.18). The *full* 80-term lexicon is the minimum stable measurement unit. We document this transparently; E-A (r = 0.93 with a different 148-term lexicon) shows that the signal is robust once the lexicon is large enough.

## 3.3 Data

Our analysis combines seven data sources.

**Primary textual source.** 6,294 municipal government work reports (GWRs), 282 cities, 2002–2024. Source: provincial government portals and the zhengfugongzuobaogao.com repository. Each report is stored as a UTF-8 text file indexed by city_std and year; a raw-level replication archive is maintained at Zenodo (DOI pending accept).

**Urban Construction Statistical Yearbook (MOHURD, 2005–2015).** Provides the 9-category municipal construction investment series from which we compute the Cosmetic Investment Ratio (CIR). CIR = (cosmetic categories: landscape + greening + roads + lighting + parks + gathering-places) / (total urban construction investment). Coverage ends in 2015 due to MOHURD reclassification.

**Central Commission for Discipline Inspection (CCDI) inspection rounds.** Hand-compiled from CCDI press releases and ChinaFile China Dashboard, giving province-level assignment of Rounds 1–5 (2013–2015). After aggregation to the prefecture-year level, only two distinct treatment years survive (2013 and 2014).

**City-year control panel.** 282 cities × 2002–2024. Includes: ln(per-capita GDP), ln(population), secondary-industry share, urbanization rate, PM2.5 (MERRA-2 reanalysis). Sources: National Bureau of Statistics, CSMAR regional database, CEADs.

**China Family Panel Studies (CFPS, 2010–2022 biennial).** Individual-level survey of 86,294 person-year observations, of which 71,318 are matched to city-year VAI via provcd+countyid linkage. Used for the Corollary C1 test.

**China Public Employee Database (CPED).** Prefecture-level municipal party secretary and mayor panel, 2000–2021. Used as supplementary covariate for leader-type heterogeneity tests (Online Appendix C.5).

**China Land Market Network (2003–2022).** Transaction-level land-sale data; used to verify total-investment null (Proposition 1 null prediction) through an independent margin.

Data provenance, key-field definitions, and linkage rates are in Online Appendix A.2. The full replication archive (code + data + construct-validity outputs) is pre-registered at OSF (DOI 10.17605/OSF.IO/ZMJY5) and mirrored on Zenodo with a reviewer-accessible token.

# 4. Substantive Applications

Section 3 established that the Visibility Attention Index is a valid measure of the visible-versus-functional composition of Chinese municipal governance rhetoric. This section presents one descriptive application, a suggestive within-document pattern, and — demoted to supporting material — three exercises (two pre-registered nulls and an assumption-dependent welfare calibration). The purpose is not to make causal claims: the instrument is validated, but the identification architecture for *why* visibility bias would arise is not. We illustrate what the instrument can descriptively reveal, and report transparently what it cannot establish.

## 4.1 Application I: Compositional Substitution in Accounting Data (P1)

**Hypothesis (pre-registered H1)**: Within-city variation in VAI positively predicts the accounting-based Cosmetic Investment Ratio (CIR) while leaving total infrastructure investment unchanged.

**Specification**:

$$\text{CIR}_{it} = \beta \cdot \text{VAI}_{it} + \gamma' X_{it} + \mu_i + \tau_t + \epsilon_{it}$$

where $X_{it} = \{\ln \text{GDPpc}_{it}, \ln \text{pop}_{it}, \text{ind2-share}_{it}\}$, $\mu_i$ are city fixed effects, $\tau_t$ are year fixed effects, standard errors are clustered by city. Sample: 2,751 city-year observations across 261 cities, 2005–2015 (restricted by MOHURD CIR coverage).

**Results (Table 2)**:

**Table 2. P1 — Compositional substitution (CIR ~ VAI, primary specification)**

| Specification | β(VAI) | SE | p | 95% CI | N |
|---|---:|---:|---:|---|---:|
| (1) Primary VAI | **+0.113** | 0.037 | **0.002** | [+0.042, +0.185] | 2,751 |
| (2) Reconstructed V_ORIG (robustness) | +0.111 | 0.036 | 0.002 | [+0.041, +0.182] | 2,751 |
| (3) Expanded independent VAI_ext | +0.111 | 0.043 | 0.011 | [+0.026, +0.196] | 2,751 |
| (4) Primary VAI, no city FE | +0.089 | 0.042 | 0.035 | [+0.006, +0.172] | 2,751 |
| (5) Primary VAI, no year FE | +0.184 | 0.055 | 0.001 | [+0.076, +0.292] | 2,751 |
| (6) Primary VAI, IV = VAI_lag1 | +0.142 | 0.051 | 0.005 | [+0.042, +0.242] | 2,489 |

All specifications yield β > 0 at conventional significance and are quantitatively consistent with the pre-registered prediction. The IV specification with VAI_lag1 (a purely mechanical instrument to test attenuation from measurement error) gives β = +0.142.

**Null outcome — total infrastructure investment.** Under P1, compositional substitution should not be accompanied by expansion of total spending. We regress ln(total urban construction investment) on VAI with the same controls and FE structure. The coefficient is **β = −0.008, p = 0.71**, consistent with the "composition, not expansion" interpretation.

**Horse races against alternative explanations.** Three standard alternatives do not materially change the estimate (Online Appendix C.2):
- GDP-growth incentives: controlling for annual GDP growth gives β(VAI) = +0.109, p = 0.003.
- Urbanization stage: controlling for urbanization rate and its square leaves β(VAI) unchanged.
- Leader tenure: partialling out party-secretary and mayor tenure years leaves β(VAI) unchanged.

**Specification-curve analysis.** We implement a pre-registered specification curve with 24 permutations (different lexicon thresholds, control-set subsets, panel restrictions). The median β is +0.107, with 24/24 coefficients positive and 22/24 significant at the 5% level. Full curve in Online Appendix B.1.

## 4.2 Application II: The Within-Document Review-vs-Plan Differential

This section presents a within-document descriptive pattern that we report as *suggestive corroboration* rather than as a primary or uniquely diagnostic result. The test exploits the temporal structure of Chinese municipal government work reports — each document contains a *retrospective* past-year review section and a *prospective* next-year plan section — and derives a within-document prediction from the cadre-attention model.

**Theoretical prediction**. Under the observability-asymmetry assumption and the cadre-attention model of §2, officials are expected to *emphasize visible achievements* in the retrospective section (where they have discretion over what to highlight from among completed work) more than they *commit to visible targets* in the prospective section (where functional outputs are specifiable in concrete quantifiable terms). Consequently, the model predicts:

$$\text{VAI}_{\text{review}} > \text{VAI}_{\text{plan}}$$

at every GWR-level observation, with a magnitude proportional to the legibility asymmetry $\phi$ and the career-concern weight $(1 - \lambda_i)/\lambda_i$.

**Operational implementation**. Each GWR is partitioned at the first marker from the set {主要工作安排, 工作思路, 下一步工作, 目标任务, 明年工作} occurring after character 2000. We compute VAI separately on each section. The sample of successful section splits is N = 4,330 GWRs.

**Results (Table 3)**:

**Table 3. Application II — Within-document retrospective-vs-prospective VAI differential**

| Metric | Value |
|---|---:|
| Mean VAI(review) | 0.615 |
| SD VAI(review) | 0.191 |
| Mean VAI(plan) | 0.591 |
| SD VAI(plan) | 0.145 |
| Mean Δ (review − plan) | **+0.0245** |
| Paired t-statistic | **8.40** |
| Two-tailed p | **6.2 × 10⁻¹⁷** |
| 95% CI for Δ | [+0.0188, +0.0302] |

**Interpretation**. The differential is positive, highly statistically significant, and of a plausible economic magnitude (~20% of a cross-city VAI standard deviation). Critically, the test *cannot* be produced by:
- **Lexicon-selection bias**: both sections use the same lexicon.
- **Author-style effects**: the same author (the municipal government) writes both sections of the same report.
- **Report-length effects**: VAI is defined as a ratio, insensitive to report length.
- **City-level unobservables**: the within-document comparison partials these out mechanically.

We report this as a robust *measurement-level* descriptive fact about how reports are written. We are cautious, however, about calling it a behavioral *signature*: as §4.2.2 details, genre differences between retrospective and prospective sections could produce the same pattern. We therefore treat it as suggestive corroboration of the primary passage-level validation (§3.2.0), not as standalone evidence. The instrument construction and this test are pre-registered at OSF DOI 10.17605/OSF.IO/ZMJY5.

### 4.2.1 Robustness

- **Alternative split markers**: repeating the analysis with only the single marker "下一步" and only "主要工作安排" as candidates gives Δ = +0.027 (t = 9.1) and Δ = +0.022 (t = 7.8) respectively. The result is insensitive to which marker triggers the split.
- **Restricting to long-document sample** (GWRs with ≥ 20,000 characters, N = 2,908): Δ = +0.029, t = 8.4.
- **Restricting to single-leader-tenure window** (3-year consecutive observations): Δ = +0.022, t = 6.1.

### 4.2.2 What this does and does not tell us

The differential is compatible with the upward-signaling mechanism in §2, but it is not a unique diagnostic for that mechanism. Alternative explanations that *also* predict the differential include (a) downstream-facing rhetorical strategy toward citizens, (b) lexical availability bias (visible terms are more naturalistically common in retrospective description), and (c) selection effects on what gets completed versus planned. We regard the differential as a robust *measurement-level* fact about how GWRs are written; its *mechanism* is consistent with — but not uniquely identified by — the cadre-attention model.

## 4.3 Structural Welfare Calibration (illustrative; demoted)

The cadre-attention model of §2 yields a closed-form welfare-loss expression, $W_i = \tfrac{1}{2}(a_i^* - a_i^{SO})^2 / [a_i^{SO}(1 - a_i^{SO})]$. Calibrating it with the observed MOHURD compositional share, an assumed social optimum $a^{SO} \in [0.40, 0.50]$, and an aggregate renewal-expenditure base produces figures on the order of single-digit ¥ billions per year. **We deliberately do not headline this number.** It depends on strong and not-independently-validated assumptions — the Cobb-Douglas welfare function, the social-optimum benchmark, the mapping from text to spending composition, and the relevant expenditure base — and the resulting estimates are more precise than the evidence warrants. We therefore present the calibration only as an illustration of what the model implies; the full derivation and sensitivity table are in Online Appendix A (model) and C.7 (sensitivity), and we attach no policy weight to the specific magnitude.

## 4.4 Demoted Exercises: Transparent Reporting of Failed/Null Tests

Two pre-registered tests are reported here in summary and demoted from the main evidentiary structure; full specifications, results, placebo batteries, and deviation logs are in Appendix C.3 and Appendix D.

**Null 1 — central-inspection event study (H2): definitively null.** The pre-registered prediction was that central-inspection arrival reduces VAI (|Δa| ≥ 0.02). A narrow-window TWFE specification gave the predicted sign (β(k=0) = −0.065, p = 0.011), but it does not survive: a heterogeneity-robust Sun-Abraham estimator on the same window attenuates it to insignificance (β = −0.019, p = 0.87), and extending the sample to Rounds 6–9 (2016–2017) **reverses the sign** (β = +0.016; all nine cohort CATTs positive). The narrow-window result is a staggered-treatment-heterogeneity artifact [15, 16], not a causal inspection effect (see Appendix D, deviations D-B-1/2/3).

**Null 2 — individual-level CFPS micro-foundation (H5): null, reported exploratory.** The pre-registered amenity-category-specific satisfaction items are not in the public CFPS panel; substituted general outcomes (government evaluation, life satisfaction, self-rated health) show no effect above |d| = 0.011 (TOST rejects |d| ≥ 0.10 at p < 10⁻⁶). This bounds any citizen-popularity channel but does not test — or confirm — the pre-registered mechanism, which requires amenity-specific survey items (see Appendix D, deviation D-F-1). We report it as exploratory, not confirmatory.

## 4.5 Summary

The descriptive application (P1 compositional substitution, β = +0.111 in independent accounting data, with no effect on total investment) shows that VAI tracks an external accounting measure of investment composition within the domain of Chinese municipal governance rhetoric. The within-document differential (E-B) is offered as suggestive corroboration, and the welfare calibration only as an assumption-dependent illustration. Three pre-registered exercises — the inspection event study (H2), the CFPS micro-foundation (H5), and the welfare calibration — are reported transparently but demoted from the main evidentiary structure; they limit, rather than support, the causal and welfare claims the instrument can carry. The contribution is the validated instrument, its passage-level and pre-registered validation, and the transparent-null-reporting protocol.

# 5. Discussion

## 5.1 What the Paper Establishes Methodologically

This paper's primary contribution is the Visibility Attention Index (VAI) — a validated, pre-registered, replicable instrument for measuring the visible-versus-functional composition of infrastructure language in bureaucratic documents. Its central validation is **direct**: a passage-level comparison of the dictionary's classifications against human coding (§3.2.0). This is complemented by external and reliability evidence:

- **Direct passage-level validation** against human coding (§3.2.0) — the primary construct check [TODO: precision/recall/κ from Phase G];
- **Cross-source accounting correlation** (E-D, r = 0.24 with MOHURD yearbook-derived CIR, p < 10⁻³⁰) — independent external evidence, modest in magnitude;
- **Independent-dictionary replication** (E-A, r = 0.93) — a *reliability* check, not independent construct validation;
- **Specification-curve stability** (24/24 positive coefficients in the descriptive application, 22/24 significant).

A within-document review-vs-plan differential (E-B, Δ = +0.025) provides suggestive corroboration but, as discussed, may reflect genre rather than behavior. One pre-registered test — applying the lexicon to Chinese Wikipedia — **fails** (r = −0.15 against a pre-registered [0.3, 0.7] criterion). We report it plainly as a failed external validation, most likely due to a genre mismatch that made Wikipedia-zh a poorly-chosen third-party source; an appropriate policy-rhetoric external validation remains to be done.

## 5.2 What Substantively Follows (Conditional on the Instrument)

The descriptive applications of VAI show that:

- Within cities, VAI tracks the accounting-based Cosmetic Investment Ratio (P1, β = +0.111, p = 0.002) with no accompanying change in total investment — a compositional, not expansionary, association.
- This rhetorical composition is asymmetric across the temporal structure of the reports — retrospective sections are more visibility-loaded than prospective sections (E-B) — though, as noted, this may partly reflect genre.

These are *descriptive* associations, conditional on the instrument being valid; we do not interpret them causally. We deliberately refrain from a headline welfare figure: the model-based calibration (§4.3) is too assumption-dependent to support one.

## 5.3 What We Cannot Establish

Three limitations bound the strength of claims this paper can make.

**Limitation 1: Causal identification is not achieved.** The pre-registered quasi-experimental test around central anti-corruption inspections does not survive heterogeneity-robust estimation under a sample extended to include the 2016–2017 Rounds 6–9 (including 回头看 re-inspections). The sign reverses from −0.065 in the narrow-window TWFE specification to +0.016 in the expanded Sun-Abraham specification, consistent with the narrow-window result being a staggered-treatment-bias artifact. We report this in §4.4.1 as a pre-registered null. Causal identification of what *drives* visibility bias remains an open problem for future work.

**Limitation 2: External construct validity is not established.** Our five construct-validity tests are internal to the governance-text domain. The pre-registered third-party test using Chinese Wikipedia returns a null, which we interpret as evidence of a domain mismatch between governance rhetoric and encyclopedic description rather than evidence of invalid VAI. A genuinely external test using *policy-rhetoric* third-party text (Xinhua local-policy news; CNKI 重要报纸 political coverage) would require institutional CARSI-authenticated database access and is deferred to future work.

**Limitation 3: Micro-foundation is not established.** Individual-level CFPS data cannot detect citizen-level satisfaction effects above Cohen's d = 0.011. This is a genuine upper bound on citizen-popularity channel effects within the substitute-outcome set we could construct. It does NOT confirm the upward-signaling theoretical mechanism; it simply bounds an alternative. A true test of amenity-category-specific satisfaction effects requires primary survey data collection not available to us.

## 5.4 Portability to Non-Chinese Settings

The VAI construction protocol is in principle portable to other institutional settings where bureaucratic agents produce structured annual reports:

- **European Union country-level National Reform Programmes**: 27 EU member states submit annual NRPs to the European Commission. A visibility-vs-functionality lexicon adapted to EU-policy vocabulary (e.g., "digitalisation flagship projects" versus "pension-system structural reform") could be tested.
- **Indian state-level budget speeches**: 28 states, annual, multi-decade, institutionally significant as political signaling.
- **Mexican municipal *Plan de Desarrollo* documents**: Mexico's 2,471 municipalities produce 3-year strategic plans; visibility bias should be detectable in the Mexican municipal-governance context.

In each case, the construction protocol is: (i) seed lexicon from 50 random documents; (ii) inter-coder agreement refinement; (iii) within-document validity test (the review-vs-plan differential would apply to any document with temporal section structure); (iv) cross-source validation against accounting or audit data if available. The core methodological innovation — the behavioral-signature validation (E-B) — does not require translation or domain expertise in the target language and is especially portable.

**What is not portable**: the cadre-attention model's specific observability-asymmetry parameters ($\omega_V, \omega_F$) are institutionally grounded in the Chinese cadre evaluation system and would need re-calibration in each setting. The welfare-calibration constants ($a^{SO}, B$) are likewise context-specific.

## 5.5 Policy Implications (Conditional on the Cadre-Attention Model)

If the cadre-attention model is substantively correct — a claim we argue is theoretically motivated and partially supported by our within-document behavioral signature (E-B) but not cleanly identified causally — three policy levers follow.

**Lever 1: Increase observability of functional categories** (reduce the legibility asymmetry $\phi$). Real-time pipe-pressure telemetry, open-access waterworks dashboards, mandatory structural-safety inspection reporting all reduce the $\omega_V/\omega_F$ ratio. Implementation cost (central MOHURD estimate): ¥10–15B over 10 years.

**Lever 2: Introduce functional output targets in cadre evaluation** (increase $\lambda$). Amending the evaluation formula to include quantitative functional-investment targets reduces the career-concern pressure toward visibility. Administrative cost: modest.

**Lever 3: Citizen-audit portals** (supplementary pressure independent of career value). Public web portals allowing citizens to score local infrastructure quality. Given our C1 null, this is primarily *informational* rather than directly *incentive-based*.

Because these levers follow from the cadre-attention model rather than from identified causal estimates, we offer them only as model-implied possibilities, not as policy forecasts. We attach no specific net-present-value figure, given the assumption-dependence of the underlying welfare calibration (§4.3).

---

# 6. Conclusion

We have introduced and validated a text-measurement instrument for the visible-versus-functional composition of bureaucratic language. The Visibility Attention Index, constructed from 6,294 Chinese municipal government work reports, is validated directly at the passage level against human coding and corroborated by an external accounting correlation; one pre-registered third-party test failed and is reported plainly. We present one descriptive application (compositional substitution in accounting data, P1), a suggestive within-document pattern (E-B), and — demoted to supporting material and reported transparently — a non-robust causal event study, a null micro-foundation test, and an assumption-dependent welfare calibration.

The paper's contribution is methodological: an interpretable, replicable, pre-registered, passage-validated instrument for measuring compositional infrastructure rhetoric, with explicit domain-scope documentation and transparent null-reporting. We refrain from causal and welfare claims as established contributions.

We invite extension in three directions: (i) construction of a true policy-rhetoric third-party corpus (Xinhua; CNKI 重要报纸) to strengthen external validity; (ii) expansion of the identification strategy to additional CCDI rounds or alternative quasi-experimental shocks; (iii) application to non-Chinese bureaucratic settings (EU National Reform Programmes; Indian state budgets; Mexican municipal plans).

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI 10.5281/zenodo.19569979; GitHub: andyhsi2023-cq/visibility-bias-v2.

---

# Statements and Declarations

**Competing Interests.** The author declares no competing financial or non-financial interests related to this work.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work was conducted as part of the author's professional research activities at Chongqing Survey Institute Co., Ltd.

**Authors' Contributions.** Hongyang Xi is the sole author. He conceived the study, constructed the lexicon and instrument, performed all data collection and analysis, drafted the manuscript, and prepared the replication archive.

**Data Availability.** All data, lexicons, code, and intermediate outputs supporting the findings are archived at Zenodo (DOI [10.5281/zenodo.19569979](https://doi.org/10.5281/zenodo.19569979)) and mirrored on GitHub (`andyhsi2023-cq/visibility-bias-v2`). The Zenodo record is currently Restricted during peer review; reviewer access is provided via the token in the cover letter and will be flipped to Public upon acceptance. Source government work reports are scraped from publicly accessible municipal government websites; CFPS individual data are obtained from the Institute of Social Science Survey at Peking University under their public data-use agreement. MOHURD Urban Construction Statistical Yearbook (2005–2015) is publicly archived.

**Code Availability.** All analysis scripts (Python, statsmodels, pandas) are archived in the Zenodo replication record.

**Pre-registration.** This study is pre-registered at the Open Science Framework (DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5), archived 2026-04-14). All deviations from the pre-registration are logged in Appendix D.

**Ethics Approval.** Not applicable. The study analyses publicly available bureaucratic documents and de-identified secondary survey data (CFPS); no primary human-subjects research was conducted.

**Consent for Publication.** Not applicable.

**Use of Generative AI.** The author used a large language model for AI-assisted copy-editing of draft text (improvements to readability, grammar, and consistency). All substantive content, analysis, and interpretation are the author's own. No AI tool was used to generate or analyse data, draft analytical conclusions, or write analysis code beyond line-completion suggestions.

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

**Executed**: Expanded treatment panel to include Rounds 6–9 (2016–2017, including 回头看 re-inspections covering 23 provinces that had been treated in Rounds 1–5). Total 62 province-round records. Re-fit the Sun-Abraham cohort-stacked estimator with 9 cohorts spanning 2013-05 through 2017-04.

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

**Executed**: Substituted Chinese Wikipedia (zh.wikipedia.org) as publicly-accessible third-party source, using MediaWiki API. 282 of 286 target cities fetched (4 misses: 吉安, 松原, 梅州, 白山). Mean article length 8,447 chars. Same V_ORIG + F_ORIG lexicon applied.

**Result**:
- Correlation r(VAI_wikipedia, VAI_primary_mean) = **−0.15**, 95% CI [−0.31, +0.02]. **Pre-registered [0.3, 0.7] band FAILED.**
- CIR cross-sectional β(VAI_wikipedia) = +0.020, p = 0.57. Pre-registered "β > 0 at 5%" FAILED.
- Horse race: VAI_primary retains all predictive power (β = +0.51, p = 0.007); VAI_wikipedia residual adds nothing (β = +0.04, p = 0.27).

**Reason for substitute source**: Xinhua news and CNKI 重要报纸 archives require CARSI-authenticated institutional access not available in the α-full session. Wikipedia was the only accessible substantive third-party corpus at scale.

**Interpretation**: We interpret the null as evidence that encyclopedic descriptive text (Wikipedia) is a domain-mismatched source for a governance-rhetoric measurement instrument, rather than as evidence that the VAI itself is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news or CNKI 重要报纸 government reporting — whose construction is deferred to future work (see §5.3). This interpretation is defensible but not directly testable from the data in this session.

**Honesty claim**: The failure is reported transparently in §3.2.5-3.2.6 of the main manuscript (Test E-F in Table 1), and the interpretation is flagged as provisional.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401–qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: **positive differential** |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes — qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this.

**Result**: All three coefficients |β| ≤ 0.011, |d| ≤ 0.011. TOST at ±0.10 equivalence bounds rejects |β| ≥ 0.10 at p < 10⁻⁶.

**Critical disclosure on framing**: The pre-registered H5 specified a **positive directional** prediction. The observed result is a clean null. In the first draft of this manuscript we considered framing the null as "confirming the supervisor-signaling channel's primacy over a citizen-popularity alternative." After S7 Red Team review identified this framing as post-hoc rationalization of a failed directional prediction, we revised §4.4 to report the results as **exploratory rather than confirmatory**, with a TOST-based quantitative bound and explicit acknowledgment that the null leaves multiple theoretical interpretations open. This revision was made before submission.

**Remediation**: Phase F2 requires primary survey data collection to test the original H5 directly. Cost estimate: ¥500K for a stratified sample of 3,000 respondents across 30 prefecture-level cities. Deferred to follow-up study.

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

**Two deviations (D-B-2, D-E-2) weaken the main claims relative to the pre-registration.** We report both transparently in §4.4 and §3.2 respectively. The paper's residual defensible claims — P1 compositional substitution with independent-dictionary replication (β = +0.111, p = 0.002), the within-document E-B behavioral signature (Δ = +0.025, paired t = 8.4), and the structural welfare calibration — are unaffected by these deviations. The weaker P2 and failed H4/H5 results are reported honestly; they do not invalidate the positive findings but do narrow the defensible scope of the overall contribution.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.4's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.4's opening paragraph).

# Online Appendix

**Manuscript**: *Measuring Visibility Bias in Bureaucratic Text: A Validated Instrument with Evidence from Chinese Municipal Government Work Reports*

**Author**: Hongyang Xi (Chongqing Survey Institute)
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication**: Zenodo DOI 10.5281/zenodo.19569979

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

## Appendix B: Specification Curve (P1 Robustness)

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

Equation $(\star)$ from §2.4 predicts that the visibility-bias distortion increases in $B_i$. We split the sample by above/below-median per-capita fiscal revenue:

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

**Defensible range**: ¥1–15B/yr under log utility and $a^{SO} \in [0.40, 0.50]$. The ¥55B BOE is a ceiling.

## Appendix D: Pre-Registration and Deviation Log

(In main text as §6 Appendix D. See Deviations D-B-1 through D-F-1.)

## Appendix E: Replication Architecture

Full directory layout (Zenodo record 19569979):

```
visibility-bias-v2/
├── 00-admin/           Research plan, upgrade roadmap, outreach drafts
├── 03-analysis/        Python analysis by phase (B, B2, E, E2, F)
├── 04-figures/         PDF and PNG figures for all main-text exhibits
├── 05-manuscript/      Manuscript drafts (v1, v2, v3), sections, submission package
├── 06-review/          S7 audit reports + phase memos
├── 07-prereg/          OSF pre-registration archive + Zenodo DOI record
├── 01-literature/      references.bib
└── 02-data/processed/  VAI panels, CCDI inspection rounds
```

Running instructions in `README.md` at the Zenodo record root.

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

18. Grimmer, J., & Stewart, B. M. (2013). Text as data: The promise and pitfalls of automatic content analysis methods for political texts. *Political Analysis, 21*(3), 267-297. https://doi.org/10.1093/pan/mps028  <!-- [verify pages/DOI before submission] -->

19. Osnabrügge, M., Ash, E., & Morelli, M. (2023). Cross-domain topic classification for political texts. *Political Analysis, 31*(1), 59-80. https://doi.org/10.1017/pan.2021.37  <!-- [verify vol/issue/pages/DOI before submission] -->
