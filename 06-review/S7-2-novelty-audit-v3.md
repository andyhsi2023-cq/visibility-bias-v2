# S7-2 Novelty Audit — v3 (Methodology Repositioning)

**Auditor**: novelty-audit (adversarial)
**Date**: 2026-04-14
**Manuscript**: `/Users/andy/Desktop/Research/visibility-bias-v2/05-manuscript/manuscript_v3_compiled.md`
**Standard applied**: Political-methodology (Political Analysis / R&P / JCSS), NOT economics.

---

## Score Summary (under political-methodology standards)

| # | Criterion | Score | Justification |
|---|---|---:|---|
| 1 | New empirical fact | 0.6 | Within-document review-vs-plan differential (Δ = +0.025, t = 8.4) is a genuinely new measurement-level fact about how Chinese GWRs are written. P1 compositional substitution in accounting data is descriptively new (β = +0.111). The CFPS null and the inspection null are also "facts" but they cut against the original story. Net: a real but modest empirical contribution; the differential is the strongest piece. |
| 2 | New theoretical insight | 0.3 | The cadre-attention model is competent but derivative (Holmström career concerns + Li-Zhou + Barro's fiscal illusion). Now explicitly demoted to "motivation for the measurement." For a methods journal this is fine — theory does not need to be original — but it carries no extra credit either. |
| 3 | New data | 0.7 | 6,294 GWRs across 282 prefectures, 2002–2024, is a substantial purpose-built corpus. Public release on Zenodo + GitHub with reviewer token is exactly what PA/JCSS values. Not unprecedented (multiple Chinese GWR corpora exist in CSSCI work) but the lexicons + section-split + replication-archive-as-template package is genuinely useful for the field. |
| 4 | **New measurement / method** (most important) | **1.4 / 1.5** | This is the paper's raison d'être and the score is correspondingly generous. The package — (i) expert-coded bilingual lexicon, (ii) five-test construct-validity battery, (iii) novel within-document review-vs-plan behavioral signature, (iv) pre-registration template, (v) explicit deviation log, (vi) transparent null reporting — is a serious methodological contribution by political-methodology standards. The within-document Δ test is the standout: it is a clean, theory-derived, falsifiable validation move that does not exist in the text-as-data literature in this form (Grimmer-Stewart 2013 review, Gentzkow-Kelly-Taddy 2019, Ash-Hansen 2023 review do not feature anything quite like it). The Cronbach-Meehl framing in §1 + §3.2 is appropriate for PA. |
| 5 | Clean identification | 0.2 | Causal identification is now openly conceded as "not achieved" (§6.3 Limitation 1). For a methods paper this is acceptable but not zero — the construct-validity protocol substitutes for identification, and the within-document test partials out city-level confounders mechanically. P2 inspection event study is a pre-registered null. CFPS micro-foundation is a pre-registered null. So credit is for what survives: the within-document test is "identified" in a measurement-validity sense. Partial credit. |
| 6 | Generalisable framework | 0.8 | §6.4 portability discussion to EU NRPs / Indian state budgets / Mexican municipal Plans de Desarrollo is concrete and credible. The construction protocol is genuinely general; the within-document differential test transfers to any document with retrospective-prospective structure (which is almost all annual government reports globally). This is a real strength under PA/JCSS standards, where "template paper" status is highly valued. |
| 7 | **Clean falsification** (extra weight in PA) | **1.0 / 1.0** | This is where v3 actually shines. Two pre-registered nulls (P2 inspection, CFPS C1), explicit Δ-sign-reversal disclosure, deviation log in Appendix D, OSF pre-registration archived BEFORE re-analysis. The honest reporting of the −0.065 → +0.016 sign flip under Sun-Abraham 9-cohort is exactly the kind of behavior PA's editorial board has publicly endorsed (Nyhan 2015; Christensen et al. 2019 cited). For a methods journal, this is worth full marks. Track 1 paid off here. |
| 8 | Robust to reasonable alternatives | 0.5 | Specification-curve (24/24 positive on P1), three horse races, IV with VAI_lag1, alternative split markers all pass. But: the E-F Wikipedia null, the E-C bootstrap r = 0.18 instability of half-lexicons, the E-A r = 0.93 over-shoot (suggesting same-source lexical contamination not independence), and the 9.7% drop of low-count documents collectively bound this. A hostile referee will note that the cross-source MOHURD correlation is only r = 0.24 — modest. |
| 9 | Policy or scientific impact | 0.4 | §6.5 policy levers (¥50–60B over 10 years) are clearly labeled as conditional-on-model. PA does not weight policy heavily; the relevant "impact" here is methodological adoption potential, which §6.4 portability addresses. ¥1–15B/yr welfare calibration is honest about its log-utility assumption. |
| 10 | Writing & clarity | 0.5 | The repositioning is clean and visible from §1.1 onward. Abstract leads with measurement contribution. Tables are clear. The 9,500-word length is over PA's 10,500 limit margin (acceptable) and under R&P's 4,000 limit (would need 60% cut for R&P). Minor: §2 still feels heavier than a methods paper warrants — could be compressed by half. |
| **TOTAL** | | **6.4 / 10** | Upper-second-tier methods paper |

---

## Tier under methodology standards

| Journal | Fit assessment | Realistic verdict |
|---|---|---|
| **Political Analysis** (Top Field methods) | Methodologically substantive, pre-registration + null reporting strong, but: single-country application, expert-coded lexicon (PA increasingly favors model-based / LLM-augmented approaches), cross-source r = 0.24 modest, cadre-attention model derivative. PA expects either (i) genuinely novel estimator with formal properties, OR (ii) general-purpose tool with multi-country demonstration. v3 has neither. | **Stretch but not crazy**. Desk-reject probability ~55–65%. If past desk → R&R probability ~30%. |
| **Research & Politics** (Second Tier, short-format) | Excellent fit *if cut to 4,000 words*. Behavioral-signature test + null reporting + replication archive are R&P bread and butter. R&P explicitly welcomes methods-and-measurement short pieces. Length cut is the only real obstacle. | **Strong fit**. Desk-reject probability ~15–20%; R&R probability ~50–60%. |
| **Journal of Computational Social Science** (Springer, Second Tier methods/CSS) | Very good fit. JCSS values text-as-data + reproducibility + corpus release. China focus is a positive (JCSS publishes a lot of Chinese-text work). Length is fine. | **Strong fit**. Desk-reject probability ~15–25%; R&R probability ~50–60%. |
| Journal of Chinese Political Science | Good substantive fit but methodology contribution would be undersold; JCPS is more substantive than methodological. Would likely accept but is a downgrade from JCSS/R&P given the methodology framing. | Safe fallback. ~70% acceptance probability. |

---

## Comparison to v2 (economics framing)

- **v2 score (economics standards)**: 3.5 / 10 → Third Tier (e.g. Habitat International, Cities) — and even there, desk-rejected by Habitat International on novelty grounds (Eddie HUI, 2026-04-13).
- **v3 score (methodology standards)**: 6.4 / 10 → Upper-Second-Tier methods.
- **Net delta**: +2.9 points. The repositioning is real, not cosmetic. Three forces drive the gain:
  1. Criterion 4 weighting: methods paper gets full credit for the construct-validity protocol that economics treated as a sideshow.
  2. Criterion 7 weighting: the Track-1 honest null reporting is worth ~1.0 in PA and ~0.3 in economics.
  3. Criterion 5 relaxation: methods papers do not need clean causal identification; the within-document Δ test substitutes effectively.

---

## Recommendation

**Primary target**: **Journal of Computational Social Science (JCSS)**.
- Best ratio of fit-to-acceptance-probability.
- Length is non-binding.
- Editorial board values text-as-data + reproducibility + China-corpus work.
- Estimated outcomes: desk-reject ~20%, R&R ~55%, eventual accept ~40%.

**Fallback (parallel-prep, sequential submit)**: **Research & Politics**.
- Requires cutting from 9,500 → 4,000 words: drop §2 to one paragraph, drop §5.3 welfare calibration entirely, drop §6.5 policy levers, condense §3 lexicon detail to appendix.
- After cut, R&P fit is very strong.
- Estimated outcomes: desk-reject ~18%, R&R ~55%, eventual accept ~40%.

**Stretch (only if PI override + co-author from top-30 institution)**: **Political Analysis**.
- Per `_meta/research-sop.md` Hard Rule: Top Field requires top-30 affiliation. Sole author from Chongqing Survey Institute does not clear this gate without override.
- Even with override, acceptance probability ~10–12%. Not recommended.

**Bottom safety**: Journal of Chinese Political Science. Only if both JCSS and R&P reject.

### Desk-reject probabilities (consolidated)
| Journal | Desk-reject | Pass-to-review | Eventual accept |
|---|---:|---:|---:|
| Political Analysis | 60% | 40% | 8–12% |
| JCSS | 20% | 80% | 35–45% |
| R&P (after cut) | 18% | 82% | 35–45% |
| JCPS | 15% | 85% | 50–65% |

### Required fixes before submission

**For JCSS (primary path)**:
1. **Cut §2 by 50%**: keep environment + equilibrium + propositions; move derivations entirely to appendix. JCSS readers do not need a full Holmström-style derivation.
2. **Reframe abstract first sentence**: lead with "We introduce VAI, a validated text-based instrument…" — currently does this, good — but explicitly add the word "computational" or "text-as-data" to hit JCSS keyword filters.
3. **Add comparison table to existing text-as-data instruments** (Slapin-Proksch wordfish, Grimmer expressed-agenda, Gentzkow-Shapiro partisan phrases). Without this, referees will ask "why do we need another lexicon-based measure?"
4. **Resolve E-A r = 0.93 over-shoot**: hostile referees will read this as same-source contamination, not independence. Either reframe pre-registered criterion (the [0.3, 0.7] band was arbitrary) or add a *truly* independent lexicon test (e.g. LLM-generated lexicon).
5. **Strengthen E-D r = 0.24 framing**: r = 0.24 is a modest correlation across sources. Either show that it is at the upper end of cross-source measurement correlations in similar text-vs-accounting literature, or concede that VAI captures additional variance accounting cannot.
6. **Add one-paragraph "what this means for non-China researchers"** at end of §6.4 — JCSS reviewers will want to see the international relevance hammered.
7. **Resolve E-F null framing**: current §3.2.6 (3) language ("Wikipedia is the wrong third-party source") will be read as ad hoc. Pre-commit to a stronger statement: "VAI is a measure of *governance rhetoric*, full stop; encyclopedic text is out of scope by construction." This is more defensible than the current half-retreat.
8. **Replication archive**: ensure Zenodo DOI is minted (currently "pending") and reviewer token is in cover letter. Without this, JCSS will desk-reject.
9. **Cover letter**: lead with the within-document E-B differential as "to our knowledge first behavioral-signature validation in text-as-data." This is the paper's strongest single claim and must be the first sentence editors see.

**For R&P (fallback)**: above + cut to 4,000 words.

---

## Critical weaknesses remaining

1. **The construct-validity battery has one genuine failure (E-F) and one over-shoot (E-A r = 0.93)**. Adversarial reading: 2/5 tests are problematic, not "4/5 pass." The E-A over-shoot is more damaging than the v3 manuscript admits — r = 0.93 with a "different" lexicon when 36/78 visible terms and 32/70 functional terms are conceptually overlapping families is *not* independence; it is the same construct measured twice with overlapping operationalization. A hostile referee at PA will spot this in 30 seconds.

2. **The within-document Δ test, while novel, is theoretically under-determined** (§5.2.2 admits this). Three alternative explanations are listed; the paper does not adjudicate among them. PA referees will ask for at least one disambiguating test (e.g. heterogeneity by leader career stage, or by economic cycle). Without it, the test is a measurement-level fact rather than a mechanism test.

3. **The cross-source correlation r = 0.24 is genuinely modest**. By comparison, Gentzkow-Shapiro 2010 partisan-phrase validation against external benchmarks reports r = 0.6–0.8. r = 0.24 means VAI and CIR share only ~6% of variance. This is honest but it limits the strength of the substantive claim.

4. **Single-country, single-document-type application limits Criterion 6 score**. Methodology papers in PA increasingly demonstrate the instrument across at least two settings (e.g. cross-country comparison). v3 only promises this for future work.

5. **The deviation log (Appendix D) is a double-edged sword**. PA editors will appreciate the transparency but referees will count the deviations: 5 logged deviations from pre-registration is on the high end. The defensive framing matters.

6. **Author affiliation risk**: Sole author from a non-top-30 institution submitting to PA triggers the SOP Hard Rule. This alone justifies dropping PA from the target list unless PI overrides.

7. **The cadre-attention model adds risk without commensurate reward in a methods paper**. A hostile referee may suggest dropping it entirely and reframing the paper as "Validated Lexicon for Compositional Policy Attention in Bureaucratic Text" — pure measurement, no theory. This would push the score from 6.4 → 6.6 by removing Criterion 5 vulnerability, but would lose the welfare-calibration application. Worth considering for the R&P short-format version.

---

## Bottom line

v3 is a real and substantial improvement over v2. The methodology repositioning is honest, not cosmetic. Score moves from 3.5 → 6.4 under appropriate (PA/JCSS) standards. The paper now belongs in the upper-second-tier methods conversation. Submit to **JCSS first, R&P second**. Do not chase Political Analysis without a top-30 co-author and PI override.
