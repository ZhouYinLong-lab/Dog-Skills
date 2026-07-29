# ljg-skills 归属声明 (Attributions)

本目录中的 `SKILL.md` 是对 [ljg-skills](https://github.com/lijigang/ljg-skills) 项目的技能化包装与定位分析。

---

## 原始项目

| 项目 | 详情 |
|------|------|
| **名称** | ljg-skills |
| **作者** | [lijigang](https://github.com/lijigang) |
| **仓库** | https://github.com/lijigang/ljg-skills |
| **许可证** | MIT |
| **格式** | org-mode（master 分支）/ Markdown（md 分支） |

---

## 改编内容

本目录的 `SKILL.md` 包含：
- ljg-skills 的完整技能清单和分类
- 与 Dog-Skills 的定位重合分析
- 安装方式汇总
- 快速映射表（任务→技能）

### Dog-Skills 精选引入的技能

以下 5 个技能已从 ljg-skills 改编为独立的 Dog-Skills 格式 SKILL.md：

- `ljg-constraint/` — 约束引擎（改编自 ljg-skills/skills/ljg-constraint/）
- `ljg-rank/` — 降秩引擎（改编自 ljg-skills/skills/ljg-rank/）
- `ljg-blind/` — 盲区扫描（改编自 ljg-skills/skills/ljg-blind/）
- `ljg-roundtable/` — 圆桌讨论（改编自 ljg-skills/skills/ljg-roundtable/）
- `ljg-invest/` — 投资分析（改编自 ljg-skills/skills/ljg-invest/）

### 改编变更
- YAML 前置元数据格式适配 Dog-Skills 约定
- 添加中英文双语触发关键词
- 移除 ljg 特定路径依赖（如 ~/.claude/PAI/、weread API 等）
- 移除 org-mode 格式要求，统一为 Markdown
- 添加 `allowed-tools` 和 `metadata` 字段
- 精简重复内容，保留核心方法论

---

*本文件遵循原始项目的 MIT 许可协议。*
