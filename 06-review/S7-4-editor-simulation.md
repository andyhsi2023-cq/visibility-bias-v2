# S7-4 Editor Simulation — Visibility Bias v2

**Manuscript**: Visibility Bias in Chinese Urban Governance: Model, Measurement, Identification
**Author**: Hongyang Xi (Chongqing Survey Institute, sole author, single institution)
**Date**: 2026-04-14
**Prior audits**: S7-2 Novelty 3.5/10 (Third Tier); S7-3 Red Team P0 blockers open (Phase E2 hidden null, Phase B2 buried attenuation)
**Lab context**: 7 desk rejects in last 30 days; HabInt rejected predecessor 2026-04-13 on "lack of sufficient novelty"

---

## 1. Regional Science and Urban Economics (RSUE)

- **Editor's first-glance reaction**: A sole-authored China-only text-analysis paper from a non-top-30 institution, with a quantitative abstract that leads on ¥4.4B welfare calibration (¥1–15B range — a 15× band). The editor checks the OSF pre-registration (zmjy5) because the abstract flags three deviations; they find Phase E2 was executed as a Wikipedia validation test and returned r = −0.15 — a failed pre-registered test not reported in the abstract or the main validity paragraph. The event-study p-value (0.011) is presented as headline, but a footnote-level concession that robustness alternatives attenuate it is enough for RSUE referees to immediately request Sun-Abraham; the editor will preempt this by desk-rejecting. Identification-sensitive editor sees P1 as a within-city correlation without exogenous variation.
- **Desk-reject probability**: **82%**
- **If desk-rejected, why**: "The identification strategy rests on a within-city correlation (P1) and a two-cohort event study (P2) whose significance does not survive heterogeneity-robust estimation; this does not meet RSUE's causal-inference standard."
- **If sent to review, likely referee verdict**: **Reject** (the Phase E2 OSF discrepancy is discoverable; a hostile referee flags pre-registration integrity).
- **Fit score**: 1 / 5

---

## 2. Journal of Housing Economics (JHE)

- **Editor's first-glance reaction**: The paper is not really about housing — it is about municipal infrastructure composition (greening, drainage, lighting). JHE's core scope is housing markets, tenure, prices, credit, and residential construction. The CIR is a municipal-renewal ratio, not a housing variable. Even a sympathetic editor finds this paper mis-scoped on first screen. Methodological quality is secondary because the topic is outside the journal's remit.
- **Desk-reject probability**: **88%**
- **If desk-rejected, why**: "The paper's subject matter — compositional bias in municipal infrastructure spending — falls outside JHE's scope of residential housing economics."
- **If sent to review, likely referee verdict**: **Reject** on scope, independent of methodology.
- **Fit score**: 1 / 5

---

## 3. China Economic Review (CER)

- **Editor's first-glance reaction**: The China-context framing is a natural fit — CER has published prior text-analysis papers on Chinese policy corpora and is tolerant of China-only identification. The 6,294-GWR corpus and 2013–2014 CCDI inspection design read as legitimate contributions. The editor is more tolerant of the two-cohort limitation but still expects honest reporting of Sun-Abraham. The Phase E2 Wikipedia null, if disclosed, is livable at CER because cross-domain measurement validation is secondary to within-corpus specification robustness. The biggest remaining risk: sole author, single non-top-30 institution, and a welfare calibration that overreaches (¥50–60B NPV) for a paper whose causal identification is acknowledged as suggestive. If the P0 Red Team fixes are made (E2 disclosed, B/B2 side-by-side, welfare downsized, C1 reframed), this is a genuine fit.
- **Desk-reject probability**: **48% as-is; 28% after P0 + P1 fixes**
- **If desk-rejected, why (as-is)**: "Overreach between the identification strength reported and the welfare claims drawn; the event-study's robustness to modern staggered-DID estimators is not transparently established."
- **If sent to review, likely referee verdict**: **Major revision** (salvageable via honest reporting, multiple-testing correction, and stripping the ¥50–60B policy NPV).
- **Fit score**: 4 / 5

---

## 4. Cities (Elsevier)

- **Editor's first-glance reaction**: Cities editors are broad and policy-oriented; the "visibility bias" narrative and the MOHURD-based CIR story read well at first glance. However, Cities has become more novelty-sensitive after its 2024–2025 flood of China urban-policy submissions, and the predecessor manuscript was rejected at a sister-title (Habitat International, same Elsevier family, Eddie Hui editor) on 2026-04-13 *for novelty*. Cities and HabInt share editorial philosophy and partially overlap in reviewer pools. A Cities editor may recognize the manuscript lineage from the OSF pre-registration or the abstract phrasing. Submitting here eleven days after a family-journal reject on novelty is a structural red flag.
- **Desk-reject probability**: **62%** (elevated by the HabInt family-reject contagion risk and the sole-author/single-institution structural weakness)
- **If desk-rejected, why**: "The paper's core contribution overlaps substantially with work previously considered within the Elsevier urban-studies portfolio; Cities seeks greater conceptual or methodological advance over the existing literature."
- **If sent to review, likely referee verdict**: **Major revision** with moderate probability of subsequent reject; Cities reviewers often pile on when novelty is borderline.
- **Fit score**: 2 / 5

---

## 5. Journal of Comparative Economics (JCE)

