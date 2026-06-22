# RFC-08：Remotion Adapter（第二个真引擎，兑现 multi-engine 叙事）

> **Status**: Draft v0.1（待 Joey review 后进 PoC）
> **Date**: 2026-06-06
> **Scope**: 把 Remotion 接成 `@html-video/adapter-remotion`，作为继 hyperframes 之后第一个真正异范式的 backend。
> **依赖**: RFC-01（Engine Adapter 接口）/ RFC-02（Template metadata）/ RFC-06（Content Graph）
> **决策**: Joey 已拍板 **两者都要、分阶段**——Phase 1 HTML→Remotion 桥接（兜底），Phase 2 原生 .tsx 模板（进阶）。本文先文档，确认后写 PoC。

---

## 0. 为什么是现在做 Remotion（动机）

整合 Remotion 不是"加个引擎"那么简单，它是**第一次真正把 meta-aggregator 卖点做实**。当前事实：

- RFC-01 把 4 引擎接口设计得完整，Remotion 的 capability 声明也早写好了（见 RFC-01 §"Remotion"）。
- 但运行时**只有 `adapter-hyperframes` 一个适配器，而且它根本没用 Hyperframes**——它是 Playwright 录屏 + ffmpeg 转码（`packages/adapter-hyperframes/src/render.ts` 开头注释自陈：*"Upstream Hyperframes was never required at runtime for this adapter"*）。
- **结论**：现状 = 单引擎（Chromium 录屏），挂着"多引擎 pluggable"的招牌。README / launch 叙事的核心差异化目前是**空的**。

Remotion adapter 是兑现 `EngineAdapter` 抽象的第一个真实证明：它是**异范式**（react-tsx vs html-css-gsap）、**异渲染路径**（deterministic 逐帧 vs 实时录屏）、**异 license**（commercial-restricted vs free-osi）。把它接通，三件事同时成立：

1. `EngineRegistry` 真的注册了 ≥2 个 adapter，`agent` 的 engine 决策有真实选项。
2. capability 字段（`licensing` / `paradigms` / `renderTarget`）从"文档示例"变成"runtime 真值"。
3. README 表格里"多引擎 pluggable"有了第二行可点的实据。

---

## 1. Remotion 事实核对（2026-06-06，全部为最新）

RFC-01 当初写下的 Remotion 假设，**逐条仍然成立**：

| RFC-01 假设 | 2026-06-06 核对结果 |
|---|---|
| 范式 `react-tsx` | ✅ 仍是 React 组件 + `<Composition>`，无变化 |
| `4.x` | ✅ 最新稳定 **v4.0.472**（2026-06-04）；5.0 开发中（强制 Automator telemetry、min Node 18、新条款） |
| `commercial-restricted`（4+ devs 付费） | ✅ 个人 / ≤3 人公司 / 非营利**免费**；4+ 人付费：Creators $25/seat/月，Automators $0.01/render（$100/月起），Enterprise $500/月起 |
| `@remotion/renderer` Node API | ✅ 三步 `bundle()` → `selectComposition()` → `renderMedia()`，有 `onProgress`、可复用 browser、本地 chromium |
| 输出 `mp4/webm/gif/png-sequence` | ✅ `renderMedia` 支持 h264/h265/vp8/vp9/gif/prores；`renderStill` 出单帧 png/jpeg/webp |
| `maxResolution 7680×4320` | ✅ 受 Chrome 单图 2^29 px 上限约束，8K 视频帧无问题 |

**License 是这个 adapter 的一等公民**（不是脚注）：html-video 是开源 meta-layer，用户里大量是 4+ 人团队。adapter 的 `capabilities.licensing = 'commercial-restricted'` 必须**真实暴露给 agent**，让 agent 在"自由/省钱"场景能主动避开 Remotion、推 hyperframes/revideo。这是我们相对"只会 Remotion"的工具的诚实优势，要讲出来。

来源（核对依据）：
- Remotion pricing & license — https://www.remotion.dev/license / https://remotion.pro
- `@remotion/renderer` SSR Node API — https://www.remotion.dev/docs/ssr-node / https://www.remotion.dev/docs/renderer/render-media
- `bundle()` — https://www.remotion.dev/docs/bundle
- `<IFrame>` — https://www.remotion.dev/docs/iframe
- `<Img>` / `staticFile()` — https://www.remotion.dev/docs/img / https://www.remotion.dev/docs/staticfile
- HTML-in-canvas（实验特性）— https://www.remotion.dev/docs/client-side-rendering/html-in-canvas

