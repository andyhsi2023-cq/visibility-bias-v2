"""
Phase E construct-validity tests for VAI (OSF H4 partial implementation).

Pre-registered H4 called for construct-validity via INDEPENDENT THIRD-PARTY TEXT
(Xinhua news). No such corpus is accessible in this session; scraping Xinhua
requires a browser session the user must oversee. We therefore execute three
INTERNAL construct-validity tests that partially address D1 (circularity):

  E-A: Expanded-dictionary validation — construct a larger, independently-built
       visible/functional keyword list (Online Appendix A.1.3 / A.1.4, ~70 terms
       each) and correlate the resulting VAI_ext with VAI_primary.

  E-B: Within-document section split — partition each GWR into a "past-year
       review" section and a "next-year plan" section using textual markers.
       Compute VAI_review and VAI_plan separately. Visibility-bias mechanism
       predicts VAI_review > VAI_plan (past-tense emphasizes visible wins;
       plan-section is constrained to list specific functional targets).

  E-C: Dictionary bootstrap — randomly split the 42 visible + 36 functional
       keywords into two halves; compute VAI_halfA and VAI_halfB; report the
       correlation across a 200-iteration resample.

Full third-party (Xinhua / Baidu Baike / CNKI) validation is deferred.
"""
import os, re, glob, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({"font.family": "serif", "font.size": 11,
                     "figure.dpi": 110, "savefig.bbox": "tight"})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
GWR_ROOT = "/tmp/gwr_sample/zf工作报告汇总/地级市工作报告2002-2024年"
PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
OUT = f"{PROJ}/03-analysis/phase-E"
FIG = f"{PROJ}/04-figures"
os.makedirs(OUT, exist_ok=True)

# ============================================================
# Dictionaries
# ============================================================
# Original 42 visible terms (6 categories of 7, per Online Appendix A.1.1)
V_ORIG = [
    "立面","外观","外墙","立面改造","粉刷","刷新","装饰",
    "景观","街景","夜景","灯光","亮化","彩化","景观带",
    "绿化","美化","花坛","雕塑","花园城市","园林城市","文明城市",
    "形象","风貌","面貌","门面","窗口","展示","城市名片",
    "示范","样板","靓丽","整洁","美丽","漂亮","焕然一新","穿衣戴帽",
    "观感","视觉","形象工程","面子","天际线","门户",
]

# Original 36 functional terms (per Online Appendix A.1.2)
F_ORIG = [
    "管网","地下管廊","排水","污水","雨污分流","供水","自来水","管道老化","渗漏",
    "供暖","供热","燃气","天然气",
    "结构加固","加固","抗震","结构安全","承重","危房改造","棚户区","检测","鉴定",
    "防水","保温","隔热","节能改造","保温层",
    "消防","防灾","应急","避难","防洪","排涝","内涝","安全隐患",
    "电梯","适老化","无障碍",
]

# Expanded visible terms (independent sample from Online Appendix A.1.3)
V_EXT = V_ORIG + [
    "外饰面","容美","扮靓","梳妆","修饰",
    "景观廊道","灯光秀","光影","水景","微景观","天际轮廓",
    "见缝插绿","透绿","增绿","口袋公园","街心花园",
    "城市客厅","城市窗口","城市品位","城市颜值","赏心悦目",
    "标杆","精品","精品街区","打造亮点","对标先进",
    "创城","创卫","迎检","达标","创建",
    "地标","大手笔","大气魄","蝶变","嬗变",
]

F_EXT = F_ORIG + [
    "管沟","雨水管","二次供水","水质","热力管网",
    "D级危房","C级危房","房屋安全","质量检测",
    "外保温","内保温","双层玻璃","气密性","建筑能耗",
    "消防通道","应急疏散","隐患排查","蓄洪",
    "加装电梯","坡道","扶手","适儿化","日间照料",
    "屋面防水","地下室渗水","维修基金","锈蚀",
    "充电桩","快递柜","垃圾分类","业委会","物业管理",
]

