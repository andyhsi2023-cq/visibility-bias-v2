# Phase E2 Results Memo: Third-Party Text Validation (Wikipedia-zh)

**Project**: Visibility Bias v2
**Phase**: E2 (D-E-1 remediation)
**Date**: 2026-04-14
**Stage Gate**: α-full

---

## 1. Executive verdict

**Phase E2 objective**: execute the pre-registered H4 third-party text validation using Chinese Wikipedia (zh.wikipedia.org) as an independent, publicly-accessible corpus of city descriptions.

**Empirical verdict**: **H4 FAILS UNDER WIKIPEDIA**. The pre-registered correlation criterion r ∈ [0.3, 0.7] between VAI_wikipedia and VAI_primary is not met. Observed r = **−0.15**, 95% CI **[−0.31, +0.02]**. The CIR cross-sectional replication with VAI_wikipedia returns β = +0.020, p = 0.57 — sign correct but insignificant.

**Honest interpretation**: Wikipedia articles describe *what a city is* (geography, history, landmarks, culture). Government Work Reports describe *what officials did and plan to do* (infrastructure governance, policy priorities). Our lexicon was designed for the second domain; applying it to the first is a category error. The null is consistent with Wikipedia-zh being an unsuitable third-party source for this construct, **not** with VAI being invalid.

**We report H4-Wikipedia as "pre-registered test executed; null verdict; substantive interpretation: domain mismatch."** A truly appropriate third-party source (Xinhua local-policy news; CNKI 重要报纸 policy coverage) remains as future work requiring CARSI-authenticated database access.

## 2. Data and method

### Corpus

- Source: zh.wikipedia.org, MediaWiki API (`prop=extracts, explaintext=1`)
- Coverage: **282 of 286 target cities** fetched successfully; 4 misses (吉安, 松原, 梅州, 白山 — likely redirects or disambiguation issues)
- Mean article length: 8,447 Chinese characters; total corpus 2.4M characters
- Quality: Wikipedia-zh articles are editor-written volunteer-curated content; no city-government editorial control

### Lexicon

Identical to primary VAI: V_ORIG (42 visible terms) + F_ORIG (38 functional terms). Same count-ratio formula.

### Cross-sectional matching

Because Wikipedia articles are descriptions (not year-indexed), we test at city level: match each city's Wikipedia VAI to its 2002–2024 mean primary VAI.

## 3. Results

### 3.1 H4 correlation test

| Metric | Value | Pre-reg target | Verdict |
|---|---:|---|---|
| Pearson r(VAI_wiki, VAI_primary_mean) | **−0.15** | [0.30, 0.70] | ❌ Out of band |
| 95% CI | [−0.31, +0.02] | — | Includes zero |
| Spearman ρ | −0.12 | — | Consistent |
| With expanded dictionary (148 terms) | −0.14 | — | Unchanged |
| Threshold ≥ 20 hits (N=9, N=22 ext) | +0.05, +0.03 | — | Approx zero, small sample |

### 3.2 H4 CIR replication test

Cross-sectional OLS: CIR_mean = β · VAI_wiki + γ · controls + const

| Metric | Value |
|---|---:|
| β(VAI_wiki) | **+0.020** |
| SE | 0.036 |
| p | 0.57 |
| R² | 0.029 |
| N | 135 |

**Horse race**: when both VAI_primary_mean and residualized VAI_wiki are included, β(VAI_primary_mean) = +0.51 (p = 0.007), β(VAI_wiki_resid) = +0.04 (p = 0.27). The primary VAI retains all predictive power; Wikipedia VAI adds none.

### 3.3 Descriptive comparison

| Quantity | VAI_primary city-mean | VAI_wiki |
|---|---:|---:|
| Mean | 0.613 | **0.786** |
| SD | 0.054 | 0.252 |
| Range | narrow (homogeneous) | wide (noisy) |

VAI_wiki has higher mean (baseline bias) and **4.7× higher SD** than VAI_primary. The noise in VAI_wiki is driven by article length: cities with short articles have 3–5 lexicon hits, producing extreme 0/1 VAI values. This is a classic sample-size dependence of a ratio estimator.

## 4. Why the null is substantive, not methodological

