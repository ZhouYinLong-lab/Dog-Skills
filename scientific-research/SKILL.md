---
name: scientific-research
description: >
  科学研究所助手——集成 K-Dense Scientific Agent Skills（139个科研技能+78个公开科学数据库），
  覆盖文献综述、生物信息学、化学信息学、药物发现、数据分析、科学写作、文档处理等领域。
  核心原则：它是加速器，不是自动驾驶仪——帮你省掉机械劳动，不做科学判断。
  Trigger keywords: 科研, 文献综述, 文献检索, 论文写作, 生信分析, 单细胞, 分子对接, 药物发现,
  化学信息学, 科学写作, 学术海报, 学术PPT, 数据库查询, 数据分析, scientific research,
  literature review, bioinformatics, drug discovery, cheminformatics, paper writing,
  single cell, molecular docking, 科学研究, 科研助手, 实验数据分析, 查文献.
metadata:
  category: thinking
---

# 科学研究所助手 (Scientific Research Assistant)

## 前置条件

本 Skill 基于 **K-Dense Scientific Agent Skills**（27.4k⭐，160,000+ 科学家在使用）。
首次使用前需要安装：

```bash
# 一键安装全部139个技能（不推荐新手）
npx skills add K-Dense-AI/scientific-agent-skills

# 推荐：按需逐个安装
gh skill install K-Dense-AI/scientific-agent-skills <skill-name>

# 锁定版本（避免"上周能跑这周结果变了"）
gh skill install K-Dense-AI/scientific-agent-skills --pin v2.39.0
```

**环境要求**：
- Windows 用户需要 **WSL2**（底层依赖 Linux 生态的 Python 科学计算库）
- 包管理使用 **uv**（非 pip/conda）
- Python 3.12+

## 技能体系总览

K-Dense 覆盖十大领域、139个技能、78个公开科学数据库（加上聚合接口实际可调用近200个数据源）：

| 领域 | 代表技能 | 核心数据库 |
|------|---------|-----------|
| 生物信息学 | scanpy, biopython, pydeseq2, scvelo, scvi-tools | NCBI Gene, UniProt, KEGG, Reactome, STRING, ClinVar, COSMIC |
| 化学信息学 | rdkit, deepchem, datamol, molfeat, medchem | PubChem, ChEMBL, PDB, AlphaFold DB, ZINC |
| 蛋白质组学 | diffdock, openmm, mdanalysis | UniProt, PDB, AlphaFold DB |
| 临床研究 | — | ClinVar, COSMIC, ClinicalTrials.gov, FDA |
| 医学影像 | — | — |
| 机器学习 | scikit-learn, statsmodels, pymc, timesfm | — |
| 材料科学 | — | — |
| 地理空间 | geopandas, geomaster | — |
| 实验室自动化 | — | — |
| 科学交流 | scientific-writing, latex-posters, scientific-slides, infographics | — |

---

## 按研究方向的技能推荐

### 1. 只需要科研写作辅助

```
核心必装：
  literature-review      — 10个数据库并行检索，文献从两三天缩到几小时
  scientific-writing     — IMRAD结构写作辅助（不是代写，是帮查结构和措辞）
  citation-management    — 自动生成BibTeX，兼容Zotero

按需补：
  peer-review            — 投稿前按审稿人视角过一遍
  latex-posters          — 学术海报
  scientific-slides      — 学术幻灯片
  mermaid                — Markdown里画流程图
  infographics           — AI生成信息图表

文档处理全装：
  pdf, docx, pptx, xlsx, markitdown
  （markitdown 支持十几种格式转 Markdown，一个技能通吃）

⚠️ 注意：写作技能默认会调用 scientific-schematics 和 generate-image 画图，
  这俩需要连外部生图服务。连不上的话告诉 AI 不要画图，否则会一直重试连接。
```

### 2. 数据分析和可视化

```
核心必装：
  matplotlib + seaborn   — 出版级图（前者精调，后者快速探索）
  statsmodels            — 统计建模（偏推断）
  scikit-learn           — 经典机器学习一站式
  eda                    — 200+格式自动检测，出数据质量报告

按需补：
  networkx               — 网络分析
  dask / polars          — 大数据
  pymc                   — 贝叶斯
  timesfm                — Google零样本时间序列
  geopandas + geomaster  — 地理空间和遥感
```

### 3. 生物信息学

```
核心必装：
  scanpy                  — 单细胞标配，质控到聚类一条龙
  biopython               — 序列处理老大哥
  pydeseq2                — 差异表达，结果直连KEGG/Reactome做通路富集

按需补：
  scvelo                  — RNA velocity
  scvi-tools              — 深度学习单细胞
  cellxgene-census        — 直连6100万+公开参考数据
  arboreto                — 基因调控网络
  pysam                   — VCF处理

database-lookup 必装（通过它连接）：
  NCBI Gene, UniProt, KEGG, Reactome, STRING, ClinVar, COSMIC
```

