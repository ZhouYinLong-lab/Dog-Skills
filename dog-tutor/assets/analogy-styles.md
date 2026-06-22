# 四种比喻风格

> 来源: SmartTutor Generator v1.1 (莫弈, 2026)

---

## 风格配置

### daily_life — 生活化类比

```yaml
name: "生活化类比"
description: "用日常场景解释抽象概念"
examples: ["遥控器", "租房", "钥匙锁", "智能管家", "餐厅点餐", "开车导航"]
suitable_for:
  - 零基础学习者
  - 概念抽象的技术主题
  - 需要降低学习焦虑
tone: "亲切、易懂、接地气"
principle: "让奶奶也能听懂"
```

**示例**:
> "防火墙就像大楼的前台接待——所有进出的人都要经过它的检查。
> 白名单就是'只有名单上的人才能进',黑名单就是'名单上的人不能进'。"

### professional — 专业领域类比

```yaml
name: "专业领域类比"
description: "用行业经验解释新概念"
examples: ["工厂流水线", "图书馆索引", "电路设计", "建筑蓝图", "物流配送"]
suitable_for:
  - 有行业背景的学习者
  - 技术迁移场景
  - B2B企业培训
tone: "专业、精准、高效"
principle: "用你已有的知识撬动新知识"
```

**示例**:
> "Docker 镜像可以类比为建筑工程中的蓝图——
> 蓝图定义了建筑的结构,镜像定义了容器的结构。
> 同一个蓝图可以建造多栋相同的建筑,同一个镜像可以启动多个相同的容器。"

### humorous — 幽默轻松风格

```yaml
name: "幽默轻松风格"
description: "用有趣场景降低学习门槛"
examples: ["魔法咒语", "宠物训练", "餐厅后厨", "游戏闯关", "穿越剧情"]
suitable_for:
  - 降低学习焦虑
  - 娱乐性内容
  - 年轻受众
tone: "轻松、有趣、记忆深刻"
principle: "笑着学会的知识永远不会忘"
```

**示例**:
> "Git 的 commit 就像 RPG 游戏里的存档点——
> 打 Boss 前存个档,翻车了还能读档重来。
> 而不commit就直接关游戏...你懂的,白打了。"

### rigorous — 严谨学术风格

```yaml
name: "严谨学术风格"
description: "用逻辑推导建立知识体系"
examples: ["数学证明", "实验设计", "逻辑推导", "分类学", "公理体系"]
suitable_for:
  - 学术内容
  - 专家受众
  - 考试导向
tone: "严谨、系统、完整"
principle: "每一步推导都有据可查"
```

**示例**:
> "时间复杂度 O(n log n) 的数学直觉来源于分治策略:
> 每次将问题规模减半(log n 层),每层需要线性时间(n)处理合并。"

---

## 风格自动匹配

| 领域 | 受众 | → 风格 |
|------|------|--------|
| technology | absolute_beginner | daily_life |
| technology | beginner | daily_life |
| technology | intermediate | professional |
| technology | expert | professional |
| business | 任意 | professional |
| academic | 任意 | rigorous |
| life | 任意 | daily_life |
| art | 任意 | humorous |

---

## 风格选择流程

```
1. 用户明确指定风格? → 使用指定风格
2. 否则,查表自动匹配(领域 × 受众)
3. 每章生成后可调整("这个比喻风格合适吗?")
4. 支持混合: 主风格 + 特定章节使用不同风格
```
