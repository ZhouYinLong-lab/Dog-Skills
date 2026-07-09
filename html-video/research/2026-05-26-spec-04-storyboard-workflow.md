# RFC-04：Storyboard-first 工作流（产品形态修订）

> **Status**: Draft v0.1 · **Supersedes部分前 3 份 RFC 假设**
> **Date**: 2026-05-26 (after Joey clarification mid-session)
> **Scope**: 修订 html-video 的核心用户工作流，从"agent 填 vars 一步 render"改为"资产 → HTML 分镜 → 用户审 → MP4"两段式

---

## 关键澄清（来自 Joey）

> 产品内支持上传各种图文资产，整合起来，生成 HTML 的分镜，用户可以先看分镜，确认分镜效果，之后再导出为 MP4。

这条话改变了 html-video 三层关键定位：

| 维度 | 前 3 份 RFC 假设 | 修订后 |
|---|---|---|
| **入口** | 用户已有 template id + 结构化 vars | 用户上传**散落资产**（图片 / 文字 / 数据） |
| **中间产物** | 无（直接 render MP4） | **HTML Storyboard**（多个 HTML 分镜，可在浏览器审） |
| **审批 gate** | 无 | Storyboard 阶段，用户必须确认才能 render MP4 |
| **创作姿态** | 工程师 fill schema | 创作者上传素材 + agent 编排 |
| **跟 HF / Remotion 差异** | meta-aggregator + 模板池 | **+ asset-to-storyboard 创作链路**（HF/Remotion 都没有） |

**这是 html-video 真正的护城河**：HF / Remotion / Motion Canvas 都假定用户已经知道想做什么；html-video 假定用户**只有素材 + 一句话意图**。

---

## 修订后的核心数据流

```
┌─────────────────────────────────────────────────────────────────┐
│  Stage 1：资产上传                                                │
│    用户:  图片 N 张 + 文字段落 + 数据表 + 音频(可选) + 一句话意图 │
│    输出:  AssetBundle (项目目录下结构化存放)                       │
└──────────────────────────────┬──────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 2：分镜生成（agent 主导）                                  │
│    agent:  根据意图 + 资产 → 选 templates → 编排 scenes           │
│    输出:  Storyboard（一组 HTML 分镜 + scene metadata）           │
└──────────────────────────────┬──────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 3：分镜审核（用户主导）                                    │
│    用户:  浏览器里逐 scene 看，文字/图片/顺序/时长可改             │
│    工具:  html-video preview-storyboard 启 dev server             │
│    操作:  inline 编辑 / 替换图 / 删 scene / 调时长 / 调顺序       │
└──────────────────────────────┬──────────────────────────────────┘
                               ↓ 确认
┌─────────────────────────────────────────────────────────────────┐
│  Stage 4：MP4 导出                                                │
│    输入:  确认后的 Storyboard                                      │
│    操作:  对每个 scene 调对应 EngineAdapter.render()               │
│    后处理: 跨 scene 拼接（ffmpeg concat）+ 整体音轨 mux            │
│    输出:  最终 MP4                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 新核心概念

### Asset

用户上传的原始物料。**不**经 agent 解读就先入库。

```ts
// core/types.ts (additions)

export interface Asset {
  id: string;                    // sha1(content)，content-addressed
  type: 'image' | 'text' | 'data' | 'audio' | 'video' | 'reference-link';
  path?: string;                 // 本地文件路径（image/audio/video）
  content?: string;              // text / data 内联（小文件）
  metadata: {
    filename?: string;
    mimeType?: string;
    sizeBytes?: number;
    width?: number;              // image/video
    height?: number;
    durationSec?: number;        // audio/video
    /** Joey 给的 caption / 用户标注 */
    userCaption?: string;
  };
  /** 用户上传时的意图标签（自由文本） */
  userTags: string[];
}

export interface AssetBundle {
  /** Bundle 唯一 id，对应 project workDir 子目录 */
  id: string;
  /** 用户的一句话意图（"做个 25 天涨 5 万的曲线视频"） */
  intent: string;
  /** 用户偏好（aspect / duration target / mood / 商用否） */
  preferences: UserPreferences;
  /** 全部资产 */
  assets: Asset[];
  /** 上传时间 */
  createdAt: string;
}

