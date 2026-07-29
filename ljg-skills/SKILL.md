---
name: ljg-skills
description: >
  lijigang 的 Claude Code 技能集（23 技能 + 2 工作流）— 思维工具 + 深度学习 + 内容可视化的精品集合。
  覆盖约束分析、降秩引擎、盲区扫描、圆桌讨论、投资分析、拆书、论文溯源、白话引擎等。
  本 skill 为元技能包装，帮助你发现、安装和使用 ljg-skills 生态。
  Trigger keywords: ljg, lijigang, 约束引擎, 降秩, 盲区扫描, 圆桌讨论, 拆书,
  论文溯源, 白话引擎, 内容铸卡, 追本之箭, 概念解剖, 思维盲区, ljg-skills,
  ljg-constraint, ljg-rank, ljg-blind, ljg-roundtable, ljg-invest,
  找约束, 找秩, 照盲区, 思维工具集, 哲学工具。
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
  - AskUserQuestion
metadata:
  category: tools
  source: https://github.com/lijigang/ljg-skills
  author: lijigang
  version: "1.0.0"
  license: MIT
---

# ljg-skills — 思维工具 + 深度学习 + 内容可视化技能集

> lijigang 的 Claude Code 自定义技能集。23 个技能，风格偏哲学/认知/个体深度思考，与 Dog-Skills 的工程开发/设计前端定位互补。

## 技能全景（23 技能 + 2 工作流）

### 🧠 思维工具（6 个）
| 技能 | 一句话 | Dog-Skills 已引入 |
|------|--------|-------------------|
| `ljg-constraint` | 约束引擎 — 找框住领域/专业的硬/软/自设三层约束 | ✅ 已引入 |
| `ljg-rank` | 降秩引擎 — 找领域不可再少的独立生成器 | ✅ 已引入 |
| `ljg-blind` | 盲区扫描 — 读 AI 对话记录找结构性思维盲区 | ✅ 已引入 |
| `ljg-think` | 追本之箭 — 纵向深钻到不可再分的本质 | 与 first-principles 高度重叠，用映射引导 |
| `ljg-learn` | 概念解剖 — 八个方向切开概念，压成一句顿悟 | 与 feynman-learning 互补 |
| `ljg-roundtable` | 圆桌讨论 — 真实人物逐轮交锋 + ASCII 结构图 | ✅ 已引入 |

### 📖 阅读/学习（5 个）
| 技能 | 一句话 |
|------|--------|
| `ljg-book` | 拆书 — f(x) 等式框架，作者站在哪个问题前 |
| `ljg-paper` | 论文阅读 — 为非学术人士提取核心想法 |
| `ljg-paper-river` | 论文溯源 — 倒读法递归挖前序论文（最多 5 层） |
| `ljg-read` | 伴读 — 英文三层翻译（信达雅）+ 深度提问 |
| `ljg-word` | 单词精通 — 深度拆解一个英语单词的核心语义 |

### ✍️ 内容/可视化（5 个）
| 技能 | 一句话 |
|------|--------|
| `ljg-card` | 内容铸卡 — 内容→PNG（长图/信息图/多卡/漫画/白板/大字） |
| `ljg-writes` | 写作引擎 — 手术刀式剖开观点，1000-1500 字 |
| `ljg-plain` | 白话引擎 — 任何内容改写 12 岁小孩能懂 |
| `ljg-qa` | 信息提问机 — 文章/论文/书→Q-A 链 |
| `ljg-present` | 演讲铸造器 — 高桥流/标语流 |

### 🎨 可视化/设计（3 个）
| 技能 | 一句话 |
|------|--------|
| `ljg-library` | 取景框借书卡 — 书→意向画面→收藏卡 PNG |
| `ljg-map` | 生态地形图卡 — 行业→可俯瞰的地形图 PNG |
| `ljg-travel` | 旅行研究 — 城市→深度文化文档 + 便携卡片 |

### 💰 专业领域（3 个）
| 技能 | 一句话 | Dog-Skills 已引入 |
|------|--------|-------------------|
| `ljg-invest` | 投资分析 — 判断项目是不是"秩序创造机器" | ✅ 已引入 |
| `ljg-relationship` | 关系分析 — 五层结构诊断 + 精神分析 |
| `ljg-skill-map` | 技能地图 — 扫描已安装技能可视化 |

