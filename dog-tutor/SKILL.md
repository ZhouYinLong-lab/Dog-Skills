---
name: dog-tutor
description: >
  智能教程编制系统(Dog-Tutor)。通过6阶段对话引导,将任意主题的学习资料转化为高质量MkDocs Material格式教程。
  支持技术/商业/学术/生活/艺术全领域,四级受众自适应,四种比喻风格,主题无关的通用教程生成引擎。
  适用于技术文档编写、课程开发、知识整理、培训材料制作、入门指南撰写等场景。
  Trigger keywords: 生成教程, 创建教程, 编制学习材料, 设计课程大纲, 写入门指南, 做教程,
  tutorial, course, 教程, 课件, 培训材料, 编写文档, Dog-Tutor, smarttutor.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
  - WebFetch
metadata:
  category: [learning, education-meta-skill]
  version: "1.0.0"
  license: MIT
  based_on: SmartTutor Generator v1.1 by 莫弈 (2026)
---

# Dog-Tutor — 智能教程编制系统

将任意主题的学习资料转化为高质量 MkDocs Material 格式教程的元技能。
通过 6 阶段结构化对话,从资料摄入到发布,全流程可控。

**核心理念**: 主题无关、受众自适应、风格可选、分阶段交互、标准输出、结果可复用。

---

## 触发条件

### 明确触发词
- "帮我生成教程" / "创建一个教程" / "编制学习材料"
- "设计课程大纲" / "写入门指南" / "做一份XX教程"
- "用Dog-Tutor做教程"

### 必需输入
| 字段 | 说明 |
|------|------|
| 教程标题 | 明确的学习主题 |
| 预计时长 | 学习所需时间 |
| 前置要求 | 学习者需具备的基础 |
| 学习目标 | 至少1项可衡量的学习成果 |

### 可选输入
- 原始学习资料(文件/链接/文本)
- 特定受众描述
- 风格偏好(生活化/专业/幽默/严谨)
- 章节数量要求

---

## 流程总控

```
Phase 1: 资料摄入       Phase 2: 领域分析       Phase 3: 大纲生成
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ 收集原始资料  │       │ 识别领域+受众 │       │ 生成章节大纲  │
│              │  →   │              │  →   │              │
│ 结构化分块    │ Gate1 │ 匹配比喻风格  │ Gate2 │ 比喻链+知识点 │ Gate3
│ 输出: 内容块  │       │ 输出: 分析报告 │       │ 输出: 大纲JSON │
└──────────────┘       └──────────────┘       └──────────────┘
                                                       │
                                                       ▼
Phase 6: 发布          Phase 5: 质量评估       Phase 4: 内容生成
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ MkDocs项目    │       │ 5维度评分     │       │ 逐章撰写      │
│              │  ←   │              │  ←   │              │
│ 打包导出      │ Gate5 │ 改进建议      │ Gate4 │ MkDocs规范    │ Gate3
│ 输出: 完整站点 │       │ 输出: QA报告   │       │ 输出: 章节MD   │
└──────────────┘       └──────────────┘       └──────────────┘
```

### 阶段门控

| 门 | 检查内容 | 不通过时的处理 |
|----|----------|---------------|
| **Gate 1** | 资料已收集,内容块已结构化 | 追问补充资料或确认从零开始 |
| **Gate 2** | 领域/受众/风格已确认 | 调整分析参数 |
| **Gate 3** | 大纲已审阅,比喻链完整 | 修改章节/调整比喻/重新生成 |
| **Gate 4** | 每章内容符合 MkDocs 规范,受众适配 | 修改/扩充/精简 |
| **Gate 5** | 质量评分 ≥ 60/100 | 针对性修改后重新评估 |

---

## 核心系统

### 四级受众模型

| 级别 | 比喻密度 | 步骤粒度 | 触发特征 |
|------|:---:|:---:|------|
| **absolute_beginner** | high | micro | "零基础""新手""入门" |
| **beginner** | medium | standard | 默认级别 |
| **intermediate** | low | condensed | "进阶""实战""精通" |
| **expert** | minimal | overview | "架构""原理""源码" |

详见: [assets/audience-model.md](assets/audience-model.md)

### 四种比喻风格

| 风格 | 特点 | 适合场景 |
|------|------|----------|
| **daily_life** | 生活化类比 | 零基础、概念抽象 |
| **professional** | 行业类比 | 有行业背景、B2B |
| **humorous** | 幽默轻松 | 娱乐内容、年轻受众 |
| **rigorous** | 严谨学术 | 学术内容、考试导向 |

详见: [assets/analogy-styles.md](assets/analogy-styles.md)

### 五大领域配置