print(f"V_ORIG: {len(V_ORIG)} terms  F_ORIG: {len(F_ORIG)} terms")
print(f"V_EXT:  {len(V_EXT)} terms  F_EXT:  {len(F_EXT)} terms")
print(f"V_EXT new terms: {len(V_EXT)-len(V_ORIG)}  F_EXT new: {len(F_EXT)-len(F_ORIG)}")


def count_hits(text, terms):
    total = 0
    for t in terms:
        total += text.count(t)
    return total


# ============================================================
# Load all GWR texts (cached)
# ============================================================
print("\nLoading GWRs ...")
files = glob.glob(f"{GWR_ROOT}/*.txt")
print(f"  Found {len(files)} files")

# Parse filename: "<city><year>.txt" with year = 4 digits
def parse_filename(path):
    stem = os.path.splitext(os.path.basename(path))[0]
    m = re.search(r"(\d{4})$", stem)
    if not m:
        return None, None
    year = int(m.group(1))
    city = stem[:m.start()]
    city = city.replace("市", "").replace("区", "").replace("县", "")
    return city, year


records = []
for f in files:
    city, year = parse_filename(f)
    if city is None:
        continue
    try:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
    except UnicodeDecodeError:
        try:
            with open(f, encoding="gb18030") as fh:
                text = fh.read()
        except Exception:
            continue
    if len(text) < 200:  # skip placeholder files
        continue
    records.append({"city_std": city, "year": year, "text": text, "text_len": len(text)})

df = pd.DataFrame(records)
print(f"  Parsed {len(df)} usable GWRs; cities={df.city_std.nunique()}, years={df.year.min()}-{df.year.max()}")


# ============================================================
# E-A: Compute VAI_orig and VAI_ext for every GWR
# ============================================================
print("\n=== E-A: expanded-dictionary VAI ===")
df["v_orig"] = df["text"].apply(lambda t: count_hits(t, V_ORIG))
df["f_orig"] = df["text"].apply(lambda t: count_hits(t, F_ORIG))
df["v_ext"]  = df["text"].apply(lambda t: count_hits(t, V_EXT))
df["f_ext"]  = df["text"].apply(lambda t: count_hits(t, F_EXT))

eps = 1e-9
df["vai_orig"] = df["v_orig"] / (df["v_orig"] + df["f_orig"] + eps)
df["vai_ext"]  = df["v_ext"]  / (df["v_ext"]  + df["f_ext"]  + eps)

valid = df[(df["v_orig"] + df["f_orig"]) >= 5].copy()  # require ≥5 hits to avoid noise
print(f"  Valid sample: {len(valid)} GWRs")
print(f"  mean VAI_orig = {valid.vai_orig.mean():.3f}  SD = {valid.vai_orig.std():.3f}")
print(f"  mean VAI_ext  = {valid.vai_ext.mean():.3f}   SD = {valid.vai_ext.std():.3f}")

r_ea = valid[["vai_orig", "vai_ext"]].corr().iloc[0, 1]
r_ea_rank = valid[["vai_orig", "vai_ext"]].corr(method="spearman").iloc[0, 1]
print(f"  Pearson  r(VAI_orig, VAI_ext) = {r_ea:.4f}")
print(f"  Spearman ρ(VAI_orig, VAI_ext) = {r_ea_rank:.4f}")

# Merge with v1 primary panel for sanity check
panel = pd.read_csv(PANEL)
panel_key = panel[["city_std", "year", "vai"]].rename(columns={"vai": "vai_v1"})
merged = valid.merge(panel_key, on=["city_std", "year"], how="inner")
print(f"  Matched to v1 panel: {len(merged)} rows")
r_v1 = merged[["vai_v1", "vai_orig"]].corr().iloc[0, 1]
r_v1_ext = merged[["vai_v1", "vai_ext"]].corr().iloc[0, 1]
print(f"  r(VAI_v1_primary, VAI_orig_reconstructed) = {r_v1:.4f}")
print(f"  r(VAI_v1_primary, VAI_ext_independent)    = {r_v1_ext:.4f}")


