# RFC-05：Project-centric 工作流（supersedes RFC-04 storyboard-first）

> **Status**: Draft v0.1 · **Supersedes** [RFC-04](./2026-05-26-spec-04-storyboard-workflow.md)
> **Date**: 2026-05-27
> **Scope**: 把"分镜/场景/时间线"的复杂模型整体移除，改成 HTML Anything-style 的"项目 + 单模板 + HTML 预览 + 导出 MP4"工作流

---

## 来源（用户原话）

> 它应该是跟 HTML anything 这个项目，产品的界面的结构是有点相似的——左边有一个项目的创建栏，创建一个项目之后呢，它可以在这个项目里面去输入或者上传文字、图片、视频等等的素材，然后可以根据他的这些素材，在右边的这个效果栏里面，它首先是可以选择一个 hyperframes 的模板，然后选完模板之后，就可以根据它的输入和上传的内容去生成一个 HTML 的预览的效果，然后他先在 HTML 的预览效果里面，先看整体的视频效果是怎么样的，然后确认之后再可以是导出一个视频。
>
> 你这里的分镜剪辑这些我觉得好像都是不用的，不用考虑剪辑，因为它本身就是 HTML 做的视频嘛，所以你只要给它能够预览到每个画面的效果就好了。

---

## 关键认知更新

之前 RFC-04 假设 html-video 要做"创作者级 storyboard 编辑器"——用 agent 把素材编排成多 scene 序列、加转场、人审、拼成 MP4。这是**借了电影制片的工作流**，但放在"HTML 模板内部已经全权决定动画序列"的语境下是**重复抽象**：

- HTML 模板本身就是一段完整视频的可视化逻辑（GSAP timeline 已经定义了视觉序列）
- 用户的真实诉求：选一个我喜欢的视觉风格 + 把我的素材塞进去 + 看效果 + 导出
- 多 scene 拼接 / 转场 / 时间线 = 二次剪辑工作流，对**用 HTML 做单段视频**这个场景是过度设计

→ 简化为：**Project = 素材 + 单模板 + 单视频**。

---

## 数据模型

```ts
// 新增
export interface Project {
  id: string;                          // proj_xxxxxx
  name: string;                        // 用户起的名字
  intent?: string;                     // 可选一句话描述
  assets: Asset[];                     // 素材（沿用 RFC-04 的 Asset 类型）
  templateId: string | null;           // 当前选中的模板 id；未选则 null
  variables: Record<string, unknown>;  // 用户填的 / 表单填的变量（template inputs schema 兼容）
  preferences: UserPreferences;        // 沿用：aspect / duration / fps / commercial
  status: ProjectStatus;               // 'draft' | 'previewed' | 'rendered'
  lastPreviewHtmlPath?: string;        // 最近一次 renderToHtml 的输出
  lastOutputMp4Path?: string;          // 最近一次 export 的 MP4 路径
  createdAt: string;
  updatedAt: string;
}

export type ProjectStatus = 'draft' | 'previewed' | 'rendered';
```

**删除**（不再使用）：
- `Storyboard`
- `Scene`
- `StoryboardOrchestrator`
- `SceneSuggestion`
- `TransitionId` / `AudioTrack`（audio 在 v0.2 重新考虑放 project level）
- `planScenes()` 启发式 planner（用户主动选模板，不需要 agent 自动拼接）

---

## 文件存储

```
project-root/
└── .html-video/
    ├── projects/
    │   └── <project_id>/
    │       ├── project.json           # Project metadata
    │       ├── assets/                # 内容寻址（沿用 RFC-04 的 AssetStore 行为）
    │       │   ├── <sha1>.png
    │       │   └── <sha1>.json
    │       ├── preview.html           # 最近一次 HTML 预览
    │       ├── preview-poster.svg
    │       └── output.mp4             # 最终导出
```

把之前的 `.html-video/bundles/` + `.html-video/storyboards/` 合并成 `.html-video/projects/`。每个 project 自包含。

---

## 工作流（端到端）

```
1. 用户点 "+ 新建项目" → 输入 name → 创建空 Project (status=draft, templateId=null)
2. 用户在素材区上传：
   - 拖拽图片 / 视频文件
   - 粘贴文字
   - 粘贴 JSON 数据
   → AssetStore 内容寻址入库，加入 project.assets[]
3. 用户在右侧选模板（下拉 / grid）：
   - 切换 templateId
   - 系统读 template inputs schema → 自动渲染表单
   - 已有变量值若 key 名匹配则保留（比如 title 模板间通用），其余清空
4. 用户在表单里改值（实时持久化到 project.variables）
   - 字段绑定素材（image_path 字段下拉选 project.assets 里的 image type 资产）
   - 文本字段直接打字
   - 数据 array 字段允许从 data type 资产载入或手填
5. 实时 HTML 预览（右侧 iframe，每次 vars 变更就 reload）
   - status 改 'previewed' 一次（首次预览成功）
6. 用户点 "导出 MP4"：
   - status 改 'rendered'
   - 调 EngineAdapter.render() → MP4 写到 project 目录 + 给用户下载
```

