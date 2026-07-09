---
name: architecture-diagram
description: >
  架构图生成器——多轮结构化提问理解系统架构，生成精美深色主题自包含 HTML+SVG 架构图。
  支持系统架构图、云基础设施图、微服务拓扑图、安全架构图、网络拓扑图等。
  Trigger keywords: 架构图, architecture diagram, 系统架构, 画架构图, 云架构,
  微服务架构, 网络拓扑, 安全架构, 基础设施图, system architecture, cloud architecture,
  AWS架构, infra diagram, 部署架构, 技术架构图, generate architecture diagram.
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
  source: Cocoon-AI/architecture-diagram-generator (MIT)
  version: "2.1.0"
  license: MIT
---

# Architecture Diagram Generator — 架构图生成器

> 基于 [Cocoon AI](https://github.com/Cocoon-AI/architecture-diagram-generator) 的 MIT 开源项目深度优化版。
> 核心改进：**Quick Mode / Deep Mode 自适应分支** + 多轮结构化发现协议，轻量场景秒出图，复杂系统深度理解。

## 工作流程总览

```
用户请求
    │
    ▼
┌─────────────────────────────┐
│ Step 0: Mode Detection      │
│ 判断走 Quick 还是 Deep       │
└──────────┬──────────────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
┌────────┐   ┌────────────────────┐
│ Quick   │   │ Deep               │
│ 0-1轮确认│   │ 5轮渐进发现         │
│ 直接生成 │   │ R1→R2→R3→R4→R5     │
└───┬────┘   └─────────┬──────────┘
    │                  │
    └──────┬───────────┘
           ▼
    Phase 1: Layout  →  Phase 2: Generate  →  Phase 3: Verify
```

---

## Step 0: Mode Detection — 自动判断走 Quick 还是 Deep

> **核心原则**：不是所有图都需要大费周章。根据用户请求的特征，自动选择最合适的路径。

### 判断标准

在收到用户请求后，先用以下规则判断模式：

| 信号 | → Quick Mode | → Deep Mode |
|------|-------------|-------------|
| **组件数量** | ≤ 5 个明确组件 | > 5 个，或数量不明 |
| **描述完整度** | 用户说清楚了组件+关系 | 描述模糊（"我们有个微服务系统"） |
| **场景类型** | 局部流程、单链路、概念草图 | 全栈系统、多子系统、企业架构 |
| **用户意图** | "快速画一下" "示意一下" "简单画个" | "完整架构图" "梳理一下" "帮我理清" |
| **领域知识** | 典型/通用架构（AI已有足够知识） | 用户自己的定制系统 |

### Quick Mode 触发示例

> 以下类型请求 → **直接走 Quick Mode，不要追问**：

| 用户说什么 | 为什么 Quick |
|-----------|-------------|
| "画一个 React + Node + PostgreSQL 的三层架构" | 经典三层，AI 完全理解 |
| "画一下 OAuth 2.0 授权码流程" | 标准协议流程 |
| "画出用户登录的时序图，从浏览器到数据库" | 单链路，组件明确 |
| "给我一个典型的 AWS serverless 架构" | 通用参考架构 |
| "CDN → ALB → ECS → RDS，画出来" | 用户已经列清楚了 |
| "画个简单的微服务示意图，API Gateway + 3个服务 + Kafka" | 组件数量少且明确 |
| "把这个数据流画一下：Kafka → Flink → ClickHouse → Grafana" | 线性管道，组件明确 |
| "示意一下前端调用后端的认证流程" | 示意级别，不需要精确 |

### Deep Mode 触发示例

> 以下类型请求 → **走 Deep Mode 5轮发现**：

| 用户说什么 | 为什么 Deep |
|-----------|------------|
| "帮我梳理我们电商系统的完整架构" | 大型系统，需要理解业务 |
| "画一下我们公司的技术架构图" | 需要大量追问才能搞清楚 |
| "我想重构现有系统，先画个现状图" | 需要深入理解现有系统 |
| "画一个包含安全边界的生产环境部署架构" | 多维度（部署+安全+网络） |
| "我们用了 K8s + Istio + 20个微服务，画个图" | 组件多，需要组织 |

### 灰色地带处理

当不确定时：
1. 先用 **1 轮轻量确认**（类似 Quick Mode 的确认方式）
2. 如果用户回复暴露出更多复杂性，自动升级到 Deep Mode
3. 如果用户回复简洁明确，继续 Quick Mode 直接生成

**一句话原则**：**用户说得越清楚，你问得越少；用户说得越模糊，你问得越多。**

---

## Quick Mode — 轻量快速出图

> 适用场景：组件 ≤ 5 个、用户描述清晰、典型通用架构、局部流程/单链路、概念草图。

### Quick Mode 流程

```
用户请求 → [可选：1轮确认] → 直接生成 → 让用户看图迭代
```

### 什么时候跳过确认直接生成

**直接生成**（0 轮确认），当：
- 组件完全明确（用户列出了每个组件名和技术栈）
- 是标准/经典架构（三层架构、OAuth 流程、典型 AWS 架构等）
- 用户说了"简单画个""示意一下""quick"

**1 轮确认**，当：
- 组件明确但关系/方向不清晰
- 有 2-3 种合理的画法（比如数据流方向不确定）
- 用户给了组件但没给连接关系

### Quick Mode 确认模板（1轮即可）

当需要确认时，用极简格式，不要抛出 5 轮问题：

```
## 🏗️ 确认一下（1 分钟）

**我理解的架构**：
  [组件A] ──HTTP──▶ [组件B] ──SQL──▶ [组件C]

**布局方向**: 左→右 / 上→下
**需要标注的协议/端口**: HTTP :443, PostgreSQL :5432

这样画可以吗？还是有什么要调整的？
```

确认后直接进入 Phase 2（跳过 Phase 1 的复杂布局规划，用默认布局）。

### Quick Mode 默认布局规则

不经过 Phase 1 规划时，使用以下默认值：

| 参数 | 默认值 |
|------|--------|
| 布局方向 | 左→右（从左到右数据流） |
| 画布 | `viewBox="0 0 1000 680"` |
| 组件尺寸 | 标准 110×60px |
| 水平间距 | 100px |
| 垂直对齐 | 所有组件垂直居中（y 相同） |
| Header | 从用户请求中提取关键词作为标题 |
| 摘要卡片 | **全部省略**（Quick Mode 不生成摘要卡片，保持简洁） |

---

## Deep Mode — 多轮结构化提问

> 适用场景：组件 > 5 个、大型系统、描述模糊、需要梳理、多子系统、企业级架构。

> **关键原则**：在生成任何 SVG 代码之前，必须通过多轮对话精确理解系统架构。
> 根据用户初始描述的详细程度，自动判断需要深入哪些轮次。
> 如果用户已经提供了非常详细的描述，可以跳过部分轮次并直接确认。

### Round 1: 系统类型识别 & 范围界定

**目标**：确定架构的顶层模式和边界。

向用户提问（根据已有信息选择性提问，不要全部抛出）：

1. **系统类型**：这是什么类型的系统？
   - Web 应用（前后端分离 / SSR / SPA）
   - 微服务系统（服务数量、服务间通信方式）
   - 数据管道 / ETL（数据源→处理→存储链路）
   - 云基础设施（AWS / Azure / GCP / 混合云）
   - 移动端后端 (BFF + Microservices)
   - Serverless 架构
   - 事件驱动架构
   - AI/ML 推理平台
   - 其他：________

2. **规模感**：系统的规模大约多大？
   - 小型（3-7 个核心组件）
   - 中型（8-15 个组件，多个子系统）
   - 大型（15+ 组件，多层嵌套，多区域）

3. **目标受众**：这张图给谁看？
   - 技术团队内部（可以偏技术细节）
   - 跨团队沟通（需要适度简化）
   - 高管/客户（需要高度抽象）
   - 文档/PPT（需要正式美观）

4. **侧重点**：用户最关心哪个维度？
   - 数据流（请求/响应路径）
   - 部署拓扑（物理/虚拟节点）
   - 安全边界（信任域、网络隔离）
   - 高可用/容灾（多区域、故障转移）
   - 全部展示

**输出**：1-2 句话的系统概要 + 架构模式标签。

---

### Round 2: 组件清单盘点

**目标**：穷举所有组件，不遗漏。

根据 Round 1 的系统类型，引导用户分层列出组件：

```
📋 组件清单模板：

[客户端层]
  - 组件名 | 技术栈 | 关键信息（URL/端口/协议）

[接入层]
  - CDN / WAF / API Gateway / Load Balancer | 技术选型 | 配置要点

[应用层]
  - 每个服务/模块 | 语言/框架 | 端口/协议 | 扩缩容策略

[数据层]
  - 数据库类型 | 具体产品 | 用途 | 高可用方案
  - 缓存 | 消息队列 | 对象存储

[基础设施层]
  - 云平台/自建 | 区域 | 编排工具 | 监控告警

[外部依赖]
  - 第三方 API | 身份提供商 | 支付网关 | 邮件服务
```

**交互策略**：
- 如果用户描述模糊（如 "用了一个数据库"），追问具体产品（PostgreSQL? MongoDB?）
- 如果用户遗漏了常见配套组件（如说了 API 但没说 API Gateway），主动提醒
- 如果组件过多（>20），建议拆分多张图或用分组折叠

**输出**：完整的组件表格，每个组件标注：名称、类型、技术栈、备注。

---

### Round 3: 关系与数据流映射

**目标**：精确理解组件间的连接关系。

对 Round 2 的每个组件，逐一确认：

1. **它调用谁？** → 出方向箭头
2. **谁调用它？** → 入方向箭头
3. **通信协议？** → HTTP/REST, gRPC, WebSocket, GraphQL, TCP, UDP, 消息队列
4. **认证方式？** → JWT, OAuth2, mTLS, API Key, 无
5. **数据方向？** → 单向读取 / 双向读写 / 异步推送
6. **是否有特殊流程？** → 启动流程、故障转移路径、定时任务链路

**交互策略**：
- 引导用户按 "请求进来 → 经过 → 到达 → 返回" 的路径描述
- 对微服务系统，额外确认服务发现、配置中心、分布式追踪的位置
- 对事件驱动系统，确认生产者→Topic→消费者的完整链路

**输出**：连接关系列表，每条标注：from → to | 协议 | 认证 | 备注。

---

### Round 4: 基础设施与部署上下文

**目标**：理解运行环境的物理/虚拟拓扑。

仅在 Round 1 确认需要展示部署拓扑时深入：

1. **云平台**：AWS / Azure / GCP / 阿里云 / 腾讯云 / 自建机房？
2. **区域部署**：单区域？多区域？具体 region 名称？
3. **容器化**：Kubernetes? Docker Compose? 无容器？
4. **网络拓扑**：VPC / 子网划分？公网/私网暴露面？
5. **CI/CD 链路**：是否需要展示构建→测试→部署流程？
6. **监控告警**：Prometheus + Grafana? Datadog? CloudWatch?

**输出**：基础设施上下文摘要。

---

### Round 5: 安全边界确认

**目标**：明确信任域和隔离边界。

1. **安全组/防火墙规则**：哪些端口对谁开放？
2. **网络隔离**：公网子网 / 私有子网 / 数据库子网？
3. **认证流程**：用户登录的完整路径（前端→Auth Provider→Token 签发→验证）
4. **敏感数据处理**：PII 数据在哪里？加密方式？
5. **合规要求**：SOC2 / HIPAA / PCI-DSS？

**输出**：安全边界列表 + 安全组标记位置。

---

### Discovery 完成确认

在进入 Phase 1 之前，向用户输出一份 **架构理解摘要**：

```
## 🏗️ 架构理解确认

**系统类型**: [识别的模式]
**规模**: [小型/中型/大型]
**组件总数**: [N] 个

**组件清单**:
  [Frontend] React SPA → CloudFront CDN
  [Backend]  Node.js/Express API (:3000)
  [Database] PostgreSQL (RDS, Multi-AZ)
  ...

**关键数据流**:
  用户 → CloudFront → ALB → API → RDS
  认证流: 用户 → Cognito → JWT → API 验证
  ...

**部署**: AWS us-east-1, EKS 集群, 2个AZ

以上理解是否正确？确认后我开始画图。
```

**只有在用户确认后，才进入 Phase 1。**

---

## Phase 1: Layout Planning — 布局规划（Deep Mode）

> 基于 Phase 0 的发现结果，在生成代码前先规划布局。
> **Quick Mode 跳过此阶段**，使用默认布局参数（左→右，组件垂直居中）。

### 1.1 布局模式选择

根据系统类型自动选择最佳布局：

| 系统类型 | 推荐布局 | 说明 |
|---------|---------|------|
| Web 应用（前后端） | **左→右** | 客户端在左，逐步向右到数据层 |
| 微服务系统 | **左→右 + 分层** | 入口层→业务服务层→数据层 |
| 数据管道/ETL | **左→右** | Source→Transform→Sink 线性流 |
| 云基础设施 | **自由分组** | 按 VPC/子网/区域分组 |
| 事件驱动 | **上→下** | Producer→Bus→Consumer 流 |
| 安全架构 | **洋葱模型** | 外层→内层信任域递增 |

### 1.2 画布尺寸计算

```
画布宽度 = max(1000, 组件列数 × 180 + 边距 × 2)
画布高度 = max(680, 组件行数 × 100 + 边界框高度 + 图例高度 + 边距)
```

### 1.3 组件分组与 z-order 规划

- **Region boundaries** (最底层)
- **Security groups** (第二层)
- **Connection arrows** (第三层，在组件后面)
- **Component boxes** (第四层，半透明背景 + 不透明底层遮挡箭头)
- **Labels & annotations** (最顶层)

### 1.4 配色分配

按组件类型自动分配（参见 Design System 章节的颜色表）：
- Frontend → Cyan
- Backend → Emerald
- Database / AI/ML → Violet
- Cloud / AWS / Infrastructure → Amber
- Security / Auth → Rose
- Message Bus / Event → Orange
- External / Third-party → Slate

---

## Phase 2: Code Generation — 代码生成

### 2.1 使用模板

从 `resources/template.html` 获取基础模板，然后：

1. 更新 `<title>` 和 Header 文字
2. 调整 SVG `viewBox` 尺寸（根据 Phase 1 计算）
3. 按 Phase 1 布局逐一定位每个组件（参考 Design System 的 Component Box Pattern）
4. 绘制所有连接箭头（在组件之前，参见 z-order 规则）
5. 添加安全组虚线框、区域边界框
6. 填充 3 张摘要卡片（关键指标、技术栈、安全要点）
7. 添加图例（放在所有边界框之外）
8. 更新 Footer 元数据

### 2.2 关键约束

- **必须**保留模板中的 2 个 CDN script（html2canvas + jsPDF，含 SRI hash）
- **必须**保留 `id="report-container"` 在外层容器
- **必须**保留 `.toolbar` 和相关 JS 导出函数
- **禁止**引入新的外部依赖（除 Google Fonts 外）

---

## Phase 3: Quality Verification — 质量验证

生成 HTML 后，逐项检查。Quick Mode 只需检查标有 ⚡ 的项目（核心项），Deep Mode 需全部检查。

### 自检清单

- [ ] ⚡ **间距**：所有组件间垂直间距 ≥ 40px，水平间距 ≥ 30px
- [ ] ⚡ **无重叠**：组件不重叠，箭头不穿过文字
- [ ] **图例位置**：图例在所有边界框下方 ≥ 20px（Quick Mode 如无图例可跳过）
- [ ] ⚡ **箭头遮蔽**：每个组件有 `fill="#0f172a"` 底层 rect 遮蔽穿透的箭头
- [ ] ⚡ **箭头方向**：所有箭头终点指向正确方向
- [ ] ⚡ **完整性**：用户提到的所有组件都在图中
- [ ] ⚡ **颜色一致**：同类组件使用相同的配色方案
- [ ] ⚡ **文字可读**：字号 ≥ 7px，标签不溢出组件边界
- [ ] ⚡ **导出功能**：工具栏 HTML + JS 完整，html2canvas/jsPDF CDN 标签完整
- [ ] ⚡ **移动端**：容器有 `overflow-x: auto`，小屏可横向滚动
- [ ] **摘要卡片**：3 张卡片内容准确（**Deep Mode only** — Quick Mode 不生成摘要卡片）

### 修复优先级

1. 功能性问题（箭头指向错误、组件缺失）→ 立即修复
2. 视觉问题（重叠、溢出）→ 调整坐标
3. 增强性改进（更好的标注、更美观的布局）→ 可选修复

---

## Design System

> 以下设计规范继承自上游 Cocoon AI v1.1，保持不变。

### Color Palette

| Component Type | Fill (rgba) | Stroke |
|---------------|-------------|--------|
| Frontend | `rgba(8, 51, 68, 0.4)` | `#22d3ee` (cyan-400) |
| Backend | `rgba(6, 78, 59, 0.4)` | `#34d399` (emerald-400) |
| Database | `rgba(76, 29, 149, 0.4)` | `#a78bfa` (violet-400) |
| AWS/Cloud | `rgba(120, 53, 15, 0.3)` | `#fbbf24` (amber-400) |
| Security | `rgba(136, 19, 55, 0.4)` | `#fb7185` (rose-400) |
| Message Bus | `rgba(251, 146, 60, 0.3)` | `#fb923c` (orange-400) |
| External/Generic | `rgba(30, 41, 59, 0.5)` | `#94a3b8` (slate-400) |

### Typography

- **Font**: JetBrains Mono (Google Fonts)
- **Sizes**: 12px (组件名), 9px (副标签), 8px (注释), 7px (微型标签)
- **Weights**: 400 (正文), 500 (强调), 600-700 (标题)

### Visual Elements

- **Background**: `#020617` (slate-950) + 40px 网格
- **Component boxes**: `rx="6"`, 1.5px stroke, 半透明 fill
- **Security groups**: `stroke-dasharray="4,4"`, 透明 fill, rose 色
- **Region boundaries**: `stroke-dasharray="8,4"`, amber 色, `rx="12"`
- **Arrows**: SVG `<marker>` 箭头, `#64748b` 颜色
- **Auth flows**: 虚线 `stroke-dasharray="5,5"`, rose 色

### Arrow Masking

箭头在 SVG 中先绘制，组件半透明 fill 会让箭头透出。解决方案：

```svg
<!-- 不透明底层遮挡箭头 -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="#0f172a"/>
<!-- 半透明风格层在顶层 -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="rgba(...)" stroke="..." stroke-width="1.5"/>
```

### Spacing Rules

- 标准组件高度: 60px (服务), 80-120px (大型组件)
- 垂直间距: ≥ 40px
- 消息总线: 放在间隙中间，不重叠相邻组件
- 图例: 在所有边界框下方 ≥ 20px

---

## Iteration Protocol — 修改迭代协议

用户提出修改需求时，按以下优先级处理：

| 修改类型 | 示例 | 处理方式 |
|---------|------|---------|
| 增删组件 | "加一个 Redis 缓存" | 重新计算受影响区域的坐标 |
| 修改连接 | "API 不直连 DB，走 DAO 层" | 调整箭头路径 |
| 样式调整 | "把 Frontend 改成蓝色" | 修改颜色常量 |
| 布局调整 | "数据库放到底部" | 局部重新布局 |
| 标注修正 | "端口号不对，应该是 8080" | 修改文本内容 |

**重要**: 修改后必须重新执行 Phase 3 的间距和重叠检查。

---

## 安装方式

### Claude Code CLI（本项目）

```bash
cp -r architecture-diagram/ ~/.claude/skills/architecture-diagram/
```

### Claude.ai

下载 `architecture-diagram.zip` 并通过 Skills 面板上传。

---

## 触发示例

**Quick Mode（快速出图）**：
- "画一个 React + Node.js + PostgreSQL 的三层架构"
- "画一下 OAuth 2.0 授权码流程"
- "简单画个 CDN → ALB → ECS → RDS 的图"
- "给我一个典型的 AWS serverless 架构"
- "示意一下前端调后端的认证流程"
- "画个 Kafka → Flink → ClickHouse 数据管道"

**Deep Mode（深度梳理）**：
- "帮我梳理一下我们电商系统的完整架构"
- "画一个包含安全边界的生产环境部署架构"
- "我们用了 K8s + Istio + 20 个微服务，画个图"
- "我想重构现有系统，先画个现状架构图"

---

## 输出示例

参考 `examples/` 目录下的示例 HTML 文件：
- `web-app.html` — Web 应用三层架构
- `aws-serverless.html` — AWS Serverless 架构
- `microservices.html` — 微服务 + Kubernetes 架构

---

## 上游致谢

本 skill 基于 [Cocoon AI 的 architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) (MIT License) 深度优化。

**v2.1 核心改进**：
- ✅ **Quick Mode / Deep Mode 自适应分支**：轻量场景秒出图（0-1轮确认），复杂系统深度发现（5轮）
- ✅ **Step 0: Mode Detection**：自动判断走哪个模式，不是所有图都要大费周章
- ✅ Quick Mode 省略摘要卡片和复杂布局规划，保持输出简洁
- ✅ 增加 **Phase 1: Layout Planning 布局规划**（模式选择 + 画布计算）
- ✅ 增加 **Phase 3: Quality Verification 质量验证清单**（区分 Quick/Deep）
- ✅ 增加 **Iteration Protocol 迭代修改协议**
- ✅ 增加中文触发关键词和双语支持
- ✅ 保留上游 v1.1 的完整设计系统、模板和导出功能
