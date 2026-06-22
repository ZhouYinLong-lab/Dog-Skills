# Dog-Tutor 归属声明 (Attributions)

Dog-Tutor 是一个**元技能(Meta-Skill)** — 它基于 SmartTutor Generator 的核心方法论,
通过结构化封装和标准化输出格式,将其转化为可复用的技能系统。

---

## 原始技能

### SmartTutor Generator — 智能教程编制系统

- **名称**: SmartTutor Generator (smarttutor-generator)
- **作者**: 莫弈
- **版本**: v1.1 (最后更新: 2026年5月4日)
- **创建时间**: 2026年5月3日
- **许可**: 原始文件未明确声明许可,整合入 Dog-Tutor 后采用 MIT License

### 原始技能核心贡献

SmartTutor Generator 原创了以下系统:

| 系统 | 说明 |
|------|------|
| **六阶段工作流** | 资料摄入→领域分析→大纲生成→内容生成→质量评估→导出发布 |
| **四级受众模型** | absolute_beginner / beginner / intermediate / expert,含自动识别与动态调整 |
| **四种比喻风格** | daily_life / professional / humorous / rigorous,含自动匹配策略 |
| **五领域配置** | technology / business / academic / life / art,含子领域与写作原则 |
| **五维度质量评估** | 格式规范(15%)/内容完整性(25%)/教学逻辑(25%)/实用价值(20%)/比喻质量(15%) |
| **MkDocs排版规范** | 空行隔离原则、粗体空格隔离、Admonition使用规范、数学公式规范 |
| **三层教程分类体系** | 领域→方向→主题,含归类流程图与跨类别处理规则 |
| **发布同步机制** | 新教程自动同步 README.md / docs/index.md / mkdocs.yml |
| **存档与复用** | 增量更新、风格迁移、受众调整、多语言版本、格式转换 |

### 原始案例

SmartTutor Generator 基于以下实战案例提炼:
- Linux 新手入门指南(技术类, beginner)
- 零基础摄影入门(生活类, absolute_beginner)
- 线性代数入门(学术类, beginner)

---

## Dog-Tutor 的整合方式

### 做了什么

| 方式 | 说明 |
|------|------|
| ✅ 结构化封装 | 将原始单一文件拆分为 SKILL.md + references/ + assets/ 的模块化结构 |
| ✅ 流程标准化 | 增加阶段门控(Gate)、验收标准、阻断性缺陷检查 |
| ✅ 格式模板化 | 将对话模板和输出格式提取为可复用的 handoff-format.md |
| ✅ 归属透明化 | 在 ATTRIBUTIONS.md 中完整记录原始作者和贡献 |

### 没做什么

| 方式 | 说明 |
|------|------|
| ❌ 不重新发明 | 六阶段流程、受众模型、比喻系统、质量评估维度的核心设计均来自原始技能 |
| ❌ 不修改核心逻辑 | 领域配置、质量标准阈值、分类体系的参数保持原始设定 |
| ❌ 不隐藏来源 | 所有输出中标注基于 SmartTutor Generator 方法论 |

---

## 版本对应

| Dog-Tutor | SmartTutor Generator | 变更 |
|-----------|---------------------|------|
| v1.0.0 | v1.1 (2026-05-04) | 结构化封装,增加门控和验收标准 |

---

*如有归属信息需要更正,请联系 Dog-Skills 维护者。*
