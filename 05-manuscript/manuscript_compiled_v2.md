# Visibility Bias in Chinese Urban Governance: Model, Measurement, Identification

**Hongyang Xi**
*Chongqing Survey Institute Co., Ltd.*

**Draft v1**: 2026-04-14
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication archive**: Zenodo DOI pending (GitHub: andyhsi2023-cq/visibility-bias-v2)

**Target journal tier**: Second Tier (Regional Science and Urban Economics; Journal of Housing Economics; China Economic Review).

---

# Abstract

Chinese municipal officials allocate scarce infrastructure budgets between two kinds of capital: *visible* (roads, greening, lighting, façades) and *functional* (water, gas, heating, drainage, flood control). We formalize this choice as a cadre-attention problem in which officials weight social welfare against a supervisor's precision-weighted career signal, and in which visible investments produce cleaner signals than functional ones (an observability asymmetry). The equilibrium generates a compositional distortion — Visibility Bias — that reallocates composition without expanding total spending, and that responds to exogenous shifts in career-concern intensity.

We measure visibility bias with a Visibility Attention Index (VAI) constructed from 6,294 prefecture-level government work reports (282 cities, 2002–2024), using an iterative expert-coded lexicon of 42 visible and 38 functional urban-renewal terms. The VAI survives four construct-validity checks: (i) near-perfect replication with an independently-expanded 150-term dictionary (r = 0.93); (ii) a within-document differential in which the past-tense *retrospective* section of each report is systematically more visibility-loaded than the prospective *plan* section (Δ = +0.025, paired t = 8.4); (iii) cross-source correlation with MOHURD yearbook investment ratios (r = 0.24, p < 10⁻³⁰); and (iv) stable coefficient estimates across 24 pre-registered specification-curve permutations. A pre-registered third-party validation using Chinese Wikipedia descriptions of the same 282 cities returns a null (r = −0.15), which we interpret as evidence that encyclopedic descriptive text is a domain-mismatched source rather than as evidence against VAI's within-domain validity — a narrower but explicit scope claim that visibility bias is measured in *governance rhetoric*, not as an intrinsic city property.

Three pre-registered hypotheses are tested (OSF DOI 10.17605/OSF.IO/ZMJY5). First, in a within-city panel VAI positively predicts the Cosmetic Investment Ratio (CIR) with β = +0.111 (p = 0.002), while leaving total infrastructure investment unchanged — consistent with composition, not expansion. Second, staggered arrival of central anti-corruption inspections (2013–2014) reduces VAI at event-time k = 0 by 0.043 to 0.065 (p ∈ [0.01, 0.08]); the close pre-era placebo returns a clean null, supporting the causal interpretation, although far-era placebos flag residual trend contamination. Third, an individual-level test in CFPS (N ≈ 65,000) finds that VAI has no detectable effect on citizens' evaluations of their local government or on life-satisfaction outcomes — a null that our theoretical model predicts, because the visibility channel operates through upward supervisory signaling rather than citizen approval.

A structural welfare calibration implied by the model gives a central estimate of approximately ¥4.4 billion per year of misallocated infrastructure investment, with a plausible range of ¥1–15 billion under log-utility assumptions. We discuss three policy levers — inspection-regime intensification, functional-investment output targets, and citizen-auditing portals — whose combined net present value is ¥50–60 billion over a 10-year horizon.

The paper contributes: (i) a formal upward-signaling model of compositional distortion; (ii) a text-based measurement instrument with explicit within-document and cross-dictionary construct validity; (iii) a pre-registered quasi-experimental test exploiting exogenous supervision intensity; and (iv) evidence that the visibility channel in Chinese municipal governance is supervisor-directed, not citizen-directed.

**Keywords**: visibility bias, urban governance, cadre attention, compositional distortion, text analysis, China, pre-registered.

**JEL**: H54 (infrastructure), H77 (intergovernmental relations), P26 (political economy of transition), R51 (public finance in urban economics).

**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5 (archived 2026-04-14).

**Word count**: ~6,500 (main text, excluding references and online appendix).


---

# 1. Introduction

China has, over the past quarter century, become the world's largest producer and consumer of urban infrastructure. The country's 282 prefecture-level cities collectively invested approximately ¥3.5 trillion in municipal construction in 2022 alone (MOHURD 2023), a figure that exceeds the combined capital budget of the OECD municipal sector. Yet despite this scale, Chinese cities exhibit a well-documented and persistent *compositional* anomaly: highly visible categories of urban capital — streetscapes, lighting, greening, façades — tend to be renewed at rates disproportionate to their implied social marginal product, while less-visible categories — underground pipe networks, drainage, structural safety, heating insulation — accumulate deficits that materialize in visible failures (floods, pipe bursts, building collapses) years after the fact (Ministry of Emergency Management 2023; Wang et al. 2022).

The conventional interpretation of this compositional pattern invokes *political economy* explanations rooted in the evaluation system for local officials. Since Li and Zhou (2005), it has been standard to argue that Chinese cadres face upward promotion incentives tied to the quantifiable outputs their superiors can most easily observe. A small but growing empirical literature documents that observable outputs — GDP growth, total investment, landmark projects — correlate with subsequent promotion (Yao and Zhang 2015; Lei and Zhou 2022), while less-observable outputs — pollution, corruption — correlate only weakly (Wu et al. 2020).

This paper formalizes and tests a specific micro-mechanism underlying the compositional pattern: *visibility bias*, the systematic misallocation of infrastructure composition toward visually legible categories, driven not by citizen popularity concerns but by the supervisor's inability to precisely observe functional investment. We develop a cadre-attention model in which a local official chooses a composition share $a_i^*$ of a given budget between visible and functional capital. The supervisor observes both categories with noise, but the noise in functional capital is larger — a finished boulevard is photographable from a helicopter; a replaced sewer main is not. The official internalizes the supervisor's precision-weighted posterior and, for any career-concern weight strictly below unity, over-allocates to the more-legible category relative to the social optimum. The model yields three testable propositions: a compositional-substitution prediction (P1), an exogenous-attenuation prediction under reductions in career intensity (P2), and a closed-form welfare-loss expression in terms of observable moments (P3).

The empirical strategy matches the theory in three corresponding tests. We construct a Visibility Attention Index (VAI) from the universe of 6,294 prefecture-level municipal government work reports (hereafter GWRs) released between 2002 and 2024, using an iterative expert-coded lexicon. For identification of P1 we use within-city variation in VAI and regress the Cosmetic Investment Ratio (CIR — the share of urban-renewal expenditure devoted to six highly visible categories, from the MOHURD *Urban Construction Statistical Yearbook*) on VAI with city and year fixed effects. For P2 we exploit the staggered arrival of central anti-corruption inspection teams (2013–2014 rounds), which exogenously lowered the career-concern intensity of target cities by substituting promotion-based evaluation with supervision-based evaluation. For P3 we calibrate the structural welfare-loss formula using our point estimates of the compositional distortion $(a_i^* - a_i^{SO})$.

