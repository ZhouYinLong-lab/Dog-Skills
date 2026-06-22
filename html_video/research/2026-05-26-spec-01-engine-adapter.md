# RFC-01：Engine Adapter 接口（核心抽象）

> **Status**: Draft v0.1
> **Date**: 2026-05-26
> **Scope**: 定义 html-video 跨 engine 的统一接口，让 Hyperframes / Remotion / Motion Canvas / Revideo 可插拔接入。
> **Audience**: 写 adapter 的 contributor / 集成 html-video 的 agent skill / 后续做 studio UI 的人

---

## 设计目标

1. **加新 backend 不改 core** —— 一个 backend = 一个独立 npm 包 `@html-video/adapter-<name>`，实现 `EngineAdapter` 接口即可
2. **agent 友好** —— `capabilities` 让 agent 程序化地决策"这个用例选哪个 engine"
3. **不强求功能并集** —— 弱 engine 不必假装支持所有功能，`validate()` 返回明确的 fail reason
4. **不发明 authoring 范式** —— 用户写的还是 HTML / React / TS-generator 原生，html-video 不引入第四种 DSL

---

## 接口（TypeScript）

```ts
// core/types.ts

export interface EngineAdapter {
  /** 稳定的 ID，下划线/小写。例: "hyperframes" "remotion" "motion-canvas" "revideo" */
  id: EngineId;

  /** 人类可读名称 */
  name: string;

  /** 版本：upstream engine 版本（例 hyperframes@0.4.x），不是 adapter 自身版本 */
  upstreamVersion: string;

  /** 静态能力声明 —— agent 决策的关键依据 */
  capabilities: EngineCapabilities;

  /** 校验 template 能否被本 engine 渲染。不实际渲染。同步即可 */
  validate(template: Template): ValidationResult;

  /** 渲染入口 */
  render(input: RenderInput, ctx: RenderContext): Promise<RenderOutput>;

  /** 启动本地 preview server（studio 用）；返回 dev URL */
  preview(template: Template, ctx: PreviewContext): Promise<PreviewHandle>;

  /** 列出 engine 知道的 native template 路径。给 template registry 做 import 用 */
  listNativeTemplates?(): Promise<NativeTemplateRef[]>;
}

export type EngineId = string; // 不预设枚举，让第三方 adapter 自由扩展

export interface EngineCapabilities {
  /** 输入范式：用户写代码用的语言/形态 */
  paradigms: Paradigm[];

  /** 输出格式 */
  outputFormats: OutputFormat[];

  /** 最大分辨率（adapter 实现层 cap，不是物理上限） */
  maxResolution: { width: number; height: number };

  /** 是否支持透明通道 */
  alpha: boolean;

  /** 音频：none = 不能加音轨；single = 一条；multi = 多轨混音 */
  audio: 'none' | 'single' | 'multi';

  /** 字幕：none / burn-in / sidecar (vtt/srt) */
  subtitles: ('none' | 'burn-in' | 'sidecar')[];

  /** 渲染 backend（关系到部署） */
  renderTarget: ('local-chromium' | 'local-canvas' | 'lambda' | 'cloud-run')[];

  /** License tier：影响 agent 决策（自由用户可能想避开 commercial-restricted） */
  licensing: 'free-osi' | 'commercial-restricted' | 'unknown';

  /** 平均渲染速度 hint：1080p / 10sec / 60fps 在标准硬件上的秒数。粗略，作为 agent tie-breaker */
  renderSpeedHint?: { resolution: string; durationSec: number; fps: number; estimatedRenderSec: number };

  /** 特长场景，自由文本 tag。agent 用 fuzzy match */
  bestFor: string[];

  /** 自报短板，文字描述。Agent decision 文档化 */
  weaknesses: string[];
}

export type Paradigm =
  | 'html-css-gsap'        // HF, htmlrec
  | 'react-tsx'            // Remotion, Rendiv, OpenMotion
  | 'ts-generator'         // Motion Canvas, Revideo
  | 'json-scene'           // Reelgen, VideoFlow
  | 'imperative-canvas';   // 通用 canvas API

export type OutputFormat = 'mp4' | 'webm' | 'webm-alpha' | 'gif' | 'png-sequence' | 'apng';

export interface Template {
  /** 跨引擎统一 id（见 RFC-02） */
  id: string;
  /** 这个 template 实际归属的 engine */
  engine: EngineId;
  /** 源代码路径（绝对或 monorepo 相对）—— adapter 知道怎么打开 */
  sourcePath: string;
  /** 用户传入的变量。schema 在 template metadata 里 */
  variables?: Record<string, unknown>;
}

export interface RenderInput {
  template: Template;
  variables: Record<string, unknown>;
  config: RenderConfig;
}

export interface RenderConfig {
  format: OutputFormat;
  resolution: { width: number; height: number };
  fps: number;
  /** 时长（秒）。某些 engine 是 template 内部决定的，传 'auto' */
  duration: number | 'auto';
  /** 输出路径（绝对路径） */
  outputPath: string;
  /** 透明背景（仅当 format=webm-alpha 或 png-sequence） */
  alpha?: boolean;
  /** 编码质量 0-100 或 ffmpeg-style preset */
  quality?: number | 'low' | 'medium' | 'high' | 'lossless';
  /** 音频文件，需要 capabilities.audio !== 'none' */
  audio?: { path: string; volumeDb?: number }[];
}

export interface RenderContext {
  /** 项目工作目录（容纳 cache / temp / output） */
  workDir: string;
  /** 进度回调（0-100）。可选 */
  onProgress?: (pct: number, stage: string) => void;
  /** 取消信号 */
  signal?: AbortSignal;
  /** dotenv-style 环境变量（adapter 透传给子进程） */
  env?: Record<string, string>;
}

export interface RenderOutput {
  outputPath: string;
  meta: {
    durationSec: number;
    fileSizeBytes: number;
    actualResolution: { width: number; height: number };
    fps: number;
    renderedFrames: number;
    renderWallClockSec: number;
    /** 实际用的 engine 版本（runtime 探测） */
    engineVersion: string;
  };
  /** stderr / log 摘要，调试用 */
  diagnostics: string[];
}

export interface ValidationResult {
  ok: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
}

export interface ValidationError {
  code: string;     // 例 'paradigm-mismatch' / 'unsupported-format' / 'missing-asset'
  message: string;
  /** 可选修复建议，agent 可以抓取直接 propose change */
  fix?: string;
}

export interface ValidationWarning extends ValidationError {}

export interface PreviewContext {
  workDir: string;
  hostname?: string;  // 默认 127.0.0.1
  port?: number;      // 默认 0 = 自动分配
}

export interface PreviewHandle {
  url: string;
  port: number;
  /** 关闭 preview server */
  close(): Promise<void>;
}

export interface NativeTemplateRef {
  /** engine-native id（不强制跟跨引擎 id 一样） */
  nativeId: string;
  /** engine-native 路径 */
  path: string;
  /** 自报描述，html-video 可借此构建 metadata */
  hints?: { name?: string; description?: string; bestFor?: string[] };
}
```

