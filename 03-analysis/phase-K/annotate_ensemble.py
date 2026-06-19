#!/usr/bin/env python3
"""annotate_ensemble.py — multi-model ENSEMBLE annotator for Phase G passage validation.

Three independent model families (Gemini 3.1 Pro / ChatGPT 5.5 / DeepSeek) — the
decorrelated panel from Pipeline 4.0 (cemetery lesson: avoid same-family blind spots).
NOTE: Claude-via-API is unavailable here (ANTHROPIC_API_KEY_DEAD in panel .env), so this
is a 3-family ensemble. Each model labels all sentences; we report majority vote,
inter-model agreement (Fleiss' kappa), and the dictionary's precision/recall vs the
ensemble majority.

This is a SILVER standard (LLM-as-annotator). It does NOT replace the human-coded subset
required for the reviewer's intercoder agreement — it scales + cross-checks it.

    python3 annotate_ensemble.py [passage_coding_sheet.csv]
    python3 compute_validation.py --sheet passage_coding_sheet_ensemble.csv --truth ensemble_majority
"""
import os, csv, re, json, sys, concurrent.futures
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/andy/Desktop/Research")
LABELS = ["visible", "functional", "mixed", "irrelevant"]

def load_env():
    p = ROOT / "_meta" / "scripts" / ".env"
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#") and "=" in ln:
            k, _, v = ln.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

# label -> (base_url env, key env, candidate model ids)
PANEL = [
    ("gemini", "GLOBALAI_BASE_URL", "GLOBALAI_API_KEY",
        ["gemini-3.1-pro-preview", "gemini-3-pro-preview", "gemini-2.5-pro"]),
    ("chatgpt", "VECTORENGINE_BASE_URL", "VECTORENGINE_API_KEY",
        ["gpt-5.5-2026-04-24", "gpt-5.5", "gpt-5.1-chat-2025-11-13"]),
    ("deepseek", "DEEPSEEK_BASE_URL", "DEEPSEEK_API_KEY",
        ["deepseek-chat", "deepseek-reasoner"]),
]

SYS = ("You are coding sentences from Chinese municipal government work reports for an "
       "infrastructure-language study. Assign EXACTLY ONE label per sentence:\n"
       "visible = observationally-salient infrastructure (roads, greening, lighting, facades, "
       "landscape, squares, appearance/image, showcase);\n"
       "functional = concealed/utility infrastructure (water/drainage/pipes, heating/gas, "
       "structural safety, flood control, accessibility);\n"
       "mixed = clearly both;\n"
       "irrelevant = not about physical infrastructure.\n"
       'Respond ONLY with a JSON object mapping id to label, e.g. {"S0001":"visible"}.')

def call(base_env, key_env, models, prompt):
    from openai import OpenAI
    key = os.environ.get(key_env)
    if not key:
        return None
    client = OpenAI(api_key=key, base_url=os.environ.get(base_env), timeout=120, max_retries=1)
    for m in models:
        for params in ({"max_completion_tokens": 2000}, {"max_tokens": 2000}, {}):
            try:
                r = client.chat.completions.create(
                    model=m, messages=[{"role": "system", "content": SYS},
                                       {"role": "user", "content": prompt}], **params)
                txt = r.choices[0].message.content or ""
                mt = re.search(r"\{.*\}", txt, re.S)
                if mt:
                    return json.loads(mt.group(0))
            except Exception as e:
                s = str(e)[:120]
                if any(t in s for t in ("max_tokens", "max_completion", "temperature", "Unsupported")):
                    continue
                break
    return None

def norm(x):
    x = (x or "").strip().lower()
    for L in LABELS:
        if x.startswith(L[:4]):
            return L
    return None

def fleiss(items):  # items: list of (l1,l2,l3) fully-rated
    N = len(items); n = 3
    if not N:
        return float("nan")
    p = {L: 0 for L in LABELS}
    Pi = []
    for it in items:
        c = Counter(it)
        Pi.append((sum(v * v for v in c.values()) - n) / (n * (n - 1)))
        for L in LABELS:
            p[L] += c.get(L, 0)
    Pbar = sum(Pi) / N
    pj = {L: p[L] / (N * n) for L in LABELS}
    Pe = sum(v * v for v in pj.values())
    return (Pbar - Pe) / (1 - Pe) if Pe < 1 else float("nan")

def main():
    load_env()
    sheet = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("passage_coding_sheet.csv")
    rows = list(csv.DictReader(open(sheet, encoding="utf-8-sig")))
    B = 25
    per_model = {name: {} for name, *_ in PANEL}
    nb = (len(rows) + B - 1) // B
    for i in range(0, len(rows), B):
        batch = rows[i:i + B]
        prompt = "\n".join(f'{r["sample_id"]}: {r["sentence"]}' for r in batch)
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
            futs = {ex.submit(call, b, k, ms, prompt): name for name, b, k, ms in PANEL}
            for f in concurrent.futures.as_completed(futs):
                name = futs[f]
                d = f.result() or {}
                per_model[name].update({k: norm(v) for k, v in d.items()})
        print(f"  batch {i//B+1}/{nb}: " + " ".join(f"{n}={sum(1 for r in batch if per_model[n].get(r['sample_id']))}" for n,*_ in PANEL))

    # assemble
    out = sheet.with_name(sheet.stem + "_ensemble.csv")
    cols = list(rows[0].keys()) + [n for n, *_ in PANEL] + ["ensemble_majority", "n_agree"]
    fully = []
    maj_dist = Counter()
    with out.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader()
        for r in rows:
            labs = [per_model[n].get(r["sample_id"]) for n, *_ in PANEL]
            for n, lab in zip([n for n, *_ in PANEL], labs):
                r[n] = lab or ""
            present = [l for l in labs if l]
            if len(present) == 3:
                fully.append(tuple(present))
            c = Counter(present)
            top, cnt = (c.most_common(1)[0] if c else ("", 0))
            r["ensemble_majority"] = top if cnt >= 2 else "tie"
            r["n_agree"] = cnt
            maj_dist[r["ensemble_majority"]] += 1
            w.writerow(r)
    print(f"\n[write] {out}")
    print(f"fully-rated (all 3): {len(fully)}/{len(rows)}")
    print(f"inter-model Fleiss kappa (3 raters): {fleiss(fully):.3f}")
    print(f"majority distribution: {dict(maj_dist)}")
    print(f"no-majority ('tie'): {maj_dist.get('tie',0)}")

if __name__ == "__main__":
    main()
