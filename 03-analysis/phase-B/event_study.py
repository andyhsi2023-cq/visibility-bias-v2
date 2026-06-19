"""
Phase B: Central anti-corruption inspection shock on VAI (H2 test).

Implements Callaway-Sant'Anna (2021) doubly-robust staggered DiD
via the linearmodels PanelOLS with event-time dummies (TWFE approximation).

Pre-registered (OSF zmjy5):
- Outcome Y: VAI, CIR
- Treatment: staggered by province, first-treatment-year = year of first
  central CCDI inspection round (rounds 1-5, 2013-2015)
- Event window: k in [-3, +3], k = -1 as reference
- Prediction: theta_k < 0 for k >= 0 in VAI regression, magnitude >= 0.02

NOTE: this is a provisional event-study via two-way fixed effects with
event-time indicators, not the full Callaway-Sant'Anna estimator. The
full C-S estimator requires the `did` package or `differences` in R/Py.
For Phase B round 1 we use TWFE as a first-pass diagnostic; if results
are interesting, Phase B round 2 will replicate with the full C-S
estimator. Any deviation from the C-S approach is logged in amendments.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from linearmodels.panel import PanelOLS

mpl.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "figure.dpi": 110,
    "savefig.bbox": "tight",
})

PROJ = "/Users/andy/Desktop/Research/visibility-bias-v2"
VAI_PANEL = "/Users/andy/Desktop/Research/visibility-bias-upgrade/02-data/processed/main_panel.csv"
INSP_CSV = f"{PROJ}/02-data/processed/ccdi_inspection_rounds.csv"
OUT_DIR = f"{PROJ}/03-analysis/phase-B"
FIG_DIR = f"{PROJ}/04-figures"
os.makedirs(FIG_DIR, exist_ok=True)


# ================================================================
# Load panel
# ================================================================
df = pd.read_csv(VAI_PANEL)
print(f"Loaded VAI panel: {len(df)} rows, {df.city_std.nunique()} cities")

# Load inspection data
insp = pd.read_csv(INSP_CSV)
print(f"Loaded inspection data: {len(insp)} province-rounds, "
      f"{insp.province_code.nunique()} provinces")

# Map cities to provinces by city_std
# We need a city -> province map. The main panel doesn't explicitly have
# province. Let's infer from the city name patterns using a helper dict.

city_to_province = {
    # Hubei (42)
    "武汉": 42, "黄石": 42, "十堰": 42, "宜昌": 42, "襄阳": 42, "鄂州": 42,
    "荆门": 42, "孝感": 42, "荆州": 42, "黄冈": 42, "咸宁": 42, "随州": 42,
    "恩施": 42, "仙桃": 42, "潜江": 42, "天门": 42,
    # Inner Mongolia (15)
    "呼和浩特": 15, "包头": 15, "乌海": 15, "赤峰": 15, "通辽": 15,
    "鄂尔多斯": 15, "呼伦贝尔": 15, "巴彦淖尔": 15, "乌兰察布": 15,
    "兴安盟": 15, "锡林郭勒": 15, "阿拉善": 15,
    # Chongqing (50)
    "重庆": 50,
    # Guizhou (52)
    "贵阳": 52, "六盘水": 52, "遵义": 52, "安顺": 52, "毕节": 52, "铜仁": 52,
    "黔西南": 52, "黔东南": 52, "黔南": 52,
    # Jiangxi (36)
    "南昌": 36, "景德镇": 36, "萍乡": 36, "九江": 36, "新余": 36, "鹰潭": 36,
    "赣州": 36, "吉安": 36, "宜春": 36, "抚州": 36, "上饶": 36,
    # Jilin (22)
    "长春": 22, "吉林": 22, "四平": 22, "辽源": 22, "通化": 22, "白山": 22,
    "松原": 22, "白城": 22, "延边": 22,
    # Yunnan (53)
    "昆明": 53, "曲靖": 53, "玉溪": 53, "保山": 53, "昭通": 53, "丽江": 53,
    "普洱": 53, "临沧": 53, "楚雄": 53, "红河": 53, "文山": 53, "西双版纳": 53,
    "大理": 53, "德宏": 53, "怒江": 53, "迪庆": 53,
    # Anhui (34)
    "合肥": 34, "芜湖": 34, "蚌埠": 34, "淮南": 34, "马鞍山": 34, "淮北": 34,
    "铜陵": 34, "安庆": 34, "黄山": 34, "滁州": 34, "阜阳": 34, "宿州": 34,
    "六安": 34, "亳州": 34, "池州": 34, "宣城": 34,
    # Hunan (43)
    "长沙": 43, "株洲": 43, "湘潭": 43, "衡阳": 43, "邵阳": 43, "岳阳": 43,
    "常德": 43, "张家界": 43, "益阳": 43, "郴州": 43, "永州": 43, "怀化": 43,
    "娄底": 43, "湘西": 43,
    # Guangdong (44)
    "广州": 44, "韶关": 44, "深圳": 44, "珠海": 44, "汕头": 44, "佛山": 44,
    "江门": 44, "湛江": 44, "茂名": 44, "肇庆": 44, "惠州": 44, "梅州": 44,
    "汕尾": 44, "河源": 44, "阳江": 44, "清远": 44, "东莞": 44, "中山": 44,
    "潮州": 44, "揭阳": 44, "云浮": 44,
    # Shanxi (14)
    "太原": 14, "大同": 14, "阳泉": 14, "长治": 14, "晋城": 14, "朔州": 14,
    "晋中": 14, "运城": 14, "忻州": 14, "临汾": 14, "吕梁": 14,
    # Beijing (11)
    "北京": 11,
    # Tianjin (12)
    "天津": 12,
    # Liaoning (21)
    "沈阳": 21, "大连": 21, "鞍山": 21, "抚顺": 21, "本溪": 21, "丹东": 21,
    "锦州": 21, "营口": 21, "阜新": 21, "辽阳": 21, "盘锦": 21, "铁岭": 21,
    "朝阳": 21, "葫芦岛": 21,
    # Fujian (35)
    "福州": 35, "厦门": 35, "莆田": 35, "三明": 35, "泉州": 35, "漳州": 35,
    "南平": 35, "龙岩": 35, "宁德": 35,
    # Ningxia (64)
    "银川": 64, "石嘴山": 64, "吴忠": 64, "固原": 64, "中卫": 64,
    # Hainan (46)
    "海口": 46, "三亚": 46, "三沙": 46, "儋州": 46,
    # Gansu (62)
    "兰州": 62, "嘉峪关": 62, "金昌": 62, "白银": 62, "天水": 62, "武威": 62,
    "张掖": 62, "平凉": 62, "酒泉": 62, "庆阳": 62, "定西": 62, "陇南": 62,
    "临夏": 62, "甘南": 62,
    # Hebei (13)
    "石家庄": 13, "唐山": 13, "秦皇岛": 13, "邯郸": 13, "邢台": 13,
    "保定": 13, "张家口": 13, "承德": 13, "沧州": 13, "廊坊": 13, "衡水": 13,
    # Shaanxi (61)
    "西安": 61, "铜川": 61, "宝鸡": 61, "咸阳": 61, "渭南": 61, "延安": 61,
    "汉中": 61, "榆林": 61, "安康": 61, "商洛": 61,
    # Heilongjiang (23)
    "哈尔滨": 23, "齐齐哈尔": 23, "鸡西": 23, "鹤岗": 23, "双鸭山": 23,
    "大庆": 23, "伊春": 23, "佳木斯": 23, "七台河": 23, "牡丹江": 23,
    "黑河": 23, "绥化": 23, "大兴安岭": 23,
    # Sichuan (51)
    "成都": 51, "自贡": 51, "攀枝花": 51, "泸州": 51, "德阳": 51, "绵阳": 51,
    "广元": 51, "遂宁": 51, "内江": 51, "乐山": 51, "南充": 51, "眉山": 51,
    "宜宾": 51, "广安": 51, "达州": 51, "雅安": 51, "巴中": 51, "资阳": 51,
    "阿坝": 51, "甘孜": 51, "凉山": 51,
    # Jiangsu (32)
    "南京": 32, "无锡": 32, "徐州": 32, "常州": 32, "苏州": 32, "南通": 32,
    "连云港": 32, "淮安": 32, "盐城": 32, "扬州": 32, "镇江": 32, "泰州": 32,
    "宿迁": 32,
    # Xinjiang (65)
    "乌鲁木齐": 65, "克拉玛依": 65, "吐鲁番": 65, "哈密": 65,
    "昌吉": 65, "博尔塔拉": 65, "巴音郭楞": 65, "阿克苏": 65, "克孜勒苏": 65,
    "喀什": 65, "和田": 65, "伊犁": 65, "塔城": 65, "阿勒泰": 65,
    # Henan (41)
    "郑州": 41, "开封": 41, "洛阳": 41, "平顶山": 41, "安阳": 41, "鹤壁": 41,
    "新乡": 41, "焦作": 41, "濮阳": 41, "许昌": 41, "漯河": 41, "三门峡": 41,
    "南阳": 41, "商丘": 41, "信阳": 41, "周口": 41, "驻马店": 41, "济源": 41,
    # Shanghai (31)
    "上海": 31,
    # Guangxi (45)
    "南宁": 45, "柳州": 45, "桂林": 45, "梧州": 45, "北海": 45, "防城港": 45,
    "钦州": 45, "贵港": 45, "玉林": 45, "百色": 45, "贺州": 45, "河池": 45,
    "来宾": 45, "崇左": 45,
    # Qinghai (63)
    "西宁": 63, "海东": 63, "海北": 63, "黄南": 63, "海南藏族": 63, "果洛": 63,
    "玉树": 63, "海西": 63,
    # Tibet (54)
    "拉萨": 54, "日喀则": 54, "昌都": 54, "林芝": 54, "山南": 54, "那曲": 54,
    "阿里": 54,
    # Zhejiang (33)
    "杭州": 33, "宁波": 33, "温州": 33, "嘉兴": 33, "湖州": 33, "绍兴": 33,
    "金华": 33, "衢州": 33, "舟山": 33, "台州": 33, "丽水": 33,
    # Shandong (37)
    "济南": 37, "青岛": 37, "淄博": 37, "枣庄": 37, "东营": 37, "烟台": 37,
    "潍坊": 37, "济宁": 37, "泰安": 37, "威海": 37, "日照": 37, "莱芜": 37,
    "临沂": 37, "德州": 37, "聊城": 37, "滨州": 37, "菏泽": 37,
}

df["province_code"] = df["city_std"].map(city_to_province)
print(f"\nCities with province match: {df.province_code.notna().sum()} / {len(df)}")
print(f"Unmatched cities (first 20): {sorted(df[df.province_code.isna()].city_std.unique())[:20]}")

# Merge treatment year
prov_treat = insp[["province_code", "first_treatment_year"]].drop_duplicates()
df = df.merge(prov_treat, on="province_code", how="left")
print(f"\nCity-years with treatment year: {df.first_treatment_year.notna().sum()}")
print(f"Treatment year distribution (city-years):")
print(df.drop_duplicates("city_std").first_treatment_year.value_counts().sort_index())

# ================================================================
# Event-time indicator
# ================================================================
df["event_time"] = df["year"] - df["first_treatment_year"]
# Clip event-time to [-3, +3] for pre-registered window, code far-past/future as -4/+4 bins
df["event_bin"] = df["event_time"].clip(-4, 4)

# Keep analysis sample: VAI non-null, 2009-2018 window (3 pre + 3 post buffer + data availability)
sample = df[df.vai.notna() & df.year.between(2009, 2018) & df.first_treatment_year.notna()].copy()
print(f"\nAnalysis sample: {len(sample)} city-years, {sample.city_std.nunique()} cities, "
      f"{sample.year.min()}-{sample.year.max()}")


# ================================================================
# Event-study via TWFE with event-time dummies (k != -1 reference)
# ================================================================
sample = sample.set_index(["city_std", "year"])

# Build event-time dummies (omit k = -1)
event_vals = [-4, -3, -2, 0, 1, 2, 3, 4]  # -1 is reference
for k in event_vals:
    sample[f"k_{k}"] = (sample["event_bin"] == k).astype(int)

# Controls
controls = []
for c in ["ln_gdppc", "ln_pop", "ind2_share"]:
    if c in sample.columns:
        sample[c] = sample[c].fillna(sample.groupby("city_std")[c].transform("mean"))
        controls.append(c)

dummies = [f"k_{k}" for k in event_vals]
formula_X = dummies + controls
X = sample[formula_X].copy()
X = X.dropna()
y = sample.loc[X.index, "vai"].astype(float)

print(f"\nFinal regression sample: {len(y)} obs")

model = PanelOLS(y, X, entity_effects=True, time_effects=True,
                 drop_absorbed=True, check_rank=False)
res = model.fit(cov_type="clustered", cluster_entity=True)
print("\n=== VAI Event Study ===")
print(res.summary.tables[1])

# Save coefficients
results_rows = []
for k in event_vals:
    if f"k_{k}" in res.params.index:
        results_rows.append({
            "event_time": k,
            "beta": res.params[f"k_{k}"],
            "se": res.std_errors[f"k_{k}"],
            "p": res.pvalues[f"k_{k}"],
            "ci_lo": res.conf_int().loc[f"k_{k}"].iloc[0],
            "ci_hi": res.conf_int().loc[f"k_{k}"].iloc[1],
        })

# Add reference period
results_rows.insert(3, {"event_time": -1, "beta": 0, "se": 0, "p": np.nan, "ci_lo": 0, "ci_hi": 0})
results = pd.DataFrame(results_rows).sort_values("event_time")
results.to_csv(f"{OUT_DIR}/event_study_vai.csv", index=False)
print(f"\nSaved: {OUT_DIR}/event_study_vai.csv")
print(results.round(4).to_string(index=False))

# Joint F-test on post-treatment coefficients
post_dummies = [f"k_{k}" for k in [0, 1, 2, 3, 4] if f"k_{k}" in res.params.index]
if post_dummies:
    wald = res.wald_test(formula=" = ".join(post_dummies + ["0"]))
    print(f"\nJoint F-test on post-treatment k in [0, 4]: stat={wald.stat:.3f}, p={wald.pval:.4f}")

# ================================================================
# Repeat for CIR outcome
# ================================================================
y_cir = sample.loc[X.index, "cir"].astype(float).dropna()
X_cir = X.loc[y_cir.index]
if len(y_cir) > 100:
    model_cir = PanelOLS(y_cir, X_cir, entity_effects=True, time_effects=True,
                         drop_absorbed=True, check_rank=False)
    res_cir = model_cir.fit(cov_type="clustered", cluster_entity=True)
    print("\n=== CIR Event Study ===")
    print(res_cir.summary.tables[1])

    cir_rows = []
    for k in event_vals:
        if f"k_{k}" in res_cir.params.index:
            cir_rows.append({
                "event_time": k,
                "beta": res_cir.params[f"k_{k}"],
                "se": res_cir.std_errors[f"k_{k}"],
                "p": res_cir.pvalues[f"k_{k}"],
                "ci_lo": res_cir.conf_int().loc[f"k_{k}"].iloc[0],
                "ci_hi": res_cir.conf_int().loc[f"k_{k}"].iloc[1],
            })
    cir_rows.insert(3, {"event_time": -1, "beta": 0, "se": 0, "p": np.nan, "ci_lo": 0, "ci_hi": 0})
    results_cir = pd.DataFrame(cir_rows).sort_values("event_time")
    results_cir.to_csv(f"{OUT_DIR}/event_study_cir.csv", index=False)

else:
    results_cir = None
    print(f"\nCIR sample too small ({len(y_cir)}) for event study.")


# ================================================================
# Parallel-trends test: joint-significance on pre-period k in [-4, -2]
# ================================================================
pre_dummies = [f"k_{k}" for k in [-4, -3, -2] if f"k_{k}" in res.params.index]
if pre_dummies:
    pretrend = res.wald_test(formula=" = ".join(pre_dummies + ["0"]))
    print(f"\nParallel-trends test on pre-treatment k in [-4, -2]:")
    print(f"  VAI Wald stat={pretrend.stat:.3f}, p={pretrend.pval:.4f}")
    print(f"  {'REJECT parallel trends (p<0.10)' if pretrend.pval < 0.10 else 'CANNOT reject parallel trends'}")

# ================================================================
# Figure: Event-study coefficient plot
# ================================================================
fig, axes = plt.subplots(1, 2 if results_cir is not None else 1,
                          figsize=(11 if results_cir is not None else 6, 4.5))
if results_cir is None:
    axes = [axes]

for ax, res_df, outcome in zip(axes,
                                 [results, results_cir] if results_cir is not None else [results],
                                 ["VAI", "CIR"] if results_cir is not None else ["VAI"]):
    if res_df is None:
        continue
    ax.errorbar(res_df["event_time"], res_df["beta"],
                yerr=[res_df["beta"] - res_df["ci_lo"], res_df["ci_hi"] - res_df["beta"]],
                fmt="o-", capsize=4, lw=1.5, color="#1f3a5f", ecolor="#6090b0")
    ax.axhline(0, color="grey", lw=0.6, ls="--")
    ax.axvline(-0.5, color="red", lw=0.8, ls=":", alpha=0.7)
    ax.set_xlabel("Event time (years relative to inspection)")
    ax.set_ylabel(f"β (on {outcome})")
    ax.set_title(f"Event-study coefficients — {outcome}")
    ax.set_xticks(list(range(-4, 5)))
    ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(f"{FIG_DIR}/phase-B-event-study.pdf")
fig.savefig(f"{FIG_DIR}/phase-B-event-study.png", dpi=200)
print(f"\nSaved figure: {FIG_DIR}/phase-B-event-study.pdf / .png")
