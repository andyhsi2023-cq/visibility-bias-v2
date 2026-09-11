#!/usr/bin/env python3
"""annotate_pilot.py — LLM-as-annotator PILOT for Phase G passage validation.

NOT a substitute for human coding. Produces a provisional second-annotator column
(coder_llm) so we can estimate the dictionary's precision/recall BEFORE investing in
human double-coding (de-risks the Plan-A bet). Uses DeepSeek via _meta/scripts/.env.

    python3 annotate_pilot.py [passage_coding_sheet.csv]
then: python3 compute_validation.py --sheet passage_coding_sheet_pilot.csv --truth coder_llm
"""
import os, csv, json, re, sys
from pathlib import Path

ROOT = Path("/Users/andy/Desktop/Research")

def load_env():
    p = ROOT / "_meta" / "scripts" / ".env"
    if p.exists():
        for ln in p.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, _, v = ln.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

SYS = ("You are coding sentences from Chinese municipal government work reports for an "
       "infrastructure-language study. Assign EXACTLY ONE label per sentence:\n"
       "visible = observationally-salient infrastructure (roads, greening, lighting, facades, "
       "landscape, squares, appearance/image, showcase);\n"
       "functional = concealed/utility infrastructure (water/drainage/pipes, heating/gas, "
       "structural safety, flood control, accessibility);\n"
       "mixed = clearly both;\n"
       "irrelevant = not about physical infrastructure.\n"
       'Respond ONLY with a JSON object mapping id to label, e.g. {"S0001":"visible","S0002":"irrelevant"}.')

def main():
    load_env()
    sheet = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("passage_coding_sheet.csv")
    rows = list(csv.DictReader(open(sheet, encoding="utf-8-sig")))
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("pip install openai")
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        sys.exit("no DEEPSEEK_API_KEY in _meta/scripts/.env")
    client = OpenAI(api_key=key, base_url=os.environ.get("DEEPSEEK_BASE_URL"), timeout=120, max_retries=2)
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")

    labels, B = {}, 25
    nb = (len(rows) + B - 1) // B
    for i in range(0, len(rows), B):
        batch = rows[i:i + B]
        prompt = "\n".join(f'{r["sample_id"]}: {r["sentence"]}' for r in batch)
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": SYS}, {"role": "user", "content": prompt}],
                response_format={"type": "json_object"})
            d = json.loads(re.search(r"\{.*\}", r.choices[0].message.content, re.S).group(0))
            labels.update(d)
            print(f"  batch {i // B + 1}/{nb}: +{len(d)}")
        except Exception as e:
            print(f"  batch {i // B + 1}/{nb} ERROR: {str(e)[:140]}")

    out = sheet.with_name(sheet.stem + "_pilot.csv")
    cols = list(rows[0].keys()) + ["coder_llm"]
    with out.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            r["coder_llm"] = labels.get(r["sample_id"], "")
            w.writerow(r)
    got = sum(1 for r in rows if r.get("coder_llm"))
    print(f"[write] {out}  ({got}/{len(rows)} labeled)")

if __name__ == "__main__":
    main()