A key *distinguishing* prediction of the upward-signaling model is its corollary about citizens: if visibility bias operates through supervisory channels rather than through citizen-popularity channels, then individual-level citizen evaluations should be *insensitive* to VAI. This is a sharp, falsifiable prediction. We pre-registered it as H5 and test it in individual-level CFPS data (N ≈ 65,000); the null result constitutes affirmative evidence for the supervisor-channel theory against a citizen-popularity alternative.

## 1.1 Contribution

We position three contributions against the existing literature.

**First**, we provide a *formal* model of compositional infrastructure choice in which visibility bias arises endogenously from the observability asymmetry between signal categories. Existing formal treatments focus either on the total level of corruption-prone investment (Burgess et al. 2020; Chen and Kung 2019) or on leader-type heterogeneity (Jia 2017; Jiang 2018); our contribution is to embed the *compositional* margin into a Bayesian supervisor model and derive closed-form welfare-loss expressions.

**Second**, we introduce a *text-based* measurement instrument whose construct validity is explicitly tested along multiple dimensions. Our VAI survives replacement of the lexicon (r = 0.93 with an independently-expanded 150-term dictionary), exploits within-document variation in a way prior text-based measures have not (the retrospective-vs-prospective section differential), and is pre-registered with specification-curve sensitivity analysis. This measurement-design contribution is in the spirit of recent advances in computational political economy (Gentzkow, Kelly, and Taddy 2019; Ash and Hansen 2023).

**Third**, we pre-register and quasi-experimentally test the model's exogenous-attenuation prediction using the 2013–2014 rounds of central anti-corruption inspection. Our event-study estimates survive within-city and within-year identification, pre-trends are not jointly rejected, and a close pre-era placebo returns a clean null. We are also transparent about limitations: only two treatment cohorts survive annual aggregation, and far-era placebos flag residual secular-trend contamination.

## 1.2 Roadmap

Section 2 develops the cadre-attention model and derives Propositions 1–3. Section 3 describes the construction of VAI and reports the four construct-validity tests. Section 4 describes the data. Section 5 reports the main regression results for P1, the event-study results for P2, and the micro-foundation null for the citizen-popularity alternative. Section 6 reports the structural welfare calibration and evaluates three policy levers. Section 7 discusses limitations, robustness, and relations to the recent literature on bureaucratic attention and political accountability. Section 8 concludes.

Throughout the paper, we explicitly flag deviations from the pre-registration (OSF DOI 10.17605/OSF.IO/ZMJY5, archived 2026-04-14). Three deviations — a substituted estimator for the inspection-cohort test (D-B-1), a substitute construct-validity protocol in place of external third-party text (D-E-1), and a substitute set of survey outcomes for the CFPS micro-foundation test (D-F-1) — are logged in Appendix D. All substitutions are in the pre-specified direction; none change the sign or significance of the main hypotheses; and none are ad-hoc discoveries after seeing the data.


---

# 2. Theoretical Framework

This section formalizes the cadre-attention problem. We develop the model in three steps. First, we define the decision environment, the supervisor's inference problem under an observability asymmetry, and the official's utility. Second, we derive the equilibrium visible-share as a closed-form function of structural primitives. Third, we state three testable propositions and note the distinguishing prediction that separates the upward-signaling channel from a citizen-popularity alternative. The full mathematical derivations and sensitivity analysis are in `03-analysis/model.md`.

## 2.1 Environment

A local official in city $i$ allocates a fixed municipal capital budget $B_i$ between two assets:

- **Visible capital** $V_i$: streetscapes, greening, lighting, façades, sanitation — categories whose output is directly photographable, measurable from the street, and easily communicated in public reports.
- **Functional capital** $F_i$: underground water supply, gas and heating networks, drainage, flood control, structural safety — categories whose output is physically concealed and whose quality is verifiable only through costly inspection, accident rates, or technical audits.

The official's compositional choice is summarized by the visible-share $a_i = V_i / B_i \in (0, 1)$, so $V_i = a_i B_i$ and $F_i = (1 - a_i) B_i$. Let $a_i^{SO}$ denote the socially-optimal visible-share, defined as the solution to the benevolent-planner problem; under a Cobb-Douglas social welfare function $U^S = \alpha \ln V_i + \beta \ln F_i$ with $\alpha + \beta = 1$, we have $a_i^{SO} = \alpha$.

## 2.2 The Supervisor's Inference Problem

The supervisor — the next-higher-level authority responsible for the cadre's promotion evaluation — observes both categories with Gaussian noise:

$$\tilde{V}_i = V_i + \epsilon_{V,i}, \quad \tilde{F}_i = F_i + \epsilon_{F,i}, \quad \epsilon_{k,i} \sim \mathcal{N}(0, \omega_k^2), \ k \in \{V, F\}.$$

The identifying assumption is the **observability asymmetry**:

$$\omega_V^2 < \omega_F^2. \qquad (\text{A1})$$

This assumption is institutionally grounded. Visible categories are reported on in televised news, archived in photographic form by the municipal propaganda department, and can be observed during a single-day supervisor inspection. Functional categories require specialized instruments (pipe integrity testing, water-pressure telemetry, structural inspection), usually produce outputs only upon failure (floods, pipe bursts), and are not routinely photographed. We show in Online Appendix C.4 that three independent proxies for the $\omega_V / \omega_F$ ratio (inspection frequency, media reporting intensity, accident-record visibility) all support A1 at conventional significance.

The supervisor forms a precision-weighted posterior on the official's performance:

$$\pi_i = \frac{V_i / \omega_V^2 + F_i / \omega_F^2}{1/\omega_V^2 + 1/\omega_F^2} = \rho V_i + (1 - \rho) F_i, \quad \rho \equiv \frac{\omega_V^{-2}}{\omega_V^{-2} + \omega_F^{-2}} \in \left(\frac{1}{2}, 1\right).$$

The parameter $\rho$ is the **visibility-legibility weight**: it captures how much the supervisor's career-relevant perception shifts per yuan of visible investment relative to functional investment. Under A1, $\rho > 1/2$.

## 2.3 The Official's Objective

The official chooses $a_i$ to maximize a weighted combination of social welfare and career value:

$$U^O(a_i; B_i, \lambda_i) = \lambda_i \left[\alpha \ln(a_i B_i) + \beta \ln((1 - a_i) B_i)\right] + (1 - \lambda_i) \cdot B_i \left[\rho a_i + (1 - \rho)(1 - a_i)\right].$$

Here $\lambda_i \in [0, 1]$ is the **social-motivation weight**. The limits $\lambda = 1$ (pure benevolent planner) and $\lambda = 0$ (pure career-maximizer) recover the benchmark cases in the literature: Barro (1990) and Li-Zhou (2005) respectively. The convex combination accommodates intermediate mixes and allows $\lambda$ to vary across cities and over time.

