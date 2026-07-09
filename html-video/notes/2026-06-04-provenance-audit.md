# Provenance audit — 模板来源核查报告

> 2026-06-04。起因:发现今天新增的 3 个模板(已回退)与仓库已有模板视觉撞车,
> 进而对整个模板库的"原创性声明 + 署名"做了一次真实上游比对。

## TL;DR

仓库里 6 个模板声明了 provenance,来自 2 个 MIT 上游。核查后发现 **3 个严肃问题**:

1. **署名链条缺了一层**:`Pentagram` / `Build` / `Takram` 不是上游(huashu-design)原创,
   而是 huashu 在**致敬真实世界的知名设计公司/设计师**。我们直接拿这些公司名当了模板
   id 和显示名,而 huashu 自己的文档明确告诫"不要直接写 in the style of Pentagram"。
2. **"original / no source copied" 声明未经核实**:这句话是模板生成时自我宣称的,从未
   真去上游 diff。实测复刻程度逐个不同(Pentagram 红+白全同;Build 共享 4 个暖灰色)。
3. **连示例数据都是照搬的**:`95.7 / 73.8 / 87.4 / AIME / SWE-bench` 直接来自上游
   ppt 源页,不是我们自编的占位数据。

## 上游核实

| 上游 repo | 真实版权人 | License | 用于我们的模板 |
|---|---|---|---|
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | **alchaincyf(花叔 · 花生)** © 2026 | MIT ✅ 已核实 | build-minimal, pentagram-stat, takram-organic |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | **Zara Zhang** © 2025 | MIT ✅ 已核实 | bold-signal, creative-voltage, electric-studio |

License 真的是 MIT,允许商用 + 再分发,**所以这不是"能不能用"的问题**——MIT 完全允许。
问题在**署名是否写清楚、风格名是否该直接挪用**。

## 关键发现:Pentagram/Build/Takram 是三层署名,不是两层

huashu-design 的 `references/design-styles.md` 明确写道:

- **01 Pentagram** = "Michael Bierut 风格 / Pentagram"(搜索词:pentagram hillary logo system)
  —— 真实的全球顶级设计公司 Pentagram,设计师 Michael Bierut
- **11 Build** = "Build studio luxury minimalism"(搜索词:build studio london branding)
  —— 伦敦设计工作室 Build
- **17 Takram** = "Takram Japanese speculative design"(搜索词:takram nhk data visualization)
  —— 日本设计公司 Takram

→ 真实署名链是:**Pentagram / Build / Takram(真实工作室)→ huashu-design 提炼为"风格 +
HTML 示例"(MIT,花叔)→ html-video 转成视频模板**。我们当前 provenance 只写到 huashu
这一层,且把工作室名当成了模板名直接挂出。

huashu 自己的规矩(design-styles.md):
> ❌ 不要直接写 "in the style of Pentagram" → ✅ 用具体设计特征描述

我们的模板 id 恰恰是 `frame-pentagram-stat` / `frame-takram-radar` / `frame-build-minimal`。

## 实质比对(上游 ppt 源页 vs 我们的模板)

| 风格 | 共享配色 | 字体 | 复刻程度 |
|---|---|---|---|
| Pentagram | 2/2(#E63946 红 + #FFFFFF 全同) | 我们换成 Archivo | 高 — 配色照搬 |
| Build | 4/7(#A8A4A0 #B0ACA4 #D4A574 暖灰全同) | 同 Inter | 高 — 配色+字体同源 |
| Takram | 0/7(配色我们重新调过) | 我们换成 Manrope | 中 — 重新着色 |

示例数据 `95.7/73.8/87.4 + AIME/SWE-bench`:**三个上游 ppt 页里都有,我们照搬。**

## 结论

- **不是侵权**(MIT 授权,允许商用+演绎),但**署名不充分 + 风格命名不当**。
- 对一个要公开发布(Apache-2.0)、给 nexu.io / OD 生态导流的项目,这是要修的诚信/署名问题。

## 整改方案 + 标准转换规范

规范已定:见 [RFC-07 PPT Skill → Hyperframes 模板 转换规范](../research/2026-06-04-spec-07-ppt-to-template.md)。
下一步用 RFC-07 回头整改本报告列出的 6 个模板(三层署名 + 重命名 + 自有示例)。
