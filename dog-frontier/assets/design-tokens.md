# 设计令牌系统 (Design Tokens)

> 来源: design-system sub-skill (ui-ux-pro-max, MIT) + W3C Design Tokens Community Group

## 三阶令牌架构

```
Layer 1: Primitive Tokens (原始令牌)
  → 原子级定义: 色值、间距值、字号、阴影参数
  → 不携带语义,纯数据

Layer 2: Semantic Tokens (语义令牌)
  → 为原始值赋予目的含义
  → 如: --color-primary 引用 --blue-600

Layer 3: Component Tokens (组件令牌)
  → 为具体组件定义令牌
  → 如: --button-bg 引用 --color-primary
```

## 完整令牌表

### 原始令牌: 颜色

```css
:root {
  /* Gray Scale */
  --gray-50: #F8FAFC;
  --gray-100: #F1F5F9;
  --gray-200: #E2E8F0;
  --gray-300: #CBD5E1;
  --gray-400: #94A3B8;
  --gray-500: #64748B;
  --gray-600: #475569;
  --gray-700: #334155;
  --gray-800: #1E293B;
  --gray-900: #0F172A;
  --gray-950: #020617;

  /* Brand Colors — 根据设计系统替换 */
  --blue-50: #EFF6FF;
  --blue-100: #DBEAFE;
  --blue-500: #3B82F6;
  --blue-600: #2563EB;
  --blue-700: #1D4ED8;

  /* Semantic Colors */
  --red-500: #EF4444;
  --green-500: #22C55E;
  --yellow-500: #EAB308;
}
```

### 语义令牌: 颜色

```css
:root {
  /* Surface */
  --color-surface: var(--gray-50);
  --color-surface-elevated: var(--white);
  --color-surface-overlay: rgba(0, 0, 0, 0.5);

  /* Text */
  --color-text-primary: var(--gray-900);
  --color-text-secondary: var(--gray-500);
  --color-text-disabled: var(--gray-300);
  --color-text-inverse: var(--white);

  /* Interactive */
  --color-primary: var(--blue-600);
  --color-primary-hover: var(--blue-700);
  --color-primary-active: var(--blue-800);
  --color-primary-text: var(--white);

  /* Status */
  --color-success: var(--green-500);
  --color-error: var(--red-500);
  --color-warning: var(--yellow-500);

  /* Border */
  --color-border: var(--gray-200);
  --color-border-focus: var(--blue-500);
}

/* Dark Mode Override */
[data-theme="dark"] {
  --color-surface: var(--gray-950);
  --color-surface-elevated: var(--gray-900);
  --color-text-primary: var(--gray-50);
  --color-text-secondary: var(--gray-400);
  --color-border: var(--gray-800);
}
```

### 原始令牌: 间距 (4px 基准)

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
}
```

### 原始令牌: 字体大小

```css
:root {
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px */
  --text-xl: 1.25rem;     /* 20px */
  --text-2xl: 1.5rem;     /* 24px */
  --text-3xl: 1.875rem;   /* 30px */
  --text-4xl: 2.25rem;    /* 36px */
  --text-5xl: 3rem;       /* 48px */
}
```

### 原始令牌: 阴影 (Elevation)

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);

  /* Glassmorphism specific */
  --shadow-glass: 0 8px 32px rgba(0, 0, 0, 0.08);
}
```

### 原始令牌: 圆角

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-full: 9999px;
}
```

### 组件令牌示例

```css
:root {
  /* Button */
  --button-bg: var(--color-primary);
  --button-text: var(--color-primary-text);
  --button-radius: var(--radius-md);
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);

  /* Card */
  --card-bg: var(--color-surface-elevated);
  --card-border: var(--color-border);
  --card-radius: var(--radius-lg);
  --card-shadow: var(--shadow-sm);
  --card-padding: var(--space-6);

  /* Input */
  --input-bg: var(--color-surface-elevated);
  --input-border: var(--color-border);
  --input-focus-border: var(--color-border-focus);
  --input-radius: var(--radius-md);
  --input-padding: var(--space-3) var(--space-4);
}
```

## Tailwind 配置映射

```js
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        surface: {
          DEFAULT: 'var(--color-surface)',
          elevated: 'var(--color-surface-elevated)',
          overlay: 'var(--color-surface-overlay)',
        },
        primary: {
          DEFAULT: 'var(--color-primary)',
          hover: 'var(--color-primary-hover)',
          active: 'var(--color-primary-active)',
        },
      },
      spacing: {
        '1': 'var(--space-1)',
        '2': 'var(--space-2)',
        '4': 'var(--space-4)',
        '6': 'var(--space-6)',
        '8': 'var(--space-8)',
      },
      borderRadius: {
        DEFAULT: 'var(--radius-md)',
        lg: 'var(--radius-lg)',
        xl: 'var(--radius-xl)',
      },
      boxShadow: {
        card: 'var(--card-shadow)',
        glass: 'var(--shadow-glass)',
      },
    },
  },
}
```

## 使用原则

1. **组件代码中只使用组件令牌**,不直接用原始令牌
2. **语义令牌可跨组件共享**,如 `--color-primary`
3. **原始令牌只在定义层出现**,不在组件代码中出现
4. **暗色模式通过 [data-theme] 覆盖**,不需要条件逻辑
5. **新增令牌前先检查是否已存在**等效令牌
