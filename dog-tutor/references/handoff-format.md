# 子任务交接格式 (Handoff Format)

> Dog-Tutor 各阶段之间的结构化交接标准。

---

## Phase 1 → Phase 2: 资料卡片

```markdown
<!-- @source: dog-tutor/phase-1 -->
<!-- @date: YYYY-MM-DD -->

## 资料卡片

| 字段 | 值 |
|------|-----|
| tutorial_id | [kebab-case] |
| title | [教程标题] |
| duration | [预计时长] |
| prerequisites | [前置要求列表] |
| learning_objectives | [学习目标列表] |
| source_type | file / url / paste / from_scratch |
| content_blocks | [结构化内容块数量] |
| key_concepts | [识别的关键概念列表] |
```

---

## Phase 2 → Phase 3: 领域分析报告

```json
{
  "@source": "dog-tutor/phase-2",
  "@date": "YYYY-MM-DD",
  "domain": "technology|business|academic|life|art",
  "subdomain": "细分方向",
  "confidence": "high|medium|low",
  "audience": {
    "level": "absolute_beginner|beginner|intermediate|expert",
    "background": "学生|职场新人|专业人士|爱好者|其他",
    "pain_points": ["痛点1", "痛点2"],
    "learning_objectives": ["目标1", "目标2"]
  },
  "style": {
    "analogy": "daily_life|professional|humorous|rigorous",
    "case_type": "项目实战|概念讲解|对比分析|故事驱动"
  }
}
```

---

## Phase 3 → Phase 4: 大纲对象

```json
{
  "@source": "dog-tutor/phase-3",
  "@date": "YYYY-MM-DD",
  "title": "教程标题",
  "total_duration": "时长",
  "chapter_count": 6,
  "metaphor_chain": ["比喻1", "比喻2", "..."],
  "chapters": [
    {
      "number": 1,
      "title": "章节标题",
      "metaphor": "核心比喻",
      "duration": "预计时长",
      "sections": [
        {"id": "1.1", "title": "小节标题", "knowledge_points": ["知识点"]}
      ],
      "practice_task": "实践任务描述"
    }
  ]
}
```

---

## Phase 4 → Phase 5: 章节内容

```markdown
<!-- @source: dog-tutor/phase-4 -->
<!-- @date: YYYY-MM-DD -->
<!-- @chapter: X/N -->
<!-- @metaphor: [比喻] -->
<!-- @audience: [级别] -->

# [章节标题] - [趣味副标题]

## 1. [第一节标题]

[内容...]

## 2. [第二节标题]

[内容...]

## 本章总结

- [ ] [要点1]
- [ ] [要点2]

## 课后练习

### 基础练习
[练习]

### 进阶挑战
[练习]

## 下一章预告
[预告]
```

---

## Phase 5 输出: 质量报告

```json
{
  "@source": "dog-tutor/phase-5",
  "@date": "YYYY-MM-DD",
  "overall_score": 92,
  "grade": "excellent|good|acceptable|needs_improvement",
  "dimensions": {
    "format": {"score": 14, "weight": 0.15, "comment": "评价"},
    "completeness": {"score": 23, "weight": 0.25, "comment": "评价"},
    "pedagogy": {"score": 23, "weight": 0.25, "comment": "评价"},
    "practicality": {"score": 18, "weight": 0.20, "comment": "评价"},
    "analogy": {"score": 14, "weight": 0.15, "comment": "评价"}
  },
  "highlights": ["亮点1", "亮点2"],
  "improvements": ["建议1", "建议2"],
  "issues": [
    {"problem": "问题", "solution": "解决方案"}
  ]
}
```

---

## Phase 6 输出: 文件清单

```markdown
<!-- @source: dog-tutor/phase-6 -->
<!-- @date: YYYY-MM-DD -->

## 交付清单

| 文件 | 状态 | 大小 |
|------|:---:|------|
| mkdocs.yml | ✅ | [size] |
| docs/index.md | ✅ | [size] |
| docs/chapter1.md | ✅ | [size] |
| ... | | |

## 同步状态
| 索引文件 | 状态 |
|----------|:---:|
| README.md | ✅ 已同步 |
| docs/index.md | ✅ 已同步 |
| mkdocs.yml | ✅ 已同步 |
```
