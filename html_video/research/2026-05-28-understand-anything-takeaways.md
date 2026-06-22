# Understand-Anything 集成思路（v0.8+）

> Source: https://github.com/Lum1104/Understand-Anything
> License: MIT
> Date: 2026-05-28

## 项目核心

把 codebase / wiki / docs 转成可交互的知识图谱。**不是直接生图**，而是**先把内容拆成结构化 JSON，再渲染**。

## 5 个能搬到 html-video 的设计决策

### ★★★★★ 1. 中间 JSON 作为真理之源（content-graph）

UA 把分析结果落在 `.understand-anything/knowledge-graph.json`，可 commit、可 diff、可在团队间共享。**渲染层（dashboard）跟数据层完全解耦**。

→ html-video 借鉴：把"用户意图 + 抽取的内容结构"落成 `content-graph.json`，**再**用 Hyperframes 模板渲染。这样：
- 同一份内容可换不同视觉风格（warm-grain / cyberpunk / Swiss）
- 改风格不需要重 chat agent
- 改内容（替换某个数据点）只刷新受影响帧
- 用户可下载 JSON 备份/分享/版本控制

### ★★★★ 2. 确定性 + 语义性分层

UA 用 Tree-sitter（确定性）抽结构事实 + LLM 抽语义（"this file is for ..."）。

→ html-video 借鉴：用户输入文本里的**结构事实**用规则抽（数字 / 列表 / 标题 / 时间线 / 对比关系），**语义解读**才喂给 LLM（这帧讲什么 / 风格是什么）。能：
- 大幅降低 token 成本
- 结构提取可复现（同输入同输出）
- LLM 失败时结构事实仍可用

### ★★★★ 3. Multi-agent pipeline（专人专事）

UA 拆 6 个 agent：scanner / file-analyzer / architecture-analyzer / domain-analyzer / tour-builder / graph-reviewer，并行 5 路。

→ html-video 借鉴：把现在单 prompt 拆成 pipeline：
- `intent-parser`：用户意图分类（branding / data-viz / explainer / promo）
- `content-extractor`：从 prompt + 附件抽实体 + 数据 + 节点
- `structure-builder`：建立帧之间的语义关系（递进 / 对比 / 因果 / 时间线）
- `style-resolver`：根据用户描述（"warm-grain" 等）生成 CSS tokens
- `frame-composer`：按 structure 生成 HTML 帧序列
- `validator`：跑 hyperframes lint + visual 检查

**好处**：每个 agent 独立 prompt 可单独迭代、可并行、可缓存。

### ★★★★ 4. tour-builder 思路：图先 → 再 sort 成线性

UA 先建图（节点+边+依赖），再 topological sort 成"教学路径"。

→ html-video 借鉴：HTML 视频是线性帧序列，但**帧之间的语义关系**（这一帧解释那一帧、这一帧承接前一帧的对比）应该先建图。然后选最佳播放顺序：
- 时间线类内容：按时间排
- 数据对比类：按重要度排
- 教学类：按依赖排（concept A 必须在 concept B 之前出现）

这是 html-video 现在完全没做的事 — 现在 agent 一次写一帧 HTML。如果用户给的是 5-frame 的 explainer，按 tour-builder 思路出来的会更连贯。

### ★★★ 5. Persona-adaptive 渲染

UA dashboard 根据 junior dev / PM / power user 调详略。

→ html-video 借鉴：同一份 content-graph.json，用户选 audience：
- 给同行：术语保留、节奏快
- 给客户：每概念一帧、慢
- 给社媒：9:16 + 字幕

**纯渲染层调整**，agent 不用重跑。

## 一句话设计原则（直接借）

UA 的金句："Graphs that teach > graphs that impress."

→ html-video 翻译："**教得清楚的视频 > 看着炫的视频**"。可以做产品 README 第一句 / 推特置顶。

## 适合 html-video v0.8 的最小集成

不要一口气吃 5 条。建议先做 **#1（content-graph 中间 JSON）+ #4（图先 → sort）** 这两条最有杠杆的：

1. 加 `@html-video/content-graph` package：定义 `ContentGraph` schema（nodes: entity/data/text；edges: sequence/contrast/dependency）
2. agent 第一轮不出 HTML，出 content-graph.json
3. 第二轮按 graph 生成 HTML 帧序列（Hyperframes-style 时间轴）
4. 用户改内容只动 graph，HTML 自动重渲染

这是 v0.8 的 RFC-06 草案种子。

## 怎么跟现状协调

v0.7 现在是直接 chat → HTML，**这条路径保留**作为快速入口（"我就要一帧"场景）。content-graph 路径是**升级路径**，给"我要做完整短视频"或者"我要把这份资料拆成 5 帧讲清楚"的用户。

具体触发点 — agent 自己判断：
- 用户描述只对应一帧 → 走当前 v0.7 直接 HTML 路径
- 用户给的是多概念 / 时间线 / 对比 → agent 先出 content-graph，再 frame 序列

## 不直接抄的事

- UA 是"分析现存代码/文档"工具，输入是路径；html-video 是"创作"工具，输入是描述/素材。pipeline 角色对应不上 1:1，借的是**思路**不是 schema。
- UA 的图谱本身是产物（用户看图）；html-video 的图谱是中间产物（用户看视频）。所以我们不需要做 dashboard，content-graph 不暴露给用户也行（除非作为"高级编辑"入口）。
