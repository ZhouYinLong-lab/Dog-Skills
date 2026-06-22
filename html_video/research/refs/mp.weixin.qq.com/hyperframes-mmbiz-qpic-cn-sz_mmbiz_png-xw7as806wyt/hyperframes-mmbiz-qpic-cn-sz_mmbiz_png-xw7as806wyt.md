---
url: https://mp.weixin.qq.com/s/fVb8VNWpevh9vQP4tPrbPw
title: "使用 HyperFrames 生成视频的完整指南"
description: "HyperFrames 是一个 用 HTML 制作视频 的开源框架。核心理念：HTML 是视频的源码，用 data-* 属性控制时间轴，GSAP 做动画，CSS 做样式，最终渲染为 MP4/WebM 视频。"
author: "yabohe"
coverImage: "https://mmbiz.qpic.cn/sz_mmbiz_jpg/XW7aS806wYv8ERNtGAEAUjSLXT6083PPxQG3G4NKtDaYzxYCAXaw8MvL6WWM4Q9mFp2x3IYibvOlNKAY5PX4Tkwj6OJmVrZ3qsficBoZtyibFE/0?wx_fmt=jpeg"
captured_at: "2026-05-27T09:33:36.626Z"
---

# 使用 HyperFrames 生成视频的完整指南

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XW7aS806wYtav7Q4VdDtFcS5ZSpbCXhNBKlI9CuiaY67YejhDQPTNvG3kIIpd4p4R0tbkiby0NnvnlIRRpMw2JkXJF5ic74FkpAnDlib0S8NGSU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

HyperFrames 是一个 用 HTML 制作视频 的开源框架。核心理念：HTML 是视频的源码，用 data-\* 属性控制时间轴，GSAP 做动画，CSS 做样式，最终渲染为 MP4/WebM 视频。

使用 HyperFrames 生成视频的流程分为下面五步：

1. init（初始化项目）
2. 编写 HTML 合成
3. lint（检查）
4. preview（预览）
5. render（渲染视频）

第 1 步：初始化项目

```cs
# 交互式向导npx hyperframes init my-video     # 从模板创建                   npx hyperframes init my-video --example warm-grain# 带视频素材   npx hyperframes init my-video --video clip.mp4# 带音频素材       npx hyperframes init my-video --audio track.mp3
```

可选模板有：blank, warm-grain, swiss-grid, kinetic-type, product-promo 等。

第 2 步：编写 HTML 合成

这是 hyperframes skill 的核心。

一个视频合成就是一个 HTML 文件，其核心结构如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/XW7aS806wYuVx8ZZ8eB2Go0lA1j90mynjdeSYW58CstTPDv04niaGUicTD377dOgzqCr3hicAVODjb8BV4NZSlEluE6HictTbfanbdBcosPyicV8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

其中关键 data 属性说明为：

![图片](https://mmbiz.qpic.cn/mmbiz_png/XW7aS806wYvB35TCLMxLYPRibhOZibXwSMcJVBMFibHKMMfTq07Br2uoz7P1Gg6zNStMGAhQRj7I9wDu3uV7wkmDSiczzqjQLWoFMS2qVULSmPI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

第 3 步：检查

```nginx
# 检查语法错误npx hyperframes lint# 显示详细信息npx hyperframes lint --verbose
```

第 4 步：预览

```nginx
# 浏览器中实时预览，支持热重载npx hyperframes preview
```

第 5 步：渲染为视频

```apache
# 标准 MP4npx hyperframes render# 快速草稿（迭代用）npx hyperframes render --quality draft# 高质量最终输出npx hyperframes render --fps 60 --quality high# 透明背景 WebMnpx hyperframes render --format webm# 指定输出文件名npx hyperframes render --output final.mp4
```

其他额外能力：

```css
# 语音转文字（字幕）npx hyperframes transcribe audio.mp3npx hyperframes transcribe video.mp4 --model medium.en
# 文字转语音（旁白）npx hyperframes tts "你的文本" --voice af_nova --output narration.wav# 查看所有可用声音npx hyperframes tts --list
```

References

- https://github.com/heygen-com/hyperframes

继续滑动看下一个

yablog

向上滑动看下一个