---

## 4 个 backend 的 capability 声明（示例）

### Hyperframes

```ts
{
  id: 'hyperframes',
  name: 'Hyperframes',
  upstreamVersion: '0.x',
  capabilities: {
    paradigms: ['html-css-gsap'],
    outputFormats: ['mp4', 'webm', 'webm-alpha', 'png-sequence'],
    maxResolution: { width: 3840, height: 2160 },
    alpha: true,
    audio: 'multi',
    subtitles: ['burn-in', 'sidecar'],
    renderTarget: ['local-chromium', 'lambda'],
    licensing: 'free-osi',
    renderSpeedHint: { resolution: '1080p', durationSec: 10, fps: 60, estimatedRenderSec: 18 },
    bestFor: ['social-shorts', 'product-marketing', 'logo-reveal', 'gsap-animations'],
    weaknesses: ['no-react-ecosystem', 'limited-3d-without-three.js']
  }
}
```

### Remotion

```ts
{
  id: 'remotion',
  name: 'Remotion',
  upstreamVersion: '4.x',
  capabilities: {
    paradigms: ['react-tsx'],
    outputFormats: ['mp4', 'webm', 'gif', 'png-sequence'],
    maxResolution: { width: 7680, height: 4320 },
    alpha: false,           // webm-alpha 支持但有 caveat，先不暴露
    audio: 'multi',
    subtitles: ['burn-in', 'sidecar'],
    renderTarget: ['local-chromium', 'lambda', 'cloud-run'],
    licensing: 'commercial-restricted',  // 4+ devs 付费
    renderSpeedHint: { resolution: '1080p', durationSec: 10, fps: 60, estimatedRenderSec: 14 },
    bestFor: ['react-team', 'lambda-scale', 'data-driven', 'long-form-narration'],
    weaknesses: ['license-cost-at-scale', 'react-only']
  }
}
```

