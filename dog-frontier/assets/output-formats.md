# 固定输出格式模板

> Dog-Frontier 各阶段的标准化输出格式。
> 直接复制模板,填充内容,保证输出一致性。

---

## 输出格式 1: 需求卡片 (Phase 1 输出)

```markdown
<!-- @source: dog-frontier/phase-1 -->
<!-- @date: YYYY-MM-DD -->

## 需求卡片: [项目名]

| 字段 | 值 |
|------|-----|
| project_id | [kebab-case] |
| project_type | [new/refactor/add-page/review] |
| stack | [vue3-tailwind/react-tailwind/vanilla/...] |
| page_type | [landing/dashboard/admin/ecommerce/blog/portfolio/component/other] |
| style_preference | [具体风格/auto] |
| product_domain | [saas/ecommerce/fintech/healthcare/education/gaming/beauty/food/luxury/ai/dashboard/other] |
| target_audience | [b2b/b2c/developer/kids/general] |
| constraints | seo:[T/F] perf:[budget] brand:[url] |

## 用户原始需求
> [用户原话]
```

---

## 输出格式 2: 设计系统 (Phase 2 输出) — DESIGN.md 标准格式

> **v2.0 更新**: 对齐 [Google DESIGN.md 格式标准](https://github.com/google-labs-code/design.md)。
> YAML front matter 为机器可读令牌, Markdown body 为人类可读设计文档。

```markdown
<!-- @source: dog-frontier/phase-2 -->
<!-- @date: YYYY-MM-DD -->
<!-- @ds_version: 2.0.0 -->
<!-- @format: DESIGN.md (google-labs-code/design.md) -->
<!-- @brand_ref: [awesome-design-md品牌名 或 "custom"] -->

---
version: "2.0"
name: [项目名]
description: >
  [一句话设计哲学, 如 "极简主义的SaaS仪表盘, 受Stripe启发"]

colors:
  bg-primary: "#[hex]"
  bg-secondary: "#[hex]"
  accent-primary: "#[hex]"
  accent-secondary: "#[hex]"
  text-primary: "#[hex]"
  text-secondary: "#[hex]"
  success: "#[hex]"
  error: "#[hex]"
  warning: "#[hex]"

typography:
  display:
    fontFamily: [Font Name]
    fontSize: [N]px
    fontWeight: [600-800]
  body:
    fontFamily: [Font Name]
    fontSize: [N]px
    fontWeight: [400-500]
  mono:
    fontFamily: [Font Name]
    fontSize: [N]px
    fontWeight: [400]

rounded:
  sm: [N]px
  md: [N]px
  lg: [N]px

spacing:
  xs: [N]px
  sm: [N]px
  md: [N]px
  lg: [N]px
  xl: [N]px

components:
  button-primary:
    backgroundColor: "{colors.accent-primary}"
    textColor: "{colors.bg-primary}"
    rounded: "{rounded.md}"
    padding: [N]px [N]px
  card:
    backgroundColor: "{colors.bg-secondary}"
    rounded: "{rounded.lg}"
    padding: [N]px
---

# [项目名] 设计系统

## Overview
- **主风格**: [名称] `[来源: skill-name 或 awesome-design-md/品牌名]`
- **辅风格**: [名称]
- **模式**: [light/dark/auto]
- **设计哲学**: [一段话描述这个设计系统的核心美学和情感目标]

## Colors
| Token | Hex | 用途 |
|-------|-----|------|
| ... (对应 YAML colors 的人读版) |

## Typography
| 角色 | 字体 | 权重 | Google Fonts |
|------|------|------|-------------|
| ... (对应 YAML typography 的人读版) |

## Layout
- 间距比例: [说明]
- 网格系统: [说明]
- 最大宽度: [说明]

## Elevation & Depth
- 阴影层级: sm=[val] md=[val] lg=[val]
- 玻璃态效果: blur=[val] border=[val] bg=[val]

## Shapes
- 圆角层级: sm=[val] md=[val] lg=[val]

## Components
- 按钮 / 卡片 / 输入框 / 导航栏 ... (对应 YAML components)

## Do's and Don'ts
- ✅ [推荐做法1]
- ✅ [推荐做法2]
- ❌ [反模式1]
- ❌ [反模式2]

## Agent Prompt Guide
- 快速色板参考
- 即用型提示词
```

---

## 输出格式 3: 组件规格 (Phase 3 输出)

```markdown
<!-- @source: dog-frontier/phase-3 -->
<!-- @date: YYYY-MM-DD -->
<!-- @ds_version: 1.0.0 -->

## 组件: [组件名]

### 状态表
| 属性 | Default | Hover | Active | Disabled | Focus |
|------|---------|-------|--------|----------|-------|
| Background | [val] | [val] | [val] | [val] | [val] |
| Text | [val] | [val] | [val] | [val] | [val] |
| Border | [val] | [val] | [val] | [val] | [val] |
| Shadow | [val] | [val] | [val] | [val] | [val] |

### Props
| Prop | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| [name] | [type] | [val] | [Y/N] | [desc] |

### Slots
| Name | Description |
|------|-------------|
| default | [desc] |
| [name] | [desc] |

### Events
| Name | Payload | Description |
|------|---------|-------------|
| [name] | [type] | [desc] |

### 来源
- 组件库: [shadcn-vue/shadcn-ui/vanilla-web] ([author], [license])
```

---

## 输出格式 4: 页面交付 (Phase 3 输出)

```markdown
<!-- @source: dog-frontier/phase-3 -->
<!-- @date: YYYY-MM-DD -->

## 页面: [页面名]

### 文件
| 文件 | 类型 | 来源 |
|------|------|------|
| [path] | page/component/layout/style | [skill-name] |

### 使用说明
1. [step]
2. [step]

### 依赖
| 包名 | 版本 | 用途 |
|------|------|------|
| [name] | [ver] | [purpose] |
```

---

## 输出格式 5: QA 报告 (Phase 5 输出)

```markdown
<!-- @source: dog-frontier/phase-5 -->
<!-- @date: YYYY-MM-DD -->

## QA 报告: [项目名]

### 阻断性缺陷
[列出 B1-B5 命中项,或 "无"]

### 评分
| 维度 | 得分 | 通过线 |
|------|------|--------|
| 1. 视觉质量 | /5 | ≥4 |
| 2. 可访问性 | /5 | ≥4 |
| 3. 响应式 | /5 | ≥4 |
| 4. 性能 | /5 | ≥3 |
| 5. 代码质量 | /5 | ≥4 |
| 6. 文案质量 | /5 | ≥3 |
| **总计** | **/30** | **≥22** |

### 不合格项
| # | 维度 | 问题 | 建议 |
|---|------|------|------|
| 1 | [dim] | [issue] | [fix] |

### 判定
[✅ 通过 / ⚠️ 有条件通过 / ❌ 不通过]
```