# ============================================================
# E-B: within-document past-vs-plan section split
# ============================================================
print("\n=== E-B: past-review vs future-plan split ===")

# Markers for "future plan" section
FUTURE_MARKERS = [
    "主要工作安排", "工作思路", "重点工作",
    "下一步工作", "明年工作", "下阶段工作", "工作计划",
    "目标任务", "主要任务", "工作任务",
    "今后五年", "未来五年", "总体要求和目标任务",
]

def split_doc(text):
    """Return (past_text, future_text). If no marker, return (full, '')."""
    best_idx = None
    for m in FUTURE_MARKERS:
        idx = text.find(m)
        if idx > 2000 and (best_idx is None or idx < best_idx):
            # require marker appears after character 2000 (not in preamble)
            best_idx = idx
    if best_idx is None:
        return text, ""
    return text[:best_idx], text[best_idx:]

def compute_vai(text, vterms=V_ORIG, fterms=F_ORIG):
    v = count_hits(text, vterms)
    f = count_hits(text, fterms)
    if v + f < 3:
        return np.nan, v, f
    return v / (v + f), v, f

results_b = []
for _, row in df.iterrows():
    past, fut = split_doc(row.text)
    if not fut or len(fut) < 1000:  # need enough plan-text
        continue
    vai_p, vp, fp = compute_vai(past)
    vai_f, vf, ff = compute_vai(fut)
    if not (np.isfinite(vai_p) and np.isfinite(vai_f)):
        continue
    results_b.append({"city_std": row.city_std, "year": row.year,
                      "vai_review": vai_p, "vai_plan": vai_f,
                      "n_review": vp + fp, "n_plan": vf + ff,
                      "review_chars": len(past), "plan_chars": len(fut)})

eb = pd.DataFrame(results_b)
print(f"  Successful splits: {len(eb)} / {len(df)}")
print(f"  mean VAI_review = {eb.vai_review.mean():.3f}  SD = {eb.vai_review.std():.3f}")
print(f"  mean VAI_plan   = {eb.vai_plan.mean():.3f}  SD = {eb.vai_plan.std():.3f}")
print(f"  mean Δ (review - plan) = {(eb.vai_review - eb.vai_plan).mean():+.4f}")

# Paired t-test on Δ
from scipy import stats as st
t, p = st.ttest_rel(eb.vai_review, eb.vai_plan)
print(f"  Paired t = {t:.3f}, p = {p:.2e}")
print(f"  Direction: {'REVIEW > PLAN' if eb.vai_review.mean() > eb.vai_plan.mean() else 'PLAN > REVIEW'}  "
      f"{'(consistent with visibility-bias prediction)' if eb.vai_review.mean() > eb.vai_plan.mean() else '(inconsistent)'}")


