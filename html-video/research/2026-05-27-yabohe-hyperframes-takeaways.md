# Hyperframes 完整指南文章笔记

> Source: yabohe (公众号 yablog), 2026-05-27
> URL: https://mp.weixin.qq.com/s/fVb8VNWpevh9vQP4tPrbPw
> Local copy: `research/refs/mp.weixin.qq.com/hyperframes-mmbiz-qpic-cn-sz_mmbiz_png-xw7as806wyt/`

## 文章内容速记

HF 五步流程：

1. **`init`** — `npx hyperframes init my-video [--example warm-grain] [--video clip.mp4] [--audio track.mp3]`
   - 内置模板：`blank / warm-grain / swiss-grid / kinetic-type / product-promo`
2. **写 HTML 合成** — 一个 HTML 文件 = 一个视频；用 `data-*` 属性控时间轴 + GSAP 做动画 + CSS 做样式
3. **`lint`** — `npx hyperframes lint [--verbose]` 语法 / schema 错误检查
4. **`preview`** — `npx hyperframes preview` 浏览器实时热重载
5. **`render`** — `npx hyperframes render [--quality draft|high] [--fps 60] [--format webm] [--output xx.mp4]`

额外能力：

- **`transcribe`** — STT 字幕：`npx hyperframes transcribe audio.mp3` / `transcribe video.mp4 --model medium.en`
- **`tts`** — 旁白：`npx hyperframes tts "你的文本" --voice af_nova --output narration.wav`，`tts --list` 看所有声色

## 给 html-video 的 5 条建议

按 ROI 排（→ 是否 v0.7 该做）：

### ★★★★★ 1. adapter-hyperframes 接 HF 真实 CLI（v0.7 必做）

文章证实 HF CLI surface area 稳定：`init / lint / preview / render`。**adapter-hyperframes/src/render.ts 现在是 stub，换成 `child_process.spawn('npx', ['hyperframes', 'render', '--output', xx])` 就能真出 MP4**。不用自己写 puppeteer / ffmpeg。

具体动作：
- adapter `render()` → `spawn('npx', ['hyperframes', 'render', '--output', config.outputPath, '--quality', config.quality === 'high' ? 'high' : 'draft', '--fps', String(config.fps)], { cwd: workDir })`
- spawn 之前先把当前 preview.html 写到 workDir 下作为 entry
- 解析 stderr 转成 progress events
- HF cli 的 doctor / version 检测进 `html-video doctor`

### ★★★★ 2. prompt 教 agent 保留 data-* 时间轴

HF 视频源码靠 `data-start` / `data-duration` / `data-anim` 等属性 + GSAP timeline 驱动。我现在 prompt 只说 "preserve visual signature"，模糊。改成显式：

> Hyperframes uses `data-start`, `data-duration`, `data-anim`, and similar `data-*` attributes on elements to drive the timeline. Preserve every `data-*` attribute (including `data-hv-text` and any HF time-axis attributes) when rewriting. Don't touch GSAP timeline IDs, animation triggers, or scene boundaries — only change visible text content and inline values.

### ★★★ 3. 加 lint step

agent 出 HTML 后 server 调一次 `npx hyperframes lint preview.html`：

- 错误进 chat 一条 system / tool message
- agent 看到错误后下一轮自动修
- 用户少踩"看起来对但其实坏了"的坑

### ★★★ 4. TTS 旁白接进 chat 流

用户说 "用 af_nova 声音读这段：xxx" → agent 调 `hyperframes tts` → 拿到 narration.wav → 嵌入 HTML `<audio>` → preview iframe 自动播。**比让用户自己上传音频更 agent-native**，是文章给我们最 leverage 的 idea。

### ★★ 5. 模板 metadata 加 HF style_family

HF 内置的 `warm-grain / swiss-grid / kinetic-type / product-promo` 是好的"风格大类"分组，比我现在 `category: intro-outro / data-viz` 之类的功能性分类**更接近用户审美决策点**。

template.html-video.yaml 加：

```yaml
style_family: warm-grain  # warm-grain | swiss-grid | kinetic-type | product-promo | bauhaus | editorial | cinematic | ambient | brutalist | cyberpunk
```

gallery 按 style_family 折叠分组（"按风格" / "按用途" 双视图）。

## 不直接抄、但要心里有数的事

- HF 自带 STT (`transcribe`) — 我们如果做"把视频转字幕段"功能，复用 HF 即可不用自己接 whisper
- HF `init --example` 已经有 example 模板向导 — 我们 gallery 已经做了类似事，但**带 example 项目脚手架**（含 README / 默认 vars / 推荐流程）这个粒度我们没做，未来 v1 可以
- HF v0.4 文档里没提"agent 协作"，**这是 html-video 真正的差异化**——HF 是给开发者的工具，html-video 是给"用 agent 帮我做视频"的创作者