### Motion Canvas

```ts
{
  id: 'motion-canvas',
  name: 'Motion Canvas',
  upstreamVersion: '3.x',
  capabilities: {
    paradigms: ['ts-generator'],
    outputFormats: ['mp4', 'png-sequence'],
    maxResolution: { width: 3840, height: 2160 },
    alpha: false,           // canvas-based 默认 opaque
    audio: 'single',
    subtitles: ['burn-in'],
    renderTarget: ['local-canvas'],   // 浏览器内或 Node canvas，不直接 lambda
    licensing: 'free-osi',
    renderSpeedHint: { resolution: '1080p', durationSec: 10, fps: 60, estimatedRenderSec: 22 },
    bestFor: ['explainer-videos', 'math-visualization', 'code-block-animation', 'latex'],
    weaknesses: ['no-html-css', 'single-author-style', 'no-server-render-natively']
  }
}
```

### Revideo

```ts
{
  id: 'revideo',
  name: 'Revideo',
  upstreamVersion: '0.4.x',
  capabilities: {
    paradigms: ['ts-generator'],
    outputFormats: ['mp4', 'webm'],
    maxResolution: { width: 3840, height: 2160 },
    alpha: false,
    audio: 'multi',
    subtitles: ['burn-in'],
    renderTarget: ['local-canvas', 'cloud-run'],
    licensing: 'free-osi',
    renderSpeedHint: { resolution: '1080p', durationSec: 10, fps: 60, estimatedRenderSec: 16 },
    bestFor: ['saas-pipelines', 'parameterized-batch-render', 'ts-team-without-react'],
    weaknesses: ['smaller-community', 'canvas-not-html']
  }
}
```

---

## render() 行为约定

### 1. 不可变性

`render()` 不修改用户 source（template `sourcePath`）。所有临时产物（middleframes / sprite / cache）写到 `ctx.workDir`。

### 2. 进程隔离

每次 `render()` 启动独立子进程跑实际 engine：

- HF: 起 puppeteer + ffmpeg
- Remotion: 起 `@remotion/renderer` 或 lambda invoke
- Motion Canvas: 起 vite dev server + browser，frame 抓取
- Revideo: 调 `renderVideo()` Node API

子进程崩溃 / 卡死，adapter 必须捕获并 reject promise，`outputPath` 文件不留半成品（成功后再 rename）。

### 3. 进度报告

- 全 engine 都按"当前帧/总帧数"算 0-100%
- 起步阶段（编译/打包/启动 chromium）报 stage `'preparing'` 0-10%
- 渲染阶段 stage `'rendering'` 10-95%
- mux/转码 stage `'muxing'` 95-100%

### 4. 取消

`ctx.signal.aborted` → adapter 必须 kill 子进程，cleanup workDir 临时文件，reject `AbortError`。