| 领域 | 默认受众 | 默认风格 | 子领域 |
|------|----------|----------|--------|
| technology | beginner | daily_life | 编程/运维/AI/数据库/前后端/DevOps |
| business | intermediate | professional | 营销/管理/财务/战略/运营 |
| academic | beginner | rigorous | 数学/物理/化学/生物/人文 |
| life | absolute_beginner | daily_life | 摄影/烘焙/瑜伽/理财/旅行 |
| art | beginner | humorous | 绘画/音乐/设计/写作 |

详见: [assets/domain-configs.md](assets/domain-configs.md)

---

## 验收标准

### 质量评分 (5维度)

| 维度 | 权重 | 关键检查 |
|------|:---:|------|
| 格式规范 | 15% | MkDocs兼容性、空行隔离、粗体空格隔离 |
| 内容完整性 | 25% | 知识点覆盖、示例充分、实践任务完整 |
| 教学逻辑 | 25% | 难度递进、概念衔接、认知负荷 |
| 实用价值 | 20% | 可操作性、场景真实、有明确产出 |
| 比喻质量 | 15% | 贴切程度、风格一致、记忆辅助 |

### 质量等级
- **90-100**: 优秀,强烈推荐
- **75-89**: 良好,可以使用
- **60-74**: 可接受,有条件使用
- **<60**: 需改进,不建议发布 — 触发重新修订

### 阻断性缺陷 (一票否决)
- 列表符号粘连正文(最高级别格式错误)
- `**粗体**` 标记前后缺少空格
- 代码块/Admonition 前后缺少空行
- 章节内容与大纲不符
- 输出未包含验证步骤

---

## MkDocs 排版强制规范

### 空行隔离原则
- 任何列表(`-`/`1.`)首行之前强制插入空行
- 代码块(` ``` `)、引用块(`>`)、Admonition(`!!!`)前后各一个空行
- 严禁列表紧跟在正文末尾

### 粗体空格隔离
- `**` 标记前后必须各有一个空格
- 中文标点(。，：；！？)紧邻 `**` 时也需空格
- 表格内、列表项内同样适用
- 验证正则: `[^\s]\*\*[^\s\*]`

### 其他规范
- 数学公式: 行内 `$公式$`, 块级 `$$公式$$`
- 代码块使用准确语言高亮
- 多系统操作用 Tabbed Content

详见: [assets/mkdocs-standards.md](assets/mkdocs-standards.md)

---

## 教程分类体系

所有教程采用三层分类: **领域 → 方向 → 主题**

| 领域 | 方向 | 示例 |
|------|------|------|
| 基础技能 | 开发工具/文档写作/环境配置 | Git/Markdown/Linux |
| 编程语言 | 通用语言/专业语言/标记语言 | Python/R/HTML |
| 技术领域 | AI/数据工程/前端/运维 | LLM/爬虫/Web |
| 工程实践 | 软件工程/团队协作/质量保障 | 设计模式/CI/CD |

详见: [assets/classification.md](assets/classification.md)

---

## 发布同步要求

教程生成后必须同步 3 个文件:
1. `README.md` — 在对应分类添加教程词条
2. `docs/index.md` — 在对应分类添加教程卡片
3. `mkdocs.yml` — 在 `nav` 列表添加导航项

---

## 使用示例

```
用户: "帮我生成一个 Linux 新手入门教程,4-5小时,零基础"
  → Phase 1: 确认从零开始
  → Phase 2: technology/beginner/daily_life
  → Phase 3: 6章大纲, 比喻链: 遥控器→租房→语音遥控器→钥匙锁→智能管家
  → Phase 4: 逐章生成(每章配实操+验证)
  → Phase 5: 质量评分 92/100
  → Phase 6: 导出完整 MkDocs 项目
```

---

## 文件导航

```
dog-tutor/
├── SKILL.md                     # 本文件 — 流程总控、触发条件、验收标准
├── ATTRIBUTIONS.md              # 原始作者归属声明
├── references/
│   ├── workflow.md              # 6阶段详细说明(输入/输出/步骤/对话模板)
│   ├── handoff-format.md        # 阶段间交接的结构化格式
│   └── qa-checklist.md          # 质量验收清单(5维度20+项)
└── assets/
    ├── audience-model.md        # 四级受众模型详解
    ├── analogy-styles.md        # 四种比喻风格配置
    ├── domain-configs.md        # 五大领域配置(YAML)
    ├── classification.md        # 三层分类体系+归类流程图
    ├── mkdocs-standards.md      # MkDocs Material排版强制规范
    └── output-formats.md        # 固定输出格式模板
```

---

## 原始出处

本技能基于 **SmartTutor Generator v1.1** (莫弈, 2026-05-04) 整合封装。
完整归属声明: [ATTRIBUTIONS.md](ATTRIBUTIONS.md)

---

*Dog-Tutor v1.0.0 — MIT License*