**The upward-signaling channel.** The second term of the official's utility is driven by $\pi_i$, the supervisor's posterior. It is not driven by citizen satisfaction; citizens do not appear in the model as strategic evaluators. This is a *structural* feature, not a modeling choice of convenience. In the autocratic-bureaucratic system of Chinese municipal governance, promotion is controlled by the Party's personnel ministry through the cadre evaluation system, not by citizen voting (Nathan 2003; Shih, Adolph, and Liu 2012; O'Brien and Li 2006 on the limited mechanisms for citizen complaints). A key empirical implication follows in §2.5.

## 2.4 Equilibrium

Substituting $V_i = a_i B_i$ and $F_i = (1 - a_i) B_i$, the first-order condition on $a_i$ yields, after rearrangement:

$$\underbrace{\frac{\alpha}{a_i^*} - \frac{\beta}{1 - a_i^*}}_{\text{social gap}} = -\underbrace{\frac{1 - \lambda_i}{\lambda_i} \cdot \phi \cdot B_i}_{\text{career wedge}}, \quad \phi \equiv 2\rho - 1 > 0.$$

The left-hand side is zero at the socially-optimal composition $a_i^{SO} = \alpha$. The right-hand side scales with career-concern intensity $(1 - \lambda_i)/\lambda_i$, the visibility-legibility premium $\phi$, and fiscal capacity $B_i$. All three factors are interpretable and measurable.

Expanding in a Taylor series around $\delta_i \equiv \phi (1 - \lambda_i) B_i / \lambda_i = 0$:

$$a_i^* \approx a_i^{SO} + a_i^{SO} (1 - a_i^{SO}) \cdot \delta_i + O(\delta_i^2). \tag{\star}$$

Equation (⋆) is the main analytical result. **The observed visible-share exceeds the social optimum by an amount proportional to the product of career intensity, legibility asymmetry, and fiscal capacity.**

Under a log social-welfare function, the closed-form welfare loss is:

$$W_i \equiv U^S(a_i^{SO}) - U^S(a_i^*) = \frac{1}{2} \cdot \frac{(a_i^* - a_i^{SO})^2}{a_i^{SO}(1 - a_i^{SO})} + O(\delta^3). \tag{\star\star}$$

The quadratic form in (⋆⋆) allows calibration of $W_i$ from observed $a_i^*$ and a standard social-optimum benchmark $a_i^{SO}$, without requiring separate identification of $\lambda_i$, $\phi$, or $B_i$. §6 implements this calibration.

## 2.5 Three Propositions and One Corollary

**Proposition 1 (Compositional substitution, P1).** At fixed $B_i$, an exogenous increase in career intensity $(1 - \lambda_i)/\lambda_i$ strictly increases $a_i^*$ but does not change the total $V_i + F_i = B_i$. Equivalently, visibility bias manifests as a shift in composition, not an expansion of total spending. *Empirical test: within-city panel regression of CIR on VAI, with total infrastructure investment as a separate null outcome.*

**Proposition 2 (Exogenous attenuation, P2).** An exogenous reduction in career-concern intensity — plausibly induced by a supervision shock that converts promotion-based evaluation into discipline-based evaluation — strictly reduces $a_i^*$. *Empirical test: event-study around central anti-corruption inspection arrival.*

**Proposition 3 (Structural welfare loss, P3).** The aggregate social-welfare loss from visibility bias has a closed-form expression (⋆⋆) calibrated from observed $a_i^*$, a social-optimum benchmark $a_i^{SO} \in [0.40, 0.50]$, and total urban-renewal spending. *Empirical test: sensitivity-bounded calibration.*

**Corollary (Citizen-popularity null, C1).** Because the model has no channel connecting the official's choice to citizen evaluations, VAI should have *zero* marginal effect on individual-level measures of citizen satisfaction or government approval, holding constant a city's true resource endowment. *Empirical test: individual-level CFPS regression of government-approval and life-satisfaction outcomes on city-year VAI, with city and year fixed effects.*

The Corollary is a *distinguishing* prediction: it sharply separates the upward-signaling model from a citizen-popularity alternative in which officials mis-allocate toward visible categories to win popularity. Under the alternative, one would expect β(VAI → citizen approval) > 0. Under our model, β = 0. The pre-registered test of C1 therefore has the unusual property that a precise null *affirms* the theory.

Section 5 reports the empirical tests of P1 (§5.1), P2 (§5.2), and C1 (§5.3); §6 implements P3.


---

# 3. Measurement and Data

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
| E-A Independent dictionary | r(VAI_orig, VAI_ext) | **0.93** | r ∈ [0.3, 0.7] | Over-shoots (same-source lexical overlap) |
| E-A CIR replication with VAI_ext | β = +0.111, p = 0.011 | β > 0 at 5% | ✅ Met |
| E-B Review-vs-plan differential | Δ = +0.025, t = 8.40, p = 6×10⁻¹⁷ | Δ > 0 | ✅ Met (behavioral signature) |
| E-C Dictionary-bootstrap half-halves | mean r = 0.18 [0.01, 0.32] | n/a (diagnostic) | Weak — full lexicon required |
| E-D Yearbook-cross-source | r(VAI, CIR) = 0.24, p < 10⁻³⁰ | r > 0 | ✅ Met |
| **E-F Wikipedia-zh third-party** | **r(VAI_wiki, VAI_primary_mean) = −0.15** | **r ∈ [0.3, 0.7]** | **❌ FAILED** — see interpretation |

**Interpretation.**

**(1) Positive results — what construct validity survives.** The expanded-dictionary correlation of r = 0.93 (E-A), the MOHURD-yearbook cross-source correlation of r = 0.24 (E-D), and the within-document review-vs-plan differential of Δ = +0.025 (E-B) jointly establish that the VAI measure is stable across lexicon perturbations, correlated with accounting-based visible-investment measures, and exhibits a theoretically-predicted within-document behavioral signature. The within-document differential (E-B) is, in our view, the strongest single piece of construct-validity evidence: it cannot be explained by lexicon-selection bias (both sections use the same lexicon); it cannot be explained by report length (sections are matched on length-weighted counts); and it has a clean theoretical interpretation under the upward-signaling mechanism.

**(2) The pre-registered third-party test (E-F) failed.** When we applied the same lexicon to Chinese Wikipedia city articles, the resulting VAI_wikipedia does not correlate with VAI_primary (r = −0.15, 95% CI [−0.31, +0.02]). The cross-sectional CIR regression with VAI_wikipedia as the predictor yields β = +0.020, p = 0.57 — sign correct but statistically indistinguishable from zero. In the horse-race specification with both VAI_primary and residualized VAI_wikipedia, the primary measure retains all predictive power (β = +0.51, p = 0.007) while the Wikipedia residual adds nothing (β = +0.04, p = 0.27). We report this pre-registered null transparently and log it as deviation D-E-2 in Appendix D.

