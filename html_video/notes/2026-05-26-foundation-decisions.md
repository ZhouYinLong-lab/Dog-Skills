# 2026-05-26 · 项目奠基决策日志

> 第一次会话产出的关键决策。串起 RFC-01/02/03，记录"为什么这么设计而不是别的"，留 open question 给后续会话。

---

## 三份 RFC 的关系

```
RFC-01: Engine Adapter 接口        ← 技术抽象层（最底）
   ↓ 定义 EngineAdapter / Capabilities / RenderInput / Output
RFC-02: Template Metadata 格式      ← 内容描述层
   ↓ 描述每个 template，含 engine 归属 + 跨引擎检索元数据
RFC-03: Agent Skill 设计           ← 用户交互层（最顶）
   ↓ CLI Contract + Claude Code SKILL.md + transpile 到其他 agent
```

三者必须**自下而上**实现：先有 adapter 抽象（RFC-01），才能写 template metadata 校验它（RFC-02），才能让 agent CLI 决策（RFC-03）。

---

## ⭐ 产品形态修订（mid-session 关键澄清）

Joey 在前 3 份 RFC 写完后澄清核心工作流："产品内支持上传图文资产 → 整合 → 生成 HTML 分镜 → 用户审 → 导出 MP4"。这是**两段式 storyboard-first** 工作流，跟前 3 份 RFC 假设的 "agent fill vars → 一步 render MP4" 显著不同。

→ 新增 [RFC-04: Storyboard-first Workflow](../research/2026-05-26-spec-04-storyboard-workflow.md)，作为前 3 份的修订指引。

**新核心命题**：
- 用户不是"工程师 with template id 和 vars"，是"创作者 with 一堆图文 + 一句话意图"
- HTML Storyboard 是关键中间产物——人可读、可调、可批准
- 只有 Storyboard 通过用户验收才 render MP4，避免渲染浪费 + 让用户保留创作主导权

**新护城河**：资产理解 + storyboard 编排 + 跨引擎渲染三层叠加，HF / Remotion 都没做前两层（他们假设用户已经知道想做什么）。

## 六个关键设计抉择（写下来不让后续会话动摇）

### 1. **不发明新 DSL，做 thin meta-layer**

拒绝："让用户写 html-video.json，我们编译到 4 个 backend"。
理由：永远落后任意 backend 的新 feature；4 个 transpile 维护地狱；用户写一段 React 想用 Remotion 优势但被 DSL 阉割 → 反向。
做法：用户写的是 backend-native 代码，html-video 只在外面包一层。

### 2. **每个 template = 一个 engine 归属**

拒绝："同一个 idea 出多 engine 实现的同一个 template id"。
理由：维护多份会漂移；用户视角下"同一模板"两版做出不同效果是 bug 不是 feature。
做法：要多 engine → 发布多个 template id（例 `bar-chart-race-mc` / `bar-chart-race-hf`），各自独立 metadata。

### 3. **CLI 是 agent 唯一接口**

拒绝："agent 直接 import @html-video/core"。
理由：进程隔离 + 跨 agent 复用（Claude Code / Cursor / Codex 都靠 shell 调），一个 contract 走天下。
做法：所有功能从 CLI 走，stdout 严格 JSON，stderr 做 progress / debug。

### 4. **不发明 cross-engine fallback**

拒绝："HF 渲染挂自动用 Revideo 重试"。
理由：用户选 engine 通常有理由（license、风格、团队偏好）；偷偷换会让结果不一致。
做法：失败 = 失败，agent 跟用户说，让 agent / 用户重新 search-templates。

### 5. **License 是一等公民**

拒绝："license 字段先留空之后再说"。
理由：商用 / 二改 / attribution 是开源生态的真实问题，跑起来再补成本翻倍；OD 已经因为 plugins 的 license 漂移踩过坑。
做法：metadata 强制要 SPDX id；CLI search 默认带 license-allow filter；CC-BY-SA / GPL 强 copyleft 给 warning。

### 6. **Storyboard 是用户审批 gate**（mid-session 新增）

拒绝："agent 一气呵成 render 出 MP4 就完了"。
理由：渲染慢且贵；用户对 HTML 改的成本远低于对 MP4 改；分镜阶段批改是创作产业的标准范式（电影、广告、动画都先 storyboard）。
做法：所有用户主流程必经 `storyboard preview` 阶段；`html-video render --template ...` 只留给开发者直跑（template 测试 / CI 用）；agent 不允许跳过 storyboard 直接 render MP4。

---

## v0.1 MVP 范围（按 RFC-04 修订后）

接下来写代码的范围：

- ✅ `@html-video/core`：Asset / AssetBundle / Storyboard / Scene 数据结构 + sqlite 持久化 + content-addressed asset store + Template registry + Engine selector
- ✅ `@html-video/adapter-hyperframes`：第一个 reference adapter，实现 `validate / render / renderToHtml / preview`
- ✅ `@html-video/cli`：`doctor / list-engines / assets upload / storyboard generate / storyboard edit / storyboard preview / storyboard render`（用户主流程）+ `render` / `inspect-template`（开发者 dev-mode）
- ✅ `@html-video/storyboard-ui`：浏览器 storyboard preview 页面（timeline + scene grid + inline edit + 全屏播放 mock）
- ✅ `@html-video/agent-skill-claude-code`：storyboard-first SKILL.md + 3-5 个 dogfood use case
- ✅ 5 个 reference templates（覆盖 intro / data-chart / image-pan / text-card / outro 五种 scene role）
- ✅ Monorepo（pnpm workspace）+ 基础 CI（type-check / lint / unit test）

