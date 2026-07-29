---
name: teach
description: >
  Matt Pocock 的三层学习框架——Knowledge（知识获取）→ Skills（交互练习）→ Wisdom（社区智慧）。
  AI 变成你的私人导师：从高质量资源提取知识生成 HTML 交互课件，设计动手练习并给即时反馈，
  对于 AI 教不了的判断力，帮你找到真实的社区和人。每句话都有引用来源，每个练习都有反馈循环。
  Trigger keywords: teach, 教我, 学习, learn, 教我学, teach me, 交互式学习,
  帮我学, 入门, 新手教程, 技能学习, 知识获取, 刻意练习, interactive learning,
  personal tutor, 私人教师, 学习框架, knowledge skills wisdom, matt pocock.
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
  category: learning
  source: https://github.com/mattpocock/skills
  author: Matt Pocock
  version: "1.0.0"
  license: MIT
---

# Teach — Knowledge · Skills · Wisdom

Matt Pocock 的三层学习框架。Teach 不是一个问答机器人——它是一套结构化的多会话学习系统，
围绕 **Knowledge（知识）→ Skills（技能）→ Wisdom（智慧）** 三层递进设计。

## 核心理念

学习要深入，三样东西缺一不可：

### 📚 第一层：Knowledge（知识获取）

事实性知识——书本上、文章里能学到的东西。比如学吉他，Knowledge 就是和弦叫什么、指法怎么按、
为什么这个和弦听起来悲伤。

- **从不信任参数化知识**：从高质量、高可信的外部资源提取知识
- **每句话都有引用**：所有知识追踪在 `RESOURCES.md` 中
- **难度是敌人**：降低认知负荷，把工作记忆留给理解本身
- **产出**：带交互的 HTML 课件（Tufte 风格排版），每句话都有引用来源

### 🛠️ 第二层：Skills（动手能力）

能不能按出 F 和弦？能不能在 C 和 G 之间流畅切换？这些东西光看文章学不会，必须动手练。

- **难度是工具**：刻意练习——费力检索才能建立长期存储强度（不只是当下的流畅感）
- **紧反馈循环**：设计交互式练习，在浏览器里操作，立刻给反馈
- **对了就是对了，错了告诉哪里错了**
- **产出**：交互式 HTML 练习页面（`lessons/0001-*.html`），包含 quiz、模拟器、实操步骤

### 🧠 第三层：Wisdom（真实判断力）

什么时候该用 F 和弦而不是 Fmaj7？什么情绪的歌曲适合什么和弦进行？这种东西 AI 教不了。

- **Wisdom 不可教**：需要真实世界的人际互动
- **承认边界**：Teach 会老实告诉你这块帮不了你
- **连接社区**：帮你找到相关的论坛、社群、线下兴趣小组
- **送你出门**：让你去真实世界里摔打

## 教学空间结构

Teach 在当前目录创建结构化的教学空间：

| 文件/目录 | 用途 |
|-----------|------|
| `MISSION.md` | 为什么学——用户的深层动机，锚定所有教学决策 |
| `RESOURCES.md` | 高质量资源清单——所有知识的引用来源 |
| `reference/*.html` | 精简速查表、术语表、语法参考——为反复查阅和打印设计 |
| `lessons/*.html` | 自包含 HTML 课件——教学的基本单元（编号 `0001-<name>.html`） |
| `learning-records/*.md` | 学习记录——关键洞察和非显而易见的教训（类似 ADR），用于计算最近发展区 |
| `assets/*` | 可复用组件——样式表、quiz 组件、模拟器 |
| `NOTES.md` | 草稿本——用户偏好和工作笔记 |

## 核心设计原则

- **最近发展区**：每节课挑战"刚刚好"——不太难也不太容易
- **存储强度 vs 流畅感**：不被当下的流畅感欺骗，通过检索练习、间隔重复、交错练习建立长期记忆
- **Tufte 风格排版**：干净、优雅、可读——值得反复回看的课件设计
- **每节课链接到主源**：最高质量、最高可信的资源
- **每节课提醒可以追问**：用户可以对 AI 提后续问题
- **参考文档是真正的长期资产**：课件很少回看；参考资料是日常工具

## 工作流程

```
1. Mission → 了解用户为什么想学，写入 MISSION.md
2. Research → 从高质量资源提取知识，写入 RESOURCES.md
3. Reference → 生成速查表和术语表（reference/*.html）
4. Lessons → 设计交互式课件（lessons/0001-*.html）
5. Practice → 设计动手练习，给即时反馈
6. Wisdom → 对教不了的部分，推荐真实社区和人
7. Record → 记录学习洞察，追踪最近发展区
```

## 安装

```bash
cp -r teach ~/.claude/skills/teach
```

或从 dist 下载 `teach.skill` 拖入 Claude Code。