- **Editor's first-glance reaction**: JCE is institutional and cross-country. A single-country (China-only) paper needs to argue strong comparative relevance up front. The manuscript's §6.4 Broader Implications paragraph asserts global relevance without a single non-China data point — a JCE editor sees this as exactly the kind of claim their reviewers will demolish. The identification concerns (Sun-Abraham attenuation, two-cohort limitation) are disqualifying at JCE's current methodological bar. Sole author, non-top-30 institution compounds the skepticism.
- **Desk-reject probability**: **78%**
- **If desk-rejected, why**: "The paper's analysis is confined to a single institutional setting and does not provide the comparative identification or cross-country evidence that the journal's scope requires."
- **If sent to review, likely referee verdict**: **Reject** on identification + scope.
- **Fit score**: 1 / 5

---

## Synthesis

### Primary target

**China Economic Review (CER)**, *conditional on executing P0 + P1 fixes from S7-3 Red Team*.

Reasoning: CER is the only venue among the five where (a) the China-only scope is a feature, not a bug; (b) the text-analysis approach has precedent in accepted papers; (c) the editor persona tolerates institutional detail and is less hostile to the two-cohort event-study limitation; (d) the sole-author single-institution structure is survivable. The S7-2 novelty audit (3.5/10) places this manuscript in the Third Tier, and CER sits at the Third-to-Second Tier boundary — the correct calibration per SOP §2 Stage 4 "no追高" rule. After P0 + P1 fixes, projected desk-reject drops from 48% to ~28%.

### Fallback (if CER desk-rejects)

**Journal of Chinese Economic and Business Studies (JCEBS)** or **Journal of Asian Economics** — both are Third Tier, China/Asia-scoped, and accept text-analysis methodology. *Cities* is **not** a safe fallback because of the Habitat International family-reject contagion (11 days prior, same Elsevier portfolio, same novelty grounds).

### Absolute do-not-submit list (desk-reject probability > 60%)

- **RSUE** (82%) — identification failure will be caught immediately
- **JHE** (88%) — scope mismatch
- **JCE** (78%) — single-country + identification failure
- **Cities** (62%) — HabInt family-reject contagion; sister-journal novelty grounds still in effect

### Required fixes before ANY submission (priority order)

**P0 — Hard blockers (ethical/integrity risk):**
1. Integrate Phase E2 Wikipedia null (r = −0.15) into §3.2 validity section and Abstract. Correct Appendix D D-E-1 to state that Phase E2 was *executed* and *failed*, not "deferred." (~4.5 hours)
2. Report TWFE β = −0.065 and Sun-Abraham β = −0.019 side-by-side in §4.2 Table 3 (main text), not in Limitations. Rewrite §4.2 conclusion to "suggestive, not decisively identified." (~3 hours)

**P1 — High priority (desk-reject risk):**
3. Drop Corollary C1 "null affirms theory" framing. Reframe CFPS as exploratory supplementary analysis with formal MDE / TOST at d = 0.05 and d = 0.10. (~6 hours)
4. Multiple-testing correction (Romano-Wolf or Bonferroni) across P1/P2/C1/E-B. Add corrected p-values to Table 6. (~2 hours)
5. Two-way or province-clustered SE on the event study (province-assigned treatment). (~3 hours)

**P2 — Medium priority:**
6. Strip welfare calibration to a single sensitivity figure; remove the ¥50–60B 10-year NPV claim. (~6 hours)
7. Cut §6.4 Broader Implications or restrict to one sentence. (~1 hour)
8. Archive the 24-permutation specification list on OSF with timestamp; cite exact node in §4.1. (~2 hours)

**P3 — Nice to have:**
9. Rewrite abstract to lead with P1 + within-document E-B differential; demote P2 and C1. (~2 hours)

### Timeline to submission

- **P0 + P1**: ~18 focused hours → **3 working days**
- **P2**: additional ~9 hours → **2 more days**
- **Re-run novelty-audit and red-team abbreviated pass after revisions**: ~1 day
- **Cover letter + submission packaging for CER**: ~1 day
- **Total: ~7 working days (8–10 calendar days)** → realistic submission window **2026-04-23 to 2026-04-25**

Do **not** compress below this. The rejection-log pattern (7 in 30 days) is itself evidence that compressed submission cycles produce desk rejects; the SOP minimum cooling window is 4 weeks, and a further-compressed turnaround on an already-flagged manuscript is exactly the failure mode the SOP was written to prevent.

### Go / no-go decision

**GO-AFTER-REVISION** — conditional on all P0 blockers closed, at least 4 of 5 P1 items closed, and a re-run novelty audit confirming the manuscript is honestly positioned at 3.5–4.0/10 (Third Tier). Target **China Economic Review**.

**Absolute NO-GO** for any of the following paths, which would produce desk reject #8:
- Submission to RSUE, JHE, JCE, or Cities in any form.
- Submission to CER without P0 fixes.
- Submission within the next 72 hours (insufficient time to close P0 honestly).

**Reasoning for GO-AFTER-REVISION rather than NO-GO**: the manuscript contains two genuinely defensible findings (P1 compositional substitution; E-B within-document differential) that survive adversarial scrutiny. These justify publication at a Third Tier venue once the overreach is trimmed and the failed pre-registered tests are transparently disclosed. Killing the project entirely would discard real empirical value; pushing it to RSUE would produce the 8th desk reject and trigger SOP pattern analysis.

---

### Calibration check against lab history

The lab's 7 recent desk rejects share a common pattern: submissions to journals approximately **one tier above** the manuscript's honest novelty score. This simulation prices the manuscript at **3.5/10 → Third Tier**, and recommends a Third-to-Second-Tier boundary venue (CER) rather than the author's self-declared target (RSUE/JHE/CER). Submitting to RSUE/JHE would repeat the exact failure mode documented in the rejection log. CER is the *in-tier* submission that breaks the pattern.

---

*End of S7-4 Editor Simulation. Word count: ~1,580.*
