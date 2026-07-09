# HTML→Video 开源生态调研（2026-05-26）

> 启动 html-video 项目时的市面竞品快照。供后续架构 / 定位讨论参考。

## 关键事实（事实核对过 GitHub API，非 web search hallucination）

| Repo | ★ | License | Last push | 描述 |
|---|---|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **21,297** | Apache-2.0 | 2026-05-26 | "Write HTML. Render video. Built for agents." 真正的赛道头部 |
| [remotion-dev/remotion](https://www.remotion.dev/) | ~21K | Source-available（4+ 人公司付费） | 活跃 | React-first，重度 backend，付费门槛 |
| [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas) | ~16K | MIT | 活跃 | TypeScript 生成器，canvas-based，单作者 explainer 场景 |
| [redotvideo/revideo](https://github.com/midrender/revideo) | ~3.7K | MIT | 2025-05 | Motion Canvas fork + 服务端渲染 API |
| thecodacus/rendiv | 41 | Apache-2.0 | 2026-05-14 | React + Playwright Remotion 替代，几乎无人用 |
| jsongo/open-motion | 5 | MIT | 2026-02 | 同上，toy 级 |
| dsplce-co/htmlrec | 2 | 无 license | 2026-04 | Rust CLI，HTML + Chromium，toy 级 |
| JohnEsleyer/clawmotion | 1 | 无 license | 2026-02 | toy 级 |
| Trejon-888/frameforge | 3 | MIT | 2026-04 | 同上 |
| endersmoon/reelgen | 0 | MIT | 2026-03 | 同上，但 idea 不错（MCP server + JSON scenes） |

**洞察**：除 Hyperframes / Remotion / Motion Canvas / Revideo 四个真竞品外，其他"alternative" 几乎都是个人 toy 项目，没有用户基础。

## 真竞品分析

### 1. Hyperframes（核心对标）

**优势**：
- 已经 21K★，Apache-2.0，agent-native
- HeyGen 背书，活跃维护
- Frame Adapter 让 GSAP / Anime.js / Lottie / Three.js / CSS / WAAPI 都 seekable
- 已有 Claude Code / Cursor / Gemini / Codex 的 agent skills

**limitation（潜在）**：
- 单一 authoring 范式（HTML + CSS + GSAP），React 用户不习惯
- 单一 rendering pipeline（Puppeteer + FFmpeg），不接 Remotion 的 Lambda 优化、不接 Motion Canvas 的 LaTeX/code-block 强项
- Template 生态围绕 HF 自家
- HeyGen 的产品方向不一定全面服务社区（例：会不会接 Sora / Runway / Veo 等 AI generative model 作为 backend？不明）

### 2. Remotion

- React 用户基数大，但 source-available license 让企业用户（4+ devs）付费 → 大量需求被劝退
- 已有 Lambda 渲染基建，单帧成本极低（10s 4K $0.013）
- **html-video 适配 Remotion 的价值**：把 Remotion 的渲染能力开放给非 React 用户 / 不愿付费的小团队

### 3. Motion Canvas / Revideo

- Canvas 渲染，纯函数式生成器，**数学/code/explainer 场景的 SOTA**（Manim 现代版）
- Motion Canvas 不做 server-side render（作者明确不打算）
- Revideo 补足这块，YC 出身 + MIT
- **html-video 适配价值**：把 explainer 场景的强项接入到统一界面

## html-video 的产品空间（meta-aggregator）

类比 OD 在 design agent 领域的 meta-layer 定位：

| 层 | OD (design) | html-video (video) |
|---|---|---|
| 用户 | 设计师 / PM / 创始人 | 内容创作者 / 营销 / 创始人 |
| Agent | Claude Code / Cursor / Codex | 同上 |
| Backend | 设计模板 + skills | Hyperframes / Remotion / Motion Canvas / Revideo |
| 价值 | "agent 帮我做 production-grade 设计" | "agent 帮我做 production-grade 视频" |

**核心命题**：用户不需要自己学 GSAP / React / TypeScript generator 三套体系。一个 agent + html-video 的 adapter 接口，描述意图 → agent 选 engine + 模板 → 出片。

## 架构草案（待定）

```
              ┌──────────────────────────┐
              │   coding agent (CC/Cursor) │
              └──────────────┬─────────────┘
                             │ 通过 skill / MCP
              ┌──────────────▼─────────────┐
              │     html-video core         │
              │   (engine selector +        │
              │    template registry +      │
              │    rendering orchestrator)  │
              └──┬──────────┬──────────┬────┘
                 │          │          │
        ┌────────▼─┐  ┌─────▼────┐  ┌──▼──────────┐  ...
        │ HF       │  │ Remotion │  │ Motion       │  pluggable
        │ adapter  │  │ adapter  │  │ Canvas/      │  engine adapters
        │          │  │          │  │ Revideo      │
        └──────────┘  └──────────┘  └──────────────┘
```

未定的关键设计点：

1. **engine adapter 接口标准** —— 输入（intent / template / variables）→ 输出（MP4/WebM）的抽象边界在哪
2. **template 格式** —— 跨引擎统一的 template metadata（agent 知道哪个 template 用哪个 engine）
3. **agent skill 设计** —— skills/ 的 trigger keywords / 参数 schema / engine 推荐逻辑
4. **studio UI** —— 是否做本地 GUI preview，类似 Hyperframes / Remotion Studio
5. **packaging** —— monorepo（pnpm workspace）vs polyrepo
