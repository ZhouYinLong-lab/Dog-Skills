# RFC-02：Template Metadata 格式

> **Status**: Draft v0.1
> **Date**: 2026-05-26
> **Depends on**: [RFC-01](./2026-05-26-spec-01-engine-adapter.md)
> **Scope**: 跨 engine 的 template 描述。让 agent 可以基于 intent 检索、选 engine、填变量、render。

---

## 设计目标

1. **Engine-agnostic 描述 + engine-specific 入口** —— metadata 跨引擎统一，但每个 template 物理上属于某个 engine
2. **Agent 可读检索** —— `category` `tags` `bestFor` 让 agent 用 intent → template 匹配
3. **Inputs 强类型** —— 用 JSON Schema，agent 可以 introspect 该填啥
4. **License 可追溯** —— 不让用户被未知 license 模板 surprise（CC-BY-NC 的素材不能商用等）
5. **预览资产指引** —— 静态预览图 / 视频示例位置统一，前端 / studio / agent 都能 render template card

---

## 文件位置

每个 template 是一个目录，metadata 文件名固定 `template.html-video.yaml`：

```
templates/
└── data-bar-chart-race/
    ├── template.html-video.yaml   # 本 RFC 定义的 metadata
    ├── source/                    # engine-native 源代码（HF: index.html / Remotion: src/Composition.tsx / MC: src/scenes/)
    ├── preview.png                # 静态预览图（必备）
    ├── preview.mp4                # 短预览视频（可选，<3MB）
    └── README.md                  # 人类可读说明（可选）
```

---

## 完整 schema（YAML 形态，给作者用）

```yaml
# template.html-video.yaml
spec_version: 1                     # RFC 版本号，将来 breaking change 用

# === 标识 ===
id: data-bar-chart-race             # kebab-case，全局唯一（namespace 同 npm scope，例 @html-video/template-XXX 内部就用 XXX）
name: Bar Chart Race                # 人类可读
description: >
  Animate ranking changes over time. Bars race left-to-right, length scales
  with value, color stays consistent per entity.

# === 引擎归属（必填）===
engine: motion-canvas               # 物理上写在哪个 engine 里。一个 template = 一个 engine
engine_version: ^3.0.0              # peerDep semver
source_entry: source/scene.tsx      # 相对本目录，engine-specific entry point

# === 跨 engine 检索元数据 ===
category: data-viz                  # 一级分类（见下方枚举）
subcategory: chart-animation        # 自由
tags:                               # 自由文本，agent 用 fuzzy match
  - chart
  - race
  - ranking
  - data-driven

best_for:                           # 短句意图描述，跟 EngineAdapter.bestFor 同思路
  - "Compare entity rankings over time"
  - "Sales / GitHub stars / user growth race"
  - "Data journalism style social shorts"

not_for:                            # 反向标记，避免 agent 错配
  - "Static infographics (use html-anything instead)"
  - "Talking-head explainer (use motion-canvas free-form)"

# === 输出能力（adapter capabilities 的子集 / 期望值）===
output:
  formats: [mp4, webm]
  default_format: mp4
  resolution:
    default: { width: 1920, height: 1080 }
    supported_aspects: ["16:9", "1:1", "9:16"]
  fps:
    default: 60
    supported: [30, 60]
  duration:
    type: variable                  # variable = 跟 inputs 走；fixed = 模板固定时长
    min_sec: 5
    max_sec: 60
  alpha: false
  audio:
    supported: true
    expected_inputs: [bgm]          # 模板内部 reference 的 audio key

# === 用户输入（最关键的部分）===
inputs:
  schema:                           # JSON Schema Draft 2020-12
    type: object
    required: [data, title]
    properties:
      data:
        type: array
        description: Time series of rankings
        items:
          type: object
          required: [date, entities]
          properties:
            date:
              type: string
              format: date
              description: ISO date string
            entities:
              type: array
              items:
                type: object
                required: [name, value]
                properties:
                  name: { type: string, description: Entity label }
                  value: { type: number, description: Ranking value (higher = better) }
                  color: { type: string, description: Hex color, optional }
        minItems: 2
      title:
        type: string
        maxLength: 80
      subtitle:
        type: string
        maxLength: 160
      duration_per_step_sec:
        type: number
        minimum: 0.5
        maximum: 5
        default: 1.5
      bgm_path:
        type: string
        description: Optional background music file path

  examples:                         # 至少 1 条，agent 用作 fewshot
    - data:
        - date: "2024-01-01"
          entities:
            - { name: "Open Design", value: 100 }
            - { name: "Hyperframes", value: 4500 }
        - date: "2025-01-01"
          entities:
            - { name: "Open Design", value: 8000 }
            - { name: "Hyperframes", value: 18000 }
        - date: "2026-05-01"
          entities:
            - { name: "Open Design", value: 50000 }
            - { name: "Hyperframes", value: 21000 }
      title: "GitHub Stars Race · 2024-2026"

# === License & Attribution ===
license:
  spdx: Apache-2.0                  # SPDX id
  attribution_required: false
  redistribution_allowed: true
  commercial_use: true
  notes: ~                          # 可选自由文本

# 模板里用到的第三方素材（字体 / 图标 / sample video / sample audio）
assets_attribution:
  - name: "Inter font"
    license: SIL-OFL-1.1
    url: https://fonts.google.com/specimen/Inter
  - name: "sample-bgm.mp3"
    license: CC-BY-4.0
    author: Joe Doe
    url: https://...

# === 作者 / 维护 ===
author:
  name: nexu-io
  url: https://github.com/nexu-io
  contact: open-design@nexu.io
maintainers:
  - github: joeylee12629-star
contributing:
  url: https://github.com/nexu-io/html-video/blob/main/CONTRIBUTING.md

# === 版本历史 ===
version: 0.1.0                      # 模板 semver，独立于 spec_version 和 engine_version
changelog:
  - { version: 0.1.0, date: 2026-05-26, notes: Initial release }

# === 预览（前端 / studio / agent 用）===
preview:
  poster: preview.png               # 必备
  loop: preview.mp4                 # 可选，3 MB cap
  thumbnail: preview-thumb.webp     # 可选，前端 grid 用，<100KB

# === 渲染参考（让 agent 评估代价）===
performance:
  reference_render:                 # 1080p / 60fps / 10s 视频在标准硬件的渲染时间，作者填
    duration_sec: 10
    render_wall_clock_sec: 22
    machine: "M2 MacBook Air"

# === 标签：social-share quick links（generate share-ready 缩略）===
share_optimized_for:
  - twitter-card
  - xiaohongshu-9-16
```