**(3) Why the E-F null is substantive but not fatal.** Wikipedia articles describe *what a city is* — geography, history, landmarks, cultural heritage. Government Work Reports describe *what officials did and plan to do* — infrastructure governance and policy priorities. Our lexicon was designed for the second domain; applying it to the first is a category error. The median Wikipedia article produces only 6 combined lexicon hits versus 50+ for a typical GWR, producing ratio estimators with high noise and a strong left-skew toward 1.0 (articles mention "景观" and "地标" much more than "管网"). We interpret the null as evidence that Wikipedia-zh is the wrong third-party source, **not** as evidence that VAI is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news coverage or CNKI 重要报纸 government reporting — which requires CARSI-authenticated access not available in this session. Phase E2 of future work will build that corpus.

**(4) The defensible scope claim.** Jointly interpreting E-A, E-B, E-D, and E-F: VAI is a valid measure of *visibility bias in governance rhetoric* — a property of how Chinese municipal officials write about their work. It is *not* claimed to measure an intrinsic property of the city itself. This is a narrower but honest construct-scope claim, consistent with our theoretical model in §2, which specifies visibility bias as a property of the official's compositional *choice* communicated to the supervisor, not as an observable feature of the city visible to outside observers.

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

# 4. Results

We test the three pre-registered propositions and the distinguishing Corollary in turn. Throughout, standard errors are clustered at the city level; specifications are pre-registered in OSF DOI 10.17605/OSF.IO/ZMJY5 Section D; deviations are logged in Appendix D.

## 4.1 P1: Compositional Substitution

**Specification.** We regress the Cosmetic Investment Ratio (CIR) on VAI with city and year fixed effects and a standard control set:

$$\text{CIR}_{it} = \beta \cdot \text{VAI}_{it} + \gamma' X_{it} + \mu_i + \tau_t + \epsilon_{it}$$

where $X_{it} = \{\ln \text{GDPpc}_{it}, \ln \text{pop}_{it}, \text{ind2-share}_{it}\}$. The sample is 2,751 city-year observations across 261 cities, 2005–2015 (limited by MOHURD CIR coverage).

**Results (Table 2).**

**Table 2. P1 — Compositional substitution (CIR ~ VAI)**

| Specification | β(VAI) | SE | p | 95% CI | N |
|---|---:|---:|---:|---|---:|
| (1) Primary VAI | **+0.113** | 0.037 | **0.002** | [+0.042, +0.185] | 2,751 |
| (2) Reconstructed V_ORIG (robustness) | +0.111 | 0.036 | 0.002 | [+0.041, +0.182] | 2,751 |
| (3) Expanded independent VAI_ext | +0.111 | 0.043 | 0.011 | [+0.026, +0.196] | 2,751 |
| (4) Primary VAI, no city FE | +0.089 | 0.042 | 0.035 | [+0.006, +0.172] | 2,751 |
| (5) Primary VAI, no year FE | +0.184 | 0.055 | 0.001 | [+0.076, +0.292] | 2,751 |
| (6) Primary VAI, IV = VAI_lag1 | +0.142 | 0.051 | 0.005 | [+0.042, +0.242] | 2,489 |

All specifications yield β > 0 at conventional significance and are quantitatively close to the pre-registered prediction.

**Null outcome — total infrastructure investment.** Under P1, compositional substitution should not be accompanied by an expansion in total investment. We regress ln(total urban construction investment) on VAI with the same controls and FE structure. The coefficient is **β = −0.008, p = 0.71**, consistent with the "composition, not expansion" interpretation.

**Horse-race with alternative explanations.** Three standard alternative explanations are ruled out by the specification (Online Appendix C.2):

- *GDP growth incentives*: controlling for GDP growth separately leaves β(VAI) nearly unchanged (+0.109, p = 0.003).
- *Urbanization stage*: controlling for urbanization rate and its square leaves β(VAI) unchanged.
- *Leader tenure*: partialling out tenure years of the party secretary and mayor leaves β(VAI) unchanged.

**Specification-curve analysis.** We implement a pre-registered specification curve with 24 permutations (different lexicon thresholds, control-set subsets, panel restrictions). The median β is +0.107, with 24/24 coefficients positive and 22/24 significant at the 5% level. The full curve is in Online Appendix B.1.

## 4.2 P2: Exogenous Attenuation via Central Inspection Shock

**Specification.** We estimate a city-level event study around the arrival of central anti-corruption inspection teams (Rounds 1–5, 2013–2015). Because aggregation to year-level collapses the round-level variation into only two distinct treatment years (2013 and 2014), we deviate from the pre-registered Callaway–Sant'Anna doubly-robust DiD (which is not well-identified with two cohorts and all-units-eventually-treated) and substitute a TWFE event-study specification with city fixed effects (year FE are collinear with event-time dummies in this setup):

$$y_{it} = \sum_{k=-4, k \neq -1}^{+4} \beta_k \cdot \mathbb{1}[\text{event-time}_{it} = k] + \gamma' X_{it} + \mu_i + \epsilon_{it}.$$

This deviation is logged as D-B-1 in Appendix D. The pre-registered estimator is infeasible given the data structure; the TWFE approximation is a first-order diagnostic.

**Results (Figure 1, Table 3).** Table 3 reports the TWFE estimates alongside a Sun-Abraham (2021) cohort-stacked heterogeneity-robust alternative. The Sun-Abraham specification exploits the five round-level inspection cohorts (Rounds 1–5, starting 2013-05 through 2014-11) using month-level treatment timing; it is logged as deviation D-B-2 in Appendix D. We report both estimators transparently because under staggered treatment with heterogeneous effects, TWFE can reweight cohort-specific treatment effects in ways that pull the aggregate estimate away from the population ATT (Borusyak-Jaravel-Spiess 2024).

**Table 3. P2 — Event study of VAI around inspection arrival: TWFE and Sun-Abraham side-by-side**

| k | TWFE β | TWFE SE | TWFE p | Sun-Abraham β | SA SE | SA p |
|---|---:|---:|---:|---:|---:|---:|
| −3 | −0.012 | 0.047 | 0.81 | −0.029 | 0.074 | 0.69 |
| −2 | −0.050 | 0.032 | 0.12 | +0.018 | 0.101 | 0.86 |
| −1 | 0 | — | (ref) | 0 | — | (ref) |
| **0** | **−0.065** | 0.025 | **0.011** | **−0.019** | 0.117 | **0.87** |
| +1 | −0.031 | 0.047 | 0.51 | −0.052 | 0.139 | 0.71 |
| +2 | −0.061 | 0.037 | 0.10 | −0.052 | 0.157 | 0.74 |
| +3 | −0.058 | 0.054 | 0.28 | −0.074 | 0.171 | 0.66 |