export interface UserPreferences {
  aspect?: '16:9' | '9:16' | '1:1' | string;
  durationTargetSec?: number;
  format?: 'mp4' | 'webm';
  resolution?: { width: number; height: number };
  fps?: number;
  mood?: string;                 // 自由文本：'energetic' / 'calm' / 'corporate' / 'playful'
  brandColors?: string[];
  fontFamilies?: string[];
  language?: string;             // 'zh-CN' / 'en-US'
  commercial?: boolean;
}
```

### Storyboard / Scene

分镜是**多个 scene 拼接**而成的"半成品 HTML 序列"，每个 scene 是 RFC-01/02 的 template 渲染产物（HTML 形态而非 MP4）。

```ts
export interface Storyboard {
  id: string;
  bundleId: string;              // 来自哪个 AssetBundle
  intent: string;                // 复制 bundle.intent 备查
  scenes: Scene[];
  /** 跨 scene 全局音轨（背景乐 / 旁白） */
  globalAudio?: AudioTrack[];
  /** 全局 transitions 偏好 */
  defaultTransition?: TransitionId;
  /** 总预计时长（所有 scene durationSec 之和） */
  estimatedDurationSec: number;
  /** 状态机 */
  status: 'draft' | 'ready-for-review' | 'approved' | 'rendered';
  createdAt: string;
  updatedAt: string;
}

export interface Scene {
  id: string;
  /** 这个 scene 用哪个 template + 哪个 engine（RFC-02） */
  template: { id: string; engine: EngineId };
  /** 填好的 inputs（RFC-02 inputs.schema 兼容） */
  variables: Record<string, unknown>;
  /** 用了哪些 asset (id 引用) */
  assetRefs: string[];
  /** 在 storyboard 时间线上的位置（秒） */
  startSec: number;
  /** 时长（秒） */
  durationSec: number;
  /** 跟下一个 scene 之间的过渡 */
  transitionToNext?: TransitionId;
  /** Agent 给这个 scene 的解释（用户审稿时看得到） */
  agentNote: string;
  /** scene-level 静态预览 */
  previewHtmlPath: string;       // 渲染好的 HTML 文件
  previewPosterPath?: string;    // 截图
}

export interface AudioTrack {
  assetId: string;               // 指向 AssetBundle.assets 中的 audio asset
  startSec: number;              // 在最终视频中的开始时刻
  fadeInSec?: number;
  fadeOutSec?: number;
  volumeDb?: number;
}

export type TransitionId = 'cut' | 'fade' | 'slide-left' | 'slide-right' | 'zoom' | string;
```

---

## 修订 EngineAdapter 接口（RFC-01 增量）

每个 adapter 需要新增一个能力：**把单 scene 渲染成 HTML 而不是 MP4**。这是 storyboard 阶段的快速预览。

```ts
// 增量加到 RFC-01 的 EngineAdapter interface

export interface EngineAdapter {
  // ... 之前的 id / capabilities / validate / render / preview ...

  /** 新增：渲染单 scene 到 HTML（不是 MP4），用于 storyboard 阶段 */
  renderToHtml?(input: RenderInput, ctx: RenderContext): Promise<HtmlSceneOutput>;
}

export interface HtmlSceneOutput {
  /** 主 HTML 文件路径 */
  htmlPath: string;
  /** 引用的资产（agent 可以用这些做 "替换图片" 操作） */
  referencedAssets: { assetId: string; usagePath: string }[];
  /** 单帧静态截图（用作 storyboard grid 缩略） */
  posterPath: string;
  /** 这个 scene 在浏览器里的预估时长（用户调整能改） */
  durationSec: number;
}
```

**fallback**：如果 adapter 没实现 `renderToHtml`，core 提供 default 实现——直接 render MP4 然后 ffmpeg 抽 1 帧 + 包一个 video tag 的 HTML。这条路径慢但能用，鼓励 adapter 自己优化（HF / Remotion 都能直接出 HTML 不出 MP4）。

---

## 修订 CLI Contract（RFC-03 增量）

### 新增命令

```bash
# 1. 上传资产，建 bundle
html-video assets upload \
  --intent "做个 25 天涨 5 万的曲线视频" \
  --aspect 16:9 \
  --commercial true \
  --files "assets/*.png" \
  --files "data/stars.csv" \
  --json
