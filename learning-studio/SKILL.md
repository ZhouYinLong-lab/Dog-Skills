---
name: learning-studio
description: >
  学习工作室元技能——整合 studyws（任意主题→完整课程+播客）、The Knowledge Guy
  （PDF/EPUB→可查询书架）、ljg-read（中英双语苏格拉底式阅读导师）、Aibrary Skills
  （9 技能：书籍搜索+推荐+阅读清单+3 种播客形式）。覆盖从课程生成→书籍消化→深度阅读→知识输出的完整学习闭环。
  Trigger keywords: 学习工具, 课程生成, 读书, 阅读导师, 播客生成,
  learning studio, study course, 生成课程, 对比阅读, 书架查询,
  苏格拉底阅读, 知识点播客, 深度学习, 知识管理, 书籍推荐。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
metadata:
  category: learning
  source: composite
  version: "1.0.0"
  license: MIT
---

# Learning Studio — 学习工作室

> 四大学习工具整合为一个元技能：从课程生成到书籍消化，从深度阅读到播客输出，完整的学习闭环。

## 子技能矩阵

```
┌──────────────────────────────────────────────────────────────────┐
│                      Learning Studio                              │
│                                                                   │
│  ① studyws          ── 任意主题→完整课程+HTML指南+测验+播客       │
│  ② The Knowledge Guy ── PDF/EPUB→可查询书架→跨书对比              │
│  ③ ljg-read         ── 中英双语·苏格拉底追问·三段标注             │
│  ④ Aibrary Skills   ── 书籍发现+播客生成(3形式)+成长计划          │
└──────────────────────────────────────────────────────────────────┘
```

---

## ① studyws — 任意主题→完整课程

**流水线**：`/sws:start` → `/sws:scope`（大纲）→ `/sws:research`（并行调研）→ `/sws:write`（并行写章）→ `/sws:diagrams`（Mermaid 图表）→ `/sws:guide`（交互 HTML+测验）→ `/sws:slides`（幻灯片）→ **`/sws:podcast`（播客脚本）**

**安装**：`npx studyws init`

**触发**："把机器学习基础做成一套课程，附带播客"

---

## ② The Knowledge Guy — PDF/EPUB→可查询书架

**核心命令**：

| 命令 | 效果 |
|------|------|
| `/book-to-skill` | PDF/EPUB → 结构化 skill（概念图+章节工具包） |
| `walk me through <主题>` | 交互式教程+测验 |
| `course <书>` | 按章学习网站（理论+自动批改测验+代码实验室） |
| `nutshell <书>` | 每章约 100 字摘要 |
| `cheatsheet <书>` | 一页纸操作速查 |
| `compare <主题>` | 跨书对比（agree/extend/tension 标签） |

**安装**：`git clone https://github.com/vitalysim/the-knowledge-guy.git`

**触发**："把这三本 AI 书的观点 compare 一下"

---

## ③ ljg-read — 中英双语·苏格拉底阅读导师

**三段标注法**：
- **[bones]** 核心论点
- **[muscles]** 证据/案例
- **[tendons]** 过渡/连接

**三种阅读速度**：快进 / 默认 / 深潜

**核心理念**：最好的阅读伴侣不回答你的问题——它**制造让你皱眉的问题**。

**安装**：SkillsMP 搜索 `ljg-read` by lijigang

**触发**："用苏格拉底方式带我读这篇文章"

---

## ④ Aibrary Skills — 9 个技能

**书籍发现**：
- `/aibrary-book-search` — 按场景搜书
- `/aibrary-book-recommend` — 1-3 本个性化推荐+阅读策略
- `/aibrary-reading-list` — 主题分级书单

**播客生成（3 种形式）**：
- `/aibrary-podcast-summary` — 单人叙述，10-15 分钟
- `/aibrary-podcast-dialogue` — 主持人+嘉宾对话
- `/aibrary-podcast-ideatwin` — **AI 分身与书作者辩论**

**成长体系**：
- `/aibrary-100` — AI 时代必读 100 本
- `/aibrary-foryou-topic` — 个性化主题推荐
- `/aibrary-growth-plan` — 结构化成长计划+周任务

**安装**：[aibrary.ai/skills](https://www.aibrary.ai/skills)

---

## 推荐学习流水线

```
studyws（生成课程框架）
       │
       ▼
The Knowledge Guy（把参考书灌入书架）
       │
       ▼
ljg-read（苏格拉底深度阅读每章）
       │
       ▼
Aibrary（生成播客输出+制定后续成长计划）
```

## 安装汇总

```bash
npx studyws init
git clone https://github.com/vitalysim/the-knowledge-guy.git ~/.claude/skills/the-knowledge-guy
# ljg-read: SkillsMP search
# Aibrary: aibrary.ai/skills
```