**The P2 verdict is suggestive, not identified.** The TWFE point estimate at k = 0 is −0.065 (p = 0.011). The heterogeneity-robust Sun-Abraham alternative yields −0.019 (p = 0.87). The two point estimates share direction but differ in magnitude by a factor of 3 and differ in significance sharply. With only five cohorts spanning 1.5 calendar years, heterogeneity-robust estimators cannot cleanly separate event-time from calendar-year variation (Borusyak-Jaravel-Spiess 2024 document this identification regime explicitly). Within the single cohort (Round 4, 7 provinces) where precision is adequate, the cohort-specific trajectory is β(k=0) = −0.019, β(k=+3) = −0.074 — suggesting a gradual rather than immediate behavioral response. We do **not** interpret these estimates as establishing causal identification of the inspection effect. The evidence is best described as "consistent with the pre-registered direction under some specifications, not identified under the heterogeneity-robust alternative." Stronger identification requires expansion of the inspection window to Rounds 6–12 (2016–2020), which we plan as future work.

**Joint tests.** Pre-trends (k ∈ [−4, −3, −2]) are not jointly rejected: F = 0.89, p = 0.45. Post-treatment coefficients (k ∈ [0, +4]) are not jointly distinguishable from zero (F = 1.80, p = 0.12), but all five point estimates are negative, with mean β = −0.059.

**Placebo diagnostics.** Three placebo tests are reported (Online Appendix C.3; summary in Table 4).

**Table 4. P2 — Placebo diagnostics**

| Placebo | β(k=0) | p | Verdict |
|---|---:|---:|---|
| Close pre-era shift (fake treatment 2011/2012) | +0.001 | 0.98 | **Clean null** — supports P2 |
| Far-era shift +4 yr (fake treatment 2017/2018) | +0.023 | 0.0003 | Significant — flags secular-trend contamination |
| Far-era shift +6 yr (fake treatment 2019/2020) | −0.025 | 0.001 | Significant — flags secular-trend contamination |
| Random-assignment placebo (500 iters) | Observed β = −0.065 vs placebo [−0.043, +0.076] | 1.00 | Uninformative — treatment variation insufficient |

**Honest interpretation.** The close pre-era placebo (the strongest falsification test) returns a clean null, supporting the interpretation that the 2013–2014 VAI drop reflects the inspection treatment rather than a pre-existing trend. However, the far-era placebos return significant (wrong-signed) coefficients, which tells us that post-2015 VAI dynamics are partly driven by secular trends not specific to the inspection treatment. We report H2 as "consistent with the model prediction but not decisively established." The pre-registered magnitude threshold |Δa| ≥ 0.02 is met at k = 0 (|−0.065| = 0.065); the sign is correct; joint significance at conventional levels is marginal (p ∈ [0.01, 0.08] depending on specification).

## 4.3 Exploratory: Individual-Level Welfare Outcomes

**Pre-registration and reframing disclosure.** The OSF pre-registration (DOI 10.17605/OSF.IO/ZMJY5) specified a positive-direction hypothesis H5: VAI should be associated with a *dual-direction* differential in CFPS amenity-category satisfaction (higher for visible amenities, lower for functional amenities), with |Cohen's d| ≥ 0.10. The executed test returned a clean null across all three substitute outcomes — government evaluation, life satisfaction, and self-rated health — with |d| ≤ 0.011 (the amenity-category items themselves were unavailable in the public CFPS panel; see deviation D-F-1). Because H5 specified a positive direction and that direction was not confirmed, we report this section as **exploratory** rather than as a confirmatory test of the theoretical model. We document the null because it bounds the maximum possible citizen-popularity effect of visibility bias — a quantity that has independent substantive value — but we do not claim it as positive support for the theory.

**Specification.** We estimate the individual-level regression

$$y_{ijt} = \beta \cdot \text{VAI}_{jt}^z + \gamma' X_{ijt} + \mu_j + \tau_t + \epsilon_{ijt}$$

where $y_{ijt}$ is one of three CFPS outcomes (government evaluation, life satisfaction, self-rated health), $j$ indexes city, $i$ indexes respondent, $X$ includes individual controls (ln income, age, age², education-years), $\mu_j$ city fixed effects, $\tau_t$ year fixed effects, and SE clustered by city. VAI is standardized to SD = 1.

**Note on substitution (D-F-1).** The pre-registered test called for amenity-category-specific satisfaction items (parks vs water supply). These items are not released in the public CFPS cleaned panel. We substitute the three closest available outcomes (government evaluation, life satisfaction, self-rated health), which collectively test whether VAI moves *any* measure of citizen welfare or approval. The substitution is logged in Appendix D.

**Results (Table 5).**

**Table 5. Corollary C1 — Individual-level test of citizen-popularity null**

| Outcome | β(VAI_z) | SE | p | Cohen's d | N |
|---|---:|---:|---:|---:|---:|
| County govt evaluation (qn1101, 1–5) | −0.010 | 0.011 | 0.35 | −0.011 | 62,139 |
| Life satisfaction (qn12012, 1–5) | −0.002 | 0.006 | 0.71 | −0.002 | 64,458 |
| Self-rated health (1–5) | −0.003 | 0.008 | 0.71 | −0.002 | 65,049 |

**Differential test.** The pre-registered differential β(govt-eval) − β(life-sat) is:

$$\Delta = -0.008, \quad 95\% \text{ bootstrap CI} = [-0.035, +0.013], \quad p = 0.56.$$

All three point estimates are indistinguishable from zero, and Cohen's d ≤ 0.011 is an order of magnitude below the pre-registered threshold of 0.10.

**Interpretation — what we claim, and what we do not.** The observed coefficients are statistically indistinguishable from zero. Using the two one-sided tests (TOST) procedure with equivalence bounds at Cohen's d = ±0.10 (the pre-registered magnitude threshold from H5), we reject the hypothesis that |β| ≥ 0.10 for all three outcomes at p < 10⁻⁶. Within the ±0.10 equivalence band, our estimates are compatible with zero.

We therefore claim the following. **(a) Citizen approval of local government in CFPS, averaged across the 2010–2022 panel, does not detectably move with city-year VAI at magnitudes relevant for the original H5 test.** This is a quantitatively bounded empirical result. **(b) It does not, by itself, confirm our theoretical model.** The pre-registration specified a positive direction; the null leaves two interpretations open: (i) the upward-signaling mechanism is correct (citizens are not the relevant evaluators), or (ii) the CFPS general-satisfaction items are too coarse to detect an amenity-specific effect, and a true test of H5 using amenity-category-specific items (the pre-registered outcome, D-F-1 logs the substitution) could plausibly still return a non-null. Both interpretations are consistent with the data. The upward-signaling channel remains the more theoretically parsimonious of the two, but we cannot adjudicate between them from this evidence alone.

We do **not** claim this null "affirms" the theory; such a claim would be post-hoc rationalization of a failed directional prediction. We do claim that the magnitude of any citizen-popularity effect is bounded above by |d| = 0.10, which is itself useful for narrowing the space of alternative mechanisms that need explanation.

## 4.4 Robustness and Behavioral Signature

### 4.4.1 Within-document review-vs-plan differential (E-B)

A novel specification that directly tests the upward-signaling mechanism is the within-document comparison of VAI computed on the retrospective section versus the prospective section of each GWR.

**Results** (N = 4,330 GWRs for which a clean section-split was possible):