# → 输出 bundle_id

# 2. agent 主导生成 storyboard
html-video storyboard generate \
  --bundle <bundle_id> \
  --json
# → 输出 storyboard_id + scenes 列表

# 3. 修改 storyboard（agent 受用户指令调用）
html-video storyboard edit <storyboard_id> \
  --op add-scene --template <id> --vars-file scene-vars.json --at 30
html-video storyboard edit <storyboard_id> \
  --op remove-scene --scene <scene_id>
html-video storyboard edit <storyboard_id> \
  --op reorder --scenes <id1>,<id2>,<id3>
html-video storyboard edit <storyboard_id> \
  --op set-duration --scene <scene_id> --duration-sec 8
html-video storyboard edit <storyboard_id> \
  --op replace-asset --scene <scene_id> --old-asset <id> --new-asset <id>

# 4. 启 storyboard 浏览器预览（不是单 scene preview，是整个 timeline）
html-video storyboard preview <storyboard_id> --json
# → 输出 url（页面里有 timeline + 每 scene 内嵌 iframe + 编辑控件）

# 5. 用户确认 → render 全片
html-video storyboard render <storyboard_id> \
  --output ~/Desktop/final.mp4 \
  --stream-progress --json
```

### 修订原来的 `render` 命令

`html-video render --template ... --vars-file ...` 仍保留，但定位改为 **"开发者直跑单模板"**（template 测试 / CI 用）。**用户主流程不该走这个**——agent 应该用 `storyboard generate / edit / render` 三件套。

---

## 修订 SKILL.md 工作流（RFC-03 增量）

新版 SKILL.md 的"Standard workflow"段落：

```markdown
## Standard workflow

### 1. Initial check
`html-video doctor --json` → 处理依赖缺失

### 2. Collect assets + intent
- If user already has files: `html-video assets upload --files ... --intent ...`
- If user gives a vague intent: ask **one batched question**: aspect / mood / duration target / commercial usage
- Always extract intent into one sentence to feed into the bundle

### 3. Generate storyboard
`html-video storyboard generate --bundle <id>`

The CLI internally:
- Searches templates per scene need (intro / data viz / CTA / outro etc)
- Selects engines based on RFC-01 capabilities + license filter
- Fills inputs using user's assets
- Returns scene list with agent_note for each

### 4. Show user the storyboard
Open `html-video storyboard preview <id>` URL in browser. Tell user:
- Estimated total duration
- Number of scenes + 1-line agent_note per scene
- "Click each scene to view, edit text inline, or tell me what to change"

### 5. Iterate on storyboard (multi-turn)
User: "把第二个 scene 里的图换成 logo.png"
→ `html-video storyboard edit <id> --op replace-asset --scene <scene_id> --new-asset <asset_id>`

User: "缩短到 30 秒以内"
→ Calculate which scenes to trim, run multiple edit commands

User: "我觉得 OK 了"
→ Move to step 6.

### 6. Final render to MP4
`html-video storyboard render <id> --output <path> --stream-progress`

Surface progress every 25%. On done, paste output path + open in default player.

### Anti-patterns
- ❌ Don't render MP4 before user approves storyboard
- ❌ Don't skip the storyboard preview link — even if user says "你看着办"
- ❌ Don't quietly add scenes the user didn't mention — propose first, edit after confirm
- ❌ Don't render same storyboard twice without explicit user request (it's slow)
```

---

## Storyboard 文件存储约定

```
project-root/
└── .html-video/
    ├── bundles/
    │   └── <bundle_id>/
    │       ├── bundle.json             # AssetBundle metadata
    │       └── assets/
    │           ├── <asset_id>.png      # 内容寻址
    │           ├── <asset_id>.csv
    │           └── <asset_id>.txt
    ├── storyboards/
    │   └── <storyboard_id>/
    │       ├── storyboard.json         # Storyboard metadata
    │       └── scenes/
    │           ├── <scene_id>/
    │           │   ├── scene.json
    │           │   ├── preview.html
    │           │   ├── poster.png
    │           │   └── source/         # adapter-rendered intermediates
    └── outputs/
        └── <storyboard_id>-<timestamp>.mp4
