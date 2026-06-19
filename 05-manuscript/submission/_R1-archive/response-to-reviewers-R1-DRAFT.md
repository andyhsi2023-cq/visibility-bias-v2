<!-- FIREWALL-OK: Stage-3 SUBMISSION revision response; venue/editor names are legitimately present at revision stage (Tier A unlocked per stage-gate §1) -->

# Response to Reviewers — DRAFT (v0)

**Manuscript**: JCSO-D-26-00240 — *Measuring Visibility Bias in Bureaucratic Text: A Validated Instrument with Evidence from Chinese Municipal Government Work Reports*
**Journal**: Journal of Computational Social Science
**Decision**: Major Revisions (EIC Takashi Kamihigashi; Reviewer #1)
**Revision due**: 2026-07-30
**Status of this draft**: skeleton for Andy review. `[TODO]` marks new results not yet produced. Source review: `06-submission/JCSO_review.pdf`.

---

## Overarching response (read first)

We are grateful for an unusually constructive report. The reviewer's central diagnosis — that the manuscript **more convincingly measures visible-infrastructure *rhetoric* than strategic *visibility bias*** — is correct, and we have restructured the paper around it. The revision makes four global moves:

1. **Reframe the contribution** from a causal claim about strategic bureaucratic incentives to a **validated measurement instrument + descriptive evidence** on visible-vs-functional infrastructure language. The strategic-bias interpretation is now presented as a *motivating hypothesis the data are consistent with but do not identify*, not as an established finding.
2. **Add the missing passage-level construct validation** the reviewer requested (random-sample human coding with precision/recall/intercoder agreement). This is the one substantive new analysis. [TODO: run per `03-analysis/phase-G-passage-validation-plan.md`]
3. **Demote the under-identified causal and welfare exercises** (CCDI inspection event study, CFPS microfoundations, welfare calibration) to a clearly-labeled online appendix as transparent failed/suggestive tests — not part of the main evidentiary structure.
4. **Fix all reproducibility materials** (OSF preregistration, code, lexicons, deviation log) so every link resolves, and **reposition** the contribution relative to the existing text-as-data literature.

We believe the result is a narrower but fully defensible paper whose claims are matched to its evidence.

---

## Reviewer #1

### Comment 1 — Construct validity (three claims must be distinguished)

> *VAI measures visible-vs-functional language (strong evidence); this language reflects bureaucratic attention (weaker); this attention reflects strategic response to observability and career incentives (insufficient). … describe VAI more cautiously as a measure of visible-infrastructure rhetoric unless stronger evidence is provided.*

**Response — accepted in full.** We now state the three-claim ladder explicitly in §3 and commit only to what the evidence supports. Throughout, VAI is defined as a measure of **visible-infrastructure rhetoric**; the bureaucratic-attention and strategic-observability interpretations are flagged as hypotheses, with the alternatives the reviewer names (genuine construction, central urban campaigns, fiscal capacity, report templates, genre conventions) discussed as live, non-excluded explanations.

**Changes**: §3 new subsection "What VAI does and does not measure"; abstract and §1 reworded to drop "visibility bias" as an established mechanism; §2 (model) reframed as a *motivating* framework, not a tested structural claim.

### Comment 2 — Institutional premise (are work reports consequential texts?)

> *The argument depends on government work reports being consequential. This is asserted more than demonstrated. Explain who drafts/reviews them, whether they enter cadre evaluation, whether provincial officials compare them, whether media/citizens use them; clarify visibility to whom.*

**Response — accepted.** We add an institutional grounding subsection (§3) documenting: the drafting/review chain (research office → leading group → People's Congress), the role of GWRs in the target-responsibility (目标责任制) cadre-evaluation system, and the audiences. We explicitly disambiguate **"visible to whom"** — our mechanism is *upward* (superior/inspector) legibility, not lateral citizen approval (a distinction we now make load-bearing; see Comment 4/CFPS). Where evidence for consequentiality is indirect, we say so.

**Changes**: §3 "Institutional role of municipal work reports" with citations; §2 narrows the model's audience to the supervisor.

### Comment 3 — Validation evidence is useful but weaker than advertised

> *Alternative-dictionary correlation is a reliability check, not construct validation. Review-vs-plan differential may be genre, not behavior. MOHURD accounting validation is the strongest check but modest. Failed Wikipedia validation should be stated plainly as failed. Provide independent passage-level validation: random sample coded visible/functional/mixed/irrelevant; report precision, recall, FP, FN, intercoder agreement, ambiguous cases.*

**Response — accepted; this drives the main new work.** We have reclassified each existing exercise by what it actually demonstrates:
- **Alternative-dictionary correlation** → relabeled a **reliability** check.
- **Review-vs-plan differential** → demoted to a **suggestive descriptive** pattern, with the genre-difference confound stated.
- **MOHURD accounting validation** → retained as the **strongest external anchor**, with the modest correlation reported honestly and no mechanism/direction claim attached. [TODO: state exact r]
- **Wikipedia** → now reported plainly as a **failed external validation**; we remove the post-hoc "wrong corpus" rationalization and discuss what the failure implies for scope.
- **NEW passage-level validation** → we draw a stratified random sample of 500 GWR sentences (pre-registered amendment to OSF ZMJY5; seed-fixed sampler), double-code them visible/functional/mixed/irrelevant, and report a full confusion matrix: precision, recall, F1 per class, false-positive/negative exemplars, an error taxonomy, and intercoder agreement (κ). An automated pilot over these 500 sentences already surfaced exactly the kind of false positive the reviewer asks us to report: a small set of polysemous visible terms — chiefly **示范** ("demonstration/model") — inflate the visible count in non-infrastructure contexts. We accordingly **refine the visible lexicon** (disambiguate/drop these terms), re-derive VAI, and re-validate; the final human-coded precision/recall populate the lead row of Table 1. [TODO: insert final precision/recall/κ after human double-coding]

**Changes**: §3.2 rewritten with passage-level validation (§3.2.0) as the primary check; new validation table; OSF amendment + coding manual + seed-fixed sampler/scorer added; visible lexicon refined for polysemy. [pending: human double-coding for final numbers]

### Comment 4 — Additional empirical exercises overextend the paper

> *Inspection event study does not support the theory (TWFE in predicted direction but disappears under heterogeneity-robust estimation, reverses on extended sample) → treat as a failed preregistered test. CFPS test uninformative (amenity-specific items unavailable; broad-outcome substitutes don't measure the mechanism). Welfare calibration should be removed or sharply demoted.*

**Response — accepted.** We independently reached the same conclusions and reported them transparently in our deviation log; we now act on them structurally.
- **CCDI inspection event study**: moved to the online appendix as a **transparently failed preregistered causal test**. We report TWFE (β(k=0)=−0.065, p=0.011) *and* the heterogeneity-robust estimate (Sun-Abraham β=−0.019, p=0.87), state that the 1.5-year rollout window precludes clean robust identification, and note the post-2015 secular dynamics our far-placebo revealed. It is no longer part of the main evidentiary structure. *(We considered rescuing identification with additional inspection rounds or an alternative shock; a feasibility review concluded no defensible identification is available within scope — see internal note 2026-06-18.)*
- **CFPS microfoundations**: moved to the appendix as an informative **null/upper-bound** on any citizen-approval channel, consistent with our (now explicit) supervisor-directed mechanism. We do not present the broad-outcome substitutes as a test of the amenity mechanism.
- **Welfare calibration**: **removed from the main text**; retained only as a brief, heavily-caveated appendix illustration with its assumptions foregrounded. No headline yuan figure in the main paper.

**Changes**: §4 (Applications) now leads with the descriptive P1 result; the welfare calibration is demoted to a brief §4.3 (no headline figure) with full detail in Online Appendix A/C.7; the event-study and CFPS nulls are condensed to §4.4 with full detail in Appendix D.

### Comment 5 — Narrow the contribution; fix positioning, reproducibility, and scope

> *Table 0 understates prior text-as-data work (Grimmer expressed agendas, agenda-setting, audience targeting, cross-domain classification) — frame VAI as a domain-specific application, not a categorical departure. None of the preregistration/replication links work. The paper tries to be too many things at once.*

**Response — accepted in full.**
- **Positioning**: Table 0 and §1 rewritten to place VAI as a **domain-specific measurement application** within the established text-as-data tradition (Grimmer & Stewart; expressed-agendas / political-attention / agenda-setting / audience-targeting / cross-domain classification), not a new paradigm.
- **Reproducibility (urgent)**: every OSF/preregistration/code/lexicon/deviation-log link has been re-deposited and verified to resolve; the revised manuscript points to a single working OSF component. [TODO: re-deposit + verify each URL — see `00-BEFORE-SUBMISSION-BLOCKERS`]
- **Scope discipline**: the paper is rebuilt around one identity — *define VAI clearly → establish the institutional importance of GWRs → validate the dictionary (human coding + accounting data) → present the review-plan difference as a suggestive descriptive pattern*. The formal model, failed causal tests, CFPS, and welfare calculation are now appendix/supporting material, not parallel main contributions.

---

## Summary of changes table [TODO: finalize once edits land]

| Reviewer point | Section(s) changed | Type |
|---|---|---|
| 1 construct validity | abstract, §1, §2, §3 | reframe |
| 2 institutional premise | §2, §3 | new text |
| 3 validation (passage-level) | §3 + new Table | **new analysis** |
| 4 demote causal/CFPS/welfare | §4, §5 → §7 | restructure |
| 5 positioning + links + scope | §1, Table 0, §6/§7, OSF | reframe + ops |

*Draft ends. Andy to review tone/strategy before any new results are slotted in.*
