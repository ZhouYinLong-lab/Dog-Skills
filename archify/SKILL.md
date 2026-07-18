---
name: archify
description: >
  JSON 驱动架构图生成器——5 种图类型（架构图·工作流·时序图·数据流·生命周期），
  深色/浅色主题切换，一键导出 PNG/JPEG/WebP/双主题 SVG。Schema 校验 +
  布局自动检测（重叠/碰撞/越界）。支持自然语言描述或粘贴 Mermaid 代码
  自动转为 archify 风格。基于 Cocoon-AI 演进版，工程化程度最高。
  Trigger keywords: 架构图, 工作流图, 时序图, 数据流图, 生命周期图,
  workflow diagram, sequence diagram, dataflow, lifecycle diagram,
  architecture diagram, archify, 状态机图, 管道图, ETL图,
  Mermaid转图, 双主题图, JSON驱动图, 自动布局图.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: development
  source: https://github.com/tt-a1i/archify (MIT)
  based_on: Cocoon-AI/architecture-diagram-generator (MIT v1.0)
  upstream-author: tt-a1i
  version: "2.11"
  license: MIT
---

# Archify — JSON 驱动架构图生成器

> 5 种图类型 × Schema 校验 × 双主题切换 × Mermaid 兼容。工程化程度最高的图工具。
> 上游来源: [tt-a1i/archify](https://github.com/tt-a1i/archify) (MIT v2.11)，基于 Cocoon-AI 演进

## 在 Dog-Skills 图技能矩阵中的位置

```
architecture-diagram     →  系统架构（Quick/Deep双模式，HTML+SVG，深色主题）
fireworks-tech-graph     →  多风格技术图（8风格14类型，SVG+PNG）
excalidraw-diagram       →  手绘协作图（.excalidraw可编辑）
text-logic-diagram       →  论述逻辑图（递进/流程/循环/层次/对比/矩阵）
archify ⭐               →  工程化架构图（5类型×JSON Schema×自动校验×Mermaid输入）
                           ↑ 独有: workflow/sequence/dataflow/lifecycle 四种工程图类型
```

**什么时候用 archify 而不是其他图技能？**
- 需要画**工作流/时序图/数据流/生命周期图** → archify 是唯一支持这些类型的
- 需要 **Schema 保证不出错** → archify 的 JSON Schema + 自动布局校验
- 有 Mermaid 代码想"美化" → archify 读 Mermaid 结构，按自己风格重绘
- 需要导出一个在明暗背景下都好看的 SVG → archify 独有的双主题 SVG

---

## 5 种图类型

| 类型 | 用途 | 触发关键词 |
|------|------|-----------|
| `architecture` | 系统组件、云资源、服务、安全边界、基础设施 | "架构图" / "系统图" / "云架构" |
| `workflow` | 技术流程、审批流、CI/CD、Runbook、事件响应 | "工作流" / "流程图" / "审批流" / "CI/CD" |
| `sequence` | API 调用链、请求生命周期、缓存回退、异步追踪 | "时序图" / "调用链" / "交互流程" |
| `dataflow` | 数据管道、ETL/ELT、PII 隔离、数据血缘 | "数据流" / "ETL" / "数据管道" / "数据血缘" |
| `lifecycle` | 状态机、状态转换、重试、终止状态 | "生命周期" / "状态机" / "状态转换" |

---

## 核心工作流

```
用户需求 →  ① 识别图类型
          →  ② 读 Schema + 示例（schemas/<type>.schema.json + examples/*.json）
          →  ③ 写 JSON（按 Schema 填组件/节点/连线）
          →  ④ 渲染: node bin/archify.mjs render <type> <input>.json <output>.html
          →  ⑤ 校验: node bin/archify.mjs validate <type> <input>.json
          →  交付自包含 HTML（含主题切换 + 导出菜单）
```

---

## 每种类型的 JSON 结构

### Architecture（架构图）

```json
{
  "schema_version": 1, "diagram_type": "architecture",
  "meta": { "title": "Web App", "subtitle": "3-tier SaaS", "output": "web-app.html" },
  "components": [
    { "id": "users", "type": "external", "label": "Users", "pos": [40, 300] },
    { "id": "api", "type": "backend", "label": "API", "pos": [460, 300] },
    { "id": "db", "type": "database", "label": "PostgreSQL", "pos": [680, 300] }
  ],
  "boundaries": [
    { "kind": "region", "label": "AWS us-west-2", "wraps": ["api", "db"] }
  ],
  "connections": [
    { "from": "users", "to": "api", "label": "HTTPS", "variant": "emphasis" },
    { "from": "api", "to": "db", "label": "SQL" }
  ]
}
```

支持自由坐标 (`pos`) 和网格布局 (`layout.mode: "grid"`) 两种模式。

### Workflow（工作流）

```json
{
  "schema_version": 1, "diagram_type": "workflow",
  "meta": { "title": "Release Workflow" },
  "lanes": [
    { "id": "dev", "label": "Developer" },
    { "id": "ci", "label": "CI" },
    { "id": "exceptions", "label": "Exception", "variant": "exception" }
  ],
  "nodes": [
    { "id": "pr", "lane": "dev", "col": 0, "type": "frontend", "label": "Open PR" },
    { "id": "build", "lane": "ci", "col": 1, "type": "backend", "label": "Build", "tag": "blocking" }
  ],
  "edges": [
    { "from": "pr", "to": "build", "label": "webhook", "variant": "emphasis" }
  ]
}
```

6 列固定网格 + lane/phases/groups 分组系统。

### Sequence（时序图）

```json
{
  "schema_version": 1, "diagram_type": "sequence",
  "meta": { "title": "Cache Miss Request" },
  "participants": [
    { "id": "web", "type": "frontend", "label": "Web App" },
    { "id": "api", "type": "backend", "label": "API" }
  ],
  "messages": [
    { "from": "web", "to": "api", "y": 200, "label": "GET /data", "variant": "emphasis" },
    { "from": "api", "to": "web", "y": 290, "label": "200 JSON", "variant": "return" }
  ]
}
```

最多 8 个参与者，消息 y 坐标控制时序。

### Dataflow（数据流）

```json
{
  "schema_version": 1, "diagram_type": "dataflow",
  "meta": { "title": "Product Analytics" },
  "stages": [ { "label": "Sources" }, { "label": "Ingest" }, { "label": "Store" } ],
  "nodes": [
    { "id": "web", "type": "frontend", "label": "Web App", "stage": 0, "row": 0 },
    { "id": "kafka", "type": "messagebus", "label": "Kafka", "stage": 1, "row": 0 }
  ],
  "flows": [
    { "from": "web", "to": "kafka", "label": "events", "classification": "PII touch" }
  ]
}
```

2-5 阶段 × 5 行网格，flow 标签必填，classification 标注数据敏感性。

### Lifecycle（生命周期）

```json
{
  "schema_version": 1, "diagram_type": "lifecycle",
  "meta": { "title": "Agent Run Lifecycle" },
  "lanes": [
    { "id": "main", "label": "Lifecycle" },
    { "id": "waiting", "label": "Interruptions" },
    { "id": "terminal", "label": "Terminal exits" }
  ],
  "states": [
    { "id": "queued", "type": "start", "label": "Queued", "lane": "main", "col": 0 },
    { "id": "running", "type": "active", "label": "Executing", "lane": "main", "col": 2 },
    { "id": "done", "type": "success", "label": "Completed", "lane": "terminal", "col": 2 }
  ],
  "transitions": [
    { "from": "queued", "to": "running", "variant": "emphasis" },
    { "from": "running", "to": "done", "label": "success" }
  ]
}
```

main/terminal 为保留 lane id，其他 lane 共享中间事件带。

---

## Mermaid 输入支持

粘贴 Mermaid 代码，archify 读取结构后按自己的风格重绘：

| Mermaid 类型 | Archify 模式 | 映射规则 |
|-------------|-------------|---------|
| `flowchart` / `graph` | `workflow` | subgraph→lane; `{}`菱形→决策节点; 标签→edge label |
| `sequenceDiagram` | `sequence` | participant→participant; `->>`→消息; `Note`→message note |
| `stateDiagram` | `lifecycle` | state→state (自动推断 type); `[*]`→start/terminal |

---

## 独有特性

### 1. 双主题 SVG 导出
导出的 SVG 跟随宿主页面的 `prefers-color-scheme`，一份文件在明暗背景下都正确显示。适合 GitHub README。

### 2. Schema 校验 + 布局自动检测
```
node bin/archify.mjs validate <type> <input>.json --json
node bin/archify.mjs check <output>.html
```
自动检测：组件重叠、标签碰撞、越界、对角线箭头、箭头穿越图例、非有限坐标值。

### 3. CSS 变量颜色系统
```svg
<!-- ✅ 正确：使用 CSS 类，主题切换生效 -->
<rect class="c-backend" stroke-width="1.5"/>
<text class="t-primary">API Server</text>

<!-- ❌ 错误：硬编码颜色，深色模式下不可见 -->
<rect fill="rgba(8,51,68,0.4)" stroke="#22d3ee"/>
```

### 4. 布局检查器
```bash
node bin/archify.mjs inspect architecture my.json
# 输出: 组件矩形、边界框、连接点路径、标签位置
```

---

## 布局原则（写 JSON 前必读）

1. **一条主路径** — 左→右（架构）或 lane→列（工作流）。读者应能无交叉线追踪主路径
2. **少标签** — 只标注跨边界或非显而易见的转换。相邻步骤不加标签
3. **短分支** — 权限/存储/bot/CI 从主路径最近节点上下连接，不斜穿其他组件
4. **卡片放细节** — 策略/技术栈说明/额外连接放 summary cards，不画箭头
5. **模式匹配** — 流程/审批/工具调用→workflow/sequence。≤12 节点组件图→architecture。超过 20 条边→删减

---

## 与 architecture-diagram 的关系

```
architecture-diagram (Dog-Skills)     archify (Dog-Skills)
        │                                    │
  基于 Cocoon-AI v1.1                  基于 Cocoon-AI v1.0 → v2.11
  Quick/Deep 双模式                    JSON Schema 驱动
  多轮对话提取需求                      5 种图类型 × 5 套 Schema
  适合: 不写代码的用户                  适合: 愿写 JSON 的开发者
  输出: 深色 HTML+SVG                  输出: 双主题 HTML+SVG+PNG/JPEG/WebP
```

两者**互补**而非替代：
- 用户说"帮我画个架构图" → architecture-diagram（对话交互）
- 用户说"给我一个精确的 CI/CD 工作流 JSON 模板" → archify
- 需要 workflow/sequence/dataflow/lifecycle → 只有 archify 支持

---

## 安装方式

### Claude Code

```bash
cp -r archify/ ~/.claude/skills/archify/
```

### 上游完整安装（含渲染器和 Schema）

```bash
npx skills add tt-a1i/archify
```

安装后运行 `node bin/archify.mjs doctor` 验证环境，`node bin/archify.mjs demo <dir>` 生成示例。

---

## 上游致谢

基于 [tt-a1i/archify](https://github.com/tt-a1i/archify) (MIT v2.11)，作者 tt-a1i。继承自 [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) (MIT)。
