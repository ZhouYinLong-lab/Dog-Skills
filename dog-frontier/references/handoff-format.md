# 子任务交接格式 (Handoff Format)

> 定义 Dog-Frontier 各阶段之间的结构化交接标准。
> 每个阶段的输出必须遵循对应格式,确保下游阶段可无歧义消费。

---

## 通用原则

1. **机器可读优先**: 使用 Markdown 表格和代码块,便于工具解析
2. **自描述**: 每个输出文件头部包含 `@source` `@phase` `@date` 元数据
3. **版本化**: 设计系统文件包含版本号,代码生成时标注基于哪个版本
4. **可追溯**: 所有设计决策标注来源(上游技能/用户选择/自动匹配)

---

## 阶段输出格式

### Phase 1 → Phase 2 交接: 需求卡片

```markdown
<!-- @source: dog-frontier/phase-1 -->
<!-- @phase: discovery -->
<!-- @date: YYYY-MM-DD -->

## 需求卡片: [项目名]

| 字段 | 值 |
|------|-----|
| project_id | [kebab-case 标识符] |
| project_type | new \| refactor \| add-page \| review |
| stack | vue3-tailwind \| react-tailwind \| vanilla \| react-native \| flutter \| other |
| page_type | landing \| dashboard \| admin \| ecommerce \| blog \| portfolio \| component \| other |
| style_preference | [具体风格名] \| auto |
| product_domain | saas \| ecommerce \| fintech \| healthcare \| education \| gaming \| beauty \| food \| real-estate \| luxury \| other |
| target_audience | b2b \| b2c \| developer \| kids \| general |
| constraints | { "seo": bool, "perf_budget": "string", "brand_guide": "url_or_path" } |

## 用户原始需求
[用户的原话,未加工]
```

### Phase 2 → Phase 3 交接: 设计系统文件

```markdown
<!-- @source: dog-frontier/phase-2 -->
<!-- @phase: design-system -->
<!-- @date: YYYY-MM-DD -->
<!-- @based_on: [需求卡片 project_id] -->
<!-- @design_system_version: 1.0.0 -->

# [项目名] 设计系统

## 1. 风格方案
```yaml
style:
  primary: [风格名]          # 来源: [ui-ux-pro-max / frontend-design / 用户指定]
  secondary: [风格名]        # 可选
  mode: light | dark | auto
  source_skills:
    - ui-ux-pro-max
    - frontend-design
```

## 2. 配色方案
```yaml
colors:
  bg_primary: { hex: "#XXXXXX", token: "--bg-primary", source: "ui-ux-pro-max color domain" }
  bg_secondary: { hex: "#XXXXXX", token: "--bg-secondary" }
  accent_primary: { hex: "#XXXXXX", token: "--accent-primary" }
  accent_secondary: { hex: "#XXXXXX", token: "--accent-secondary" }
  text_primary: { hex: "#XXXXXX", token: "--text-primary" }
  text_secondary: { hex: "#XXXXXX", token: "--text-secondary" }
  semantic:
    success: { hex: "#XXXXXX", token: "--color-success" }
    error: { hex: "#XXXXXX", token: "--color-error" }
    warning: { hex: "#XXXXXX", token: "--color-warning" }
```

## 3. 字体搭配
```yaml
typography:
  display: { family: "Font Name", weight: "700", google_fonts: "url", source: "ui-ux-pro-max typography domain" }
  body: { family: "Font Name", weight: "400;500;600", google_fonts: "url" }
  mono: { family: "Font Name", weight: "400;500", google_fonts: "url" }
  scale:
    xs: "0.75rem"
    sm: "0.875rem"
    base: "1rem"
    lg: "1.125rem"
    xl: "1.25rem"
    2xl: "1.5rem"
    3xl: "1.875rem"
    4xl: "2.25rem"
    5xl: "3rem"
```

## 4. 效果系统
```yaml
effects:
  shadows:
    sm: "0 1px 2px rgba(0,0,0,0.05)"
    md: "0 4px 6px -1px rgba(0,0,0,0.1)"
    lg: "0 10px 15px -3px rgba(0,0,0,0.1)"
    xl: "0 20px 25px -5px rgba(0,0,0,0.1)"
  radius:
    sm: "4px"
    md: "8px"
    lg: "12px"
    xl: "16px"
  glass:
    blur: "12px"
    border: "rgba(255,255,255,0.1)"
    bg: "rgba(255,255,255,0.05)"
```

## 5. 反模式警告
```yaml
antipatterns:
  - "[具体反模式描述]"
  - "[具体反模式描述]"
  source: "ui-ux-pro-max product domain"
```

## 6. 组件令牌映射
```yaml
component_tokens:
  button:
    bg: "var(--accent-primary)"
    text: "#FFFFFF"
    radius: "var(--radius-md)"
    padding: "8px 16px"
  card:
    bg: "var(--bg-secondary)"
    border: "rgba(255,255,255,0.08)"
    radius: "var(--radius-lg)"
    shadow: "var(--shadow-sm)"
    padding: "24px"
  input:
    bg: "var(--bg-secondary)"
    border: "rgba(255,255,255,0.08)"
    radius: "var(--radius-md)"
    padding: "12px 16px"
```
```

### Phase 3 → Phase 4 交接: 代码交付包

```markdown
<!-- @source: dog-frontier/phase-3 -->
<!-- @phase: implementation -->
<!-- @date: YYYY-MM-DD -->
<!-- @ds_version: [引用的设计系统版本] -->

## 交付包: [项目名]

### 文件清单
```
project/
├── design-system/
│   └── MASTER.md                 # 设计系统 [版本]
├── src/
│   ├── styles/
│   │   └── tokens.css            # CSS 变量 [来源: design-system]
│   ├── components/
│   │   ├── ui/                   # [来源: shadcn-ui/shadcn-vue]
│   │   │   ├── Button.vue
│   │   │   ├── Card.vue
│   │   │   └── ...
│   │   ├── layout/               # 布局组件
│   │   └── feature/              # 业务组件
│   ├── pages/
│   │   ├── Home.vue              # [来源: landing-page-generator]
│   │   └── ...
│   └── App.vue
├── tailwind.config.js            # [来源: tailwind-design-system]
├── package.json
└── README.md
```

### 组件来源映射
| 文件 | 来源技能 | 许可 |
|------|----------|------|
| Button.vue | shadcn-vue (noartem, MIT) | MIT |
| Card.vue | shadcn-vue (noartem, MIT) | MIT |
| Home.vue | landing-page-generator (kostja94, MIT) + 自编写 | MIT |
| tokens.css | design-system sub-skill (claudekit, MIT) | MIT |
```

### Phase 5 输出: QA 报告

参见 [qa-checklist.md](qa-checklist.md) 的评分格式。

---

## 元数据头部规范

所有交接文件必须包含以下元数据行(HTML注释格式):

```markdown
<!-- @source: dog-frontier/[phase-name] -->
<!-- @phase: discovery | design-system | implementation | handoff | review -->
<!-- @date: YYYY-MM-DD -->
<!-- @ds_version: [MASTER.md版本号] -->    (Phase 3 输出专用)
<!-- @based_on: [上游交接文件] -->         (Phase 2+ 输出专用)
```

---

## 版本兼容性

| 设计系统版本变更 | 代码处理方式 |
|-----------------|-------------|
| PATCH (1.0.x) — Token 值微调 | 自动替换,无需重新生成 |
| MINOR (1.x.0) — 新增 Token/组件 | 增量更新,仅生成新增部分 |
| MAJOR (x.0.0) — 风格/配色大改 | 触发完整重新生成 |
