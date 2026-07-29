---
name: agency-agents-zh
description: >
  266 个即插即用的 AI 专家角色库 — 覆盖工程、设计、产品、营销、金融、安全、游戏等 20 个部门。
  每个角色都有独立的人设、专业流程和可交付成果，不是通用提示词模板。
  含 50 个中国市场原创智能体（小红书/抖音/微信/B站/飞书/钉钉等）。
  搭配编排器 agency-orchestrator，一句话即可让多位专家按 DAG 自动协作。
  Trigger keywords: 专家角色, 智能体, agent, 角色提示词, 切换角色, 启用专家, 专家模式,
  代码审查员, 产品经理, 技术文档工程师, 前端开发者, 后端架构师, 安全工程师, 小红书运营,
  抖音运营, 公众号编辑, B站内容策划, 跨境电商, 飞书集成, 钉钉开发, agency agents,
  expert role, 角色库, agent库, 266个专家, 即插即用角色, 用什么角色,
  帮我找一个XX专家, 切换到XX角色, 加载XX角色, 用XX的视角, 以XX身份, 作为XX专家。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
  - AskUserQuestion
metadata:
  category: tools
  source: https://github.com/jnMetaCode/agency-agents-zh
  upstream: https://github.com/msitarzewski/agency-agents
  author: jnMetaCode
  version: "1.0.0"
  license: MIT
---

# Agency Agents 中文版 — 266 个 AI 专家角色库

> 把"你是一个XXX专家"从一句话变成一套完整的工作流程。

## 这是什么？

一套**开箱即用的 AI 角色库**。每个智能体都有明确的身份定义、关键规则、工作流程和交付物。

**和普通提示词的区别**：普通提示词告诉 AI "你是一个专家"；这里的智能体定义了专家**怎么思考、怎么做事、交付什么**。