---

## 2. 根本性矛盾：HTML-centric pipeline vs React-tsx 范式

这是整合 Remotion **最先要解决的事**，决定路线形态。

### 我们的 pipeline 是 HTML-centric

RFC-06 的 content-graph 流水线：用户意图 → `content-graph`（节点）→ 每个节点产出**一份 HTML 文件**（`writeFrameHtml`）→ adapter 录这份 HTML（hyperframes adapter 用 Playwright `page.goto(file://...)`）。

整套 authoring 资产 = **27 个 HTML 模板**，全是 inline CSS + CSS keyframes / GSAP。

### Remotion 的范式是 React 组件

Remotion 要的是 `<Composition>` + React 组件 + `useCurrentFrame()` 驱动动画。**它根本不吃 HTML 文件**。

所以"整合 Remotion"分裂成两条范式上完全不同的路线（Joey 已决定两条都做、分阶段）：

```
                       ┌─ Phase 1: 桥接 ─ 把现有 HTML 帧塞进 Remotion 时间轴
HTML-centric pipeline ─┤
                       └─ Phase 2: 原生 ─ 新增一批 React-tsx 写的原生 Remotion 模板
```

---

## 3. Phase 1：HTML→Remotion 桥接（兜底，先做）

**目标**：零改 / 极少改现有 27 个模板，让它们能走 Remotion 渲染管线出 MP4。立刻让 `EngineRegistry` 有第二个真 adapter。

### 3.1 朴素方案为什么不行（核心技术坑）

最直觉的写法是写一个通用 React 组件，用 Remotion 官方 `<IFrame>` 把 HTML 帧塞进去：

```tsx
import { IFrame, staticFile } from 'remotion';
export const HtmlFrame: React.FC<{ src: string }> = ({ src }) => (
  <IFrame src={staticFile(src)} style={{ width: '100%', height: '100%' }} />
);
```

`<IFrame>` 会自动 `delayRender()` 等 `onLoad`，文件加载没问题。**但官方明确警告**（iframe 文档 + img 文档都强调）：

> 内嵌网页**最好没有动画**——只有 `useCurrentFrame()` 驱动的动画会被 Remotion 同步，**否则会闪烁 / 动画不同步**。

机制：Remotion 渲染是 **deterministic 逐帧**——它把时间钟"冻"在第 N 帧、截图、再跳到第 N+1 帧。而 CSS keyframes / GSAP 用的是**浏览器自己的 wall-clock**（`requestAnimationFrame` / `Date.now()`），跟 Remotion 的逐帧时钟**完全脱钩**。结果：Remotion 截每一帧时，iframe 内的动画处在"随机的真实时间点"，每帧之间不连续 → 闪烁/抖动。

**这恰恰是我们 27 个模板的命门**——它们全是 CSS/GSAP 动画（hyperframes adapter 里那段 probe `animationDuration` / `gsap.globalTimeline` 的逻辑就是在伺候这些动画）。所以朴素 `<IFrame src>` 桥接 = **动画全乱**。

### 3.2 解法：时间钟桥接（time-driver injection）

要让 iframe 内的 CSS/GSAP 动画跟 Remotion 的逐帧时钟同步，桥接组件在每一帧把 Remotion 的当前时间**注入 iframe 并强制把动画"seek"到那个时间点**。两种实现强度，递进选择：

