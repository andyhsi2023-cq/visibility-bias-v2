<!-- FIREWALL-OK: Stage-3 SUBMISSION revision response; venue/editor/reviewer references are legitimate at revision stage -->

# Response to the Editor and Reviewer

**Manuscript**: JCSO-D-26-00240 — *Visibility Bias in Chinese Municipal Government Work Reports: Measurement and Behavioral Validation* (revised subtitle; the instrument and structure are unchanged from the reviewed version)
**Journal**: Journal of Computational Social Science · **Decision**: Major Revisions (Editor-in-Chief: Takashi Kamihigashi; Reviewer #1)

Dear Professor Kamihigashi and Reviewer #1,

We thank you for an exceptionally constructive review. Your central diagnosis was correct: the manuscript measured visible-infrastructure *rhetoric* more convincingly than strategic *visibility bias*, and overclaimed beyond its evidence. We have kept the Visibility Attention Index (VAI) as the paper's instrument and kept the paper's structure, and used your comments to substantially strengthen the validation and narrow the claims along four lines:

1. **Direct passage-level validation** (human double-coding plus a three-model LLM ensemble) that honestly maps what the visibility dictionary can and cannot measure, including a **polysemy precision ceiling** we had not previously recognized (§3.2.0).
2. **A high-precision alternative** (LLM-ensemble classification) where the dictionary ceiling binds (§3.2.0).
3. **Behavioral (criterion) validity**, which answers the rhetoric-vs-strategy question: under a quasi-exogenous incentive shock, the *valid* concrete measure co-moves with *real* cosmetic investment while the naive measure does not (§3.2.7).
4. **Demotion** of the under-identified causal and welfare exercises, with the claims narrowed to what the evidence supports (§4.4–§4.5).

The paper a reviewer reads is the same paper. It now carries much stronger validation.

## A note on the author team

We strengthened the author team with two contributors whose work directly answers needs the review surfaced:

- **Liu Can** (co-first author; urban & rural planning) constructed and verified the visible-versus-functional classification behind the new procurement evidence (§4.3); domain judgment a keyword scheme alone cannot supply.
- **Zhihui Li** independently double-coded the passage-validation sample, furnishing the **human intercoder agreement** the reviewer requested (Comment 3).

Authorship follows ICMJE criteria; contributions are in the Statements and Declarations. The LLM ensemble was also used, transparently, to *assist* the procurement-lexicon adjudication, which the domain-expert coauthor then signed off, a workflow consistent with the paper's own thesis about combining dictionaries, LLMs, and human validation. Section numbers below refer to the revised manuscript.

---

## Reviewer #1

### Comment 1 — Construct validity; distinguish the three claims; describe VAI as *rhetoric* unless stronger evidence

**Accepted, and answered with new evidence — the core of the revision.** Your three-claim ladder (VAI measures *language* → the language reflects *attention* → the attention reflects *strategic* response to incentives) is addressed directly. (a) We give a **principled construct definition** (§2, §3.1.1): "visible" = **observability/salience to the evaluating superior**, not surface appearance; the instructive boundary case is **metro/rail**: physically underground yet a daily-used, media-celebrated prestige achievement, hence maximally salient and coded *visible*. (b) We add the **behavioral (criterion) validity** you asked for (§3.2.7): using plausibly-exogenous, retirement-driven secretary turnover as an incentive shock, real cosmetic investment **and** the validated concrete measure both rise in the year after turnover with clean pre-trends, whereas the **naive** measure does not move:

| outcome | turnover (t−1) | pre-trend (lead) | retirement-exogenous |
|---|---|---|---|
| real cosmetic investment (CIR) | +0.025 (p<0.001) | n.s. (clean) | +0.024 (p=0.04) |
| validated concrete measure | +0.010 (p=0.01) | n.s. (clean) | +0.016 (p=0.01) |
| **naive** measure | +0.002 (**p=0.54**) | — | +0.004 (**p=0.39**) |

A genre/template artifact would not co-move with money under an exogenous shock; a strategic-attention measure does. We retain "visibility bias" as the construct but ground it **behaviorally**, and are explicit (§3.2.7) that text alone identifies *what is emphasized*, with the strategic interpretation resting on this co-movement, the cautious framing you requested.

### Comment 2 — Institutional premise: are work reports consequential?

**Accepted.** §3.1.0 is a new institutional-grounding subsection: the GWR is **drafted** by the city government's research office, **revised** through leadership readings, and **adopted by vote** of the municipal People's Congress; its commitments feed the **target-responsibility cadre-evaluation** system; its audiences include the promotion-controlling superior, NPC delegates, and the public. We make **"visible to whom" explicit**: the salience criterion is defined relative to the *upward* principal, and report the citizen channel as a bounded null (§4.5), not the asserted mechanism.

### Comment 3 — Validation weaker than advertised; provide passage-level validation (precision/recall/FP/FN/intercoder/ambiguous cases)

**Accepted; this drove the main new work (§3.2).** We relabel the earlier checks for exactly what they establish: the alternative-dictionary correlation as **reliability** not validity (E-A, §3.2.1); the review-vs-plan differential as **suggestive**, possibly genre (E-B, §3.2.2/§4.2); the MOHURD accounting correlation as a **modest external** check (E-D, §3.2.4); and the Chinese-Wikipedia test plainly as a **failed external validation** (E-F, §3.2.5). We then add exactly the passage-level validation you specified (§3.2.0, Online Appendix C.8): a stratified sentence sample, four-way coding, a full confusion matrix, per-class precision/recall, false-positive/negative exemplars, an error taxonomy, and **intercoder agreement**. The honest findings:

- **The naive dictionary fails**: human-coded visible-class precision is only **0.10**, driven by polysemous appearance words (示范 *shìfàn* "model" alone accounts for **60–61 of 84** visible false positives; also 形象, 展示, 美丽).
- **A concrete, salience-based lexicon reaches 0.50→0.60 at 0.79 recall**, but meets a **polysemy ceiling (~0.60–0.64)**: residual metaphorical uses (道路 *dàolù* in 新型工业化道路; 轨道交通 in 轨道交通产业) cannot be pruned without destroying recall.
- **For high precision we recommend LLM-ensemble classification** (three independent families): **0.84 accuracy, inter-model Fleiss κ = 0.835**.
- **Human intercoder agreement** (the second coder, Zhihui Li, on the identical 120-sentence locked set): **Cohen κ = 0.70** (substantial); residual disagreement concentrates on the visible-vs-mixed boundary, itself a manifestation of the polysemy we document.

### Comment 4 — Inspection event study, CFPS, and welfare calibration overextend the paper

**Accepted.** All three are demoted and reported transparently (§4.4–§4.5, Appendices C/D): the inspection event study is **definitively null** (the narrow-window TWFE sign reverses under Sun–Abraham with an extended sample — a staggered-treatment artifact); the CFPS test is a **bounded null** on substitute outcomes that do not measure the mechanism; the welfare calibration is **assumption-dependent with no headline figure**. The retirement-turnover design we *do* use (Comment 1) serves *measurement* (criterion) validity, not a welfare magnitude, and is methodologically distinct from the failed inspection design.

### Comment 5 — Narrow the contribution; fix Table 0 positioning; fix reproducibility

**Accepted.** We narrow the contribution to **the validated instrument and its honest limits** (not causal or welfare claims), and recast Table 0 (§3.0) to compare on *passage-level validation* and *behavioral validity* rather than implying prior text-as-data work is mere ideological scaling; we position VAI as a **domain-specific application within the expressed-agendas / political-attention tradition** [2, 18, 19], updated with the recent dictionary-vs-LLM-annotation literature [5, 20, 21]. The formal model, specification curve, CFPS, and welfare calculation are in appendices.

As a supplementary, large-scale construct check we add **procurement evidence** (§4.3; Zhejiang public-bidding records, ≈2.96M, classified by the domain-verified scheme): visible-type projects outnumber functional ones **≈2:1** (in 97 of 108 localities). Going beyond counts, we recover each project's **investment amount**: visible and functional projects are of similar typical size (median ¥5.8M vs ¥4.7M), but the visible category owns the **high-value tail** (99th percentile ¥0.90B vs ¥0.20B; maximum ¥11.5B, the Hangzhou Metro Line 7 contract), addressing your concern that project counts are confounded by packaging.

On **reproducibility**: we have re-deposited and verified that all links resolve. The replication archive is now **open access** on Zenodo (concept DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978), always resolving to the latest version) and the GitHub mirror is live and public (`andyhsi2023-cq/visibility-bias-v2`). We apologize that the reviewer could not access the original record and have corrected it.