**关键约定**：
- **预览即效果** —— HTML iframe 里看到的就是最终视频效果，没有"分镜阶段 vs 完成阶段"的区分。MP4 export 只是把 HTML 录成视频。
- **没有 approval gate** —— RFC-04 那个 `approved` 中间状态删除。预览满意直接 export。
- **没有跨模板拼接** —— 想要更复杂的多段视频？建多个 project，最终用户自己用其他工具拼（v0.3 可能加 "compose projects" 功能，v0.1 不做）。

---

## CLI（新命令集）

```bash
# 项目管理
html-video project create --name "OD plugins demo" [--intent "..."] [--aspect 16:9]
html-video project list
html-video project show <projectId>
html-video project delete <projectId>

# 素材管理（在某个 project 上下文中）
html-video project add-asset <projectId> --file <path>
html-video project add-asset <projectId> --inline-text "..."
html-video project add-asset <projectId> --inline-data-file <path>
html-video project remove-asset <projectId> --asset <assetId>

# 模板与变量
html-video project set-template <projectId> --template <templateId>
html-video project set-vars <projectId> --vars-file vars.json
html-video project set-var <projectId> --key <key> --value <json>

# 渲染
html-video project preview <projectId>           # 启 HTTP server 给 iframe 看
html-video project render <projectId> --output out.mp4

# 全 studio（最高频用法 = 一个命令打开 IDE-style 三栏 UI）
html-video studio [--port 3071]                  # 起 project studio，浏览器打开
```

**保留命令**（不变）：
- `html-video doctor`
- `html-video list-engines`
- `html-video search-templates`
- `html-video inspect-template <id>`

**删除命令**：
- `upload`（合并到 `project add-asset`）
- `sb-generate / sb-edit / sb-preview / sb-render`（整个 storyboard 子树）

---

## UI（项目 Studio，HTML Anything-style 三栏）

```
┌────────────┬──────────────────────────────────────────────────────────┐
│  PROJECTS  │  ASSETS                          │  TEMPLATE & PREVIEW    │
│ ─────────  │ ─────────────────────────────── │ ───────────────────── │
│  + New     │  📷 [image] od-logo.png          │ ▼ [data-bar-chart]   │
│            │  📝 [text] "Design that ..."     │                       │
│  ▶ proj 1  │  📊 [data] plugin-stats.json     │ ┌──── form ──────┐   │
│    proj 2  │                                  │ │ Title:         │   │
│    proj 3  │  [ + Drop or paste assets ]      │ │ ▢ "OD Plugins" │   │
│            │                                  │ │                │   │
│            │                                  │ │ Subtitle:      │   │
│            │                                  │ │ ▢ ""           │   │
│            │                                  │ │                │   │
│            │                                  │ │ Data: 4 rows   │   │
│            │                                  │ │ ▾ from asset:  │   │
│            │                                  │ │   [📊 plug...] │   │
│            │                                  │ └────────────────┘   │
│            │                                  │                       │
│            │                                  │ ┌─── iframe ────┐    │
│            │                                  │ │  HTML preview  │    │
│            │                                  │ │  (live re-     │    │
│            │                                  │ │   render on    │    │
│            │                                  │ │   var change)  │    │
│            │                                  │ └────────────────┘    │
│            │                                  │                       │
│            │                                  │  [📥 Export MP4]      │
└────────────┴──────────────────────────────────────────────────────────┘
```

**关键交互细节**：

1. **左侧 PROJECTS**
   - 列表 + "New project" 按钮
   - 选中态高亮
   - 项目缩略图（最近一次 preview poster），无则用文字 placeholder

2. **中间 ASSETS**
   - 拖拽 / 粘贴 / 点击上传按钮
   - 每个资产一行：icon + 文件名 + size + 删除按钮
   - 资产支持点击预览（图片小弹窗、文字 hover 显示前 200 字）

