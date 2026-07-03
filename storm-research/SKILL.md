---
name: storm-research
description: >
  斯坦福 STORM 深度研究方法 — 4 个提示让 Claude 像博士一样做研究。
  STORM = Systematic（系统化）+ Thorough（彻底）+ Organized（有组织）+
  Rigorous（严谨）+ Methodical（有条理）。5 分钟产出博士 48 小时级别的研究简报。
  适用于文献综述、技术调研、竞品分析、行业研究等场景。
  Trigger keywords: STORM方法, 深度研究, 博士级研究, 学术研究, 文献综述,
  系统研究, 技术调研, Stanford STORM, 研究简报, thorough research。
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
  - WebSearch
  - Bash
  - Agent
  - Glob
  - Grep
  - TaskCreate
  - TaskUpdate
metadata:
  category: thinking
  source: https://mp.weixin.qq.com/s/aLhdKzW24AheR9pmoQj3eg
  author: 卡尔的AI沃兹
  version: "1.0.0"
  license: MIT
---

# STORM 深度研究 — Stanford STORM Research Method

4 个提示让 Claude 像博士一样做研究，5 分钟产出博士 48 小时级别的研究简报。

## STORM 原则

| 字母 | 含义 | 说明 |
|------|------|------|
| **S** | Systematic（系统化） | 建立完整的知识框架，不遗漏关键维度 |
| **T** | Thorough（彻底） | 多源交叉验证，深入每个关键节点 |
| **O** | Organized（有组织） | 结构化输出，逻辑清晰可追溯 |
| **R** | Rigorous（严谨） | 区分事实与观点，标注证据强度 |
| **M** | Methodical（有条理） | 可复现的研究流程，明确每一步的输入输出 |

## 四步研究提示

### Prompt 1: 研究框架构建
```
请为 [研究主题] 构建一个系统化的研究框架，包括：
1. 核心问题拆解（拆成 5-10 个子问题）
2. 每个子问题的关键概念和术语
3. 研究边界和排除项
4. 与邻近领域的关系图谱
```

### Prompt 2: 多源信息收集
```
针对上述每个子问题，请：
1. 搜索并总结不同来源的观点（学术 / 工业界 / 开源社区）
2. 标注每个来源的可信度（高/中/低）和潜在偏见
3. 识别各来源之间的一致观点和矛盾点
4. 如果某个子问题信息不足，明确标注为「知识缺口」
```

### Prompt 3: 深度分析与综合
```
基于收集的信息，请：
1. 对每个子问题给出综合分析（不简单罗列，而是提炼洞察）
2. 用「主张-证据-推理」结构呈现每个结论
3. 标注每个结论的置信度（确认/很可能/推测/待验证）
4. 识别跨子问题的模式和联系
```

### Prompt 4: 研究简报生成
```
请生成一份面向 [目标读者] 的研究简报：
1. 一页纸核心摘要（TL;DR）
2. 研究框架概览（一图胜千言）
3. 每个子问题的关键发现和结论
4. 开放问题和未来研究方向
5. 推荐阅读清单（按优先级排列）
```

## 质量检查清单

- [ ] 每个结论都有明确来源
- [ ] 区分了事实、观点和推测
- [ ] 标注了知识缺口（不知道比错误更诚实）
- [ ] 不同来源的矛盾点已被识别和讨论
- [ ] 研究简报可在 5 分钟内读完核心内容
- [ ] 研究流程可被另一个人复现

## 触发示例

- "用 STORM 方法研究：Rust 在嵌入式领域的应用现状"
- "帮我做一个 LLM Agent 框架的技术调研，用 STORM 方法"
- "STORM 研究：2025 年前端技术趋势"
- "做一份 LangChain vs LlamaIndex 的深度对比研究"
