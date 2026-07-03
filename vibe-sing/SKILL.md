---
name: vibe-sing
description: >
  Vibe Sing——让 Claude Code 在会话结束时为你唱一首歌。读取当前会话记录→
  Gemini 分析情绪和氛围→Google Lyria 3 作曲并演唱→自动播放。
  支持 30 秒片段和 2 分钟完整版。写完代码听一首总结你今天痛苦（或快乐）的歌。
  Trigger keywords: vibe-sing, 唱歌, 写歌, 音乐, vibe music, 生成歌曲,
  AI唱歌, 会话总结歌, 编曲, 作曲, 播放音乐, 结束唱歌, make music.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
metadata:
  category: tools
  source: https://github.com/harajlim/vibe-sing
  version: "1.0.0"
  license: MIT
---

# Vibe Sing — 让 Claude Code 为你唱歌

> 写了一下午 bug，Claude 给你唱了一首总结你痛苦（或快乐）一天的歌。

## 工作原理

```
会话记录 (JSONL) → Gemini 分析情绪 → Lyria 3 作曲+演唱 → 自动播放
```

1. **读取会话** — 定位当前 Claude Code 会话的 transcript，提取用户消息和 agent 文本
2. **分析氛围** — Gemini 读取情绪/幽默/能量，输出 Lyria 音乐 prompt
3. **Lyria 3 作曲** — Google 最新的音乐生成模型，含人声
4. **自动播放** — macOS `afplay` / Linux `mpg123`

## 命令

| 命令 | 效果 | 费用 |
|------|------|------|
| `/vibe-sing` | 30 秒片段 | ~4 美分 |
| `/vibe-sing pro` | 2 分钟完整版（带人声） | ~8 美分 |
| `/vibe-sing stop` | 停止播放 | 免费 |

## 安装

```bash
git clone https://github.com/harajlim/vibe-sing.git ~/.claude/skills/vibe-sing
cd ~/.claude/skills/vibe-sing
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 填入 GOOGLE_API_KEY
```

需要 [Google AI Studio](https://aistudio.google.com/apikey) API Key。

## 触发示例

- "/vibe-sing — 今天写了好多代码，给我来一首"
- "/vibe-sing pro — 完整版，认真点"
- "vibe sing my session"
