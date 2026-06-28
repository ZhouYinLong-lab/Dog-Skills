# Website Cloner 归属声明 (Attributions)

Website Cloner 技能基于 [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) 项目改编,该项目由 **JCodesMore** 创建并维护。

---

## 原始项目

| 项目 | 详情 |
|------|------|
| **名称** | ai-website-cloner-template |
| **作者** | [JCodesMore](https://github.com/JCodesMore) |
| **仓库** | https://github.com/JCodesMore/ai-website-cloner-template |
| **许可证** | MIT |
| **Stars** | 22,400+ |
| **Forks** | 3,200+ |
| **语言** | TypeScript |
| **主页** | https://dsc.gg/jcodesmore |

---

## 改编内容

本目录中的 `SKILL.md` 是基于原始项目 `.claude/skills/clone-website/SKILL.md` 文件改编的,适配了 Dog-Skills 项目的技能格式约定。

### 保留的核心内容
- 完整的 5 阶段克隆工作流(Reconnaissance → Foundation → Component Spec & Build → Assembly → Visual QA)
- 9 条核心原则(Completeness Beats Speed, Small Tasks Perfect Results, etc.)
- 调度前检查清单
- "不该做的事"反模式列表
- 所有浏览器提取脚本模式
- 组件规格文件模板

### 改编的变更
- YAML 前置元数据格式适配 Dog-Skills 约定
- 添加中英文双语触发关键词
- 添加 `allowed-tools` 配置
- 添加 `metadata` 字段(version, license, original-author, original-repo)
- 调整为更适合独立技能文件的格式

---

## 包含的原始文件

`references/` 目录包含原始项目的以下文件:

- `INSPECTION_GUIDE.md` — 网站逆向工程检查指南(原始: `docs/research/INSPECTION_GUIDE.md`)
- `AGENTS.md` — 代理规则模板(原始: `AGENTS.md`)

---

## 免责声明

本技能是一个 **AI 代理指令文件** — 它教会 AI 编码代理如何复刻网站供学习和合法使用。用户有责任:
- 仅用于合法目的
- 遵守目标网站的服务条款
- 尊重知识产权
- 不将克隆用于钓鱼、冒充或欺骗

---

*本文件遵循原始项目的 MIT 许可协议。*
