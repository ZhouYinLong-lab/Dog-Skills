# GPT Researcher — 开源深度研究 Agent

基于 [GPT Researcher](https://github.com/assafelovic/gpt-researcher) v3.5.1（28,000+ ⭐）的 Claude Code 技能封装。

## 快速开始

```bash
# 1. 安装 Python 包
pip install gpt-researcher

# 2. 配置 API Keys
export OPENAI_API_KEY="sk-..."
export TAVILY_API_KEY="tvly-..."

# 3. 运行研究
python scripts/research.py "你的研究主题"
```

## 输出位置

所有研究报告保存到 `D:\Projects\Dog\Dog-Research/<topic-slug>/`，每次研究一个独立文件夹。

## 文件结构

```
gpt-researcher/
├── SKILL.md              # 技能定义
├── README.md             # 本文件
├── scripts/
│   └── research.py       # 研究包装脚本（自动管理输出目录）
└── references/           # 参考资料
```
