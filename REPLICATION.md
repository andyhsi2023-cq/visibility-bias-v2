# Replication guide — *When Dictionaries Hit a Polysemy Ceiling* (JCSO-D-26-00240, R2)

This repository reproduces every headline number in the manuscript. It is **self-contained** except for two large/raw inputs noted under *Data access*. Pre-registration: OSF [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5). Archive: Zenodo [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978).

## Environment
Python 3.11+; `pip install pandas statsmodels matplotlib openai`. LLM steps (ensemble classification, lexicon adjudication) require API keys in `_meta/scripts/.env` (`DEEPSEEK_API_KEY`, `GLOBALAI_API_KEY`, `VECTORENGINE_API_KEY`) — **not** distributed; their *outputs* are included so all downstream numbers reproduce without keys.

## Claim → reproduce map

| Manuscript claim | Script | Input → Output |
|---|---|---|
| Naive dict visible precision **0.10** / ensemble 0.37; 示范 = 61/84 FPs (§3.2.1) | `03-analysis/phase-G/PILOT-FINDINGS.md`, `phase-K/score_anchor.py`, `annotate_ensemble.py` | anchor labels → confusion matrix |
| Concrete precision **0.50→0.60**, ceiling 0.60–0.64 (§3.3, Fig 1) | `phase-K/score_anchor.py anchor_human_labels.csv` | `anchor_human_labels.csv` + `anchor_key.csv` → per-class P/R |
| LLM ensemble **0.84**, Fleiss κ **0.835** (§3.4) | `phase-K/annotate_ensemble.py` | sentences → `passage_coding_sheet_ensemble.validation.json` |
| Human intercoder **κ = 0.70** (§3.3, App C.8) | `phase-K/score_anchor.py coder2_labels.csv li_labels.csv` | two coders, same 120 → κ |
| **Behavioral co-movement** CIR +0.025 / concrete +0.010 / naive +0.002 (§4.2, Fig 2) | `phase-J-criterion-validity/verify_comovement_master.py` | `02-data/processed/master_2002_2024.csv` → `verify_results_master.csv` |
| `wr_visibility` (concrete text series) construction | `phase-J-criterion-validity/build_workreport_text.py` | GWR corpus (P1) → text panel (already merged into master_2002_2024.csv) |
| Procurement **frequency** 2.0–2.1:1, 97/108 localities (§4.3, ESM-6) | `phase-L-bidding/classify_bidding.py` + `bidding_lexicon.py` (v2) | `ggzy.db` (P1) → `by_city.csv`, `results_summary.json` |
| Procurement **amount** median ¥5.8M vs ¥4.7M; P99 4.45×; max ¥11.5B (§4.3) | `phase-L-bidding/repull_amounts.py` → re-classify | `amounts_2023_2024.csv` → `amounts_final.csv`, `amount_summary.json` |
| Lexicon adjudication (DeepSeek-4.0 + domain-expert sign-off) | `phase-L-bidding/deepseek_adjudicate.py`, `liucan_review.html` | → `lexicon_adjudication_deepseek.csv` |
| Main figures | `04-figures/make_main_figures.py`, `phase-L-bidding/make_figure.py` | → `fig1_precision_ladder`, `fig2_comovement`, `fig_bidding_by_city` |
| Demoted (appendices): inspection / Wikipedia / CFPS / welfare | `phase-B,B2,E,E2,F`, `welfare-sensitivity.py` | reported as failed/assumption-dependent |
| Manuscript build | `05-manuscript/sections/*.md` → `manuscript_compiled_R2.md` | concatenation |

## Data access (the two inputs not redistributed in full)
- **GWR corpus** (6,294 municipal government work reports, 2002–2024): scraped from public provincial portals + zhengfugongzuobaogao.com; full text on local store `/Volumes/P1/城市研究/工作报告汇总/`. The **derived** city-year series (`vai_composite`, `wr_visibility`, CIR, turnover) needed for §4 are included in `02-data/processed/master_2002_2024.csv`.
- **Zhejiang procurement DB** `ggzy.db` (~2.5 GB SQLite, 2,957,789 records): collected from the national `ggzy.gov.cn` aggregator + provincial `inteligentsearch` API (crawler + rate-limit notes in the dataset's own README); too large for Zenodo. The **derived** per-locality counts (`by_city.csv`) and project amounts (`amounts_final.csv`) are included; raw DB available on request or rebuildable via the crawler / a commercial feed (剑鱼/千里马/比地).
- Public secondary sources: MOHURD Urban Construction Statistical Yearbook (2005–2015); CFPS (PKU ISSS); CCDI inspection rounds.

## Archive status (R2, 2026-06-19)
- **Zenodo**: v2 published, **Open access** (CC-BY-4.0). Concept DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978) resolves to the latest version (v2 = 10.5281/zenodo.20762481).
- **GitHub mirror**: live and public at [github.com/andyhsi2023-cq/visibility-bias-v2](https://github.com/andyhsi2023-cq/visibility-bias-v2).
- The concrete visible/functional lexicon is the authors' own construction (validated by the passage coding, §3.3), mirroring the cosmetic-vs-functional split of the MOHURD construction-investment categories (§3.7).