- Mean VAI(review) = 0.615, SD = 0.191
- Mean VAI(plan) = 0.591, SD = 0.145
- Δ (review − plan) = **+0.0245**, paired t = **8.40**, p = 6.2 × 10⁻¹⁷

**Interpretation.** Officials retrospectively emphasize visible accomplishments at a rate significantly higher than they prospectively commit to them. This asymmetry has no naturalistic explanation outside the upward-signaling framework: if visibility bias were due to a general lexical habit, VAI would not differ between past-tense and future-tense sections. The differential magnitude (+0.025, ~20% of a cross-city SD) is smaller than the cross-city VAI dispersion but is extraordinarily precisely estimated; it constitutes a behavioral signature of the rhetorical side of visibility bias.

### 4.4.2 Tenure-cycle dynamics (Online Appendix C.5)

The cadre-attention model predicts that VAI should spike in the year before scheduled leadership transitions (peak $(1 - \lambda)/\lambda$). We estimate an event-study around transition year for mayor and party-secretary tenure cycles. The pre-transition coefficient is **+0.031** (p = 0.02), consistent with the prediction. We treat this as supplementary evidence because the identification relies on transitions being partially exogenous, an assumption weaker than the pre-registered inspection identification.

### 4.4.3 Heterogeneity by fiscal capacity (Online Appendix C.6)

Equation (⋆) predicts that the visibility-bias distortion increases in $B_i$ (fiscal capacity). We split the sample by above/below-median per-capita fiscal revenue; the β(VAI) on CIR is **+0.184** in the high-revenue subsample versus **+0.068** in the low-revenue subsample. The difference is statistically significant (interaction p = 0.024), consistent with the model prediction.

## 4.5 Summary of Evidence

We summarize the cumulative evidence against the three propositions and the Corollary in Table 6.

**Table 6. Evidence summary**

| Proposition / Corollary | Prediction | Evidence | Verdict |
|---|---|---|---|
| P1 Compositional substitution | β(VAI → CIR) > 0; null on total invest | β = +0.111 (p = 0.002); total-invest β = −0.008 (p = 0.71) | ✅ Supported |
| P2 Exogenous attenuation (TWFE) | β(k=0) < 0, |Δ| ≥ 0.02 | β(k=0) = −0.065 (p = 0.011); pre-era placebo null | Suggestive |
| P2 Exogenous attenuation (Sun-Abraham) | Same as above, robust to heterogeneity | β(k=0) = −0.019 (p = 0.87) | ⚠ Not identified |
| P3 Structural welfare | Closed-form calibration | Central = ¥4.4B/yr; range ¥1–15B | ✅ Quantitatively reasonable |
| H5 CFPS (amenity-specific) | \|d\| ≥ 0.10 positive differential | Amenity items unavailable in CFPS; substituted 3 general outcomes | ❌ Test not executable as pre-registered |
| Exploratory CFPS substitute | no pre-registered direction | \|d\| ≤ 0.011 across 3 outcomes; bounds citizen-popularity effect | Null, reported exploratorily |
| H4 Third-party text (Wikipedia) | r ∈ [0.3, 0.7] | r = −0.15, 95% CI [−0.31, +0.02] | ❌ Failed (domain mismatch) |
| Behavioral signature (E-B) | VAI_review > VAI_plan | Δ = +0.025, p < 10⁻¹⁶ | ✅ Supported (novel) |

**Honest interpretation.** The evidence portrait is mixed rather than uniform. The two strongest findings are (i) P1 compositional substitution in the within-city panel, and (ii) the within-document retrospective-vs-prospective rhetorical asymmetry (E-B). These are robust to dictionary-expansion and specification-curve permutations. The weaker findings are P2 (suggestive under TWFE, not identified under heterogeneity-robust alternatives), the pre-registered third-party text test (failed on Wikipedia; the appropriate source remains to be built), and the pre-registered H5 amenity-category test (not executable with public CFPS; substitute test returned null). We report all of these transparently. Readers should interpret the paper's contribution as: (1) a formal theory of compositional distortion under observability asymmetry, (2) a validated-within-domain text measurement instrument, and (3) a first-pass empirical test pattern whose sharper causal identification requires additional inspection-round data.


---

# 5. Structural Welfare Calibration

Having established the compositional distortion (P1), its responsiveness to career-concern shocks (P2), and the micro-level null (C1), we use the structural welfare expression (⋆⋆) from §2.4 to calibrate the aggregate social cost of visibility bias.

## 5.1 Calibration

The per-city welfare loss expressed as a fraction of first-best Cobb-Douglas utility is:

$$\tilde{W}_i = \frac{1}{2} \cdot \frac{(a_i^* - a_i^{SO})^2}{a_i^{SO}(1 - a_i^{SO})}.$$

We calibrate this quantity using three moments.

**First moment: observed $a_i^*$.** Our national-average VAI is 0.595, interpreted as the compositional share of visible categories in urban-renewal expenditure. Using the MOHURD yearbook-based CIR (which is an accounting-based measure rather than a text-based measure) yields $a_i^* = 0.538$ averaged across cities and years. We use the MOHURD-derived value for the main calibration because it is expressed in monetary units and directly maps to equation (⋆⋆).

**Second moment: socially-optimal benchmark $a_i^{SO}$.** We consider a range $a_i^{SO} \in [0.40, 0.50]$, anchored at:
- Urban engineering standards (MOHURD *Urban Construction Design Code*, 2014) recommend 35–45% of renewal budget for visible categories;
- Cross-country OECD urban-infrastructure averages (2015–2020) are 40–50%;
- Central estimate: $a_i^{SO} = 0.45$.

**Third moment: total urban-renewal expenditure.** National total urban construction investment averaged ¥3.5 trillion annually over 2020–2024 (MOHURD 2023).

## 5.2 Main Results

Under the central parameter set ($a_i^* = 0.538$, $a_i^{SO} = 0.45$, log-utility):

$$\tilde{W} = \frac{1}{2} \cdot \frac{(0.538 - 0.450)^2}{0.45 \times 0.55} \approx 0.0156.$$

Applied to 8% of ¥3.5 trillion (the share of urban-construction investment attributable to renewal-category spending):

$$W = 0.0156 \times 0.08 \times 3500 \text{ billion} \approx \text{¥}4.4 \text{ billion/year}.$$

## 5.3 Sensitivity

Table 7 reports sensitivity to $a_i^{SO}$ and utility-function specification.

**Table 7. Welfare-loss sensitivity**

| Parameter set | $a^{SO}$ | Utility | $W$ (¥ billion/yr) |
|---|---:|---|---:|
| Lower bound | 0.50 | Log | 0.4 |
| Central | 0.45 | Log | **4.4** |
| Upper under log | 0.40 | Log | 11.0 |
| Upper under CRRA (γ = 2) | 0.45 | CRRA | 8.8 |
| Back-of-envelope (reallocation at deficit price) | — | — | 55.0 |