**不**进 MVP（推到 v0.2+）：
- ❌ adapter-remotion / motion-canvas / revideo（先把 HF 路径 + storyboard 闭环跑通）
- ❌ AI 智能编排（v0.1 是 LLM 即兴选 template，v0.2 加规则 + ML）
- ❌ AI 视觉理解资产（v0.1 用 mime + 文件名启发）
- ❌ 协作 / 多人审稿
- ❌ Cloud / Lambda 部署（先本地 chromium）
- ❌ Telemetry（默认 off，alpha 不发）
- ❌ Template marketplace 网站（先 GitHub repo + npm 发布）

---

## 命名约定（避免后续 bikeshed）

| 类型 | 命名 | 例 |
|---|---|---|
| Repo | `nexu-io/html-video` | — |
| Monorepo workspace | `pnpm` | — |
| Core 包 | `@html-video/core` | — |
| Adapter 包 | `@html-video/adapter-<engine-id>` | `@html-video/adapter-hyperframes` |
| CLI 包 | `@html-video/cli` 或 binary 名 `html-video` | — |
| Agent skill 包 | `@html-video/agent-skill-<agent>` | `@html-video/agent-skill-claude-code` |
| Template 包 | `@html-video/template-<kebab-id>` | `@html-video/template-data-bar-chart-race` |
| Template metadata 文件 | `template.html-video.yaml` | — |
| Config 文件 | `html-video.config.json` | — |

---

## 跟姊妹项目的接口（提前想好）

| 项目 | 接口点 | 状态 |
|---|---|---|
| `growth-dashboard` (T7) | 数据源（SQLite）→ html-video template vars | 待 v0.2，写一个 `html-video-data` adapter |
| `open-design`（T5）/ OD 客户端 | OD 客户端 plugins-home 是否要列 html-video templates？ | 待 v0.2，等 html-video alpha 发布 |
| `od-pitch` (T6) | launch deck / 杂志风介绍页 | 等用户决定何时 launch |
| `od-landing` (T8) | nexu.io 主域 落地页给 html-video 加入口？ | 待 v1 |

---

## 风险 / 不确定性 register

| 风险 | 严重度 | 缓解 |
|---|---|---|
| HF 上游 breaking change | 高 | adapter peerDep 锁 semver 范围；CI 跑 HF latest 兼容性 |
| Remotion license 变更 | 中 | 不依赖 Remotion 收入模型；adapter 只是壳 |
| Motion Canvas 无 server render → adapter 难做 | 中 | v0.2 才接，先用 Revideo 替代 explainer 路径 |
| 用户嫌 4 个 backend 太重 | 中 | adapter lazy install，doctor 自动 hint，按需 pull |
| HF 自己迭代到 multi-backend → 跟我们重叠 | 高 | 早点 ship + 强调 "neutral aggregator" 定位（HF 是参与者不是中立方） |
| AI generative video（Sora / Veo / Runway）取代 HTML 路线 | 中 | v0.3+ 加 generative-video adapter（"生成 → HTML 模板再加工"两段式） |

---

## 下次会话该做什么（顺序明确）

按重要性 / 解锁度排：

1. **写 `@html-video/core` 骨架**（pnpm workspace + TS 配置 + EngineAdapter type 落地）
2. **写 `@html-video/adapter-hyperframes` 骨架**（先实现 capabilities + validate，render 跑通再说）
3. **挑 1 个 HF native template 当 reference**（直接拷一个 HF 仓库的 example template，套上 RFC-02 metadata 验证 schema 合理性）
4. **写 CLI `html-video doctor` + `list-engines`**（最简单的两个命令，跑通端到端最小回路）
5. **手写一次 SKILL.md，让 Claude Code 这边的本人会话试用**（dogfood，发现 prompt-level 问题）

每一步独立 commit，PR 评审走 nexu-io org（等 GitHub repo 推上去后开始）。

---

## Open Questions 集合（汇总三份 RFC 的）

### 来自 RFC-01

1. template variables 的 schema 校验放 core 还是 adapter？
2. 音频混音 core helper vs adapter 各自处理？
3. 字幕 burn-in / sidecar 谁烧？
4. 资产 resolver（图片字体）放哪？
5. 跨 engine retry —— v0.1 已决定不做

### 来自 RFC-02

1. i18n 多语言 metadata
2. 复杂模板的 input grouping
3. Template 之间的依赖（transition + main 组合）
4. 外部数据源（CSV / Sheets URL）支持
5. A/B 变体共享同源代码

### 来自 RFC-03

1. Skill 之间协作（html-video → growth-dashboard 直接读 SQLite vs MCP）
2. Multi-shot timeline composer skill
3. Content-hash cache
4. OpenCode 集成路径

这些不是 v0.1 阻塞，但写代码时遇到要回查这一节避免重新发明。

---

## 给 Joey 的复盘 sentence

> 一次会话沉淀了 4 份 RFC（adapter / template / agent-skill / storyboard）+ 1 份决策日志，定下：**meta-layer / 不发明 DSL / template engine-locked / CLI 唯一 agent 接口 / license 一等公民 / Storyboard-first 用户审批 gate**。下次会话可直接进 `@html-video/core` 代码骨架（按 RFC-04 修订后的 v0.1 范围），不再 bikeshed 抽象。
