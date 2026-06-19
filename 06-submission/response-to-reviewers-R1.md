<!-- FIREWALL-OK: Stage-3 SUBMISSION revision response; venue/editor/reviewer references are legitimate at revision stage -->

# Response to the Editor and Reviewer

**Manuscript**: JCSO-D-26-00240 — *Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation* (revised title; was *Measuring Visibility Bias in Bureaucratic Text*)
**Journal**: Journal of Computational Social Science · **Decision**: Major Revisions (Editor-in-Chief: Takashi Kamihigashi; Reviewer #1)

Dear Professor Kamihigashi and Reviewer #1,

We thank you for an exceptionally constructive review. The central diagnosis — that the manuscript measured visible-infrastructure *rhetoric* more convincingly than strategic *visibility bias*, and overclaimed beyond its evidence — was correct, and it prompted us to **reconceive the paper as a study in the validation of dictionary text-as-data measures**, using visibility bias as the case. The revised paper makes four moves that, together, address every point raised:

1. **A rigorous passage-level validation** (human double-coding + a three-model LLM ensemble) that honestly maps what a visibility dictionary can and cannot measure — including a **polysemy precision ceiling** we did not previously recognize.
2. **A high-precision alternative** (LLM-ensemble classification) for users who need it.
3. **Behavioral (criterion) validity** — the decisive answer to the rhetoric-vs-strategy question: under a quasi-exogenous incentive shock, the *valid* text measure co-moves with *real* cosmetic investment, while the naive measure does not.
4. **Demotion** of the under-identified causal and welfare exercises, as you advised, and a narrowing of the paper to a single measurement-validation identity.

## A note on the author team

To meet the methodological bar the review implied, we strengthened the author team with two contributors whose work directly answers needs the review surfaced:

- **Liu Can** (co-first author; urban & rural planning) constructed and verified the visible-versus-functional classification behind the new procurement evidence (§4.3) — the domain judgment that a keyword scheme alone cannot supply.
- **Zhihui Li** independently double-coded the passage-validation sample, furnishing the **human intercoder agreement** the reviewer explicitly requested (Comment 3).

Authorship follows ICMJE criteria; per-author contributions are listed in the Statements and Declarations. We note that the LLM-ensemble classification central to the paper was also used, transparently, to *assist* the procurement-lexicon adjudication, which the domain-expert coauthor then signed off — a workflow consistent with the paper's own thesis about combining dictionaries, LLMs, and human validation.

We respond point by point below. Section numbers refer to the revised manuscript.

---

## Reviewer #1

### Comment 1 — Construct validity; distinguish the three claims; describe VAI as *rhetoric* unless stronger evidence

**Accepted, and answered with new evidence — this is the core of the revision.** Your three-claim ladder (VAI measures *language* → the language reflects *attention* → the attention reflects *strategic* response to incentives) is now addressed directly.

*What we changed.* (a) We give a **principled construct definition** (§1–§2): "visible" = **observability/salience to the evaluating audience** (superiors, inspectors, media, citizens), not surface appearance. The instructive boundary case is **metro/rail** — physically underground yet a daily-used, media-celebrated prestige achievement, hence maximally salient and coded *visible*. (b) We supply the **behavioral (criterion) validity** you asked for (§4). Using plausibly-exogenous, retirement-driven secretary turnover as an incentive shock, both real accounting-based cosmetic investment **and** the validated concrete text measure rise in the year after turnover, with clean pre-trends, whereas the **naive** measure does not move:

| outcome | turnover (t−1) | pre-trend (lead) | retirement-exogenous |
|---|---|---|---|
| real cosmetic investment (CIR) | +0.025 (p<0.001) | n.s. (clean) | +0.024 (p=0.04) |
| validated concrete text measure | +0.010 (p=0.01) | n.s. (clean) | +0.016 (p=0.01) |
| **naive** dictionary measure | +0.002 (**p=0.54**) | — | +0.004 (**p=0.39**) |

A genre/template artifact would not co-move with money under an exogenous shock; a strategic-attention measure does. We retain "visibility bias" as the construct but ground it **behaviorally**, and we are explicit (§3.6) that text alone identifies *what is emphasized*, with the strategic interpretation resting on the behavioral co-movement — exactly the cautious framing you requested.

### Comment 2 — Institutional premise: are work reports consequential?

**Accepted.** §3.1.0 is a new institutional-grounding subsection documenting that the GWR is **drafted** by the city government's research office, **revised** through leadership readings, and **adopted by vote** of the municipal People's Congress; that its commitments feed the **target-responsibility  cadre-evaluation** system; and that its audiences include the promotion-controlling superior, NPC delegates, and the public. We make **"visible to whom" explicit**: the salience criterion is defined relative to the *upward* principal, and the citizen channel is reported as a bounded null (§4.4) rather than asserted as the mechanism.

### Comment 3 — Validation weaker than advertised; provide passage-level validation (precision/recall/FP/FN/intercoder/ambiguous cases)

**Accepted; this drove the main new work (§3).** We relabel the earlier exercises for exactly what they establish — the alternative-dictionary correlation as **reliability** (not validity); the review-vs-plan differential as a **suggestive** pattern that may reflect genre; the MOHURD accounting correlation as a **modest external** check; and the Chinese-Wikipedia test plainly as a **failed external validation** (and we now state why preregistering it was a mis-step — a governance-rhetoric lexicon was never going to transfer to encyclopedic prose). We then add exactly the passage-level validation you specified — a stratified sentence sample, four-way coding (visible/functional/mixed/irrelevant), a full confusion matrix, per-class precision/recall, false-positive/negative exemplars, an error taxonomy, ambiguous cases, and **intercoder agreement** (Online Appendix C.8). The honest findings:

- **The naive dictionary fails**: human-coded visible-class precision is only **0.10**, driven by polysemous appearance/image terms (示范 alone accounts for 61 of 84 visible false positives; also 形象/展示/美丽).
- **A concrete, salience-based lexicon raises precision to 0.50→0.60 at 0.79 recall**, but meets a **polysemy ceiling (~0.60–0.64)**: residual metaphorical uses (道路 in "新型工业化道路"; 轨道交通 in "轨道交通产业") cannot be pruned without destroying recall.
- **For high precision we recommend LLM-ensemble classification** (three independent families): **0.84 accuracy, inter-model Fleiss κ = 0.835**.
- **Human intercoder agreement** (the second coder, Zhihui Li, on the identical 120-sentence locked set): **Cohen κ = 0.70** (substantial); residual disagreement concentrates on the visible-vs-mixed boundary — itself a manifestation of the polysemy we document.

### Comment 4 — Inspection event study, CFPS, and welfare calibration overextend the paper

**Accepted.** All three are demoted to supporting material and reported transparently (§4.4, Appendices C/D): the inspection event study is **definitively null** (the narrow-window TWFE sign reverses under Sun–Abraham with an extended sample — a staggered-treatment artifact); the CFPS test is a **bounded null** on substitute outcomes that do not measure the mechanism; and the welfare calibration is reported as **assumption-dependent with no headline figure**. The retirement-turnover design we *do* use (Comment 1) serves *measurement* (criterion) validity, not a welfare magnitude, and is methodologically distinct from the failed inspection design.

### Comment 5 — Narrow the contribution; fix Table 0 positioning; fix reproducibility

**Accepted.** The paper now has a **single identity** — a measurement-validation study — and Table 0 (§3.0) is recast to compare on *passage-level validation* and *behavioral validity* rather than implying prior text-as-data work is mere ideological scaling; we position the measure as a **domain-specific application within the expressed-agendas / political-attention tradition** (Grimmer; cross-domain priority classification; the dictionary-vs-LLM-annotation literature, now updated with recent work). The formal model, DiD, CFPS, and welfare calculation are moved to appendices, and the review-plan difference is presented as suggestive.

As a supplementary, large-scale construct check we add **procurement evidence** (Zhejiang public-bidding records, ~2.96M, classified by Liu Can's domain-verified scheme): visible-type construction projects outnumber functional ones **≈2:1** (visible exceeds functional in 97 of 108 localities). Going beyond counts, we recovered each project's **investment amount** from the tender briefs: visible and functional projects are of similar typical size (median ¥5.8M vs ¥4.7M), but the visible category owns the **high-value tail** (99th percentile ¥0.90B vs ¥0.20B; maximum ¥11.5B, the Hangzhou Metro Line 7 contract) — visible construction predominates on both frequency and big-ticket spend, directly addressing your concern that project counts are confounded by packaging. *[Pending: re-deposit and verify that all OSF/Zenodo/GitHub links resolve — we acknowledge the reviewer could not access them and are correcting this before the editorial check.]*

---

## Summary of changes

| Reviewer point | Resolution | Section |
|---|---|---|
| C1 construct validity | salience-based definition + **behavioral criterion validity** (valid measure co-moves with real investment under an exogenous shock; naive does not) | §1, §2, §4 |
| C2 institutional premise | new institutional-grounding subsection; "visible to whom" = upward principal | §3.1.0 |
| C3 validation | passage-level human+LLM validation; precision ceiling; **human intercoder κ = 0.70** (second coder added); LLM high-precision route | §3, App. C.8 |
| C4 overextension | inspection/CFPS/welfare demoted; no welfare headline | §4.4, appendices |
| C5 narrowing / positioning / reproducibility | single measurement identity; Table 0 recast; procurement frequency **and amount**; links being re-deposited | §1, §3, §4.3 |

We believe the paper is now both narrower and substantially better-evidenced: it honestly delimits dictionary text measurement, offers a high-precision alternative, establishes the construct's reality in behavior, and adds large-scale procurement corroboration. We are grateful for guidance that materially improved the work.

Sincerely,
Hongyang Xi (corresponding author), on behalf of all authors — Hongyang Xi and Liu Can (co-first authors) and Zhihui Li