3. **右侧 TEMPLATE & PREVIEW**
   - 顶部：模板选择下拉（带搜索 / 缩略图）
   - 切模板时：弹一个 toast "保留了 N 个共名变量，新模板还需要补 M 个字段"
   - 中部：**按 inputs schema 自动渲染表单**：
     - `type: string` → `<input type="text">`
     - `type: number` → `<input type="number" min/max>`
     - `type: string + enum` → `<select>`
     - `type: array of {label,value}` → 简易 table 编辑器（增/删行）
     - `type: string + filename pattern image_path` → asset picker dropdown filtering project.assets[type=image]
     - 默认值从 schema `default` 取
     - 必填字段标 `*`
   - 底部：iframe 实时预览
   - "Export MP4" 按钮：disabled 直到 templateId 有 + 必填字段全填

4. **变量持久化**：表单字段每次 blur 自动 save 到 project.json（debounce 300ms）。

---

## 表单自动渲染规则（关键技术点）

变量编辑表单是从 template `inputs.schema` 自动生成的（运行时反射）。规则：

| schema feature | UI |
|---|---|
| `type: string` | text input |
| `type: string` + `enum` | select dropdown |
| `type: string` + `format: date` | date picker |
| `type: string` + key contains `_path` | **asset picker** —— 只列 project.assets 里 type 匹配的（image_path → image 资产） |
| `type: string` + `maxLength` | textarea if > 100 else input |
| `type: number` | number input with `min/max` |
| `type: boolean` | toggle |
| `type: array` of primitives | tag-input |
| `type: array` of objects | inline table（每个 item 一行，按 item schema 展开） |
| `type: object` | nested fieldset |
| `default` | pre-filled |
| `required` | red asterisk |
| `description` | hover tooltip |

asset picker 的过滤启发式（v0.1）：

- `image_path` / `logo_path` / `*_image` → image
- `audio_path` / `bgm_path` → audio
- `video_path` → video
- `data` / `*_data` → data
- 其他 → 不绑定，用户手填字符串

v0.2 加 schema custom annotation `x-asset-type`（更精确）。

---

## EngineAdapter 接口影响

无变化。`render()` 和 `renderToHtml()` 接口都保留（RFC-01 v0.2 增量）：

- 项目预览 = `EngineAdapter.renderToHtml({ template, variables, config }, ctx)`
- 项目导出 = `EngineAdapter.render({ template, variables, config }, ctx)`

简化点：input 不再有 `Scene` 概念，直接是 Project 的 `templateId + variables`。

---

## TemplateRegistry / TemplateMetadata 影响

无变化（RFC-02）。只是说明 `inputs.schema` 现在被 UI 自动渲染表单消费——之前 RFC-02 已经定义了 schema 是 JSON Schema 兼容，UI 渲染器只是它的 consumer 之一（agent 也是 consumer，跟 RFC-03 一致）。

唯一新增：**强烈建议**作者在 schema 字段上加 `description`（现在用作 form tooltip）和 `default`（用作 form 初值）。已有 5 个 reference templates 都满足。

---

## v0.1 MVP 范围（修订）

✅ 重构：
- 删 storyboard 整套
- core 加 Project / ProjectStore / ProjectOrchestrator (render preview / export)
- cli 改 project 命令族
- UI 改三栏 studio（form 自动渲染）

✅ 不变：
- EngineAdapter 抽象 + adapter-hyperframes（保留 stub render，v0.2 接真 HF）
- TemplateRegistry + 5 reference templates
- AssetStore 内容寻址
- doctor / list-engines / search-templates / inspect-template

❌ 不进 MVP：
- 多项目拼接
- agent 自动选模板（用户主动选）
- 富文本素材编辑
- 模板预览 grid（v0.2 做缩略图 + tag filter）
- 协作 / 多人审稿

---

## 给 Joey 的话

承认我的设计偏了——把"创作者用 HTML 做单段视频"理解成了"剧情片导演用 storyboard 拼镜头"。新版回归 HTML Anything 的极简心智，**项目 = 素材 + 模板 + 视频，仅此而已**。

下一次 commit 会做完整重构（删 storyboard 全树，加 project + 三栏 studio + 表单自动渲染），跑完 smoke 重启 preview server 给你看。

---

## Open Questions（v0.2 待定）

1. **变量与素材绑定的精确度** —— `image_path` 启发式可能误判，是否引入 `x-asset-type` 扩展？
2. **多素材同字段** —— 如果模板要 1 个 image_path，但用户有 N 张图，建议开 N 个项目？还是模板支持 multi-image 的 v2？
3. **预览实时性** —— 字段 blur debounce 300ms 够吗？还是需要 explicit "Refresh preview" 按钮（避免大模板每键入一次都重 render）？
4. **历史版本** —— 项目要不要支持 "undo / 历史快照"？v0.1 不做，更新即覆盖
5. **导出选项** —— 导出 MP4 时让用户选分辨率 / fps / 时长？还是按模板默认值？
