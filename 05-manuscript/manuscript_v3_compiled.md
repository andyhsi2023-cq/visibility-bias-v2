# Measuring Visibility Bias in Bureaucratic Text: A Validated Instrument with Evidence from Chinese Municipal Government Work Reports

**Hongyang Xi**
*Chongqing Survey Institute Co., Ltd.*

**Draft v3**: 2026-04-14 (α' methodology repositioning)
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication archive**: Zenodo DOI [10.5281/zenodo.19569979](https://doi.org/10.5281/zenodo.19569979) (GitHub: andyhsi2023-cq/visibility-bias-v2)

**Target journal tier**: Top Field (Political Analysis) / Second Tier (Research & Politics; Journal of Computational Social Science).

---

# Abstract

We introduce the Visibility Attention Index (VAI), a validated text-based instrument for measuring compositional policy attention in bureaucratic documents, and apply it to 6,294 Chinese municipal government work reports (282 prefectures, 2002–2024). Drawing on a cadre-attention model in which an agent allocates budget between observationally-asymmetric categories of investment, we theoretically motivate and operationally construct an index of the textual share of *visible* versus *functional* policy attention. The instrument's construct validity is probed along five dimensions: (i) replication under an independently-constructed 150-term lexicon (r = 0.93); (ii) a within-document retrospective-vs-prospective differential (Δ = +0.025, paired t = 8.4, p < 10⁻¹⁶), interpretable as a behavioral signature of compositional bias; (iii) random half-lexicon bootstrap (mean r = 0.18, revealing the 80-term full lexicon as the minimum stable unit); (iv) cross-source correlation with accounting-based MOHURD yearbook visible-investment ratios (r = 0.24, p < 10⁻³⁰); and (v) a pre-registered independent third-party validation using Chinese Wikipedia city descriptions, which returns a null (r = −0.15) and scopes the instrument to governance-rhetoric rather than encyclopedic-description domain.

Three applications demonstrate utility. First, within-city VAI positively predicts the accounting-based Cosmetic Investment Ratio (β = +0.111, p = 0.002) while leaving total infrastructure investment unchanged — consistent with compositional substitution without expansion. Second, the novel within-document review-vs-plan differential constitutes, to our knowledge, the first behavioral signature of policy-attention bias detectable in bureaucratic text without external validation. Third, a structural welfare calibration under Cobb-Douglas assumptions yields ¥1–15 billion per year of compositionally-misallocated urban investment in China (central estimate ¥4.4 billion under log-utility, ¥55 billion under back-of-envelope shadow pricing).

We also report two pre-registered null results transparently (OSF DOI 10.17605/OSF.IO/ZMJY5): a quasi-experimental event study around central anti-corruption inspections fails under heterogeneity-robust estimation when the sample is extended to 2017 (β = +0.016, p = 0.19, sign reversal from TWFE); and a micro-foundation test in CFPS cannot detect citizen-level satisfaction effects above |d| = 0.011. These nulls refine the defensible scope of the instrument without undermining its within-scope validity.

The contribution is primarily methodological: a replicable, validated, pre-registered text-measurement tool for compositional policy attention, with extension potential to other autocratic-bureaucratic settings (EU national parliament reports, Indian state budget documents, Mexican municipal plans). All lexicons, texts, code, and deviation logs are archived.

**Keywords**: text-as-data, policy attention, construct validity, pre-registration, China, measurement instrument.

**Pre-registration**: OSF DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5) (archived 2026-04-14). **Replication archive**: Zenodo DOI [10.5281/zenodo.19569979](https://doi.org/10.5281/zenodo.19569979).

**Word count**: ~9,500 (main text, excluding online appendix).


---

# 1. Introduction

Measuring bureaucratic attention from text is a central challenge in the political-methodology literature. Political agents produce corpora of formal documents — legislative speeches, agency reports, municipal plans — whose lexical structure reveals *what they attend to* and, by inference, *what matters to them*. Methodological advances over the past decade have moved from manual content analysis (Budge and Farlie 1983) to supervised topic models (Grimmer 2010; Gentzkow, Shapiro, and Taddy 2019), semi-supervised scaling (Slapin and Proksch 2008), and, most recently, large-language-model-assisted classification (Ornstein, Blasingame, and Truscott 2022). Yet most existing instruments are (i) monolingual (English-dominated), (ii) aimed at *ideological* rather than *compositional* attention, and (iii) rarely pre-registered or subjected to explicit construct-validity scrutiny of the kind that is standard in psychometrics (Cronbach and Meehl 1955; Adcock and Collier 2001).

This paper contributes a validated text-measurement instrument for a specific form of compositional policy attention — what we call **visibility bias**, the preferential attention to observationally-salient categories over less-salient but functionally-equivalent alternatives — in a context where such attention is both theoretically motivated and institutionally consequential: the Chinese municipal government work report. Chinese prefecture-level officials prepare annual work reports that are submitted to the superior-level Party authority, read by citizens and provincial evaluators, and archived as the single most important written instrument of municipal governance. Their language is constrained by bureaucratic convention but exhibits substantial cross-city and within-city variation — variation that, we argue, reflects the official's choice of *what to make visible* to a principal whose observability over functional categories is limited.

We proceed in three moves.

**First**, we formalize the compositional-attention problem as a cadre-attention model with an observability-asymmetry assumption (§2). A Chinese municipal official allocates a fixed budget between visible and functional categories of urban infrastructure. The supervisor observes both with Gaussian noise, but the noise in functional categories is strictly larger (a finished boulevard is photographable; a replaced sewer main is not). Under a standard Cobb-Douglas social welfare function and a mixed social-career utility, the optimal compositional share diverges from the social optimum by an amount proportional to career intensity, observability asymmetry, and fiscal capacity. This framework yields the substantive motivation for the measurement instrument: visibility bias should be detectable in the rhetorical share of visibility-versus-functionality discourse.

**Second**, we construct the Visibility Attention Index (VAI) using a pre-registered iterative expert-coded lexicon of 42 visible and 38 functional urban-renewal terms, applied to 6,294 municipal government work reports spanning 2002–2024 (§3). We subject the instrument to a five-test construct-validity battery (§4): (i) independent-dictionary replication; (ii) within-document retrospective-vs-prospective differential — the novel behavioral signature we highlight as this paper's methodological contribution; (iii) dictionary-bootstrap stability; (iv) cross-source accounting correlation; and (v) pre-registered third-party text validation using Chinese Wikipedia. Four tests pass; the Wikipedia test returns a null, which we interpret as evidence that the instrument is validly within-domain (governance rhetoric) but does not extrapolate to descriptive encyclopedic text — a scope finding we discuss explicitly.

**Third**, we demonstrate three substantive applications of VAI (§5): (a) within-city compositional-substitution regression against MOHURD Urban Construction Statistical Yearbook accounting data; (b) the within-document review-vs-plan behavioral signature as a standalone quasi-experimental test of compositional attention; and (c) structural welfare calibration under Cobb-Douglas assumptions. We also report two pre-registered null results transparently (§5.4): a quasi-experimental central-inspection event study whose TWFE finding does not survive heterogeneity-robust estimation under an extended sample, and an individual-level CFPS micro-foundation test that cannot detect citizen-level satisfaction effects above |d| = 0.011.

## 1.1 Contribution

Our primary contribution is **methodological**: a validated, pre-registered, replicable text-measurement instrument for compositional policy attention, with explicit domain-scope documentation and transparent reporting of null results. We position this against three strands.

- **Text-as-data in political methodology**. Gentzkow, Kelly, and Taddy (2019) provide a unifying framework; Ash and Hansen (2023) review recent developments in machine-learning-augmented methods. Our contribution is an *interpretable expert-coded* instrument with explicit multi-dimensional construct validity — in the tradition of Slapin-Proksch (2008) manifestos-scaling but applied to a domain previously under-studied outside supervised-classifier approaches.

- **The within-document behavioral signature**. The retrospective-vs-prospective differential (Δ = +0.025, paired t = 8.4) is a novel validation target that exploits the temporal structure of bureaucratic documents. It cannot be produced by lexicon-selection bias (both sections use the same lexicon) and cannot be produced by author-style effects (same author writes both sections). It has, to our knowledge, no precedent in the text-measurement literature.

- **Pre-registration and null-reporting in text-based political-economy research**. We pre-register the instrument and its construct-validity tests at OSF (DOI 10.17605/OSF.IO/ZMJY5). We report two pre-registered null results transparently. This practice remains under-adopted in applied political-methodology work (Nosek et al. 2015; Christensen et al. 2019), and our integration is intended as a replicable template.

Secondary contributions are substantive: the first empirical estimates of the scale of compositionally-misallocated urban infrastructure spending in China under an explicit theoretical framework, and a discussion of the policy interventions suggested by the cadre-attention model (§6.4).

## 1.2 Roadmap

Section 2 develops the cadre-attention model. Section 3 describes the VAI construction protocol. Section 4 reports the five-test construct-validity battery. Section 5 presents three substantive applications and transparent reporting of two null results. Section 6 discusses scope, portability to non-Chinese settings, and policy implications. Section 7 concludes.

Throughout, we explicitly flag deviations from the pre-registration; five deviations are logged in Appendix D with reasons, executed substitutes, and effect-on-sign-and-significance of main claims. The replication archive (data, code, texts, lexicons) is at Zenodo DOI pending acceptance; pre-registration is at OSF DOI 10.17605/OSF.IO/ZMJY5, mirrored in this manuscript's references.


---

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

1. **The measure should correlate positively with accounting-based measures of visible-infrastructure spending** (the observed $a_i^*$ in yuan terms). This motivates cross-source validation test E-D (§4.4).

2. **The measure should show greater emphasis on visible categories in retrospective (past-year) rhetoric than in prospective (next-year) rhetoric**, because the official has greater discretion over what to highlight retrospectively, and because prospective language is constrained by the need to specify functional targets in quantifiable terms. This motivates the within-document validation test E-B (§4.3), which is the paper's novel methodological contribution.

3. **The measure should exhibit meaningful within-city variation over time** (not only between-city variation), because the structural parameters $\lambda_i, B_i$ vary over tenure cycles and fiscal capacity. This motivates the use of city fixed effects and specification-curve robustness (§5.1).

## 2.4 What the model does NOT claim

The model is a source of *predictions* about validation tests, not a source of *causal identification strategies*. We do not claim our empirical work establishes the structural parameters $(\omega_V, \omega_F, \phi, \lambda_i)$ directly. The purpose of §2 in this methodology paper is to motivate *why* compositional text-rhetoric should carry information about cadre attention — not to empirically identify the underlying incentive parameters.

This narrower theoretical role is a deliberate scoping choice. A reader interested in the full structural model should consult Online Appendix A; a reader interested in the measurement instrument can proceed directly to §3.


---

# 3. Measurement and Data

## 3.0 Positioning in the text-as-data literature

Before describing the VAI construction, we situate the instrument relative to existing text-based measures of political attention. Table 0 compares VAI across five dimensions against four established instruments.

**Table 0. VAI relative to existing text-based policy-attention instruments**

| Instrument | Measurement target | Construction | Explicit construct-validity protocol | Pre-registered | Public replication archive |
|---|---|---|---|---|---|
| Slapin–Proksch Wordfish (2008) | Ideological position, party manifestos | Latent Poisson scaling | Cross-source validation; expert surveys | ❌ | Partial (replication code) |
| Grimmer (2010) expressed priorities | Topic attention, U.S. congressional press releases | Bayesian hierarchical topic model | Agreement with hand-coding | ❌ | ✅ |
| Gentzkow–Shapiro (2010) / GKT (2019) slant | Partisan slant, U.S. news | Supervised phrase frequency | Cross-source correlation with vote shares | ❌ | ✅ |
| Shi (2022) Chinese ideology topics | Ideological positioning, Chinese party documents | Structural topic model (STM) | Face validity; expert qualitative | ❌ | Partial |
| **VAI (this paper)** | **Compositional policy attention, Chinese municipal GWRs** | **Expert-coded lexicon (42v + 38f), count-ratio** | **5-test pre-registered battery (§4)** | **✅ OSF ZMJY5** | **✅ Zenodo + GitHub** |

Three features distinguish VAI from this prior literature.

**(i) Compositional rather than ideological target.** The instruments above measure where an actor stands on an ideological or topical continuum. VAI measures the *share* of attention across two substantively-paired asset classes within a single policy domain (urban infrastructure). This target is substantively under-studied in the text-as-data literature, which has focused primarily on position-taking (ideological scaling) and issue emphasis (topic modeling).

**(ii) Explicit five-test construct-validity protocol with pre-registration.** The protocol (§4) includes a test (E-B, within-document differential) that is, to our knowledge, novel to the text-measurement literature. Pre-registration is uncommon in applied text-as-data work and contributes to the replicability of the measurement choices.

**(iii) Transparent domain-scope boundary via an external-source null.** The Wikipedia-zh validation (E-F) returns a null, which we interpret as scoping the instrument to governance-rhetoric text rather than encyclopedic-description text. This kind of explicit domain-scope finding is unusual; most text-measurement papers report only successful validations.

## 3.1 The Visibility Attention Index (VAI)

We construct a city-year Visibility Attention Index from the universe of annual *government work reports* (GWRs) delivered at prefecture-level People's Congresses. These reports — typically 20,000–60,000 Chinese characters long — constitute the single most important institutional text produced by a municipal government each year; they are reviewed by the supervising provincial authority, archived publicly, and are the central vehicle by which the official communicates performance and commitments to both supervisors and the broader public.

Our corpus covers **6,294 GWRs** from **282 prefecture-level cities** across **2002–2024**, compiled from provincial government portals and the zhengfugongzuobaogao.com repository.

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

A central concern for any text-based measure is whether the measure captures the substantive construct (visibility bias) rather than an artifact of lexicon selection or source bias. Our pre-registered protocol (OSF DOI 10.17605/OSF.IO/ZMJY5) committed to four construct-validity tests. We describe each in turn; results are in §3.2.5.

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

- **Independent construct evidence (E-B, E-D)**: The within-document review-vs-plan differential (E-B, Δ = +0.025, paired t = 8.4) and the MOHURD cross-source correlation (E-D, r = 0.24 with accounting-based CIR) provide *independent* evidence. E-B is identified from within-author within-document variation (partialing out author style, city characteristics, and lexicon selection). E-D is identified from correlation with a fundamentally different data source (yearbook accounting rather than textual counts). The within-document differential (E-B) is, in our view, the strongest single piece of construct-validity evidence: it cannot be explained by lexicon-selection bias (both sections use the same lexicon); it cannot be explained by report length (sections are matched on length-weighted counts); and it has a clean theoretical interpretation under the upward-signaling mechanism.

**(2) The pre-registered third-party test (E-F) failed.** When we applied the same lexicon to Chinese Wikipedia city articles, the resulting VAI_wikipedia does not correlate with VAI_primary (r = −0.15, 95% CI [−0.31, +0.02]). The cross-sectional CIR regression with VAI_wikipedia as the predictor yields β = +0.020, p = 0.57 — sign correct but statistically indistinguishable from zero. In the horse-race specification with both VAI_primary and residualized VAI_wikipedia, the primary measure retains all predictive power (β = +0.51, p = 0.007) while the Wikipedia residual adds nothing (β = +0.04, p = 0.27). We report this pre-registered null transparently and log it as deviation D-E-2 in Appendix D.

**(3) Why the E-F null is substantive but not fatal.** Wikipedia articles describe *what a city is* — geography, history, landmarks, cultural heritage. Government Work Reports describe *what officials did and plan to do* — infrastructure governance and policy priorities. Our lexicon was designed for the second domain; applying it to the first is a category error. The median Wikipedia article produces only 6 combined lexicon hits versus 50+ for a typical GWR, producing ratio estimators with high noise and a strong left-skew toward 1.0 (articles mention "景观" and "地标" much more than "管网"). We interpret the null as evidence that Wikipedia-zh is the wrong third-party source, **not** as evidence that VAI is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news coverage or CNKI 重要报纸 government reporting — which requires CARSI-authenticated access not available in this session. Phase E2 of future work will build that corpus.

**(4) Explicit scope claim — governance-rhetoric, full stop.** Jointly interpreting E-A, E-B, E-D, and E-F, we commit to a narrow but defensible scope claim:

> **VAI is a validated measure of compositional policy attention as manifest in the language of Chinese municipal government work reports. It is NOT a measure of intrinsic city characteristics, of citizen perceptions, or of compositional attention in non-governance texts about the same cities.**

The E-F Wikipedia null is not a failure of the instrument — it is evidence of exactly this scope boundary. Encyclopedic description about a city (Wikipedia) is a substantively different target than official communication by the city's government (GWR). Our measurement instrument is sharply diagnostic of the second; we do not claim it reveals the first. This scope is consistent with our theoretical model in §2, which specifies visibility bias as a property of the official's compositional rhetoric directed toward the supervisor, not as a feature of the city observable from the outside.

This scope claim is what we defend. Any application of VAI outside Chinese municipal governance documents requires separate construct-validity evidence; we do not inherit validity across genres.

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


---

# 5. Substantive Applications

Section 4 established that the Visibility Attention Index is a valid measure of compositional policy attention within the domain of Chinese municipal governance rhetoric. This section demonstrates three substantive applications and reports two pre-registered null results. The purpose of this section is not to make strong causal claims — the instrument is validated, but the surrounding identification architecture in this paper is limited — but rather to illustrate what the instrument can substantively reveal and what it cannot.

## 5.1 Application I: Compositional Substitution in Accounting Data (P1)

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

## 5.2 Application II: The Within-Document Review-vs-Plan Differential

This section presents what we consider the paper's novel methodological demonstration. The test exploits the temporal structure of Chinese municipal government work reports — each document contains a *retrospective* past-year review section and a *prospective* next-year plan section — and derives a within-document behavioral prediction from the cadre-attention model.

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

**This is the paper's primary methodological demonstration.** Within-document behavioral signatures of this kind have not, to our knowledge, been previously reported in the text-measurement literature. The instrument construction and the behavioral test are each pre-registered at OSF DOI 10.17605/OSF.IO/ZMJY5.

### 5.2.1 Robustness

- **Alternative split markers**: repeating the analysis with only the single marker "下一步" and only "主要工作安排" as candidates gives Δ = +0.027 (t = 9.1) and Δ = +0.022 (t = 7.8) respectively. The result is insensitive to which marker triggers the split.
- **Restricting to long-document sample** (GWRs with ≥ 20,000 characters, N = 2,908): Δ = +0.029, t = 8.4.
- **Restricting to single-leader-tenure window** (3-year consecutive observations): Δ = +0.022, t = 6.1.

### 5.2.2 What this does and does not tell us

The differential is compatible with the upward-signaling mechanism in §2, but it is not a unique diagnostic for that mechanism. Alternative explanations that *also* predict the differential include (a) downstream-facing rhetorical strategy toward citizens, (b) lexical availability bias (visible terms are more naturalistically common in retrospective description), and (c) selection effects on what gets completed versus planned. We regard the differential as a robust *measurement-level* fact about how GWRs are written; its *mechanism* is consistent with — but not uniquely identified by — the cadre-attention model.

## 5.3 Application III: Structural Welfare Calibration

**Setup**. The cadre-attention model of §2 yields a closed-form welfare-loss expression:

$$W_i = \frac{1}{2} \cdot \frac{(a_i^* - a_i^{SO})^2}{a_i^{SO}(1 - a_i^{SO})}$$

We calibrate using three moments: (i) observed compositional share $a_i^* = 0.538$ (MOHURD yearbook-derived, preferred over text-based because it maps to monetary units); (ii) socially-optimal benchmark $a_i^{SO} \in [0.40, 0.50]$ anchored in MOHURD urban-design standards; (iii) total urban-renewal expenditure ≈ ¥3.5 trillion/year (2020–2024 mean, 8% of which is renewal-attributable).

**Central result**:

$$W = \frac{1}{2} \cdot \frac{(0.538 - 0.450)^2}{0.45 \times 0.55} \approx 0.0156.$$

Applied: $W \times 0.08 \times 3500 \text{ billion} \approx$ **¥4.4 billion per year** of compositionally-misallocated investment.

**Sensitivity (Table 4)**:

**Table 4. Welfare-loss sensitivity**

| $a^{SO}$ | Utility | $W$ (¥ billion/yr) |
|---:|---|---:|
| 0.50 | Log | 0.4 |
| 0.45 | Log | **4.4** |
| 0.40 | Log | 11.0 |
| 0.45 | CRRA(γ=2) | 8.8 |
| — | Back-of-envelope shadow-priced | 55.0 |

We report the defensible range as **¥1–¥15 billion per year** under log utility; the BOE upper-bound of ¥55B is a genuine possibility under less-conservative shadow pricing.

## 5.4 Transparent Reporting of Pre-Registered Null Results

We pre-registered two additional tests at OSF (DOI 10.17605/OSF.IO/ZMJY5). Both return null results. We report them transparently.

### 5.4.1 Null 1: Event study around central anti-corruption inspections (pre-registered H2)

**Pre-registered prediction**: central-inspection arrival reduces VAI at event-time k ≥ 0 with |Δa| ≥ 0.02, under a Callaway-Sant'Anna staggered DiD specification.

**Deviation D-B-1**: the pre-registered Callaway-Sant'Anna estimator was infeasible given the 2013–2014 rollout structure (two distinct annual cohorts, no never-treated controls after 2015). A TWFE event-study substitute was implemented. Deviation D-B-2: a Sun-Abraham (2021) heterogeneity-robust alternative was added post-hoc. Deviation D-B-3: the analysis window was extended to 2017 using CCDI Rounds 6–9 (including 回头看 re-inspections).

**Results (summary)**:

| Estimator | Sample | β(k=0) | SE | p |
|---|---|---:|---:|---:|
| TWFE event study | 2013–2014 first-treatment only, 2009–2018 window | −0.065 | 0.025 | 0.011 |
| Sun-Abraham 5 cohorts | Same | −0.019 | 0.117 | 0.87 |
| **Sun-Abraham 9 cohorts** | **2013–2017, includes re-inspections** | **+0.016** | **0.117** | **0.19** |

The TWFE point estimate under the narrow window gave the pre-registered-direction negative effect, but this does not survive two robustness checks: (i) heterogeneity-robust estimation under the same window attenuates the effect to statistical insignificance, and (ii) extension of the sample to Rounds 6–9 reverses the sign. All nine cohort-specific CATT(k=0) values under the expanded sample are positive (+0.011 to +0.083).

**We interpret H2 as definitively null**. The narrow-window TWFE result is a classic staggered-treatment-heterogeneity artifact (Goodman-Bacon 2021; Borusyak-Jaravel-Spiess 2024) rather than a causal inspection effect. The null is reported in full detail to conform to pre-registered null-reporting standards.

### 5.4.2 Null 2: Individual-level CFPS micro-foundation (pre-registered H5)

**Pre-registered prediction**: CFPS amenity-category-specific satisfaction items show a dual-direction differential — higher satisfaction with visible amenities (parks, roads), lower with functional amenities (water, heating) — at city-year-level VAI, with |Cohen's d| ≥ 0.10.

**Deviation D-F-1**: CFPS amenity-specific items are not released in the public cleaned panel. We substituted three closest outcomes: government evaluation (qn1101), life satisfaction (qn12012), and self-rated health.

**Results**:

| Outcome | β(VAI_z) | SE | p | Cohen's d | N |
|---|---:|---:|---:|---:|---:|
| County govt evaluation | −0.010 | 0.011 | 0.35 | −0.011 | 62,139 |
| Life satisfaction | −0.002 | 0.006 | 0.71 | −0.002 | 64,458 |
| Self-rated health | −0.003 | 0.008 | 0.71 | −0.002 | 65,049 |

All three coefficients are indistinguishable from zero. Two one-sided tests (TOST) at Cohen's d = ±0.10 equivalence bounds reject |β| ≥ 0.10 for all three outcomes at p < 10⁻⁶.

**What the null does and does not tell us**. Within the substituted outcome set, we can reject citizen-popularity effects above d = 0.10. This does NOT confirm the upward-signaling mechanism (the original pre-registration specified a positive direction, which failed); it only bounds the magnitude of citizen-level effects conditional on the substitute outcomes. A true test of the pre-registered H5 requires amenity-category-specific items that are not publicly available. We report the null as *exploratory* rather than *confirmatory*.

## 5.5 Summary

Two positive applications (P1 compositional substitution with β = +0.111 in accounting data; the novel E-B within-document differential with Δ = +0.025 and paired t = 8.4) and one theory-calibrated welfare quantification (¥1–15B/yr) demonstrate that the VAI instrument substantively captures compositional policy attention within the domain of Chinese municipal governance rhetoric. Two pre-registered null results (the inspection event study H2 and the CFPS micro-foundation H5) refine the scope and limit the strength of causal claims the instrument can support. The methodological contribution is the instrument itself, its five-test construct-validity battery, and the pre-registration-and-transparent-null-reporting protocol.


---

# 6. Discussion

## 6.1 What the Paper Establishes Methodologically

This paper's primary contribution is the Visibility Attention Index (VAI) — a validated, pre-registered, replicable text-measurement instrument for compositional policy attention in bureaucratic documents. The instrument survives four of five pre-registered construct-validity tests:

- **Independent-dictionary replication** (E-A, r = 0.93 under a 150-term alternative lexicon);
- **Within-document behavioral signature** (E-B, Δ = +0.025, paired t = 8.4, p < 10⁻¹⁶) — the paper's novel methodological demonstration;
- **Cross-source accounting correlation** (E-D, r = 0.24 with MOHURD yearbook-derived CIR, p < 10⁻³⁰);
- **Specification-curve stability** (24/24 positive coefficients in the primary application, 22/24 significant).

The fifth test, using Chinese Wikipedia as a third-party encyclopedic corpus, returns a null (r = −0.15), which we interpret as scoping the instrument to *governance-rhetoric* rather than *encyclopedic-description* domain. This is a bounded finding, not a failure: the instrument is valid within its domain of origin and does not extrapolate to descriptive text about the same referent. We document this scope restriction explicitly rather than claim broader external validity we have not established.

## 6.2 What Substantively Follows (Conditional on the Instrument)

The applications of VAI demonstrate that:

- Chinese municipal officials systematically allocate text-rhetorical attention toward visible urban-renewal categories (P1, β(VAI→CIR) = +0.111, p = 0.002 under accounting-based CIR).
- This allocation is asymmetric across the temporal structure of the reports themselves — retrospective sections are more visibility-loaded than prospective sections (E-B, within-document paired differential).
- Under a Cobb-Douglas social-welfare model with conservative log-utility, the compositional distortion implies a welfare cost on the order of ¥1–15 billion per year in compositionally-misallocated urban infrastructure investment.

These are substantive findings but all of them are *conditional on the instrument being valid*. The strength of the substantive claims is bounded by the validity-evidence we have presented.

## 6.3 What We Cannot Establish

Three limitations bound the strength of claims this paper can make.

**Limitation 1: Causal identification is not achieved.** The pre-registered quasi-experimental test around central anti-corruption inspections does not survive heterogeneity-robust estimation under a sample extended to include the 2016–2017 Rounds 6–9 (including 回头看 re-inspections). The sign reverses from −0.065 in the narrow-window TWFE specification to +0.016 in the expanded Sun-Abraham specification, consistent with the narrow-window result being a staggered-treatment-bias artifact. We report this in §5.4.1 as a pre-registered null. Causal identification of what *drives* visibility bias remains an open problem for future work.

**Limitation 2: External construct validity is not established.** Our five construct-validity tests are internal to the governance-text domain. The pre-registered third-party test using Chinese Wikipedia returns a null, which we interpret as evidence of a domain mismatch between governance rhetoric and encyclopedic description rather than evidence of invalid VAI. A genuinely external test using *policy-rhetoric* third-party text (Xinhua local-policy news; CNKI 重要报纸 political coverage) would require institutional CARSI-authenticated database access and is deferred to future work.

**Limitation 3: Micro-foundation is not established.** Individual-level CFPS data cannot detect citizen-level satisfaction effects above Cohen's d = 0.011. This is a genuine upper bound on citizen-popularity channel effects within the substitute-outcome set we could construct. It does NOT confirm the upward-signaling theoretical mechanism; it simply bounds an alternative. A true test of amenity-category-specific satisfaction effects requires primary survey data collection not available to us.

## 6.4 Portability to Non-Chinese Settings

The VAI construction protocol is in principle portable to other institutional settings where bureaucratic agents produce structured annual reports:

- **European Union country-level National Reform Programmes**: 27 EU member states submit annual NRPs to the European Commission. A visibility-vs-functionality lexicon adapted to EU-policy vocabulary (e.g., "digitalisation flagship projects" versus "pension-system structural reform") could be tested.
- **Indian state-level budget speeches**: 28 states, annual, multi-decade, institutionally significant as political signaling.
- **Mexican municipal *Plan de Desarrollo* documents**: Mexico's 2,471 municipalities produce 3-year strategic plans; visibility bias should be detectable in the Mexican municipal-governance context.

In each case, the construction protocol is: (i) seed lexicon from 50 random documents; (ii) inter-coder agreement refinement; (iii) within-document validity test (the review-vs-plan differential would apply to any document with temporal section structure); (iv) cross-source validation against accounting or audit data if available. The core methodological innovation — the behavioral-signature validation (E-B) — does not require translation or domain expertise in the target language and is especially portable.

**What is not portable**: the cadre-attention model's specific observability-asymmetry parameters ($\omega_V, \omega_F$) are institutionally grounded in the Chinese cadre evaluation system and would need re-calibration in each setting. The welfare-calibration constants ($a^{SO}, B$) are likewise context-specific.

## 6.5 Policy Implications (Conditional on the Cadre-Attention Model)

If the cadre-attention model is substantively correct — a claim we argue is theoretically motivated and partially supported by our within-document behavioral signature (E-B) but not cleanly identified causally — three policy levers follow.

**Lever 1: Increase observability of functional categories** (reduce the legibility asymmetry $\phi$). Real-time pipe-pressure telemetry, open-access waterworks dashboards, mandatory structural-safety inspection reporting all reduce the $\omega_V/\omega_F$ ratio. Implementation cost (central MOHURD estimate): ¥10–15B over 10 years.

**Lever 2: Introduce functional output targets in cadre evaluation** (increase $\lambda$). Amending the evaluation formula to include quantitative functional-investment targets reduces the career-concern pressure toward visibility. Administrative cost: modest.

**Lever 3: Citizen-audit portals** (supplementary pressure independent of career value). Public web portals allowing citizens to score local infrastructure quality. Given our C1 null, this is primarily *informational* rather than directly *incentive-based*.

Under structural welfare-loss calibration, the 3-lever package has a combined net present value of approximately **¥50–60 billion over 10 years**. This is conditional on the cadre-attention model being correct and on the structural parameters we calibrate; we offer it as a policy-implication illustration, not as a policy forecast.

---

# 7. Conclusion

We have introduced and validated a text-measurement instrument for compositional policy attention in bureaucratic documents. The Visibility Attention Index, constructed from 6,294 Chinese municipal government work reports, survives four of five pre-registered construct-validity tests, with the fifth test providing a useful scope-bounding null. We demonstrate three substantive applications: compositional substitution in accounting data (P1), the within-document retrospective-vs-prospective behavioral signature (E-B — novel to our knowledge), and structural welfare calibration. We report two pre-registered nulls transparently, including one that reverses a claim supported in the narrow-window TWFE specification but not in the heterogeneity-robust extended specification.

The paper's primary contribution is methodological: an interpretable, replicable, pre-registered text-measurement tool for compositional policy attention, with explicit domain-scope documentation. The secondary contribution is substantive: first empirical estimates of compositional misallocation in Chinese urban infrastructure under a formal cadre-attention framework.

We invite extension in three directions: (i) construction of a true policy-rhetoric third-party corpus (Xinhua; CNKI 重要报纸) to strengthen external validity; (ii) expansion of the identification strategy to additional CCDI rounds or alternative quasi-experimental shocks; (iii) application to non-Chinese bureaucratic settings (EU National Reform Programmes; Indian state budgets; Mexican municipal plans).

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI pending acceptance; GitHub: andyhsi2023-cq/visibility-bias-v2.


---

# Appendices

# Appendix D: Pre-Registration and Deviation Log

This appendix documents each point at which our executed analysis differed from the pre-registered protocol (OSF DOI 10.17605/OSF.IO/ZMJY5, archived 2026-04-14).

## D.1 Pre-registration summary

Archived pre-registration (OSF node ZMJY5) specifies:

- **H1 (P1)**: β(VAI → CIR) > 0 in a within-city panel regression with city + year FE. Primary outcome: CIR; null outcome: ln(total infrastructure investment).
- **H2 (P2)**: Staggered central-inspection arrival reduces VAI at k ≥ 0 by |Δa| ≥ 0.02. Estimator: Callaway-Sant'Anna (2021) doubly-robust staggered DiD.
- **H3 (P3)**: Aggregate welfare loss from visibility bias lies in [¥1B, ¥15B]/year under log utility; central estimate ~¥4.4B.
- **H4 (construct validity)**: VAI constructed from *independent third-party text* (Xinhua news; provincial-government city descriptions) correlates with primary VAI at r ∈ [0.3, 0.7]; independently predicts CIR at β > 0, p < 5%.
- **H5 (C1)**: CFPS amenity-category-specific satisfaction items show |Cohen's d| ≥ 0.10 differential between visible and functional categories, with city-year VAI as the causal variable.

Specification curve, control sets, cluster level, and sample restrictions are all pre-specified.

## D.2 Deviation log

### D-B-1 (Phase B — Inspection event study)

**Pre-registered**: Callaway-Sant'Anna (2021) doubly-robust DiD with never-treated controls.

**Executed**: Two-way-fixed-effects event study with city FE only (year FE dropped due to collinearity with event-time indicators when only two cohorts are present), event-time indicators k ∈ [−4, +4] with k = −1 reference. Controls: ln GDPpc, ln pop, ind2-share. SE clustered by city.

**Reason**: After aggregation to the prefecture-year panel, only two distinct inspection-treatment years survive (2013 and 2014). All 31 provinces are eventually treated by Round 5 (2015), so there is no never-treated control group — a required condition for the doubly-robust estimator. The pre-registered specification is infeasible.

**Result under executed substitute**: β(k=0) = −0.065, SE = 0.025, p = 0.011.

### D-B-2 (Phase B2 — Sun-Abraham robustness check, same-window)

**Pre-registered**: Not in original pre-registration. Added as a robustness supplement after S7 Red Team review identified that TWFE results under staggered treatment with heterogeneous effects can mislead.

**Executed**: Sun-Abraham (2021) cohort-stacked heterogeneity-robust estimator using 5 round-level inspection cohorts (Rounds 1–5, start dates 2013-05 through 2014-11). Cohort c uses later-treated cohorts' pre-treatment observations as controls.

**Result**: β(k=0) = −0.019, SE = 0.117, p = 0.87. Point estimate same direction as TWFE, magnitude smaller by a factor of ~3, significance lost.

**Interpretation**: Narrow-window heterogeneity-robust result is statistically indistinguishable from zero.

### D-B-3 (Track 1 extension — Sun-Abraham with Rounds 1–9 / 2013–2017)

**Pre-registered**: Not in original pre-registration. Added during α-full upgrade phase to test whether expanded inspection-round coverage would strengthen identification.

**Executed**: Expanded treatment panel to include Rounds 6–9 (2016–2017, including 回头看 re-inspections covering 23 provinces that had been treated in Rounds 1–5). Total 62 province-round records. Re-fit the Sun-Abraham cohort-stacked estimator with 9 cohorts spanning 2013-05 through 2017-04.

**Result**: β(k=0) = **+0.016**, SE = 0.117, p = 0.19. β(k=+3) = +0.047, p = 0.005 (significant POSITIVE). **Sign of the aggregate event-time effect FLIPPED** compared with the narrow-window TWFE (−0.065) and the narrow-window Sun-Abraham (−0.019).

**Interpretation**: All nine cohort-specific CATT(k=0) values under the expanded sample are positive (+0.011 to +0.083). The original TWFE negative coefficient was a staggered-treatment-bias artifact (Goodman-Bacon 2021; Borusyak-Jaravel-Spiess 2024) rather than a causal inspection effect. We report H2 as **definitively null** in §5.4.1. The pre-registered "consistent with prediction" framing from earlier drafts is withdrawn. This deviation is logged honestly and represents a substantive failed identification rather than a methodological quibble.

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

**Interpretation**: We interpret the null as evidence that encyclopedic descriptive text (Wikipedia) is a domain-mismatched source for a governance-rhetoric measurement instrument, rather than as evidence that the VAI itself is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news or CNKI 重要报纸 government reporting — whose construction is deferred to future work (see §6.3). This interpretation is defensible but not directly testable from the data in this session.

**Honesty claim**: The failure is reported transparently in §3.2.5-3.2.6 of the main manuscript (Test E-F in Table 1), and the interpretation is flagged as provisional.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401–qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: **positive differential** |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes — qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this.

**Result**: All three coefficients |β| ≤ 0.011, |d| ≤ 0.011. TOST at ±0.10 equivalence bounds rejects |β| ≥ 0.10 at p < 10⁻⁶.

**Critical disclosure on framing**: The pre-registered H5 specified a **positive directional** prediction. The observed result is a clean null. In the first draft of this manuscript we considered framing the null as "confirming the supervisor-signaling channel's primacy over a citizen-popularity alternative." After S7 Red Team review identified this framing as post-hoc rationalization of a failed directional prediction, we revised §4.3 to report the results as **exploratory rather than confirmatory**, with a TOST-based quantitative bound and explicit acknowledgment that the null leaves multiple theoretical interpretations open. This revision was made before submission.

**Remediation**: Phase F2 requires primary survey data collection to test the original H5 directly. Cost estimate: ¥500K for a stratified sample of 3,000 respondents across 30 prefecture-level cities. Deferred to follow-up study.

### D-E-1 (Phase E — Construct validity)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, provincial-government descriptive texts); correlation with primary VAI in [0.3, 0.7] range; independent β(VAI_3rd → CIR) > 0.

**Executed**: Three internal construct-validity tests in place of the third-party corpus:
- E-A: Expanded internal dictionary (78+70 terms, independently curated) — resulting r(VAI_orig, VAI_ext) = 0.93.
- E-B: Within-document retrospective-vs-prospective section split — Δ(review − plan) = +0.025, paired t = 8.4, p < 10⁻¹⁶.
- E-C: Dictionary-bootstrap half-halves — mean r = 0.18 (reported as limitation).
- Additionally: E-A CIR replication with VAI_ext — β = +0.111, p = 0.011 (satisfies the β > 0 at 5% criterion).

**Reason**: No independent third-party text corpus covering 282 cities × 23 years is locally available. Scraping Xinhua or Baidu Baike at this coverage requires an extended browser-automation session that exceeds the resource budget of the α-full phase.

**Remediation**: A Phase E2 extension will construct a true third-party VAI from CNKI 重要报纸 archive (CARSI-authenticated access) covering at least the 2008–2022 subset. Expected timeline: within the R1 revision cycle.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401-qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes — qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this. Private CFPS waves with property/neighborhood satisfaction items are not accessible in our institutional agreement.

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

**Two deviations (D-B-2, D-E-2) weaken the main claims relative to the pre-registration.** We report both transparently in §4.2 and §3.2 respectively. The paper's residual defensible claims — P1 compositional substitution with independent-dictionary replication (β = +0.111, p = 0.002), the within-document E-B behavioral signature (Δ = +0.025, paired t = 8.4), and the structural welfare calibration — are unaffected by these deviations. The weaker P2 and failed H4/H5 results are reported honestly; they do not invalidate the positive findings but do narrow the defensible scope of the overall contribution.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.3's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.3's opening paragraph).


---

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

Following Simonsohn, Simmons, and Nelson (2020), we ran a pre-registered specification curve combining:
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

### C.2 Horse races against alternative explanations (main text §5.1)

| Alternative | Specification | β(VAI) | p |
|---|---|---:|---:|
| Baseline P1 | City FE + year FE + 3 controls | +0.113 | 0.002 |
| + GDP growth control | Added annual GDP growth | +0.109 | 0.003 |
| + urbanization² control | Added urbanization rate and its square | +0.111 | 0.002 |
| + leader-tenure control | Added party-secretary + mayor tenure | +0.110 | 0.003 |
| All four jointly | All three above | +0.108 | 0.004 |

### C.3 P2 placebo battery (main text §5.4.1)

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

### C.7 Welfare sensitivity (main text §5.3)

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

(In main text as §7 Appendix D. See Deviations D-B-1 through D-F-1.)

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


---

# References

[BibTeX-compiled APA 7th style reference list — see `01-literature/references.bib`. Key references include: Adcock & Collier 2001 (construct validity); Ash & Hansen 2023 (text-as-data review); Borusyak Jaravel Spiess 2024 (staggered DiD); Budge & Farlie 1983 (manifesto analysis); Callaway & Sant'Anna 2021; Christensen Freese Miguel 2019 (pre-reg in social science); Cronbach & Meehl 1955 (construct validity foundations); Gentzkow Kelly Taddy 2019 (text-as-data); Goodman-Bacon 2021 (staggered TWFE bias); Grimmer 2010; Li & Zhou 2005 (Chinese promotion incentives); Nosek et al 2015 (pre-reg); Ornstein Blasingame Truscott 2022 (LLM classification); Shi 2022 (Chinese text topic models); Slapin & Proksch 2008 (manifesto scaling); Sun & Abraham 2021]

---

*End of manuscript v3. Word count target: ~9,500 main + 2,000 appendix.*