---

## 一级分类（受控枚举）

`category` 字段必须从下表选一项。新增需 PR + RFC。

| Category | 说明 | 典型 engines |
|---|---|---|
| `data-viz` | 数据可视化（chart race / line / bar / map / network） | MC, Revideo, HF |
| `social-shorts` | 短视频（Twitter / TikTok / 小红书 9:16） | HF, Remotion, Revideo |
| `product-demo` | 产品 demo / SaaS landing video / launch | HF, Remotion |
| `explainer` | 教程 / 知识 / 对话 / 数学 | MC, Revideo |
| `marketing` | 营销 / 广告 / 倒计时 / promo | HF, Remotion |
| `intro-outro` | logo reveal / intro / outro / branding bumper | HF, Revideo |
| `ambient` | 循环背景 / loop / VJ / live-art | HF, Revideo |
| `documentary` | 长篇叙事 / b-roll + 字幕 | Remotion |
| `presentation` | slides 风（参照 Prezi 动效） | HF, Remotion |
| `transition` | 单场转场组件（不独立成片） | HF, Revideo |

---

## JSON Schema 形态（给程序用）

YAML 是给作者写的。`@html-video/core` 启动时会编译成 JSON 形态供 agent / studio / CI 用，并用 [Ajv](https://ajv.js.org/) 强校验。

```ts
// core/template-schema.ts
import { JSONSchemaType } from 'ajv';

export interface TemplateMetadata {
  spec_version: 1;
  id: string;
  name: string;
  description: string;
  engine: string;
  engine_version: string;
  source_entry: string;
  category: TemplateCategory;
  subcategory?: string;
  tags: string[];
  best_for: string[];
  not_for?: string[];
  output: OutputCapabilities;
  inputs: { schema: object; examples: object[] };
  license: LicenseInfo;
  assets_attribution?: AssetAttribution[];
  author: { name: string; url?: string; contact?: string };
  maintainers?: { github: string }[];
  contributing?: { url: string };
  version: string;
  changelog?: ChangelogEntry[];
  preview: { poster: string; loop?: string; thumbnail?: string };
  performance?: { reference_render: PerformanceRef };
  share_optimized_for?: string[];
}
```

---

## Agent 检索 / 选 engine 流程（说明性）

```
用户意图 → agent 调 html-video 的 search/match
         ↓
     [Stage 1] tag/category fuzzy match
         ↓ 候选 N 个 template
     [Stage 2] 看每个 template.engine 在用户机器上 adapter 是否安装可用
         ↓ 过滤掉不可用的
     [Stage 3] 按 license tier × renderSpeedHint × bestFor 排 top 3
         ↓
     agent 把 top 3 + preview poster URL 给用户选
         ↓ 用户确认
     [Stage 4] 用 inputs.schema introspect 缺哪些参数
         ↓ agent 跟用户对话补齐
     [Stage 5] 调 EngineAdapter.render()
```

---

## License 列举（agent 决策用）

`license.spdx` 是必填的 [SPDX identifier](https://spdx.org/licenses/)。Agent 在以下场景必查：

- 用户标记"商用" → 过滤掉非 commercial-use 的
- 用户标记"二改重新发布" → 过滤掉 NoDerivatives 的
- 跨国用户 → 提示 attribution requirement

允许的 license 白名单（v0.1）：

| SPDX | 商用 | 修改 | Attribution | html-video 收录 |
|---|---|---|---|---|
| Apache-2.0 | ✅ | ✅ | needed | ✅ default |
| MIT | ✅ | ✅ | needed | ✅ |
| CC0-1.0 | ✅ | ✅ | none | ✅ |
| CC-BY-4.0 | ✅ | ✅ | needed | ✅ |
| CC-BY-SA-4.0 | ✅ | ✅ (must SA) | needed | ⚠️ 须给用户 share-alike 警告 |
| CC-BY-NC-4.0 | ❌ | ✅ | needed | ⚠️ 仅个人/非商用入口 |
| GPL-3.0 | ✅ | ✅ (copyleft) | needed | ⚠️ 须给用户 copyleft 警告 |
| Other | — | — | — | ❌ 拒绝收录 |

---

## 关键设计决策记录

### 为什么 inputs 用 JSON Schema 不用 TS interface

JSON Schema 可以**运行时**校验 + 序列化传给 agent。TS interface 编译后丢失，agent 拿不到。

### 为什么 engine 字段必填且单值

强制每个 template 物理归属一个 engine，**避免维护多 engine 实现的同名 template**（容易漂移、维护成本翻倍）。如果某个 idea 适合多个 engine 实现，就发布为多个 template id（`bar-chart-race-mc` / `bar-chart-race-hf`），各自独立。

### 为什么 preview.poster 必填

agent 跟用户对话时一定要能 paste 一个截图让用户秒选；没 poster 的 template 不收录。这是入门门槛，不是限制——降低用户决策成本。

### 为什么 performance 是可选 + 作者填

中心化 benchmark 不现实（硬件 / 版本太多），让作者自报 reference 数字（hardware / engine version 标清），agent 用作 ranking tie-breaker 即可。

---

## Open Questions（v0.2 待定）

1. **i18n** —— `name` `description` 多语言？建议 v0.2 加 `i18n: { zh-CN: { name, description } }`，v0.1 默认英文
2. **变量 group** —— 复杂模板（>20 字段）需要分组渲染 UI；JSON Schema 标准的 `x-ui-order` / `x-ui-group` 扩展？
3. **依赖图** —— 一个 template 能不能 include 另一个 template（transition + main 组合）？v0.1 不支持，每模板独立
4. **变量来源** —— 是否预设 "data source" 类型让用户 paste CSV / Google Sheet URL？v0.1 只接 inline，外部数据靠 agent 自己拉
5. **A/B 变体** —— 一个模板出多版（不同色 / 不同 motion）共享同源代码？v0.2 加 `variants` 字段
