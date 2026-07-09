# Architecture Diagram Generator — 架构图生成器

> 说人话就能画架构图。跟 Claude 描述系统架构，直接生成深色主题 HTML+SVG，浏览器打开就能看，还能一键导出 PNG/PDF。再见 Draw.io！

## 特性

- 🗣️ **说人话就能画** — 不需要写代码、不用学标记语法，用自然语言描述即可
- 🎨 **深色主题 + 语义配色** — 青色前端、翠绿后端、紫色数据库、琥珀色云服务、玫瑰色安全模块
- 📤 **一键三导出** — Copy PNG 到剪贴板 / Download PNG / Download PDF，零命令行零额外依赖
- 🧠 **智能自适应** — Quick Mode（轻量秒出图）和 Deep Mode（5轮深度发现）自动切换
- 🔄 **聊天式改图** — "加一个 Redis""把数据库挪到右边"——在对话里说就行，实时重新生成

## 安装

```bash
# Claude Code
cp -r architecture-diagram/ ~/.claude/skills/architecture-diagram/

# Codex / Cursor / Copilot 等
npx skills add Cocoon-AI/architecture-diagram-generator -g
```

## 使用方式

三种路子获得架构描述：

1. **让 AI 分析代码库**：把代码丢给 Claude/Codex，让它分析结构并输出组件清单
2. **自己手写**：直接列出组件和连接关系，如 "React 前端 → Node.js API → PostgreSQL + Redis"
3. **让 Claude 给模板**：没有具体系统时，直接问 "画一个典型的 SaaS 应用架构图"

把描述贴进对话，加一句"用你的架构图 Skill 生成一张架构图"，Claude 返回 HTML 文件。

## 适用场景

| ✅ 擅长 | ❌ 不适合 |
|---------|-----------|
| 软件架构图 | 物理硬件图 |
| 云基础设施图 (AWS/Azure/GCP) | 流程图（用 [process-flow-diagram-generator](https://github.com/Cocoon-AI/process-flow-diagram-generator)） |
| 微服务拓扑图 | |
| 安全架构图 | |
| 网络拓扑图 | |
| 数据管道图 | |

## 版本

v2.1 — 基于 [Cocoon AI v1.1](https://github.com/Cocoon-AI/architecture-diagram-generator) 深度优化。

## 中文介绍

详见卡兹克的介绍文章：[《又一个神级画图 Skill 开源，再见 draw.io！》](https://mp.weixin.qq.com/s/h2pD2DrC6fkHSRatzmI-tg)

## 许可

MIT License — [Cocoon AI](https://github.com/Cocoon-AI/architecture-diagram-generator)
