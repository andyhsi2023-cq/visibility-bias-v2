# -*- coding: utf-8 -*-
"""从6294篇市×年政府工作报告全文构造独立文本可视性指标(第三数据源)"""
import os, re, glob, pandas as pd, numpy as np, warnings; warnings.filterwarnings('ignore')
DIR='/Volumes/P1/城市研究/工作报告汇总/extracted/zf工作报告汇总/地级市工作报告2002-2024年/'
def norm(s): return re.sub(r'(市|地区|自治州|盟)$','',str(s))
# 面子(可视)词 vs 里子(非可视)词 — 对齐 MOHURD 城建投资"面子/里子"(可见 vs 隐蔽)分类
FACADE=['绿化','园林','景观','亮化','公园','绿地','美化','广场','风貌','绿道','街景','花园','道路','路网','桥梁','立交','轨道','地铁','大道','景观带']
LIZI  =['排水','排涝','管网','管道','防洪','地下管','污水','供水','管廊','内涝','下水道','排污','给排水','防汛','地下空间','雨水']
def cnt(txt, words): return sum(txt.count(w) for w in words)
rows=[]
for f in glob.glob(DIR+'*.txt'):
    base=os.path.basename(f)[:-4]
    m=re.match(r'(.+?)(\d{4})$', base)
    if not m: continue
    cname, year = m.group(1), int(m.group(2))
    try:
        with open(f, encoding='utf-8', errors='ignore') as fh: txt=fh.read()
    except: continue
    L=len(txt)
    if L<200: continue
    fc, lc = cnt(txt,FACADE), cnt(txt,LIZI)
    rows.append({'city_std':norm(cname),'year':year,'wr_len':L,'fac_freq':fc,'lizi_freq':lc,
                 'wr_visibility': fc/(fc+lc) if (fc+lc)>0 else np.nan,
                 'fac_density':fc/L*1000,'lizi_density':lc/L*1000})
t=pd.DataFrame(rows)
print("解析报告:", len(t), "| 城市名:", t.city_std.nunique(), "| 年:", t.year.min(),"-",t.year.max())
# merge city4 via CSMAR crosswalk
m=pd.read_parquet('/tmp/csmar_municipal.parquet')
def c4(x):
    try: return str(int(float(x)))[:4]
    except: return None
m['city4']=m['ccode'].map(c4); cw=m[['city4','cname']].dropna().drop_duplicates()
cw['city_std']=cw['cname'].map(norm); cw=cw[['city_std','city4']].drop_duplicates('city_std')
t=t.merge(cw, on='city_std', how='left')
print("匹配city4:", t.city4.notna().sum(), "/", len(t), "未匹配城市样例:", t[t.city4.isna()].city_std.unique()[:8])
t[t.city4.notna()].to_csv('/Users/andy/Desktop/Research/officials-turnover-cn/02-data/processed/workreport_text_panel.csv', index=False)
print("\n可视性指标 wr_visibility 分布: 均值",round(t.wr_visibility.mean(),3),"中位",round(t.wr_visibility.median(),3))
print("面子词密度均值:",round(t.fac_density.mean(),3),"里子词密度均值:",round(t.lizi_density.mean(),3))
print("按年 wr_visibility 趋势(抽样):")
print(t.groupby('year')['wr_visibility'].mean().round(3).loc[[2003,2008,2012,2016,2020,2024]].to_string())
