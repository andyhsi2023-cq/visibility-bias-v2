# Phase G Coding Manual — Visible / Functional / Mixed / Irrelevant

**Task**: read each sentence (from a Chinese municipal government work report) and assign **exactly one** label. Code the *sentence's content*, not the dictionary's guess. Coders work blind to the dictionary label and to each other.

## Labels

| Label | Definition | Decision cue |
|---|---|---|
| **visible** | Infrastructure salient to an outside observer without specialist access | roads, greening, lighting, façade/appearance, landscape, squares, image/"市容市貌", showcase/"亮点" |
| **functional** | Infrastructure whose quality is not externally legible without inspection/records | drainage/pipes/"管网", water/gas/heating, structural safety/"抗震", flood control/"排涝", accessibility/"无障碍" |
| **mixed** | Genuinely both in the same sentence, or a dual-purpose item | "改造老旧小区道路与地下管网" (roads + pipes) |
| **irrelevant** | Not about *physical* infrastructure at all | fiscal/personnel/Party-building/social-policy/slogans with no infrastructure referent |

## Decision rules (hard cases)

1. **Code the dominant infrastructure referent.** If a sentence is 80% about a visible item with a passing functional mention, code `visible` (reserve `mixed` for genuine balance).
2. **Greening / parks = visible**; **ecological/sewage treatment plants = functional** (process facilities, not streetscape).
3. **"老旧小区改造" (old-community renovation)** alone is ambiguous → `mixed` unless the sentence specifies visible (façade/painting) or functional (pipes/elevators) work.
4. **Negation / future aspiration** still counts by referent ("将加强排水" = functional).
5. **Metaphorical use** ("打造发展高地") with no physical referent = `irrelevant`.
6. **Numbers/targets without a category** ("完成投资10亿元") = `irrelevant` unless the category is named in the same sentence.

## Procedure
- Two coders label all rows independently in the `coder1` / `coder2` columns of `passage_coding_sheet.csv`.
- Disagreements are resolved in the `adjudicated` column (third pass or discussion).
- Record any genuinely ambiguous sentences in `notes` — these become the "ambiguous cases" exhibit the reviewer asked for.
- Run `compute_validation.py --truth adjudicated` for the final precision/recall/F1; `--coder2 coder2` for Cohen's κ.

## Pre-set success criteria (pre-registered)
- Per-class precision & recall for **visible** and **functional** ≥ **0.75** → instrument well-validated.
- 0.50–0.75 → report honestly + error taxonomy + soften claims.
- < 0.50 on a core class → disclose as a dictionary limitation (cautionary measurement note).