```

`.html-video/` 放在用户项目根，跟 `.git/` 平级。`.gitignore` 默认 ignore（避免大文件入 git）。

---

## 跟 RFC-01/02/03 的关系（明确）

| 修订项 | RFC-01 | RFC-02 | RFC-03 |
|---|---|---|---|
| EngineAdapter 加 `renderToHtml` | ✅ 修订（增量） | — | — |
| Template metadata 加 `scene_role`（intro / data / cta / outro） | — | ✅ 修订（v0.2 加） | — |
| Template metadata 加 `assets_consumed`（声明吃哪类 asset） | — | ✅ 修订（v0.2 加） | — |
| CLI 加 `assets upload` / `storyboard generate / edit / preview / render` | — | — | ✅ 修订 |
| SKILL.md 的工作流改成 storyboard-first | — | — | ✅ 修订 |
| `html-video render --template ...` 降格为 dev-mode 命令 | — | — | ✅ 修订 |

后续会话写代码时按这份 RFC-04 的优先级实现。

---

## v0.1 MVP 范围（修订后）

按"两段式工作流"重排优先级：

- ✅ `@html-video/core`：Asset / AssetBundle / Storyboard / Scene 数据结构 + sqlite 存储 + content-addressed asset store
- ✅ `@html-video/adapter-hyperframes`：实现 `renderToHtml` + `render`
- ✅ `@html-video/cli`：`doctor` / `assets upload` / `storyboard generate` / `storyboard preview` / `storyboard render`
- ✅ `@html-video/storyboard-ui`：浏览器里的 storyboard preview 页面（**新增**，原 RFC-03 没考虑）
  - timeline 视图
  - scene grid + 内嵌 iframe
  - inline edit 文字 / 替换图 / 调时长 / 删 / 重排
  - 全屏播放 mock（每个 scene HTML loop 起来串）
- ✅ 5 个 reference templates（覆盖 intro / data-chart / image-pan / text-card / outro 五种 scene role）
- ✅ Claude Code SKILL.md（按 storyboard-first 工作流）

**不**进 MVP（推到 v0.2+）：
- ❌ adapter-remotion / motion-canvas / revideo（先把 HF 路径 + storyboard 闭环跑通）
- ❌ AI 智能编排（v0.1 agent 是 LLM 即兴选 template，v0.2 加规则 + ML 优化）
- ❌ 协作（多人审稿）
- ❌ 云端 storyboard 持久化（先纯本地）

---

## 给 Joey 的话

这条澄清把 html-video 从"meta-aggregator + agent CLI" 升级成 **"asset-to-video 创作流水线"**——后者是真正有差异化的产品形态，HF / Remotion 都没做这件事，因为他们假设用户是开发者。**新护城河 = 资产理解 + storyboard 编排 + 跨引擎渲染**，三层一起才是 html-video。

下一步如果你点头，我会按修订后的 v0.1 MVP 范围动手写代码骨架（core 数据结构 + adapter-hyperframes + CLI 几个命令 + storyboard-ui 草稿）。

---

## Open Questions（v0.2 待定）

1. **资产理解** —— agent 拿到一堆图，怎么知道哪张是 logo / 产品 / 人物头像？v0.1 用 mime + 文件名启发；v0.2 接 vision model
2. **AI 写文案** —— 用户没给文字只给图，agent 是否自动生成 caption？v0.1 提示用户补；v0.2 LLM 生成
3. **音频自动选** —— 用户没传 BGM，是否从 license-free 库自动选？v0.1 不做；v0.2 接 Pixabay / FreePD API
4. **数据自动可视化** —— 用户上传 CSV，agent 直接选 chart 类型？v0.1 让用户选；v0.2 用 grammar-of-graphics 启发
5. **Storyboard 模板**（meta-template） —— 不只是单 scene，整片节奏（"先 intro 再 3 个 data 最后 cta"）也能模板化？v0.2 加 `storyboard-template` 概念