例如：
- [安全工程师](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-security-engineer.md) 会按 OWASP Top 10 逐项审查代码
- [小红书运营专家](https://github.com/jnMetaCode/agency-agents-zh/blob/main/marketing/marketing-xiaohongshu-operator.md) 会输出完整的种草笔记策略和达人合作方案
- [技术文档工程师](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-technical-writer.md) 会按文档类型生成标准化技术文档

## 角色覆盖（20 个部门，266 个角色）

| 部门 | 角色数 | 典型角色 |
|------|--------|----------|
| 🛠️ 工程部 | 41 | 前端开发者、后端架构师、代码审查员、安全工程师、DevOps 自动化师、SRE |
| 🎨 设计部 | 9 | UI 设计师、UX 架构师、品牌守护者、视觉叙事师 |
| 📦 产品部 | 15 | 产品经理、产品策略师、用户研究员、A/B 测试专家 |
| 📢 营销部 | 25 | 小红书运营、抖音运营、公众号编辑、B站内容策划、跨境电商 |
| 🏦 金融部 | 8 | 财务分析师、投资研究员、税务策略师、风控分析师 |
| 🔒 安全部 | 12 | 渗透测试员、威胁猎人、安全审计员、事件响应指挥官 |
| 🎮 游戏开发部 | 20 | 游戏设计师、Godot 脚本开发者、Blender 插件工程师 |
| 🎓 学术部 | 6 | 人类学家、历史学家、心理学家、学习规划师 |
| 💼 策略部 | 9 | 商业策略师、创新顾问、竞争情报分析师 |
| 📊 项目管理部 | 7 | 项目经理、Scrum Master、风险管理师 |
| ... | ... | 还有法律部、HR部、销售部、GIS部、供应链部、支持部、测试部等 |

> 完整列表 → [AGENT-LIST.md](https://github.com/jnMetaCode/agency-agents-zh/blob/main/AGENT-LIST.md) 或 [在线专家库](https://ao.aiolaola.com/experts)

## 使用方式

### 方式一：在线浏览（最推荐）

直接访问 **[ao.aiolaola.com/experts](https://ao.aiolaola.com/experts)**，搜索→找到角色→复制提示词→粘贴到 Claude Code 中激活。

### 方式二：安装到 Claude Code

```bash
# 克隆仓库
git clone https://github.com/jnMetaCode/agency-agents-zh.git /tmp/agency-agents-zh

# 复制所有角色到 Claude Code agents 目录
mkdir -p ~/.claude/agents
cp -r /tmp/agency-agents-zh/engineering ~/.claude/agents/
cp -r /tmp/agency-agents-zh/design ~/.claude/agents/
cp -r /tmp/agency-agents-zh/product ~/.claude/agents/
cp -r /tmp/agency-agents-zh/marketing ~/.claude/agents/
cp -r /tmp/agency-agents-zh/finance ~/.claude/agents/
cp -r /tmp/agency-agents-zh/security ~/.claude/agents/
cp -r /tmp/agency-agents-zh/game-development ~/.claude/agents/
cp -r /tmp/agency-agents-zh/academic ~/.claude/agents/
cp -r /tmp/agency-agents-zh/strategy ~/.claude/agents/
cp -r /tmp/agency-agents-zh/project-management ~/.claude/agents/
cp -r /tmp/agency-agents-zh/sales ~/.claude/agents/
cp -r /tmp/agency-agents-zh/hr ~/.claude/agents/
cp -r /tmp/agency-agents-zh/legal ~/.claude/agents/
cp -r /tmp/agency-agents-zh/testing ~/.claude/agents/
cp -r /tmp/agency-agents-zh/support ~/.claude/agents/
cp -r /tmp/agency-agents-zh/supply-chain ~/.claude/agents/
cp -r /tmp/agency-agents-zh/gis ~/.claude/agents/
cp -r /tmp/agency-agents-zh/spatial-computing ~/.claude/agents/
cp -r /tmp/agency-agents-zh/specialized ~/.claude/agents/
cp -r /tmp/agency-agents-zh/paid-media ~/.claude/agents/
cp -r /tmp/agency-agents-zh/integrations ~/.claude/agents/

# 在 Claude Code 中激活角色：
# "加载 engineering/engineering-code-reviewer.md 角色，审查我的代码"
```

### 方式三：使用编排器（多 Agent 协作）

```bash
npm install -g agency-orchestrator
ao compose "帮我写一篇关于 AI Agent 的深度分析文章" --run
```

编排器会自动挑选合适的专家角色，按 DAG 并行协作，几分钟交付完整方案。

### 方式四：作为提示词参考

直接浏览 [在线专家库](https://ao.aiolaola.com/experts) 或 [AGENT-LIST.md](https://github.com/jnMetaCode/agency-agents-zh/blob/main/AGENT-LIST.md)，复制/改编需要的角色提示词。

## 你的任务

当用户触发本 skill（提到需要某个专家角色、询问用什么角色、或直接说角色名）时：

### 第一步：理解需求
- 分析用户的任务目标和领域
- 确定需要哪种类型的专家角色

### 第二步：推荐角色
- 从 266 个角色库中匹配最合适的角色
- 告诉用户角色名、所在文件路径、以及这个角色能做什么
- 如果用户需要，直接从 [在线专家库](https://ao.aiolaola.com/experts) 或 [AGENT-LIST.md](https://github.com/jnMetaCode/agency-agents-zh/blob/main/AGENT-LIST.md) 检索对应提示词

### 第三步：角色激活
- 将对应角色的提示词加载到当前会话中
- 按照角色定义的工作流程和交付标准执行任务
- 确保输出符合角色要求的交付物格式

### 第四步：多角色协作（可选）
- 如果任务需要多个角色配合，建议使用 Agency Orchestrator 编排
- 或手动按顺序切换不同角色完成不同阶段的任务

## 常见场景 → 角色映射

| 场景 | 推荐角色 |
|------|----------|
| 改 README / 写文档 | `engineering/engineering-technical-writer.md` |
| 代码审查 | `engineering/engineering-code-reviewer.md` |
| 产品规划 | `product/product-product-manager.md` |
| 小红书内容 | `marketing/marketing-xiaohongshu-operator.md` |
| 抖音运营 | `marketing/marketing-douyin-operator.md` |
| 公众号编辑 | `marketing/marketing-wechat-official-account-editor.md` |
| B站内容策划 | `marketing/marketing-bilibili-content-planner.md` |
| 前端开发 | `engineering/engineering-frontend-developer.md` |
| 后端架构 | `engineering/engineering-backend-architect.md` |
| 安全审计 | `engineering/engineering-security-engineer.md` |
| 飞书集成 | `engineering/engineering-feishu-integration-developer.md` |
| 钉钉开发 | `engineering/engineering-dingtalk-integration-developer.md` |
| 微信小程序 | `engineering/engineering-wechat-mini-program-developer.md` |
| 跨境电商 | `marketing/marketing-cross-border-ecommerce-specialist.md` |
| 数据库优化 | `engineering/engineering-database-optimizer.md` |
| DevOps | `engineering/engineering-devops-automator.md` |

## 上游项目

- 英文原版：[agency-agents](https://github.com/msitarzewski/agency-agents) by msitarzewski
- 中文社区版：[agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) by jnMetaCode
- 在线专家库：[ao.aiolaola.com/experts](https://ao.aiolaola.com/experts)
- 编排器：[agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator)
