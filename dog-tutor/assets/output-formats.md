# 固定输出格式模板

> Dog-Tutor 各阶段的标准化输出格式。直接复制模板,填充内容。

---

## 输出格式 1: 章节内容模板

```markdown
# 第X章 [章节标题] — [趣味副标题]

## 📋 本章概览

| 项目 | 内容 |
|:---|:---|
| 学习时长 | [时长] |
| 核心概念 | [概念1, 概念2, ...] |
| 核心比喻 | [比喻] |
| 实践任务 | [任务描述] |
| 难度等级 | [★☆☆☆☆ ~ ★★★★★] |

---

## 1. [第一节标题]

[正文内容...]

!!! info "术语解释: [术语]"
    [用指定风格比喻解释术语]

!!! example "生活化案例"
    [案例描述]

```[language]
# [代码示例 - 含中文注释]
```

!!! tip "经验技巧"
    [技巧]

!!! warning "常见错误"
    [错误描述和避免方法]

!!! danger "安全警示"
    [风险提示] (仅在涉及安全时使用)

---

## 2. [第二节标题]

[同上结构...]

---

## 📝 本章总结

- [ ] [要点1]
- [ ] [要点2]
- [ ] [要点3]

---

## ✏️ 课后练习

### 基础练习
1. [练习1 - 验证掌握程度]
2. [练习2]

### 进阶挑战
1. [挑战1 - 拓展应用能力]

---

## 🔮 下一章预告

下一章我们将学习 [预告内容], 敬请期待!
```

---

## 输出格式 2: 教程首页模板 (docs/index.md)

```markdown
# [教程标题]

## 📖 关于本教程

[教程简介 - 2-3句话]

## 🎯 学习目标

完成本教程后,你将能够:
- [ ] [目标1]
- [ ] [目标2]
- [ ] [目标3]

## 📋 前置要求

- [要求1]
- [要求2]

## 🗺️ 学习路线

| 章节 | 标题 | 核心比喻 | 时长 |
|:---|:---|:---|:---|
| 第1章 | [标题] | [比喻] | [时长] |
| 第2章 | [标题] | [比喻] | [时长] |
| ... | ... | ... | ... |

## 🚀 快速开始

[如何开始学习的说明]
```

---

## 输出格式 3: mkdocs.yml 模板

```yaml
site_name: [教程标题]
site_description: [教程描述]
theme:
  name: material
  language: zh
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - content.code.copy
    - content.tabs.link
  palette:
    - scheme: default
      primary: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

nav:
  - 首页: index.md
  - 第1章 [标题]: chapter1.md
  - 第2章 [标题]: chapter2.md
  - ...
```

---

## 输出格式 4: 存档文件模板

### domain_analysis.json
```json
{
  "@source": "dog-tutor/phase-2",
  "@date": "YYYY-MM-DD",
  "domain": "technology",
  "subdomain": "操作系统",
  "confidence": "high",
  "audience": {
    "level": "beginner",
    "background": "学生",
    "pain_points": ["命令行恐惧", "环境搭建困难"],
    "learning_objectives": ["理解Linux概念", "掌握基本命令"]
  },
  "style": {
    "analogy": "daily_life",
    "case_type": "项目实战"
  }
}
```

### outline.json
```json
{
  "@source": "dog-tutor/phase-3",
  "@date": "YYYY-MM-DD",
  "title": "教程标题",
  "total_duration": "4-5小时",
  "chapter_count": 6,
  "metaphor_chain": ["遥控器", "租房", "语音遥控器", "房间抽屉", "钥匙锁", "智能管家"],
  "chapters": [...]
}
```

### quality_report.json
```json
{
  "@source": "dog-tutor/phase-5",
  "@date": "YYYY-MM-DD",
  "overall_score": 92,
  "grade": "excellent",
  "dimensions": {
    "format": {"score": 14, "weight": 0.15},
    "completeness": {"score": 23, "weight": 0.25},
    "pedagogy": {"score": 23, "weight": 0.25},
    "practicality": {"score": 18, "weight": 0.20},
    "analogy": {"score": 14, "weight": 0.15}
  },
  "highlights": [...],
  "improvements": [...]
}
```