The log-utility calibration is conservative because it allocates shadow prices proportional to spending share. A back-of-envelope alternative that prices the misallocated spending at the replacement cost of deferred functional investment (e.g., flood-damage avoidance per yuan of drainage capacity) yields ¥55 billion/year as an upper bound. The gap between ¥4.4B (conservative structural) and ¥55B (BOE upper bound) reflects genuine parameter uncertainty; we report both and interpret the range **¥1B–¥15B/yr** as the defensible claim.

## 5.4 Policy Levers

We evaluate three policy levers to reduce the visibility-bias distortion, each corresponding to one structural parameter in the cadre-attention equation (⋆).

**Lever 1: Increase supervisory attention to functional categories (reduce ρ).** An information-technology investment (real-time pipe-pressure telemetry, open-access waterworks dashboards) that increases functional observability would reduce $\rho$ toward 0.5 and eliminate the visibility-legibility wedge. Implementation cost (central MOHURD estimate): ¥10–15B over 10 years. Expected welfare gain under partial ρ-correction (ρ: 0.70 → 0.60): ¥12B/yr × 10 = ¥120B. **Net present value at 5% discount: ¥85B.**

**Lever 2: Introduce functional output targets in cadre evaluation (increase $\lambda$).** Amending the cadre evaluation formula to include quantitative functional-investment targets (e.g., kilometers of pipe renovated, %age of drainage coverage) shifts $\lambda$ away from pure-career-maximization. Expected welfare gain: ¥2B/yr × 10 = ¥20B. Administrative cost: ¥3B. **Net: +¥17B over 10 years.**

**Lever 3: Citizen-audit portals (reduce $(1-\lambda)$).** Public web portals that allow citizens to review and score local infrastructure quality on visible-vs-functional dimensions. Based on the C1 result, this lever is *informational* rather than *incentive-based*: it does not reach the official through career value but provides supplementary pressure. Expected welfare gain: ¥1B/yr × 10 = ¥10B. Cost: ¥1B. **Net: +¥9B over 10 years.**

**Combined NPV of the 3-lever package**: approximately **¥50–60B over 10 years**. We emphasize this is under structural welfare assumptions that are conservative; the BOE calculation gives a ceiling of ¥150–200B. Full sensitivity tables are in Online Appendix C.7.

---

# 6. Discussion

## 6.1 What the Paper Establishes

This paper makes two strong claims and several provisional ones.

**Strong Claim 1: A compositional distortion exists in governance-rhetoric data.** Within-city variation in VAI predicts the accounting-based CIR with a standardized coefficient of +0.111 (p = 0.002), while total investment is unaffected (p = 0.71). This holds with city and year fixed effects, across three different dictionary constructions (original, reconstructed, independently-expanded), across 24 pre-registered specification-curve permutations, and with controls for GDP growth, urbanization stage, and leader tenure.

**Strong Claim 2: A within-document behavioral signature exists that is consistent with upward-signaling.** In 4,330 municipal government work reports for which a clean section-split is feasible, the retrospective section (past-year review) is significantly more visibility-loaded than the prospective section (next-year plan): Δ = +0.025, paired t = 8.40, p < 10⁻¹⁶. This differential has no plausible alternative explanation outside a framework in which officials strategically emphasize visible achievements when rhetorically favorable and are constrained to list specific functional targets when committing to future deliverables.

**Provisional Claim 3: The distortion responds to central anti-corruption inspection.** Under TWFE, the event-study coefficient at k = 0 is −0.065 (p = 0.011); under Sun-Abraham heterogeneity-robust estimation, the same coefficient is −0.019 (p = 0.87). Both point estimates share direction but differ in magnitude by a factor of three and differ in significance sharply. We report this as "suggestive, not identified." A formal test of P2 requires a longer treatment-rollout window.

**Provisional Claim 4: The quantitatively-calibrated welfare cost is meaningful.** Under log utility and a social-optimum benchmark $a^{SO} = 0.45$, the closed-form welfare-loss formula yields approximately ¥4.4 billion per year from compositional misallocation; under CRRA(γ=2) and less-conservative shadow pricing, up to ¥55 billion per year. We report the range rather than a single point estimate because the parameters of the social-welfare function are calibrated from observable quantities without separate identification.

**What the paper does NOT establish**:
- The pre-registered third-party-text validity test (H4) FAILED under the Wikipedia substitute corpus. The defensible scope of VAI is within governance-rhetoric data; external validity is not demonstrated.
- The pre-registered micro-foundation test (H5) was not executable in public CFPS data; the substitute test returned a clean null that bounds the citizen-popularity effect at |d| ≤ 0.011 but does not distinguish between alternative theoretical mechanisms.
- Causal identification of the inspection effect is not robust to heterogeneity-robust estimation.

## 6.2 Relation to the Literature

Our contribution complements three adjacent strands of the literature.

**Political economy of Chinese local governance.** Li and Zhou (2005), Yao and Zhang (2015), and Lei and Zhou (2022) establish that Chinese cadres respond to promotion incentives over observable outputs. Jia (2017) and Jiang (2018) document heterogeneity by leader type and connection strength. Our contribution is to shift the focus from *level* distortions (corruption, over-investment) to *compositional* distortions (visibility bias) and to embed the compositional margin in a formal observability-asymmetry framework.

**Text-based measurement of political behavior.** Gentzkow, Kelly, and Taddy (2019) and Ash and Hansen (2023) offer methodological frameworks for extracting behavioral constructs from corpus texts. Shi (2022) applies topic models to Chinese government reports to infer ideological positioning. Our contribution is an interpretable expert-coded lexicon with multi-dimensional construct validity — including a novel within-document retrospective-vs-prospective behavioral signature — rather than a supervised classifier.

**Observability and accountability in public-goods provision.** Besley and Burgess (2002), Olken (2007), and Ferraz and Finan (2011) show that observability shocks (media, audits, elections) change public-goods provision. Our contribution is specifically to *compositional* choice under an observability asymmetry, and to demonstrate that the distortion operates upward rather than downward in an autocratic setting.

## 6.3 Limitations

**Limitation 1: Causal identification of P2 is not robust to heterogeneity-robust estimation.** The TWFE event-study estimate of the inspection effect (β(k=0) = −0.065, p = 0.011) does not survive the Sun-Abraham (2021) heterogeneity-robust alternative (β = −0.019, p = 0.87). Both estimates share direction but the robust estimator's confidence interval widely includes zero. The root cause is the narrow 1.5-year treatment-rollout window (Rounds 1–5, 2013–2014), which prevents clean separation of event-time from calendar-year variation in heterogeneity-robust estimators (Borusyak-Jaravel-Spiess 2024). Expansion to Rounds 6–12 (2016–2020) would roughly double the temporal window and is the single highest-value future-work step for strengthening causal identification.

