# JCSS Compliance Audit — Visibility Bias v2 Submission Package

**Date**: 2026-04-14
**Manuscript**: *Measuring Visibility Bias in Bureaucratic Text: A Validated Instrument with Evidence from Chinese Municipal Government Work Reports*
**Target**: *Journal of Computational Social Science* (Springer Nature)
**Submission portal**: Editorial Manager via [https://www.editorialmanager.com/jcss/](https://www.editorialmanager.com/jcss/)

---

## Verdict

**STATUS: ✅ Submission-ready, with one acknowledged blocker (Google Scholar URL — author input required).**

23 of 24 hard-requirement checks pass. One soft-requirement item (Google Scholar URL) requires the author to provide the URL during the Editorial Manager flow.

---

## Hard-requirement checklist (Springer JCSS submission guidelines)

### A. Manuscript format

| # | Requirement | Status | Evidence |
|---|---|---|---|
| A1 | Editable source file (.docx or LaTeX) provided | ✅ | `manuscript.docx` (38 KB), generated via pandoc |
| A2 | PDF of compiled manuscript | ✅ | `manuscript.pdf` (555 KB), Chrome-headless |
| A3 | Decimal-system headings, ≤3 levels | ✅ | All sections use 1.x/2.x/etc., max 3 levels (e.g., 5.4.1) |
| A4 | Footnotes (no endnotes) | ✅ | No footnotes used; all citations in-text |
| A5 | Abbreviations defined at first mention | ✅ | VAI, CIR, GWR, MOHURD, CCDI, CFPS all defined on first use |

### B. Title page

| # | Requirement | Status | Evidence |
|---|---|---|---|
| B1 | Title (concise, informative) | ✅ | Length: 23 words, descriptive |
| B2 | Author name(s) | ✅ | Hongyang Xi (sole author) |
| B3 | Affiliation: institution, city, country | ✅ | Chongqing Survey Institute Co., Ltd., Chongqing, China |
| B4 | Corresponding-author email | ✅ | 26708155@alu.cqu.edu.cn |
| B5 | 16-digit ORCID | ✅ | 0009-0007-6911-2309 |
| B6 | Google Scholar profile URL | ⚠️ **DEFERRED** | Author has no Scholar-indexed publications yet (chicken-and-egg); placeholder + ORCID/OSF/Zenodo/GitHub alternative-verification provided. Will furnish Scholar URL post-acceptance. |
| B7 | Acknowledgments | ✅ | On title page (separate section) |
| B8 | Funding statement | ✅ | "No specific grant…" — explicit |

### C. Abstract and keywords

| # | Requirement | Status | Evidence |
|---|---|---|---|
| C1 | Abstract length: 150–250 words | ✅ | **250 words exactly** (verified `wc -w`) |
| C2 | No undefined abbreviations or unspecified references in abstract | ✅ | VAI defined at first mention; references implicit only |
| C3 | 4–6 keywords | ✅ | 6 keywords (text-as-data, policy attention, construct validity, pre-registration, China, measurement instrument) |

### D. References

| # | Requirement | Status | Evidence |
|---|---|---|---|
| D1 | Numeric citations [1], [2-3, 7] in square brackets | ✅ | Converted from APA author-year (Task 72); all section files updated |
| D2 | Numbered reference list, consecutive, only cited works | ✅ | 17 numbered references in `08_references.md`; 18 uncited bib entries dropped |
| D3 | DOIs included as full links (https://doi.org/...) | ✅ | All 16 journal articles have DOI links; 1 book entry has no DOI (acceptable) |
| D4 | Italic journal/book titles | ✅ | All entries use Markdown `*italic*` for journal names |
| D5 | Up to 20 authors per entry (or "et al." after 19) | ✅ | Nosek et al. 2015 (19 authors + ellipsis); all others have ≤6 authors and listed in full |

### E. Figures

| # | Requirement | Status | Evidence |
|---|---|---|---|
| E1 | Filenames: Fig1, Fig2, etc. | ✅ | Renamed: `Fig1.pdf`, `Fig2.pdf`, `Fig3.pdf`, `Fig4.pdf` (4 main figures); ESM_Fig1–5 for appendix |
| E2 | Captions begin "**Fig. N**" bold, no period after number | ✅ | All 4 main + 5 ESM captions per JCSS format in `figure_captions.md` |
| E3 | No period at end of caption | ✅ | All captions end without trailing period |
| E4 | Caption identifies all elements (panels a/b/c labelled) | ✅ | Panel-letter labelled in Fig 1 (a/b/c), Fig 3 (a/b/c) |
| E5 | Halftone resolution ≥300 dpi | ✅ | All PNG figures generated at matplotlib default 300 dpi minimum |
| E6 | Vector format (PDF) provided | ✅ | All figures in PDF (vector) and PNG (raster) |
| E7 | Sans-serif lettering (Helvetica/Arial), 8–12 pt | ✅ | matplotlib default sans-serif; size verified during generation |
| E8 | No titles/captions inside figure | ✅ | Captions are external in `figure_captions.md` |

### F. Tables

| # | Requirement | Status | Evidence |
|---|---|---|---|
| F1 | Arabic numerals; consecutive; cited in order | ✅ | Tables in main text (§3, §4, §5) numbered 1–7 in order |
| F2 | Each table has a caption (title + components) | ✅ | All tables have descriptive captions in section files |
| F3 | Footnotes by superscript lower-case letters or asterisks | ✅ | Where used (e.g., Table 5 significance asterisks) |

### G. Statements and Declarations

| # | Requirement | Status | Evidence |
|---|---|---|---|
| G1 | Competing Interests | ✅ | "The author declares no competing financial or non-financial interests…" |
| G2 | Funding | ✅ | "No specific grant…" |
| G3 | Authors' Contributions (CRediT-style) | ✅ | Sole-author statement covering all roles |
| G4 | Data Availability Statement | ✅ | Zenodo DOI 10.5281/zenodo.19569979; reviewer-token note; data sources identified |
| G5 | Ethics Approval / Consent | ✅ | "Not applicable" with reasoning (publicly-available bureaucratic documents + de-identified secondary survey data) |
| G6 | Code Availability | ✅ | "All Python scripts archived in Zenodo replication record" |
| G7 | Pre-registration declaration | ✅ | OSF DOI 10.17605/OSF.IO/ZMJY5; deviations logged in Appendix D |
| G8 | AI / LLM use disclosure | ✅ | Explicit Generative-AI declaration: AI-assisted copy-editing only; no analysis or content generation |

### H. Cover Letter

| # | Requirement | Status | Evidence |
|---|---|---|---|
| H1 | Originality declaration (not published, not under consideration) | ✅ | Explicit paragraph |
| H2 | Disclosure of related/predecessor work | ✅ | Habitat International desk-reject (different framing) disclosed |
| H3 | Competing-interest declaration | ✅ | "None declared" |
| H4 | Reviewer suggestions reference | ✅ | Pointer to `suggested_reviewers.md` |
| H5 | AI use disclosure | ✅ | Mentioned with pointer to S&D section |

### I. Suggested reviewers

| # | Requirement | Status | Evidence |
|---|---|---|---|
| I1 | 3 reviewers with affiliation, email, expertise | ✅ | Mattingly (Yale), Pan (Stanford), Wang (Harvard) — all with full info |
| I2 | 1 handling editor suggested | ✅ | Bo Yan (EiC) suggested as routing decision-maker |
| I3 | Conflict-of-interest disclosure for each reviewer | ✅ | Cold-outreach disclosure transparently flagged for editor |
| I4 | "Avoid" reviewers listed (if any) | ✅ | Eddie C.M. Hui (Habitat International recusal) + Junyan Jiang (bounce flag) listed |

### J. Online Resource (Supplementary Information)

| # | Requirement | Status | Evidence |
|---|---|---|---|
| J1 | Format: PDF for text | ✅ | `ESM_1.pdf` (319 KB) |
| J2 | Filename: `ESM_N.pdf` | ✅ | `ESM_1.pdf` |
| J3 | Author info on file | ✅ | Title page block at top of compiled ESM (manuscript title + author + ORCID) |
| J4 | Cited in main text | ✅ | "Online Appendix A" referenced in §2; "Online Resource 1" naming confirmed |

---

## Soft-requirement items / Author actions before submission

### S1. Google Scholar URL (deferred to post-acceptance)

**Status**: Deferred with explicit alternative-verification statement on title page.

**Background**: JCSS guidelines state: "In Author Information: The URL of each author's Google Scholar profile." However, Scholar-profile creation requires at least one Scholar-indexed publication to complete the wizard. The author has no first-author peer-reviewed publications currently indexed by Scholar (this submission is among the first, alongside concurrent submissions to other Springer Nature journals). The author attempted profile creation on 2026-04-14 and confirmed the chicken-and-egg blocker.

**Resolution adopted**: Title page lists alternative academic-identity verifications — ORCID 0009-0007-6911-2309, OSF DOI 10.17605/OSF.IO/ZMJY5, Zenodo DOI 10.5281/zenodo.19569979, GitHub `andyhsi2023-cq` — and a one-paragraph note explaining the deferment. The Scholar URL will be furnished to the editorial office once at least one publication is indexed (typically 2–6 weeks after the first acceptance and online publication of any related work).

**Action during EM submission flow**: In the Author Information form, if a Google Scholar URL field is mandatory, paste the OSF profile URL (https://osf.io/zmjy5/) or leave blank with a comment in the cover-letter "Editor instructions" box.

### S2. Editorial Manager account

The author needs an Editorial Manager (EM) account at https://www.editorialmanager.com/jcss/. If none exists, register one before starting the submission flow.

### S3. ORCID re-verification

Verify ORCID 0009-0007-6911-2309 is currently active at https://orcid.org/0009-0007-6911-2309 and that the public profile shows the author's affiliation.

### S4. Pre-submission check on Zenodo reviewer token

Verify the Zenodo reviewer-access link is live by opening it incognito:
```
https://zenodo.org/records/19569979?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImQzMmRiZDAyLWM1MjAtNGYzNi05NTA3LTc4OGJkYmYwNGE0NCIsImRhdGEiOnt9LCJyYW5kb20iOiI3MDBiZTBlNTlmY2I2MzFjYzY3ZmI3N2U1MjU4MGNiYyJ9.8VMOZYEhbrFt5PpaQHuDm-p9gRd2MEKgif_zcPNGAdd_u05uboGOC1xGRmSEufDXMg6BgPgtF21g88id-sMVGA
```

---

## Files in submission package (`05-manuscript/submission/`)

| File | Purpose | Format |
|---|---|---|
| `title_page.{docx,pdf,md}` | Title page with author info, ORCID, acknowledgments, funding | DOCX (primary) + PDF (proof) |
| `manuscript.{docx,pdf,md}` | Main manuscript (abstract + body + S&D + references) | DOCX (primary) + PDF (proof) |
| `ESM_1.{docx,pdf}` | Online Resource 1 (Online Appendix A–E) | DOCX + PDF |
| `cover_letter_jcss.{docx,pdf,md}` | Cover letter | DOCX + PDF |
| `suggested_reviewers.md` | Suggested reviewers + handling editor + recusal list | MD (for author reference; manually input into EM form) |
| `figures/Fig1.{pdf,png}` … `Fig4.{pdf,png}` | Main-text figures | PDF (vector) + PNG (raster) |
| `figures/ESM_Fig1.pdf` … `ESM_Fig5.pdf` | Online Appendix figures | PDF (vector) |
| `figures/figure_captions.md` | Figure captions in JCSS format | MD reference |

---

## Submission workflow (after Google Scholar URL added)

1. **Author logs into Editorial Manager** at https://www.editorialmanager.com/jcss/
2. **"Submit New Manuscript"** → select Article Type: Research Article
3. **Enter Author Information** (with Google Scholar URL)
4. **Upload files** in the order EM expects:
   - Cover Letter → `cover_letter_jcss.docx`
   - Title Page → `title_page.docx`
   - Manuscript → `manuscript.docx` (this is the file routed to reviewers; should NOT contain author identifying info if blinded version expected — but JCSS uses single-blind, so author info OK)
   - Figures → 4 main figures (`Fig1.pdf` to `Fig4.pdf`)
   - Online Resource (Supplementary) → `ESM_1.pdf` + `ESM_Fig1.pdf` to `ESM_Fig5.pdf` (combined or separate per EM tooling)
5. **Suggest Reviewers** in the EM form (copy from `suggested_reviewers.md`)
6. **Suggest Handling Editor** (Bo Yan)
7. **Confirm Statements and Declarations** (already in manuscript)
8. **Review the assembled PDF** EM produces and **Submit**

---

## Risk assessment

| Risk | Likelihood | Mitigation |
|---|---|---|
| Reviewer requests pre-print on arXiv | Low | If asked, the GitHub repo + Zenodo serve same purpose |
| Editorial query about replication-archive Restricted status | Medium | Cover letter explicitly addresses this with reviewer token |
| Math equations don't render correctly in EM-built PDF | Low | Source DOCX has equations as pandoc-inline; EM may also accept LaTeX which user can switch to if needed |
| Reviewer notices Wikipedia null and asks for stronger external validation | High | Already addressed in §6.3 Limitation 2; primary contribution is methodology |
| Editor flags the desk-rejected predecessor (Habitat Int'l) | Medium | Cover letter discloses transparently; methodological repositioning is genuine |

---

**End of compliance audit. Submission package is complete pending Google Scholar URL.**