**(A) CSS Animation 同步——`document.getAnimations()` + `currentTime`**（首选，覆盖纯 CSS keyframes 模板）

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const tMs = (frame / fps) * 1000;
// 每帧把 iframe 内所有 CSS 动画 seek 到 tMs，并暂停（不让浏览器自走）
iframe.contentWindow.document.getAnimations().forEach(a => {
  a.pause();
  a.currentTime = tMs;
});
```

Web Animations API 的 `getAnimations()` 能拿到 CSS keyframes 动画句柄，`currentTime` 可精确 seek。这把"浏览器 wall-clock 驱动"换成"Remotion 帧驱动"，逐帧一致、零闪烁。

**(B) GSAP 同步——驱动 `gsap.globalTimeline`**（覆盖 GSAP 模板）

```tsx
const tl = iframe.contentWindow.gsap?.globalTimeline;
if (tl) { tl.pause(); tl.time(tMs / 1000); }   // seek 到秒
```

GSAP timeline 本就支持 `.time(seconds)` seek + `.pause()`，比 CSS 还好控。hyperframes adapter 已经在读 `gsap.globalTimeline.getChildren()`，证明模板里 GSAP 实例在 `window.gsap` 上可达。

**(C) 注入策略**：桥接组件 mount 时用 `useDelayRender` 等 iframe `onLoad` → 拿 `contentWindow` → 每帧 seek。把 (A)+(B) 合成一个 `<HtmlFrameDriver>` 组件，对模板**无侵入**（不要求模板改代码，只要求动画跑在 CSS Animations 或全局 GSAP timeline 上——我们 27 个模板都满足）。

> ⚠️ 同源限制：`contentWindow.document` 访问要求 iframe 同源。`staticFile()` 出来的本地 HTML 在 bundle 里同源，OK；远程 URL 会被跨域挡住——桥接只对**本地 HTML 帧**生效（正是我们的用例），远程页面退回"无动画静态嵌入"。

### 3.3 备选：HTML-in-canvas（实验特性，先不用）

Chrome 149+ 有实验 API `allowHtmlInCanvas`，整帧截 HTML 不靠 CSS 模拟，更精确。**但**：① 要 Chrome 149+ 且开 flag；② **不能渲染含 `<IFrame>` 的合成**（跟我们桥接组件直接冲突）；③ 实验阶段不稳。**v0.1 不用**，列为未来观察项。

### 3.4 Phase 1 的诚实定位

桥接方案把 Remotion 当"**一个换皮的逐帧 Chromium 渲染器**"用。相比现有 Playwright 录屏，它的**真实增益**有限但具体：

- ✅ deterministic 逐帧（不丢帧、不受机器负载抖动影响时长——Playwright 录屏靠 wall-clock 录制，机器卡了就丢帧）
- ✅ 接上 Remotion 多轨音频 / `<Audio>` / 字幕生态
- ✅ 一行切到 `renderMediaOnLambda` 做云端规模化（hyperframes adapter 没有这条路）
- ⚠️ **但桥接本身不解锁 Remotion 的招牌能力**（数据驱动动画、`spring()`、`interpolate()` 等）——那些要 Phase 2 原生模板才有。

所以 Phase 1 的卖点是"**多引擎成立 + Lambda 可扩展 + deterministic**"，不是"动画更强"。文档/对外别夸过头。

---

## 4. Phase 2：原生 Remotion 模板（进阶，后做）

**目标**：把 Remotion 当成 RFC-01 设想的"第二种 authoring 范式"，新增一批**真正用 React-tsx + `useCurrentFrame` 写的原生 Remotion 模板**，解锁桥接给不了的能力。

### 4.1 这才是 Remotion 的差异化价值

- **数据驱动动画**：`interpolate(frame, [0,30],[0,100])` + `spring()`——柱状图涨、数字滚动、折线生长。正是 RFC-01 capability 里写的 `bestFor: ['data-driven', 'long-form-narration']`。content-graph 的 `data` 节点（RFC-06）天生适配。
- **逐帧精确 + 长片**：narration 旁白对齐、章节、长时间轴。
- **Lambda 规模化 + 参数化批量**：同一 `<Composition>` 喂不同 `inputProps` 批量出片。

### 4.2 content-graph 如何产出 tsx

RFC-06 的节点目前产出 HTML（`writeFrameHtml`）。Phase 2 要让节点能产出 `.tsx`：

- template metadata（RFC-02）的 `engine: remotion` 模板，其 `source/` 放的是 React 组件 + `Root.tsx`（注册 `<Composition>`）。
- studio agent 的 prompt 要新增"写 Remotion 组件"的分支（教 `useCurrentFrame` / `interpolate` / `<Sequence>`）。
- `variables` → Remotion `inputProps`（天然契合，Remotion 一等公民支持 `inputProps` + zod schema 校验，对上 RFC-01 Open Question #1 的"core 用 zod 统一校验"）。

### 4.3 工作量诚实评估

Phase 2 = **建第二套模板生态**（不是改 adapter）。要：① 起码 3-5 个原生 tsx 模板打样；② agent prompt 第二范式分支；③ content-graph → tsx 产出路径；④ preview（Remotion Studio / `@remotion/player`）。比 Phase 1 大一个量级。**先把 Phase 1 跑通见效，Phase 2 单独立 RFC 再细化。**

---

## 5. Adapter 包结构（落地 Phase 1）

遵循 RFC-01 §"Adapter 包结构"约定：

```
@html-video/adapter-remotion/
├── package.json          # peerDependency: remotion@^4 / @remotion/renderer@^4 / @remotion/bundler@^4
├── src/
│   ├── index.ts          # export default EngineAdapter 实例（id:'remotion'）
│   ├── capabilities.ts    # 静态 capability（直接搬 RFC-01 的声明 + license 字段）
│   ├── validate.ts        # 校验：engine===remotion / format / sourcePath 存在（<50ms，只读）
│   ├── render.ts          # bundle()→selectComposition()→renderMedia()，onProgress 映射到我们的 stage
│   ├── preview.ts         # 可选：起 Remotion Studio / @remotion/player dev server
│   ├── bridge/            # Phase 1 桥接资产
│   │   ├── Root.tsx       # 注册一个通用 <Composition id="HtmlFrame">
│   │   ├── HtmlFrameDriver.tsx  # §3.2 的 iframe + 时间钟 seek 组件
│   │   └── entry.ts       # registerRoot 入口（bundle 的 entryPoint）
│   └── native/            # Phase 2 占位（原生模板支持，先空）
└── README.md
```

### render() 与现有契约对接（关键映射）

| 我们的 `RenderInput/Config` | Remotion 侧 |
|---|---|
| `template.sourcePath`（HTML 帧路径） | 拷进 bundle 的 `public/`，作为 `inputProps.htmlSrc` 传给 `<HtmlFrame>` |
| `config.resolution / fps` | `selectComposition` 的 metadata override（`width/height/fps`） |
| `config.duration`（'auto' 时） | 桥接帧探测动画时长（复用 hyperframes adapter 那段 probe 逻辑）→ `durationInFrames = sec*fps` |
| `config.outputPath` | `renderMedia({ outputLocation })`，**先写 tmp 成功再 rename**（RFC-01 §"不可变性"） |
| `config.audio[]` | Phase 1 可先用 ffmpeg 后混；Phase 2 走 Remotion `<Audio>` |
| `ctx.onProgress` | `renderMedia({ onProgress })` 的 `{progress}` 映射到 preparing/rendering/muxing 三段 |
| `ctx.signal` | abort → `renderMedia` 无原生 cancel，需 kill 进程 / 关 browser；reject `cancelled` |
| 错误 | `engine-not-installed`（peer dep 没装）/ `render-failed`（renderMedia throw）等，对齐 RFC-01 错误码表 |

### bundle() 复用（性能）

`bundle()` 是 webpack 打包，**贵、应只跑一次**。多帧渲染（content-graph 多节点）时：bundle 一次 → 循环 `selectComposition` + `renderMedia` 喂不同 `inputProps.htmlSrc`。adapter 内缓存 bundleLocation。这跟 hyperframes adapter 的"per-frame 独立录屏 + 上层 concat"不同——Remotion 这条更省。

---

## 6. License 边界与对外口径

- adapter 的 `capabilities.licensing = 'commercial-restricted'` **必须真实**；agent 决策时据此提示用户"4+ 人团队商用需 Remotion 商业 license"。
- **html-video 自身（Apache-2.0）不受影响**——我们只在 `peerDependencies` 引 Remotion，不打包、不分发 Remotion 代码。用户自己 `pnpm add remotion` 时同意其 license。这跟我们引 Playwright（Apache-2.0）是两种 license 关系，README/ATTRIBUTIONS 要写清。
- **对外别把 Remotion 当默认引擎宣传**——默认仍是 free-osi 的 hyperframes(playwright)/revideo 路线，Remotion 是"你的团队已经在用 React / 需要 Lambda 规模"时的可选项。这保护"开源、自由"的产品定位。
- ATTRIBUTIONS.md 需加 Remotion 条目（作者 Jonny Burger / remotion.pro / license 链接 / "not affiliated"）。

---

## 7. 风险 & Open Questions

| 项 | 说明 | 处置 |
|---|---|---|
| **桥接闪烁**（§3.1） | CSS/GSAP 不被 Remotion 时钟同步 | §3.2 time-driver 注入；PoC 第一件事就是验证这个能不能消闪烁 |
| **同源限制** | 跨域 iframe 拿不到 `contentWindow.document` | 桥接只保证本地 HTML 帧；远程页退回静态 |
| **`delayRender` 超时** | iframe / 动画 seek 慢于 28s 默认超时 | 调 `delayRenderTimeoutInMilliseconds`；动画时长本来就 cap 30s |
| **字体 / OS 渲染差异** | `renderMedia` 本地 vs Lambda 文字位置可能偏 | 模板显式 `lineHeight`；约定同 OS 渲染 |
| **bundle 体积 / webpack 慢** | 首次 bundle 几秒~十几秒 | adapter 内缓存 bundleLocation，多帧复用 |
| **Remotion 5.0 强制 telemetry** | Automator 路径 5.0 起强制遥测 | 钉 `remotion@^4`；5.0 升级前单独评估 |
| **Phase 1 增益有限** | 桥接不解锁 Remotion 招牌能力 | 文档诚实定位；真价值在 Phase 2 |

**Open Questions（PoC 阶段定）**：

1. 桥接组件放 adapter 包内（bundle 时一起打），还是生成到项目 workDir？倾向**包内**（用户不该看到桥接胶水）。
2. `duration='auto'` 的动画探测——复用 hyperframes adapter 的 probe 逻辑（抽成 `@html-video/core` 共享 helper），还是在桥接组件内用 `getAnimations()` 算？倾向**抽 core helper**，两 adapter 共用。
3. preview() 是否做？Phase 1 可先不做（OS 跑 render 即可），studio 现有 iframe 实时预览已覆盖看动效需求。

---

## 8. 推荐落地顺序（PoC → 增量）

> Joey 点头后执行。每步都能独立验证，不憋大招。

1. **PoC（最小可行）**：建 `packages/adapter-remotion` 骨架 + `capabilities.ts`（搬 RFC-01）+ `validate.ts`。写 `bridge/HtmlFrameDriver.tsx`（§3.2 含 CSS+GSAP seek）+ `Root.tsx`。`render.ts` 走 bundle→select→renderMedia。**验收：拿现有一个 GSAP 模板（如 `frame-glitch-title`）渲出 MP4，肉眼确认无闪烁、动画完整。**
2. **接 registry / CLI**：`EngineRegistry.register(remotionAdapter)`；CLI `doctor` 探测 remotion 是否安装；`search-templates` 的 engine 过滤能看到 remotion。
3. **多帧 + bundle 复用**：content-graph 多节点走"bundle 一次 + 循环 renderMedia"，对比 hyperframes concat 路径出片一致。
4. **文档**：README 多引擎表格补 Remotion 实据；ATTRIBUTIONS 加条目；本 RFC 转 Accepted。
5. **（Phase 2 另起 RFC-09）**：原生 tsx 模板生态。

---

## 附：与 hyperframes adapter 的对照（一眼看清两条渲染路径）

| | adapter-hyperframes（现有） | adapter-remotion（本 RFC） |
|---|---|---|
| 实际引擎 | Playwright + ffmpeg（没用 HF） | Remotion `@remotion/renderer` |
| 渲染方式 | 实时录屏（wall-clock） | deterministic 逐帧 |
| 吃什么 | HTML 文件（file://） | React 组件；Phase 1 用桥接吃 HTML |
| 动画同步 | 录屏天然同步（就是真跑） | 桥接需 time-driver seek（§3.2） |
| 多帧 | per-frame 录屏 + ffmpeg concat | bundle 一次 + 循环 renderMedia |
| 云端 | 无 | renderMediaOnLambda 可扩展 |
| license | free-osi | commercial-restricted（4+ 人付费） |