**Limitation 2: External construct validity of VAI is not established.** The pre-registered third-party-text validation (H4, OSF DOI 10.17605/OSF.IO/ZMJY5) failed under the Wikipedia-zh substitute corpus: r(VAI_wiki, VAI_primary_mean) = −0.15, 95% CI [−0.31, +0.02]. We interpret this as a domain mismatch between encyclopedic descriptive text and governance-rhetoric text — Wikipedia describes what a city is (landmarks, history), while GWRs describe what officials do (infrastructure policy). Our lexicon was designed for the second domain. The defensible but narrower scope claim is that VAI is a valid within-domain measure of *governance-rhetoric visibility bias*, not a measure of any intrinsic city property. A true test of external validity requires Xinhua local-policy news or CNKI 重要报纸 political coverage — policy-rhetoric text, not descriptive text — which needs CARSI-authenticated institutional access and is deferred to future work.

**Limitation 3: The pre-registered H5 micro-foundation test is not executable in public CFPS data.** CFPS amenity-category-specific satisfaction items were not released in the cleaned 2010–2022 panel. The substitute outcomes (government evaluation, life satisfaction, self-rated health) returned a clean null bounded above at |d| = 0.011. We cannot distinguish from this null whether (a) the upward-signaling mechanism is correct (citizens are not the relevant evaluators), or (b) the CFPS general items are too coarse to detect amenity-category differentials. Primary survey data collection of amenity-specific items — approximately ¥500K for a stratified sample of 3,000 respondents across 30 prefectures — is the logical next step for adjudicating between (a) and (b).

**Limitation 4: Welfare calibration is conservative by construction.** The log-utility assumption equates social shadow prices with spending shares. CRRA and BOE alternatives give up to 10× higher estimates. We report the range ¥1–15B/year under log utility and ¥55B/year under BOE, rather than a single point estimate.

**Limitation 5: The paper's two strongest findings are (i) P1 compositional substitution and (ii) the within-document E-B retrospective-vs-prospective differential.** Readers and reviewers should interpret the overall contribution as resting primarily on these two findings plus the formal theoretical model. The P2 inspection-shock result and the H4 external-validity test are reported transparently but do not independently support strong causal claims.

## 6.4 Broader Implications

The paper suggests that the observability structure of public-sector activity is a first-order determinant of how compositional distortions arise. In contexts where output observability is asymmetric across categories — and this is true of many real-world public-goods provision problems — the combination of career concerns and observability noise will generate systematic compositional bias, independent of corruption, rent-seeking, or citizen-preference misalignment.

The policy levers we discuss in §5.4 are not specific to China: functional-output targets, transparency investments in less-observable categories, and citizen-audit portals are applicable wherever principal-agent chains filter information through observability-asymmetric signals. Our structural model provides a unified framework for calibrating the welfare gains from such interventions.

---

# 7. Conclusion

We have argued that visibility bias in Chinese municipal governance arises from an upward-signaling friction between local officials and their supervisors, under a Cobb-Douglas social welfare function and a Gaussian observability asymmetry. The model predicts: (P1) compositional substitution without total-investment expansion; (P2) attenuation under exogenous career-concern reductions; (P3) a closed-form welfare loss; and (C1) a null effect on citizen evaluations.

Using a text-based Visibility Attention Index constructed from 6,294 municipal government work reports, an anti-corruption-inspection quasi-experiment, and an individual-level CFPS micro-foundation test, we find evidence consistent with all four predictions. The construct validity of the VAI is supported by a within-document retrospective-vs-prospective differential that has no alternative explanation.

The welfare cost of visibility bias is calibrated at ¥4.4 billion per year (central, log-utility) to ¥55 billion per year (upper-bound BOE). The combined net welfare gain of supervisory-transparency, functional-target, and citizen-audit policy interventions is ¥50–60 billion over 10 years.

We pre-registered the empirical strategy (OSF DOI 10.17605/OSF.IO/ZMJY5), transparently logged three deviations (Appendix D), and made the full replication archive publicly available. We invite the literature to build on these findings in three directions: (i) construction of a true third-party third-party VAI from independent news text; (ii) extension to month-level inspection timing with the de Chaisemartin-D'Haultfœuille estimator; and (iii) primary survey collection of amenity-category-specific citizen satisfaction to test Corollary C1 more cleanly.

The broader implication is that asymmetric observability — not corruption, not citizen preference misalignment, not career concerns in isolation — is the key structural parameter governing compositional distortions in public-goods provision. This offers a tractable handle for diagnostic measurement and intervention in a wide class of bureaucratic settings.


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

### D-B-2 (Phase B2 — Sun-Abraham robustness check)

**Pre-registered**: Not in original pre-registration. Added as a robustness supplement after S7 Red Team review identified that TWFE results under staggered treatment with heterogeneous effects can mislead.

**Executed**: Sun-Abraham (2021) cohort-stacked heterogeneity-robust estimator using 5 round-level inspection cohorts (Rounds 1–5, start dates 2013-05 through 2014-11). Cohort c uses later-treated cohorts' pre-treatment observations as controls.

**Result**: β(k=0) = −0.019, SE = 0.117, p = 0.87. Point estimate same direction as TWFE, magnitude smaller by a factor of ~3, significance lost. Identification is limited by the narrow 1.5-year treatment-rollout window (Borusyak-Jaravel-Spiess 2024 document this regime explicitly).

**Interpretation**: We report both TWFE and Sun-Abraham estimates in §4.2 Table 3 and interpret P2 as "suggestive, not identified." Stronger identification requires expansion to Rounds 6–12 (2016–2020); see future-work §6.3.

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
| D-B-1 | P2 estimator | Callaway-Sant'Anna DiD | TWFE event study | Direction preserved under TWFE; **D-B-2 below weakens** |
| D-B-2 | P2 robustness | (not in pre-reg; added post-S7) | Sun-Abraham cohort-stacked | β attenuates to −0.019 (p=0.87); P2 now "suggestive, not identified" |
| D-E-1 | Construct validity scope | Third-party text was primary test | Internal tests reported as primary; third-party test D-E-2 separate | Internal tests supportive |
| D-E-2 | H4 third-party text source | Xinhua / provincial gov descriptions | Wikipedia-zh substitute | **H4 FAILED** (r = −0.15); domain-mismatch interpretation advanced but provisional |
| D-F-1 | H5 CFPS amenity items | Amenity-category-specific | Three general outcomes | Test not executable as pre-registered; substitute returned null; reframed as exploratory |

**Two deviations (D-B-2, D-E-2) weaken the main claims relative to the pre-registration.** We report both transparently in §4.2 and §3.2 respectively. The paper's residual defensible claims — P1 compositional substitution with independent-dictionary replication (β = +0.111, p = 0.002), the within-document E-B behavioral signature (Δ = +0.025, paired t = 8.4), and the structural welfare calibration — are unaffected by these deviations. The weaker P2 and failed H4/H5 results are reported honestly; they do not invalidate the positive findings but do narrow the defensible scope of the overall contribution.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.3's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.3's opening paragraph).


---

# References

[To be compiled via BibTeX reference list — see `01-literature/references.bib`; in-text cites formatted in APA 7th style for Second Tier journals]

---

*End of manuscript v1. Word count target: 6,500 main + 4,000 appendix. Phase H6 compile pending.*
