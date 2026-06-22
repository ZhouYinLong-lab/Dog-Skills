# 五大领域配置

> 来源: SmartTutor Generator v1.1 (莫弈, 2026)

---

## technology — 技术

```yaml
technology:
  name: "技术"
  subdomains: ["编程", "运维", "AI/ML", "数据库", "前端", "后端", "DevOps", "安全"]
  default_analogy: "daily_life"
  default_audience: "beginner"
  writing_principles:
    - "每个技术概念必须配生活化比喻"
    - "命令必须有实际可运行的示例"
    - "强调安全意识和最佳实践"
    - "提供排错指南和常见错误"
  visual_rules:
    - "代码块使用准确语言高亮"
    - "命令输出必须展示预期结果"
    - "使用表格对比不同选项"
```

## business — 商业

```yaml
business:
  name: "商业"
  subdomains: ["营销", "管理", "财务", "战略", "运营", "创业"]
  default_analogy: "professional"
  default_audience: "intermediate"
  writing_principles:
    - "结合实际商业场景"
    - "强调ROI和成本效益"
    - "提供可落地的执行方案"
    - "包含案例分析和数据支撑"
```

## academic — 学术

```yaml
academic:
  name: "学术"
  subdomains: ["数学", "物理", "化学", "生物", "人文", "社科"]
  default_analogy: "rigorous"
  default_audience: "beginner"
  writing_principles:
    - "概念定义准确,引用权威来源"
    - "逻辑严密推导,避免跳跃"
    - "提供习题和详细解答"
    - "标注知识在学科体系中的位置"
```

## life — 生活

```yaml
life:
  name: "生活"
  subdomains: ["摄影", "烘焙", "瑜伽", "理财", "旅行", "家居", "健身"]
  default_analogy: "daily_life"
  default_audience: "absolute_beginner"
  writing_principles:
    - "步骤极细,可操作性强"
    - "强调安全注意事项"
    - "提供失败案例和补救方案"
    - "鼓励动手实践,降低完美主义"
```

## art — 艺术

```yaml
art:
  name: "艺术"
  subdomains: ["绘画", "音乐", "设计", "写作", "摄影艺术"]
  default_analogy: "humorous"
  default_audience: "beginner"
  writing_principles:
    - "降低完美主义焦虑"
    - "强调过程而非结果"
    - "提供创作灵感来源"
    - "鼓励个性化表达"
    - "展示多种风格/流派供参考"
```

---

## 领域识别关键词

| 关键词 | → 领域 |
|--------|--------|
| 编程/代码/API/服务器/数据库/AI/ML/框架/前端/后端/命令行/Linux/Docker/K8s | technology |
| 营销/销售/管理/财务/战略/ROI/KPI/创业/融资/商业计划 | business |
| 数学/物理/化学/生物/定理/证明/公式/习题/考试 | academic |
| 摄影/烘焙/瑜伽/理财/旅行/健身/穿搭/家居/美食 | life |
| 绘画/音乐/设计/写作/配色/构图/创作/灵感 | art |

---

## 领域 × 风格默认映射

| 领域 | audience → | absolute_beginner | beginner | intermediate | expert |
|------|-----------|:---:|:---:|:---:|:---:|
| technology | | daily_life | daily_life | professional | professional |
| business | | professional | professional | professional | professional |
| academic | | rigorous | rigorous | rigorous | rigorous |
| life | | daily_life | daily_life | daily_life | daily_life |
| art | | humorous | humorous | humorous | humorous |
