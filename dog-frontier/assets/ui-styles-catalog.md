# 67 种 UI 风格速查目录

> 来源: ui-ux-pro-max (MIT) — 67种UI风格分类体系
> 本文件提供风格速查,完整数据请调用 `python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain style`

## 现代主流风格 (Top 20)

| # | 风格 | 核心特征 | 最适合 | CSS关键词 |
|---|------|----------|--------|-----------|
| 1 | **Minimalism** | 大量留白, 极简色彩, 无冗余 | SaaS, Tech, Portfolio | white-space, simplicity |
| 2 | **Glassmorphism** | 半透明+模糊+微边框 | SaaS, Dashboard, App | backdrop-filter, blur, rgba |
| 3 | **Brutalism** | 原始HTML感, 强对比, 无圆角 | Creative, Portfolio, Art | bold borders, monospace |
| 4 | **Neumorphism** | 软阴影, 凸起/凹陷感 | Health, Fitness, IoT | box-shadow, soft UI |
| 5 | **Bento Grid** | 模块化网格, 大小不一卡片 | Dashboard, Landing, Portfolio | grid, varied sizes |
| 6 | **Dark Mode** | 深色背景, 低亮度, 高对比 | Developer Tools, Gaming | dark theme, low light |
| 7 | **Claymorphism** | 3D软泥感, 内阴影+外阴影 | Kids, Creative, Gaming | 3D, soft shadows |
| 8 | **Flat Design** | 无阴影, 纯色块, 清晰边界 | Enterprise, Gov, Finance | flat, no shadow |
| 9 | **Skeuomorphism** | 模拟真实材质纹理 | Legacy, Luxury, Craft | realistic, texture |
| 10 | **Gradient** | 渐变背景, 流动色彩 | Modern Brand, SaaS | gradient, mesh |
| 11 | **Aurora UI** | 极光色彩, 流动渐变 | Creative, Brand, Music | aurora, blend mode |
| 12 | **Vaporwave** | 霓虹粉紫, 复古未来感 | Music, Event, Gaming | neon pink, synthwave |
| 13 | **Cyberpunk** | 霓虹绿蓝, 高科技低生活 | Gaming, Tech, Sci-Fi | neon, dark, terminal |
| 14 | **Y2K Aesthetic** | 千禧年金属色, 塑料感 | Fashion, Youth, Music | chrome, metallic |
| 15 | **Frutiger Aero** | 光面玻璃, 自然元素 | Health, Nature, Wellness | glossy, nature, glass |
| 16 | **Memphis Design** | 几何图形, 波普色彩 | Creative, Event, Youth | geometric, pop, bold |
| 17 | **Swiss Design** | 网格系统, Helvetica, 严谨 | Corporate, Editorial | grid, sans-serif |
| 18 | **Organic/Biophilic** | 自然曲线, 暖色调, 有机形 | Wellness, Eco, Food | organic shapes, curves |
| 19 | **Editorial** | 大标题, 衬线体, 栏式布局 | Blog, Magazine, News | serif, columns |
| 20 | **AI-Native UI** | 对话式, 流式, 动态生成 | AI Products, Chat | chat, streaming, genUI |

## 完整风格-产品匹配表 (Top 30)

| 产品类型 | 首选风格 | 备选风格 | 避免 |
|----------|----------|----------|------|
| SaaS (B2B) | Minimalism, Glassmorphism | Flat, Dark | Brutalism, Maximalist |
| SaaS (B2C) | Gradient, Glassmorphism | Aurora, Bento | Brutalism, Flat |
| E-commerce | Photo-Based, Bold Typography | Minimal, Vibrant | Brutalism, Dense |
| Fintech/Crypto | Dark Mode, Glassmorphism | Flat, Geometric | Playful, Vaporwave |
| Healthcare | Soft UI, Organic | Neumorphism, Clean | Cyberpunk, Brutalism |
| Education | Clean, Accessible | Flat, Minimalism | Dark, Complex |
| Gaming | Cyberpunk, Vaporwave | Neon, Dark Mode | Flat, Corporate |
| Social Media | Vibrant, Gradient | Y2K, Glassmorphism | Dense, Enterprise |
| Portfolio | Brutalism, Editorial | Minimalism, Swiss | Generic, Template |
| Admin Dashboard | Bento, Dark Mode | Flat, Minimalism | Maximalist, Playful |
| AI/Chat Product | AI-Native, Minimalism | Dark Mode, Glass | Complex, Cluttered |
| Beauty/Spa | Soft UI, Organic | Glassmorphism, Warm | Cyberpunk, Brutalism |
| Food/Restaurant | Photo-Based, Warm | Organic, Vintage | Cold, Dark |
| Real Estate | Photo-Based, Clean | Minimalism, Luxury | Dense, Playful |
| Luxury Brand | Editorial, Swiss | Minimalism, Elegant | Playful, Brutalism |

## 风格组合矩阵

某些风格可组合使用,产生独特效果:

| 组合 | 效果 | 场景示例 |
|------|------|----------|
| Glassmorphism + Dark Mode | 科技感半透明卡片 | AI SaaS 仪表盘 |
| Bento Grid + Minimalism | 模块化极简布局 | Apple 风格产品页 |
| Brutalism + Editorial | 原始排版风格 | 独立设计师作品集 |
| Claymorphism + Gradient | 3D 柔和渐变 | 儿童教育 App |
| Aurora + Glassmorphism | 极光玻璃效果 | 音乐流媒体 |
| Swiss + Dark Mode | 严谨暗色系统 | 金融数据平台 |
| Organic + Minimalism | 自然极简 | 健康养生品牌 |
| AI-Native + Glassmorphism | AI 对话界面 | ChatGPT 风格产品 |

## 风格选择决策流程

```
1. 确定产品类型 (从161种产品中匹配)
        ↓
2. 确定目标受众 (C端/B端/开发者/儿童/...)
        ↓
3. 匹配首选风格 (查上表)
        ↓
4. 考虑风格组合 (是否需要混搭?)
        ↓
5. 反模式检查 (该产品类型应避免什么?)
        ↓
6. 最终风格方案 (1个主风格 + 0-2个辅风格)
```

## 快捷命令

```bash
# 搜索风格详情
python3 skills/ui-ux-pro-max/scripts/search.py "glassmorphism dark" --domain style

# 获取 AI 绘图提示词/CSS 关键词
python3 skills/ui-ux-pro-max/scripts/search.py "minimalism" --domain prompt

# 搜索落地页风格
python3 skills/ui-ux-pro-max/scripts/search.py "hero social-proof pricing" --domain landing
```