---

## Summary of changes

| Reviewer point | Resolution | Section |
|---|---|---|
| C1 construct validity | salience-based definition + **behavioral criterion validity** (valid measure co-moves with real investment under an exogenous shock; naive does not) | §2, §3.1.1, §3.2.7 |
| C2 institutional premise | new institutional-grounding subsection; "visible to whom" = upward principal | §3.1.0 |
| C3 validation | passage-level human+LLM validation; precision ceiling; **human intercoder κ = 0.70** (second coder added); LLM high-precision route | §3.2.0, App. C.8 |
| C4 overextension | inspection/CFPS/welfare demoted; no welfare headline | §4.4–§4.5, appendices |
| C5 narrowing / positioning / reproducibility | narrowed to the validated instrument; Table 0 recast; procurement frequency **and amount**; links re-deposited (Zenodo open; GitHub live) | §3.0, §4.3 |

The paper is now narrower and substantially better-evidenced: it honestly delimits the dictionary, offers a high-precision LLM alternative, establishes the construct's reality in behavior, and adds large-scale procurement corroboration, all on the structure you reviewed. We are grateful for guidance that materially improved the work.

Sincerely,
Hongyang Xi (corresponding author), on behalf of all authors — Hongyang Xi and Liu Can (co-first authors) and Zhihui Li