# ============================================================
# E-C: dictionary bootstrap split
# ============================================================
print("\n=== E-C: dictionary bootstrap halves ===")
rng = np.random.default_rng(20260414)
B = 200
rs = []
for b in range(B):
    v_idx = rng.permutation(len(V_ORIG))
    f_idx = rng.permutation(len(F_ORIG))
    vA = [V_ORIG[i] for i in v_idx[:len(V_ORIG) // 2]]
    vB = [V_ORIG[i] for i in v_idx[len(V_ORIG) // 2:]]
    fA = [F_ORIG[i] for i in f_idx[:len(F_ORIG) // 2]]
    fB = [F_ORIG[i] for i in f_idx[len(F_ORIG) // 2:]]
    # Use pre-computed counts at the bigram level? Cheaper to recount per split
    # but that's 6,294 × 200 × ~40 ops = a lot. Precompute a term-doc matrix.
    # For speed, restrict to a random subsample each iter
    sub = valid.sample(n=min(400, len(valid)), random_state=b)
    def vai_sub(terms_v, terms_f, sub):
        v = sub["text"].apply(lambda t: count_hits(t, terms_v))
        f = sub["text"].apply(lambda t: count_hits(t, terms_f))
        return v / (v + f + eps)
    vaiA = vai_sub(vA, fA, sub)
    vaiB = vai_sub(vB, fB, sub)
    # only rows where both halves have hits
    mask = (vaiA > 0) & (vaiB > 0) & ((sub["v_orig"] + sub["f_orig"]) >= 10)
    if mask.sum() > 50:
        rs.append(vaiA[mask].corr(vaiB[mask]))
rs = np.array([r for r in rs if np.isfinite(r)])
print(f"  N iters: {len(rs)}")
print(f"  mean r(half_A, half_B) = {rs.mean():.4f}  SD = {rs.std():.4f}")
print(f"  5-95 percentile: [{np.percentile(rs, 5):.4f}, {np.percentile(rs, 95):.4f}]")


# ============================================================
# Save and figure
# ============================================================
valid.to_csv(f"{OUT}/vai_orig_vs_ext.csv", index=False)
eb.to_csv(f"{OUT}/vai_review_vs_plan.csv", index=False)
pd.DataFrame({"bootstrap_r": rs}).to_csv(f"{OUT}/dictionary_bootstrap.csv", index=False)

summary = pd.DataFrame({
    "test": ["E-A_pearson", "E-A_spearman", "E-A_vs_v1_orig", "E-A_vs_v1_ext",
             "E-B_delta_mean", "E-B_t", "E-B_p",
             "E-C_mean_r", "E-C_sd_r"],
    "value": [r_ea, r_ea_rank, r_v1, r_v1_ext,
              (eb.vai_review - eb.vai_plan).mean(), t, p,
              rs.mean(), rs.std()],
})
summary.to_csv(f"{OUT}/construct_validity_summary.csv", index=False)
print(f"\nSaved outputs → {OUT}/")

# Figure
fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))

ax = axes[0]
ax.scatter(valid.vai_orig, valid.vai_ext, s=6, alpha=0.3, color="#1f3a5f")
ax.plot([0, 1], [0, 1], "k--", lw=0.5)
ax.set_xlabel("VAI (original dictionary, 42v+36f)")
ax.set_ylabel("VAI (expanded, 70v+60f)")
ax.set_title(f"E-A: Expanded-dictionary validation\nPearson r = {r_ea:.3f}")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)

ax = axes[1]
diff = eb.vai_review - eb.vai_plan
ax.hist(diff, bins=40, color="#d62728", edgecolor="black", alpha=0.7)
ax.axvline(0, color="grey", lw=0.8)
ax.axvline(diff.mean(), color="blue", lw=1.5,
           label=f"mean Δ = {diff.mean():+.3f}\n(t={t:.1f}, p={p:.1e})")
ax.set_xlabel("VAI(review) − VAI(plan)")
ax.set_ylabel("Count")
ax.set_title("E-B: Within-document section differential")
ax.legend(frameon=False, loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[2]
ax.hist(rs, bins=30, color="#2ca02c", edgecolor="black", alpha=0.7)
ax.axvline(rs.mean(), color="blue", lw=1.5, label=f"mean r = {rs.mean():.3f}")
ax.set_xlabel("r(VAI_halfA, VAI_halfB) across bootstrap iters")
ax.set_ylabel("Count")
ax.set_title(f"E-C: Dictionary-bootstrap halves\n(N = {len(rs)} iters)")
ax.legend(frameon=False, loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(f"{FIG}/phase-E-construct-validity.pdf")
fig.savefig(f"{FIG}/phase-E-construct-validity.png", dpi=200)
print(f"Saved: {FIG}/phase-E-construct-validity.pdf")