### 🔧 工具（1 个）
| 技能 | 一句话 |
|------|--------|
| `ljg-push` | 推送引擎 — 本地技能一键同步到 GitHub |

### ⛓️ 工作流（2 个）
| 工作流 | 技能链 |
|--------|--------|
| `ljg-paper-flow` | ljg-paper → ljg-library（论文+借书卡一气呵成） |
| `ljg-word-flow` | ljg-word → ljg-card -i（单词+信息图一气呵成） |

---

## 与 Dog-Skills 的定位关系

```
Dog-Skills:  工程开发 · 设计前端 · 全栈工作流 · 商业诊断 · 内容创作
ljg-skills:  哲学思维 · 认知工具 · 深度学习 · 个体成长 · 投资分析

重合区:      first-principles ↔ ljg-think (追本之箭)
             feynman-learning ↔ ljg-learn (概念解剖)
             article-poster  ↔ ljg-card (内容铸卡)
             writing-assistant ↔ ljg-writes (写作引擎)
```

**结论**：ljg-skills 是 Dog-Skills 在思维深度/认知工具维度的最佳补集。

---

## 安装方式

### 方式一：skills CLI 一键安装（推荐）

```bash
# 安装全部 23 个技能
npx skills add lijigang/ljg-skills -g --all

# Markdown 格式（适用于 Obsidian / VSCode）
npx skills add lijigang/ljg-skills#md -g --all

# 按需安装单个
npx skills add lijigang/ljg-skills -g --skill ljg-constraint
npx skills add lijigang/ljg-skills -g --skill ljg-rank
```

### 方式二：git clone

```bash
# org-mode 版本
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/plugins/ljg-skills

# Markdown 版本
git clone -b md https://github.com/lijigang/ljg-skills.git ~/.claude/plugins/ljg-skills
```

### 方式三：Dog-Skills 已引入的精选技能

以下 6 个技能已作为独立 SKILL.md 引入 Dog-Skills，直接 `cp -r` 即可使用：

```bash
cp -r ljg-constraint ~/.claude/skills/ljg-constraint
cp -r ljg-rank ~/.claude/skills/ljg-rank
cp -r ljg-blind ~/.claude/skills/ljg-blind
cp -r ljg-roundtable ~/.claude/skills/ljg-roundtable
cp -r ljg-invest ~/.claude/skills/ljg-invest
```

---

## 快速映射：我要做 X → 用哪个技能

| 我想做什么 | ljg 技能 | Dog-Skills 已有替代 |
|-----------|---------|-------------------|
| 深钻一个观点到本质 | `ljg-think` | `first-principles`（推荐用 Dog 的） |
| 找一个领域的边界约束 | `ljg-constraint` | ✅ 已引入，直接用 |
| 把复杂领域砍到几根骨架 | `ljg-rank` | ✅ 已引入，直接用 |
| 照出自己思维的盲区 | `ljg-blind` | ✅ 已引入，直接用 |
| 多视角圆桌辩论一个议题 | `ljg-roundtable` | ✅ 已引入，直接用 |
| 分析一个项目值不值得投 | `ljg-invest` | ✅ 已引入，直接用 |
| 把一个概念吃透 | `ljg-learn` | `feynman-learning`（推荐用 Dog 的） |
| 拆解一本书的核心框架 | `ljg-book` | 安装 ljg 原版 |
| 把文章转成 Q&A 链 | `ljg-qa` | 安装 ljg 原版 |
| 把内容转成视觉卡片 | `ljg-card` | `article-poster` / `canvas-design` |
| 内容改写 12 岁能看懂 | `ljg-plain` | 安装 ljg 原版 |
| 读一篇论文 | `ljg-paper` | `scientific-research` |

---

## 上游项目

- **作者**：[lijigang](https://github.com/lijigang)
- **仓库**：[ljg-skills](https://github.com/lijigang/ljg-skills)
- **许可证**：MIT
- **格式**：支持 org-mode（master 分支）和 Markdown（md 分支）
