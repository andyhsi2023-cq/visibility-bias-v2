"""
Phase E2-1: fetch Chinese Wikipedia articles for 282 prefecture-level cities
as a TRUE THIRD-PARTY text corpus for VAI construct validity.

Wikipedia-zh articles are written by volunteer editors, not city government
employees, which addresses the D1 circularity concern that Phase E internal
tests could not fully resolve.

Rate-limiting: 0.5s between requests; User-Agent identifies academic use.

Note: Wikipedia articles are city-DESCRIPTIONS, not year-specific. We therefore
test H4 at the city cross-section level: is mean city-level VAI_primary
(averaged across years) correlated with VAI_wikipedia?
"""
import os, time, json, urllib.request, urllib.parse
import pandas as pd

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
OUT_DIR = f"{PROJ}/02-data/raw/wikipedia_zh"
os.makedirs(OUT_DIR, exist_ok=True)

# Get unique city list from primary panel
df = pd.read_csv(PANEL)
cities = sorted(df["city_std"].dropna().unique().tolist())
print(f"Target cities: {len(cities)}")

# Build candidate search titles: try city_std first, then +市 variant
def fetch_wiki(title):
    """Fetch Wikipedia-zh extract. Return (text, page_title, found)."""
    url = (f"https://zh.wikipedia.org/w/api.php?action=query&prop=extracts"
           f"&explaintext=1&redirects=1&format=json"
           f"&titles={urllib.parse.quote(title)}")
    req = urllib.request.Request(url, headers={
        "User-Agent": "VisibilityBiasResearch/1.0 (academic; mailto:researcher@cqsurvey.org)"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        pages = data.get("query", {}).get("pages", {})
        for pid, p in pages.items():
            if pid == "-1":  # not found
                return None, None, False
            extract = p.get("extract", "")
            return extract, p.get("title"), len(extract) > 500
    except Exception as e:
        return None, None, False
    return None, None, False

# Load existing scrape cache if present
cache_path = f"{OUT_DIR}/_cache.json"
cache = {}
if os.path.exists(cache_path):
    with open(cache_path) as f:
        cache = json.load(f)
    print(f"Loaded {len(cache)} cached entries")

records = []
n_hit, n_miss = 0, 0
for i, c in enumerate(cities):
    if c in cache:
        records.append(cache[c])
        if cache[c]["found"]:
            n_hit += 1
        else:
            n_miss += 1
        continue

    # Try with 市 suffix first (better match for prefectures)
    attempts = [f"{c}市", c, f"{c}地区", f"{c}州"]
    found_entry = None
    for attempt in attempts:
        text, title, ok = fetch_wiki(attempt)
        time.sleep(0.4)  # rate limit
        if ok:
            found_entry = {"city_std": c, "attempt": attempt, "title": title,
                           "text_len": len(text), "text": text, "found": True}
            # Save individual file
            with open(f"{OUT_DIR}/{c}.txt", "w") as f:
                f.write(text)
            n_hit += 1
            break
    if not found_entry:
        found_entry = {"city_std": c, "attempt": attempts[-1], "title": None,
                       "text_len": 0, "text": "", "found": False}
        n_miss += 1
    cache[c] = found_entry
    records.append(found_entry)

    # Periodic cache save
    if (i + 1) % 25 == 0:
        with open(cache_path, "w") as f:
            json.dump(cache, f, ensure_ascii=False)
        print(f"  [{i+1}/{len(cities)}] hits={n_hit}, miss={n_miss}")

# Final cache save
with open(cache_path, "w") as f:
    json.dump(cache, f, ensure_ascii=False)

# Summary
meta = pd.DataFrame([{
    "city_std": r["city_std"], "title": r["title"],
    "text_len": r["text_len"], "found": r["found"]
} for r in records])
meta.to_csv(f"{OUT_DIR}/_meta.csv", index=False)
print(f"\n=== Scrape complete ===")
print(f"Cities hit:  {n_hit} / {len(cities)}")
print(f"Cities miss: {n_miss}")
print(f"Mean text length (hits): {meta[meta.found].text_len.mean():.0f} chars")
print(f"Total corpus chars: {meta[meta.found].text_len.sum():,}")