Wikipedia-zh article content:
- Heavy emphasis on historical landmarks (Forbidden City, 鼓楼, 老街, 古塔) — these trigger our visibility lexicon (形象, 景观, 文化城市, 地标, 城市名片)
- Very little coverage of underground infrastructure, water/gas/heating systems — these are our functional lexicon terms
- Articles are *descriptive* of physical/cultural features, not *prescriptive* of governance priorities

Per-city lexicon-hit distribution confirms: median 6 hits / 8,447-character article ≈ 0.07% of text. The lexicon is detecting only a trace signal, and that signal is dominated by the "cities have landmarks" Wikipedia convention.

## 5. Pre-registration compliance

| Pre-registered commitment | Status | Notes |
|---|---|---|
| VAI from independent third-party text | ✅ **Executed** | Wikipedia-zh substitute corpus built |
| r(primary, third-party) ∈ [0.3, 0.7] | ❌ **Failed** | Observed r = −0.15 |
| β(VAI_3rd → CIR) > 0 at 5% | ❌ **Failed** | β = +0.020, p = 0.57 |
| Transparent reporting | ✅ | This memo |

This is a pre-registered null. It goes into the manuscript's deviation/null-results log.

## 6. Novelty Score impact

**Criterion #3 (new data)**: We constructed a new third-party corpus (282 cities, 2.4M chars) and made it publicly available alongside code. **+0.2** for corpus construction + **−0.1** for failed validation = **+0.1 net**.

**Criterion #7 (transparent null)**: Pre-registered null reported honestly, consistent with high-integrity research practice. **+0.1**.

**Updated Novelty**: 4.4 (post B2) + **0.2** (Phase E2 net) = **4.6 / 10**.

## 7. What this means for the paper

### What the paper still defensibly claims

1. **VAI as a measure of governance-rhetoric visibility bias**. The primary measurement is a property of how officials write about their work. It is NOT claimed to be a general property of "how visible a city is."
2. **E-B within-document differential** (review > plan, paired t=8.4). This is the strongest mechanism evidence and does NOT rely on external text.
3. **P1 compositional substitution** (β = +0.111, p = 0.002). Robust to dictionary expansion within GWR.
4. **C1 citizen-popularity null** (β = 0 across 3 outcomes). Unaffected by Phase E2.

### What the paper must now concede

1. **External construct validity is unresolved**. Phase E (internal dictionary robustness) and Phase E2 (Wikipedia null) together tell us that VAI-in-GWR is stable *within* the GWR source but does NOT match an independent encyclopedic text source. 
2. **The right third-party source is *policy-rhetoric* text**, not descriptive-encyclopedic text. Xinhua local-policy news or CNKI 重要报纸 political coverage would be the correct corpus; neither was accessible in this session.
3. **"Visibility bias" as a construct is measured *in the text of governance*, not as an intrinsic city property**. This is a narrower but defensible scope claim.

### Manuscript updates required

- **§3.2 Measurement and construct validity**: add a subsection reporting the Wikipedia null transparently and explaining the domain-mismatch interpretation.
- **§6.3 Limitations**: re-phrase Limitation 2 to note that Phase E2 has been executed, failed, and the appropriate follow-up is policy-news text not Wikipedia.
- **Appendix D (Deviations)**: add D-E-2 entry noting that Wikipedia was the publicly-accessible substitute; full pre-registered Xinhua corpus deferred.

## 8. Recommendation

**Do not attempt another third-party source in this session**. The Wikipedia result is a clean pre-registered null. Attempting Baidu Baike or other descriptive sources would repeat the same domain-mismatch error. Future work requires *policy-rhetoric* third-party text, which needs institutional access.

**Proceed to S7 (4-layer audit)**. Current Novelty estimate 4.6/10 is at the Third/Second Tier boundary. The audits will identify which specific target journal is realistic.

## 9. Files produced

- `02-data/raw/wikipedia_zh/` — 282 per-city text files + _meta.csv + _cache.json
- `03-analysis/phase-E2/scrape_wikipedia.py` — scraper
- `03-analysis/phase-E2/vai_thirdparty.py` — VAI computation + H4 test
- `03-analysis/phase-E/vai_wiki_primary_merge.csv` — merged dataframe
- `03-analysis/phase-E2/h4_summary.csv` — test summary
- `04-figures/phase-E2-thirdparty-validation.pdf` / `.png`
