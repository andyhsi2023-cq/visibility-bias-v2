# NEXT-SESSION KICKOFF — visibility-bias-v2 (R1 正文重写)

**目标**:把 JCSS 稿(§1–§6 + 标题)重写到已收敛的新论点;**不放过 JCSS**。
**不要重跑实证**——全部已完成并落盘。只做写作。

## 先读这两个文件(所有东西都在里面)
1. `03-analysis/phase-K/V2-EVIDENCE-CORE.md` — 全部数字 + 显著度原理 + 最终词表 + **逐 section 重写蓝图(§7)** + 审稿人映射。
2. `06-submission/response-to-reviewers-R1.md` — 目标结构与口径(已答 C1–C5)。

## 论点(一句话)
政务文本测量的**验证案例**:朴素词典败(可见精度 0.10,毁于 形象/示范 多义)→ 显著度原理的具体词表改善但撞**多义天花板(~0.60,道路/轨道交通隐喻不可删)**→ **LLM 集成高精度(0.84/κ0.835)**→ **行为标准效度决定一切**(退休外生更替下,有效文本与真实 CIR 投资同步、朴素不动)= 答死"只是话术吗"。

## 重写任务(按 evidence-core §7 蓝图)
- §1 引言:论点 + 四点贡献 + text-as-data 定位
- §2 理论:可观察性/显著度不对称(地铁=可见边界案例),轻
- §3 测量:词表阶梯(naive→具体→显著度v4)+ 多义诊断(示范/形象/道路)+ 段级人工+LLM 验证 + 精度阶梯 0.10→0.60→LLM 0.84 + 天花板
- §4 行为效度(中心):退休外生更替→有效文本&CIR 同步、naive 不动;招投标 3:1 补充
- §5 讨论:多义天花板 / LLM 推荐 / 行为同步=决定性效度 / 局限
- §6 结论;**更新标题**(从"A Validated Instrument"→ 体现"多义天花板+LLM+行为效度")
- 物理存量/空间/福利**不并**(审计判弱 + 审稿人已要求降级)

## 关键数据/脚本
- 词表:`02-data/processed/lexicon_visible_v4_salience.txt` + `lexicon_functional_concrete.txt`
- 合并面板:`../officials-turnover-cn/02-data/processed/main_panel.csv`(列 vai_composite / wr_visibility / cir / change / retire_driven)
- 行为效度复算:`03-analysis/phase-J-criterion-validity/replicate_comovement.py`
- 段级验证:`03-analysis/phase-K/`(人工 anchor + 集成 + 评分)

## Andy 的人工/外部项(我做不了)
① 第二编码员补人工 intercoder κ(现仅 human↔ensemble κ=0.66);② OSF/Zenodo 重存 + 验证链接可访问;③ 最终 EM 上传(Word/Tex,due 2026-07-30,但已决定质量优先不赶)。

## 注意
- 教训:重计算别交给后台 agent(本会话多次 600s 看门狗卡死),用后台 **Bash 脚本**。
- officials-turnover-cn **不单独发**,材料并入 V2;故行为效度/识别可直接当 V2 自有,无双发问题。
