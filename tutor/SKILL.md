---
name: exam-review-generator
description: >
  Generate structured exam review materials from course PDFs — chapter-by-chapter
  tutorials and exercise class handouts — by analyzing past exam papers, answer keys,
  and textbook content. Use whenever the user wants to create 复习资料, 期末复习,
  考试复习, 考点整理, 习题课讲义, exam study guides, or review notes from textbooks
  and past papers. Triggers when the task involves reading course PDFs, analyzing exam
  patterns, identifying high-frequency topics, and producing organized markdown review
  content with quality audits.
---

# 复习资料生成器

从教材 PDF、往年试卷、课后习题答案中，自动分析考点、生成逐章复习教程和习题课讲义。

## 前置条件

调用此 skill 前，确认 `source/` 目录下至少存在：

- **教材**：PDF（推荐）、Markdown、或已提取的 `.txt` 文本
- **往年试卷**：PDF（推荐）、Markdown、或已提取的 `.txt` 文本（≥2 年）
- （可选）课后习题答案、往年卷答案
- （可选）`source/user_scope.md`——用户指定的考试范围与不考内容

> 支持格式：**PDF**（直接读取）、**Markdown**（`.md`）、**纯文本**（`.txt`）。如果提供 PPT/PPTX，建议先导出为 PDF 再放入 `source/`。如果材料不齐全，先提示用户补充，不要凭空生成。

## 工作流程

先判断任务范围：

| 特征 | 轻量模式 | 完整模式 |
|------|---------|---------|
| 触发 | 单个知识点、一道题、纯考点分析 | 整章或多章教程+习题课 |
| 阅读 | 只读 source/ 中相关材料 | 读 SKILL.md + 全部 references |
| 产出 | 单文件 markdown | 教程 + 习题课 + 审计文件 + 图片 |
| 审计 | 不需要 | 需要 coverage.csv + md_check.txt + text_quality_check.txt |

### 轻量模式

只做以下 3 步，不读 references：

1. **读材料**：从 source/ 和 output/_work/ 中找到相关内容
2. **写内容**：根据任务类型遵循核心写作原则——
   - **教程类**：概念本质 → 公式含义 → 使用条件 → 做题识别 → 常见误区 → 例题（含来源+思路+验证）
   - **习题讲解类**：来源+题目+答案 → 逐步思考过程（每步解释"为什么"）→ 通用步骤模板 → 易错点（含具体场景）→ 答案验证方法
   - **考点分析类**：逐题映射到章节/知识点 → 标注高频/低频 → 输出 CSV
   - 数学公式用 `$...$` / `$$...$$`，禁止 `\(...\)` / `\[...\]`
3. **自检**：写完确认格式正确、公式闭合、链接有效

### 完整模式（整章/多章教程）

执行以下全部阶段。

#### 阶段 0：材料盘点

1. 列出 `source/` 下所有文件，确认材料齐全
2. 有 `source/user_scope.md` 则提取考试范围和不考内容
3. 浏览教材目录，向用户确认章节范围

#### 阶段 1：范围分析与考点映射

1. 通读往年卷和答案，将每道题映射到章节和知识点
2. 生成 `output/audit/past_paper_topic_map.csv`（格式见 `references/audit-spec.md`）
3. 对每章知识点做三分类：**保留**（高频/用户要求）/**压缩保留**（前置依赖）/**剔除**（未出现且非前置），记录到 `output/audit/chXX_coverage.csv`

分类必须有证据。误删核心前置知识是最高优先级错误。详细规则见 `references/quality-gates.md`。

#### 阶段 2：逐章教程生成

1. 精读教材对应章节，确定需要截取的图/表（按 `references/image-rules.md`）
2. 按 `references/tutorial-structure.md` 模板写教程，核心结构：考试相关性总结 → 知识结构 → 逐知识点深度讲解 → 典型题型 → 复习清单
3. 每个知识点覆盖：概念本质、公式含义、使用条件、做题识别、常见误区、例题
4. 数学公式遵循 `references/formula-rules.md`
5. 用 `scripts/check_md.py` 自检格式

#### 阶段 3：习题课生成

1. 从 topic_map.csv 筛选本章题目，按知识点分组（同类题放一起）
2. 按 `references/exercise-class-structure.md` 模板写，每题包含：来源、题目、答案、逐步思考过程（每步解释"为什么"）、题型识别、易错点、答案验证

#### 阶段 4：质量门禁

通过以下检查后才能宣布完成（详见 `references/quality-gates.md`）：

- 格式正确 + 公式无 KaTeX 报错 + 图片链接有效
- "常见考法"与"典型题型"覆盖 ≥80%
- 必须掌握考点均有证据来源
- 所有核心公式有解释、所有例题有详解
- 审计文件齐全：`chXX_coverage.csv`、`chXX_md_check.txt`、`chXX_text_quality_check.txt`，有图片再加 `chXX_image_audit.csv`

未通过 → 输出"未完成问题清单"（模板见 `references/report-templates.md`）。

#### 阶段 5：完成汇报

按 `references/report-templates.md` 模板汇报。

## 核心原则

- **从材料出发**：所有内容必须有教材/试卷/习题作为来源，不凭记忆生成
- **以学生看懂为目标**：每个知识点都要解释"本质是什么、为什么引入、怎么用、容易错在哪"
- **宁可压缩不误删**：不确定是否要剔除的内容，压缩保留而非直接删除
- **证据驱动分类**：每个保留/剔除决定必须有往年卷题号、习题题号或用户指令支撑
- **完成前必自检**：不通过质量门禁不宣布完成

## 学科适配

本 skill 默认以数学类课程（微积分、线性代数等）为基准。对于其他学科，参考 `references/subject-guide.md` 获取特殊要求：

- **电路/电子技术**：需额外说明每个元件作用、直流/交流等效、小信号模型等
- **大学物理**：需额外说明受力分析、物理图像、守恒律使用条件等
- **计算机/编程**：需额外说明算法复杂度、代码执行流程、边界条件等
- **化学/生物**：需额外说明反应机理、结构-功能关系、实验条件等

开始时先判断学科类型，再查阅对应指南。

## 参考文件索引

| 当你需要... | 阅读... |
|---|---|
| 教程 Markdown 完整模板和写作要求 | `references/tutorial-structure.md` |
| 习题课 Markdown 完整模板和组题规则 | `references/exercise-class-structure.md` |
| 审计文件 (csv/txt) 的具体格式 | `references/audit-spec.md` |
| LaTeX/KaTeX 数学公式格式规则 | `references/formula-rules.md` |
| 图片截取、裁剪、质量检查规则 | `references/image-rules.md` |
| 质量门禁、文本验收、自检清单 | `references/quality-gates.md` |
| 不同学科的特殊写作要求 | `references/subject-guide.md` |
| 完成报告和未完成问题清单模板 | `references/report-templates.md` |

## 脚本工具

| 脚本 | 用途 | 何时使用 |
|---|---|---|
| `scripts/check_md.py` | 检查 Markdown 格式：标题层级、`$`/`$$` 闭合、图片链接 | 每章教程和习题课写完后运行 |
| `scripts/extract_images.py` | 从 PDF 指定页码和坐标区域提取图片 | 阶段 2 需要从教材 PDF 截取图片时使用 |
