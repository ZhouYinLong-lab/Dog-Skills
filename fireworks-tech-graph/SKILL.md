---
name: fireworks-tech-graph
description: >
  技术图生成器——用中文或英文描述系统，几秒钟得到可直接发布的 SVG+PNG 技术图。
  8 种视觉风格（扁平/暗黑极客/蓝图/Notion极简/玻璃态/Claude官方/OpenAI官方/暗黑奢华），
  14 种图类型（架构图·数据流·流程图·序列图·UML全系·ER图·思维导图·时间线等），
  内置 AI/Agent 领域 Pattern（RAG·Agentic Search·Mem0·Multi-Agent·Tool Call）。
  Trigger keywords: 画图, 帮我画, 生成图, 架构图, 流程图, 可视化, 技术图,
  generate diagram, draw diagram, create chart, visualize, architecture diagram,
  flowchart, sequence diagram, data flow, UML, ER图, 网络拓扑, 思维导图,
  RAG架构图, Agent架构图, 微服务图, 系统架构图, 时序图, 技术架构图, SVG.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: design
  source: https://github.com/yizhiyanhua-ai/fireworks-tech-graph (MIT, 8.7k+ stars)
  version: "1.0.0"
  license: MIT
---

# Fireworks Tech Graph — 技术图生成器

> 停止手动画图。用自然语言描述你的系统，几秒钟得到可直接发布的 SVG + PNG 技术图。
> 基于 [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) (8.7k+ stars, MIT 协议)。

## 核心亮点

- **自然语言输入** — 说人话就能出图，不需要写 Mermaid/PlantUML/Graphviz DSL
- **8 种视觉风格** — 扁平图标 / 暗黑极客 / 工程蓝图 / Notion 极简 / 玻璃态卡片 / Claude 官方 / OpenAI 官方 / 暗黑奢华
- **14 种图类型** — 完整 UML 14 图支持 + AI/Agent 领域专用图
- **语义化形状+箭头** — LLM=双边框矩形，Agent=六边形，箭头颜色+线型编码读写/异步/循环语义
- **SVG + PNG 双输出** — SVG 可二次编辑，1920px PNG 直接嵌入文档
- **Loop Engineering** — 生成→校验→渲染→视觉复核→定向修正，有界收敛不无限循环

## 8 种视觉风格

| # | 名称 | 背景 | 适用场景 |
|---|------|------|----------|
| 1 | 扁平图标风 *(默认)* | 白色 | 博客、文档、幻灯片 |
| 2 | 暗黑极客风 | `#0f0f1a` | GitHub README、开发者文章 |
| 3 | 工程蓝图风 | `#0a1628` | 架构设计文档 |
| 4 | Notion 极简风 | 白色 | Notion、Confluence、Wiki |
| 5 | 玻璃态卡片风 | 深色渐变 | 产品官网、Keynote |
| 6 | Claude 官方风格 | 暖奶油色 `#f8f6f3` | Anthropic 风格图 |
| 7 | OpenAI 官方风格 | 纯白 | OpenAI 风格图 |
| 8 | 暗黑奢华风 *(AI手绘)* | `#0a0a0a` | 高级文档、README Hero |

## 支持的图类型

**通用技术图：** 架构图 · 数据流图 · 流程图 · 序列图 · 对比矩阵 · 思维导图 · 时间线 · 网络拓扑

**UML 全系（14种）：** 类图 · 组件图 · 部署图 · 包图 · 复合结构图 · 对象图 · 用例图 · 活动图 · 状态机图 · 序列图 · 通信图 · 时序图 · 交互概览图 · ER 图

**AI/Agent 领域 Pattern：** RAG Pipeline · Agentic RAG · Agentic Search · Mem0 记忆架构 · Agent 记忆类型(5层) · Multi-Agent 协作 · Tool Call 执行流

## 使用示例

### 基础用法
```
画一张 RAG 流程图
```
```
Generate a microservices architecture diagram, dark terminal style
```

### 指定风格
```
画一张微服务架构图，风格 3（工程蓝图风）
```
```
Draw a multi-agent collaboration diagram --style glassmorphism
```

### 完整 Prompt（稳定输出）
```
画一张 Mem0 记忆架构图，扁平图标风。分四个横向区域：Input Layer、Memory Manager、
Storage Layer、Output / Retrieval。包含 User、LLM、Memory Manager、Vector Store、
Graph DB、Context Builder。使用 read/write/control/data 四类语义箭头。
```

## 安装与更新

### 本地安装（推荐，完整功能）
```bash
# Claude Code
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.claude/skills/fireworks-tech-graph

# Codex
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.agents/skills/fireworks-tech-graph
```

### 更新
```bash
git -C ~/.claude/skills/fireworks-tech-graph pull
```

### 依赖（PNG 导出需要）
```bash
# 推荐：cairosvg
python3 -m pip install cairosvg

# 备选：rsvg-convert
brew install librsvg           # macOS
sudo apt install librsvg2-bin  # Ubuntu/Debian
```

> ⚠️ 某些版本的 `npx skills add` 只复制 SKILL.md，会漏掉 `references/`、`scripts/`、`templates/` 等目录。请使用 `git clone` 获得完整安装。

## 与 Mermaid/draw.io 对比

| | Mermaid | draw.io | fireworks-tech-graph |
|--|---------|---------|---------------------|
| 自然语言输入 | ✗ | ✗ | ✅ |
| AI/Agent 领域 Pattern | ✗ | ✗ | ✅ |
| 多种视觉风格 | ✗ | 手动 | ✅ 8 种内置 |
| 高分辨率 PNG 导出 | ✗ | 手动 | ✅ 自动 1920px |
| 语义箭头 | ✗ | 手动 | ✅ 自动 |

## 文件结构

安装后的完整目录：
```
fireworks-tech-graph/
├── SKILL.md                   # 主 Skill 文件
├── references/                # 8 种风格 token + 图标库 + PNG导出指南
├── scripts/                   # 生成/校验/导出脚本
├── templates/                 # 各类型 SVG 模板
├── fixtures/                  # 回归测试用例
├── tests/                     # Validator 测试
└── assets/samples/            # 示例图 PNG
```

## 工作流程

1. **分类** — 识别图类型（架构图/序列图/UML/...）
2. **提取结构** — 从描述中识别层、节点、边、流
3. **规划布局** — 按图类型布局规则排布
4. **加载风格** — 默认风格 1，用户可指定风格 2-8
5. **映射形状** — 按语义形状词汇表选形状
6. **生成 SVG** — Python list 方法逐行生成
7. **校验** — `validate-svg.sh` 检查 XML/路径/箭头碰撞
8. **导出 PNG** — cairosvg 导出 1920px PNG
9. **视觉复核** — 读回 PNG 检查裁切/重叠/标签位置

## 触发词

中英文均可触发：画图、帮我画、生成图、架构图、流程图、可视化、出图、generate diagram、draw diagram、create chart、visualize、architecture diagram、flowchart、sequence diagram、data flow、UML、ER图、网络拓扑、思维导图、RAG架构图、Agent架构图、微服务图、系统架构图、时序图、技术架构图、SVG
