# Outreach Log — 2026-04-14

Visibility Bias v2 — cold outreach to top-30 scholars. All sent via CQU alumni mail (26708155@alu.cqu.edu.cn).

## Status

| # | Recipient | Email | Time | Status | Subject |
|---|---|---|---|---|---|
| 1 | Junyan Jiang (NUS) | junyan.jiang@nus.edu.sg | 22:08 | ❌ **BOUNCED** (postmaster 22:09) | "Feedback request: a validated text-measurement instrument..." (correct) |
| 2 | Jennifer Pan (Stanford) | jp1@stanford.edu | 22:10 | ✅ Delivered | ⚠️ Subject shows as attachment filename "research_summary_1page" — bug in my JS subject-fill approach |
| 3 | Daniel Mattingly (Yale) | daniel.mattingly@yale.edu | 22:14 | ✅ Delivered | "Within-document behavioral signature..." (correct) |
| 4 | Yuhua Wang (Harvard) | yuhuawang@fas.harvard.edu | 22:18 | ✅ Delivered | "Construct validity for a governance-text measure..." (correct) |

## Issues and follow-up

### Email 1 bounce
- Likely causes: (a) address outdated; (b) NUS mail server rejects unknown-origin Chinese academic domain.
- **Action needed**: locate Jiang's current email. Try alternatives:
  - `junyanj1@nus.edu.sg` (NUS Political Science variant)
  - `junyanj@hku.hk` (old HKU affiliation)
  - Web search his NUS faculty page for the current listing.

### Email 2 subject error
- Root cause: I used JS `el.value = ...` to set the subject, which bypassed Coremail's input-event listener. Result: subject was reset to empty and Coremail defaulted to the attachment filename at send time.
- **Mitigation**: For emails 3 and 4, used `browser_type` (fill + triggers input events) — confirmed subject preserved through send.
- **Decision on Pan email**: User chose (b) no corrective action. Leave as-is; accept the cosmetic hit.

## Attachments
All four emails attached `research_summary_1page.pdf` (97.32 KB), generated 2026-04-14 via Chrome headless HTML→PDF pipeline.

## Next steps
1. Track responses over next 7–14 days
2. If no response from Pan/Mattingly/Wang by 2026-04-28, send a one-line bump
3. Resolve Jiang bounce via alternate address when identified
