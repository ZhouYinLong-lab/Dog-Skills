---
name: excalidraw-diagram
description: >
  手绘风技术图生成器——自然语言描述系统，输出可编辑的 .excalidraw 文件。
  支持 9 种图类型（流程图·关系图·思维导图·架构图·数据流图·泳道业务流·
  类图·时序图·ER 图）。内置 Prompt 优化层，生成前自动帮你梳理组件和关系，
  确认后再出图。与 architecture-diagram（正式风）和 fireworks-tech-graph
  （多风格）形成互补三角——Excalidraw 走"AI起稿→人工精调"的协作路线。
  Trigger keywords: 手绘风格图, 白板图, Excalidraw, 可编辑图表,
  画个草图, 手绘架构图, 手绘流程图, draw diagram, whiteboard sketch,
  excalidraw diagram, hand-drawn diagram, 画个示意草图,
  画个流程图草稿, 协作白板图, 画图然后我再改, 生成excalidraw,
  create excalidraw, make a sketch diagram, 画草图.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
metadata:
  category: design
  source: https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator (MIT)
  upstream: github/awesome-copilot
  version: "1.0.0"
  license: MIT
---

# Excalidraw Diagram Generator — 手绘风技术图生成器

> 说人话 → 得草图。生成可编辑的 `.excalidraw` 文件，拖进 [excalidraw.com](https://excalidraw.com) 就能继续改。
> 与 `architecture-diagram`（正式文档风）和 `fireworks-tech-graph`（多风格成品图）形成互补三角。
> 上游来源：[github/awesome-copilot](https://github.com/github/awesome-copilot) (MIT, 36K+ ⭐)

## 三种图技能的分工

```
architecture-diagram     →  正式文档用（深色HTML/SVG，精美专业，一次性成品）
fireworks-tech-graph     →  多场景用（8风格14类型，SVG+PNG，可直接发布）
excalidraw-diagram       →  协作讨论用（手绘风.excalidraw，可后续编辑）  ← NEW
```

**什么时候用 Excalidraw 而不是另外两个？**
- 你需要在技术方案评审中和同事一起改图 → Excalidraw
- 你想要手绘白板风格，而不是精致的工程图 → Excalidraw
- 你还没想清楚最终结构，需要先画个草稿 → Excalidraw
- 你需要导出后放到文档里继续标注 → Excalidraw（编辑后导出PNG/SVG）

---

## 核心工作流：Prompt 优化 → 确认 → 生成

本 skill 在 Excalidraw 生成之上增加了一个 **Prompt 优化层**。每次生成图之前，先帮你梳理组件、关系和布局，确认后再出图。

### 完整流程

```
用户描述想要的图
       │
       ▼
┌──────────────────────────┐
│ ① Prompt 分析与优化       │  梳理：图类型·组件清单·连接关系·布局方向
│    输出：结构化图描述     │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ ② 用户审阅               │  ← AskUserQuestion
│    · 确认：直接生成       │    展示结构化描述
│    · 修改：增删组件/调关系 │    等用户决定
│    · 取消：重新描述       │
└──────────┬───────────────┘
           │
           ▼  (用户确认后)
┌──────────────────────────┐
│ ③ 生成 .excalidraw 文件  │  用最终确认的描述生成 JSON
│    写入本地文件           │
└──────────────────────────┘
```

---

## Step 1: Prompt 分析与优化

收到用户的图需求后，按以下四步逐项检查和补全：

### 1.1 识别图类型

| 用户描述中的关键词 | 图类型 |
|------------------|--------|
| "流程" / "步骤" / "工序" / "workflow" | **Flowchart** 流程图 |
| "关系" / "关联" / "ER" / "实体" | **Relationship Diagram** / **ER Diagram** |
| "思维导图" / "脑图" / "mindmap" | **Mind Map** |
| "架构" / "系统" / "architecture" | **Architecture Diagram** |
| "数据流" / "数据管道" / "ETL" | **Data Flow Diagram** |
| "泳道" / "跨部门" / "swimlane" | **Swimlane Business Flow** |
| "类图" / "UML" / "class diagram" | **Class Diagram** |
| "时序" / "交互" / "sequence" | **Sequence Diagram** |
| "表结构" / "数据库" / "ER图" | **ER Diagram** |

### 1.2 梳理组件清单

从描述中提取所有组件，如果缺少关键信息则补全：

```
📋 组件清单:
  1. [组件名] | 类型: [服务/数据库/用户/外部系统/...] | 备注: [关键信息]
  2. ...
  
总计: N 个组件
```

如果组件数量 > 15，建议拆分为两张图。

### 1.3 明确连接关系

```
🔗 关系清单:
  [组件A] ──[关系类型]──▶ [组件B]
  例如: 用户服务 ──HTTP──▶ 订单服务
      订单服务 ──写入──▶ PostgreSQL
```

### 1.4 推荐布局方向

| 图类型 | 推荐布局 |
|--------|---------|
| 流程图 | 上→下 或 左→右 |
| 架构图 | 左→右（分层） |
| 数据流图 | 左→右 |
| 思维导图 | 中心→四周辐射 |
| 泳道图 | 上→下（泳道横向） |
| 时序图 | 上→下 |
| ER 图 | 自由分布 |

---

## Step 2: 优化结果展示模板

每次分析后，用以下格式展示给用户：

```
## 🏗️ 图结构确认

**图类型**: [识别出的类型]
**布局方向**: [推荐方向]
**组件总数**: N 个

**组件清单**:
  ├─ [组件1] — [类型]
  ├─ [组件2] — [类型]
  └─ ...

**连接关系**:
  [组件A] → [组件B] ([协议/操作])
  ...

**颜色方案**: [手绘默认配色 / 用户指定]

---
请选择：
1. ✅ **确认生成** — 按此结构生成 .excalidraw 文件
2. ✏️ **我要修改** — 告诉我你想调整什么
3. ❌ **取消** — 重新描述需求
```

---

## Step 3: 生成 .excalidraw 文件

用户确认后，生成标准的 `.excalidraw` JSON 文件。

### 设计规范

#### 手绘风格参数

```json
{
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": 20
  }
}
```

关键元素属性：
- `strokeSharpness: "round"` — 圆角线条（手绘感）
- `roughness: 1` — 轻微粗糙度
- `fillStyle: "hachure"` — 手绘填充风格（交叉线）
- `opacity: 100`

#### 语义配色（8色系统）

| 颜色 | 用途 | Hex |
|------|------|-----|
| 蓝色 | 服务/后端组件 | `#1e80ff` |
| 绿色 | 数据库/存储 | `#2ecc71` |
| 红色 | 外部系统/API | `#e74c3c` |
| 橙色 | 消息队列/事件 | `#f39c12` |
| 紫色 | 认证/安全 | `#9b59b6` |
| 青色 | 前端/客户端 | `#1abc9c` |
| 灰色 | 通用/其他 | `#95a5a6` |
| 黄色 | 高亮/重点 | `#f1c40f` |

#### 布局网格

- 组件默认大小：160×80px
- 水平间距：80px
- 垂直间距：60px
- 字体大小：20px（标题），16px（正文）
- 字体：系统默认手写体（Virgil / Comic Shanns / 或 Excalidraw 默认字体）

### 文件保存

生成的 `.excalidraw` 文件保存到当前工作目录，命名规则：
```
<图类型>-<简短描述>.excalidraw
例如: architecture-ecommerce-system.excalidraw
```

文件可使用以下方式打开：
1. 拖入 [excalidraw.com](https://excalidraw.com) 在线编辑
2. VS Code 安装 Excalidraw 扩展后直接打开
3. Obsidian 安装 Excalidraw 插件后打开

---

## 支持的图类型详解

### 1. Flowchart 流程图
```
节点: 矩形(流程步骤) / 菱形(决策) / 圆角矩形(开始/结束)
连线: 单箭头
方向: 上→下 或 左→右
```

### 2. Architecture Diagram 架构图
```
节点: 矩形分组（前端层/应用层/数据层）
连线: 带标签箭头（HTTP/gRPC/SQL）
方向: 左→右分层
```

### 3. Mind Map 思维导图
```
根节点: 居中
子节点: 放射状分布
连线: 曲线连接
```

### 4. Data Flow Diagram 数据流图
```
节点: 圆角矩形（处理节点）/ 矩形（数据存储）
连线: 带数据描述箭头
方向: 左→右
```

### 5. Swimlane Business Flow 泳道业务流
```
泳道: 横向或纵向分组框
节点: 在各泳道内放置
连线: 跨泳道箭头
```

### 6. Sequence Diagram 时序图
```
参与者: 顶部水平排列
生命线: 垂直虚线
消息: 水平箭头
```

### 7. Class Diagram 类图
```
类框: 三行矩形（类名 / 属性 / 方法）
连线: 继承(空心三角) / 关联(实线) / 依赖(虚线)
```

### 8. ER Diagram ER图
```
实体: 矩形（实体名在上）
属性: 椭圆
连线: 菱形(关系类型)
```

### 9. Relationship Diagram 关系图
```
节点: 矩形/圆形
连线: 带文字标签
布局: 自由分布
```

---

## 迭代修改协议

生成图后，用户可以继续对话修改，无需重新生成整个文件：

| 修改类型 | 示例 | 处理方式 |
|---------|------|---------|
| 增删节点 | "加一个 Redis 缓存" | 计算新节点位置，插入 JSON elements 数组 |
| 修改连接 | "订单服务不直连数据库" | 移除旧连线，添加新连线 |
| 调整布局 | "把数据库层放到底部" | 重新计算受影响节点的坐标 |
| 修改文字 | "用户服务改名叫 User Service" | 修改对应 text 元素的 text 字段 |
| 颜色调整 | "把所有的数据库改成绿色" | 修改对应元素的 strokeColor |
| 添加标注 | "在这里加个注释" | 添加 text + arrow 元素 |

---

## 与 Mermaid/draw.io 对比

| | Mermaid | draw.io | Excalidraw (本 skill) | architecture-diagram | fireworks-tech-graph |
|--|---------|---------|----------------------|---------------------|---------------------|
| 自然语言输入 | ✗ | ✗ | ✅ | ✅ | ✅ |
| 输出格式 | 渲染图 | .drawio XML | .excalidraw JSON | HTML+SVG | SVG+PNG |
| 可继续编辑 | ✗ | ✅ | ✅ | ✗ | ✗ |
| 手绘风格 | ✗ | ✗ | ✅ | ✗ | ✗ |
| 正式风格 | ✗ | ✅ | ✗ | ✅ | ✅ |
| 协作白板 | ✗ | ✗ | ✅ | ✗ | ✗ |
| 导出 PNG/SVG | ✅ | ✅ | ✅ (通过excalidraw.com) | ✅ | ✅ |

---

## 安装方式

### Claude Code（本项目）

```bash
cp -r excalidraw-diagram/ ~/.claude/skills/excalidraw-diagram/
```

### 上游安装（通过 npx）

```bash
npx skills add https://github.com/github/awesome-copilot --skill excalidraw-diagram-generator
```

本 skill 在上游基础上增加了 Prompt 优化层和双语支持。

---

## 触发示例

- "画一个电商订单系统的架构草图"
- "用 Excalidraw 画个用户登录流程图"
- "帮我画一个微服务的泳道图，我之后还要改"
- "画个思维导图，梳理一下这个项目的模块结构"
- "create a hand-drawn architecture diagram for my SaaS app"
- "make an excalidraw flowchart of the CI/CD pipeline"
- "画个数据库 ER 图的草稿"
- "generate an excalidraw sequence diagram for OAuth flow"
- "画个草图示意一下数据怎么从前端流到数据库"

---

## 上游致谢

本 skill 基于 [github/awesome-copilot](https://github.com/github/awesome-copilot) 的 excalidraw-diagram-generator (MIT License)。

**v1.0 增强**：
- ✅ **Prompt 优化层**：生成前自动梳理组件·关系·布局，降低返工率
- ✅ **4 步分析框架**：图类型识别 → 组件梳理 → 关系映射 → 布局推荐
- ✅ **语义 8 色系统**：按组件类型自动分色，视觉一致
- ✅ **迭代修改协议**：支持增量修改，不需要整图重新生成
- ✅ **中文触发关键词和双语支持**
- ✅ **与 architecture-diagram / fireworks-tech-graph 的明确分工指南**