### 4. 药物发现 / 化学信息学（整套技能最成熟的领域）

```
核心必装：
  rdkit                   — 化学信息学瑞士军刀
  deepchem                — 深度学习药物设计（ADMET预测、QSAR建模）
  diffdock                — 分子对接（AI直接驱动，不用手动准备输入文件）

按需补：
  datamol                 — RDKit现代包装，API更顺手（建议直接必装）
  molfeat                 — 分子特征工程
  openmm + mdanalysis     — 分子动力学模拟 + 轨迹分析
  medchem                 — 药物化学性质优化

database-lookup 必装：
  ChEMBL, PubChem, PDB, AlphaFold DB, ZINC
```

### 5. 通用必装（不管什么方向）

```
database-lookup           — 78个数据库统一接口，最值得装的一个
markitdown                — 格式转换万能胶
citation-management       — 查文献随手导BibTeX
paper-lookup              — 比PubMed网页快，比Google Scholar结构化
```

---

## 核心使用原则

### 1. 它是加速器，不是自动驾驶仪

- ✅ 帮你省掉"怎么写代码"的时间
- ❌ 不能替代"怎么分析数据"的判断
- 你的角色从"写脚本的人"变成"审结果的人"——你得有这个判断力

### 2. 跨数据库串联是真正的杀手锏

以前：ChEMBL查活性 → 导出CSV → Python脚本 → PubMed查文献 → 写报告（三四个工具来回切）

现在：`"查ChEMBL里EGFR抑制剂的活性数据，用RDKit做SAR分析，同步搜PubMed耐药机制，最后汇总"`——一次搞定。切换成本被抹掉了。

### 3. 写作类比分析类更稳

分析类技能需要对领域知识做正确判断——这在目前AI能力边界上还是模糊地带。
写作、排版、格式转换是结构化任务，规则明确，AI执行更稳。

### 4. 结果必须验证

例如 RDKit 跑分子描述符——某些含特殊官能团的分子，默认参数给出的质子化状态可能不对。
结果看起来漂亮，实际上不准。**如果你不懂底层原理，你根本看不出来结果有问题。**

### 5. 安装前花五分钟读 SKILL.md

知道这个技能依赖哪些包、调什么API、有什么限制。比出问题了回头排查省时间。

---

## 典型工作流示例

### 文献综述加速
```
1. 用 paper-lookup 检索关键词（比PubMed快，结构化输出）
2. 用 literature-review 跑10个数据库并行检索，自动去重，按主题分组
3. 用 citation-management 导出 BibTeX
4. 人工精读筛选——它给你的是阅读路线图，不是替你读
```

### 单细胞数据分析
```
1. 用 scanpy 跑标准流程：质控 → 标准化 → 降维 → 聚类
2. 用 database-lookup 查标记基因（CellMarker/PanglaoDB）
3. 人工判断细胞类型注释——技能给的标注比较粗糙
   （比如只标"T细胞"，你得自己判断是CD4+/CD8+/Treg/Th17）
4. 用 pydeseq2 做差异表达
5. 用 database-lookup 连 KEGG/Reactome 做通路富集
```

### 文档处理流水线
```
markitdown: 十几种格式 → Markdown
pdf/docx/pptx/xlsx: 格式互转
scientific-slides: 学术幻灯片骨架
latex-posters: 学术海报
```

---

## 避坑指南

1. **Windows用户必须WSL2**，原生PowerShell会编译报错
2. **uv可能跟conda冲突**，注意环境隔离
3. **生图技能需要外部API**（Nano Banana2/OpenRouter），连不上就跳过，否则一直重试
4. **不要一键全装139个技能**——按研究方向选装，读完SKILL.md再决定
5. **锁定版本号**，科研最怕"上周能跑这周结果变了"
6. **很多技能只是"文档搬运工"**——把官方API文档搬过来加最佳实践，不是领域专家深度指导
7. **AI的"懂" ≠ 人的"懂"**——你还是要手动验证关键步骤

---

## 与其他科研工具的关系

| 工具 | 定位 | 与本技能的关系 |
|------|------|--------------|
| K-Dense Scientific Skills | 肌肉——142个具体技能+78个数据库 | 本技能的知识来源 |
| academic-research-skills | 骨架——五阶段研究流程管理 | 互补，可同时使用 |
| Stanford Virtual Lab | AI Agent自主设计实验 | 同一种激进方向 |

---

## 参考

- K-Dense GitHub: https://github.com/K-Dense-AI/scientific-agent-skills
- academic-research-skills: 26.5k⭐, 博士全流程研究管理
- 安装命令: `npx skills add K-Dense-AI/scientific-agent-skills`
- 单技能安装: `gh skill install K-Dense-AI/scientific-agent-skills <name>`