### 5. 错误码（统一）

| Code | 含义 | retryable |
|---|---|---|
| `engine-not-installed` | 用户没装 npm 包 / lambda 无凭证 | no |
| `template-invalid` | validate() 已 fail，仍调 render | no |
| `render-failed` | engine 子进程非 0 退出，diagnostics 含详情 | maybe |
| `render-timeout` | 超 ctx.timeout（默认 5min/分辨率比例） | maybe |
| `output-corrupt` | mux 完文件不可读 | yes |
| `disk-full` | workDir 写不下 | no |
| `cancelled` | signal aborted | no |

---

## validate() 行为约定

`validate(template)` 必须**只读**且**快**（< 50ms）。它做：

1. 读 template metadata（RFC-02），看 `engine` 字段是不是自己
2. 看 template 的 paradigm 在自己 `capabilities.paradigms` 里
3. 看 template 声明的 output format 在自己 `capabilities.outputFormats` 里
4. 看 template `sourcePath` 实际存在（不读内容）
5. 不要执行用户代码 / 不启 chromium

返回的 `errors` 让 agent 可读：

```ts
{
  code: 'paradigm-mismatch',
  message: 'Template uses react-tsx but motion-canvas adapter only supports ts-generator',
  fix: 'Switch engine to remotion or rendiv'
}
```

---

## preview() vs render()

`preview()` 启 dev server 让用户在浏览器里实时调试（HF studio / Remotion Studio / MC editor 都已有）；adapter 把 dev server URL 透出来即可。`preview()` **可选实现**（先 OS 跑 render 也能用）。

---

## Adapter 包结构（约定）

```
@html-video/adapter-hyperframes/
├── package.json          # peerDependency: hyperframes@^0.4.0
├── src/
│   ├── index.ts          # 导出 default: EngineAdapter 实例
│   ├── render.ts         # render() 实现
│   ├── validate.ts       # validate() 实现
│   ├── preview.ts        # preview() 实现
│   └── capabilities.ts   # 静态 capability 声明
└── README.md
```

`@html-video/core` 通过 `import('@html-video/adapter-hyperframes')` 动态加载，**不**直接依赖任何 backend。

---

## 反例：错误的抽象会长什么样

设计过程中拒绝过的几条路线（明确写下来防后续偏航）：

❌ **统一 DSL**：发明 html-video 自己的"video markup"，再编译到 4 个 backend。
→ 好处：用户只学一套；坏处：永远落后任意 backend 的新 feature，4 个 transpile 永远做不全 + 维护地狱。html-video **不是新 DSL**。

❌ **Frame-level 抽象**：把 backend 的 frame 输出统一成 PNG 序列再自己 mux。
→ 好处：可复用 ffmpeg pipeline；坏处：每个 backend 都已经有自己的 mux 优化（HF/Remotion 直接 ffmpeg pipe，MC canvas-encode 不出 PNG），强行打散反而慢一倍。

❌ **Sandbox / VM 隔离**：用 docker / vm 跑 backend。
→ 好处：环境干净；坏处：本地 dev / 离线场景慢 10x，违反"agent friendly"原则。子进程隔离够用。

---

## Open Questions（v0.2 待定）

1. **template variables 的 schema 校验**：放 core 还是 adapter？目前倾向 core 用 zod 统一校验（agent 可读 schema 推参数）。
2. **音频混音**：core 提供帮工具（ffmpeg 调）还是 adapter 各自处理？倾向 core helper，因为 ffmpeg 不该重复封装。
3. **字幕**：burn-in / sidecar 谁烧入？倾向 adapter——某些 engine 已原生支持。
4. **资产打包**：用户引用的图片 / 视频 / 字体怎么收集进 render context？倾向 core 提供 `AssetResolver`，adapter 收 resolved paths。
5. **跨 engine retry**：如果 HF 渲染挂，core 是否自动 fallback 到 Revideo？v0.1 不做（决策权给 agent，不偷偷换 engine）。
