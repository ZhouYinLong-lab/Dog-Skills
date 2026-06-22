# Vue 3 组件设计模式

> 来源: vue-component-patterns (The Bushido Collective, MIT) + shadcn-vue (noartem, MIT)
> + Vue 3 官方文档

## 推荐的组件结构

```
src/components/
├── ui/              # shadcn-vue 基础组件 (Button, Card, Dialog...)
├── layout/          # 布局组件 (Header, Sidebar, Footer)
├── feature/         # 业务功能组件
└── shared/          # 跨业务共享组件
```

## 组件模式 1: 类型安全的 Props + Emits

```vue
<script setup lang="ts">
import { computed } from 'vue'
import type { ButtonVariant, ButtonSize } from '@/types'

// === Props 定义 ===
interface Props {
  variant?: ButtonVariant       // 'primary' | 'secondary' | 'ghost' | 'destructive'
  size?: ButtonSize             // 'sm' | 'md' | 'lg'
  loading?: boolean
  disabled?: boolean
  icon?: string                 // Icon component name
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  loading: false,
  disabled: false,
})

// === Emits 定义 ===
const emit = defineEmits<{
  click: [e: MouseEvent]
}>()

// === Computed ===
const classes = computed(() => [
  `btn-${props.variant}`,
  `btn-${props.size}`,
  { 'btn-loading': props.loading },
  { 'btn-disabled': props.disabled },
])
</script>

<template>
  <button
    :class="classes"
    :disabled="props.disabled || props.loading"
    @click="emit('click', $event)"
  >
    <span v-if="props.loading" class="spinner" />
    <component :is="props.icon" v-if="props.icon" />
    <slot />
  </button>
</template>
```

## 组件模式 2: Composable 提取 (状态逻辑复用)

```typescript
// composables/useAsync.ts
import { ref, type Ref } from 'vue'

interface AsyncState<T> {
  data: Ref<T | null>
  error: Ref<Error | null>
  loading: Ref<boolean>
  execute: (...args: any[]) => Promise<T>
}

export function useAsync<T>(
  fn: (...args: any[]) => Promise<T>
): AsyncState<T> {
  const data = ref<T | null>(null) as Ref<T | null>
  const error = ref<Error | null>(null)
  const loading = ref(false)

  async function execute(...args: any[]): Promise<T> {
    loading.value = true
    error.value = null
    try {
      const result = await fn(...args)
      data.value = result
      return result
    } catch (e) {
      error.value = e as Error
      throw e
    } finally {
      loading.value = false
    }
  }

  return { data, error, loading, execute }
}
```

## 组件模式 3: 透传 (Fallthrough) + 组件扩展

```vue
<!-- components/ui/Dialog.vue -->
<script setup lang="ts">
import {
  DialogRoot,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
  DialogClose,
} from 'radix-vue'

interface Props {
  open?: boolean
  title?: string
  description?: string
}

const props = defineProps<Props>()
const emit = defineEmits<{
  'update:open': [value: boolean]
}>()
</script>

<template>
  <DialogRoot :open="props.open" @update:open="emit('update:open', $event)">
    <DialogContent>
      <DialogHeader>
        <DialogTitle>{{ props.title }}</DialogTitle>
        <DialogDescription>{{ props.description }}</DialogDescription>
      </DialogHeader>
      <slot />
      <DialogFooter>
        <slot name="footer" />
      </DialogFooter>
      <DialogClose />
    </DialogContent>
  </DialogRoot>
</template>
```

## 组件模式 4: Provide/Inject (跨层级通信)

```vue
<!-- 祖先组件 -->
<script setup lang="ts">
import { provide, ref, type InjectionKey, type Ref } from 'vue'

interface FormContext {
  values: Ref<Record<string, any>>
  errors: Ref<Record<string, string[]>>
  registerField: (name: string) => void
}

export const FORM_KEY: InjectionKey<FormContext> = Symbol('form')

const values = ref<Record<string, any>>({})
const errors = ref<Record<string, string[]>>({})

provide(FORM_KEY, {
  values,
  errors,
  registerField: (name) => { /* ... */ }
})
</script>

<!-- 后代组件 -->
<script setup lang="ts">
import { inject } from 'vue'
import { FORM_KEY } from './Form.vue'

const form = inject(FORM_KEY)
if (!form) throw new Error('FormField must be used inside Form')
</script>
```

## 组件模式 5: 插槽 (Slots) 灵活性最大化

```vue
<!-- components/ui/Card.vue -->
<script setup lang="ts">
interface Props {
  padding?: 'none' | 'sm' | 'md' | 'lg'
  hover?: boolean
}
const props = withDefaults(defineProps<Props>(), {
  padding: 'md',
  hover: false,
})
</script>

<template>
  <div
    :class="[$style.card, $style[`padding-${props.padding}`], { [$style.hover]: props.hover }]"
  >
    <header v-if="$slots.header" :class="$style.header">
      <slot name="header" />
    </header>

    <div v-if="$slots.media" :class="$style.media">
      <slot name="media" />
    </div>

    <div :class="$style.body">
      <slot />
    </div>

    <footer v-if="$slots.footer" :class="$style.footer">
      <slot name="footer" />
    </footer>
  </div>
</template>
```

## 组件模式 6: v-model 双向绑定

```vue
<script setup lang="ts">
interface Props {
  modelValue: string
  label?: string
  error?: string
}

const props = defineProps<Props>()
const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

// 多个 v-model
interface Props {
  modelValue: string
  search: string
}
const emit = defineEmits<{
  'update:modelValue': [value: string]
  'update:search': [value: string]
}>()
</script>

<!-- 使用: <MyInput v-model="text" v-model:search="query" /> -->
```

## shadcn-vue 集成速查

### 安装

```bash
npx shadcn-vue@latest init
npx shadcn-vue@latest add button card dialog dropdown-menu form input label select separator sheet table tabs textarea toast toggle tooltip
```

### 常用组件组合

```vue
<!-- 数据表格 (Table + Card + Input + DropdownMenu) -->
<Card>
  <CardHeader>
    <div class="flex items-center justify-between">
      <CardTitle>用户列表</CardTitle>
      <Input v-model="search" placeholder="搜索用户..." class="max-w-xs" />
    </div>
  </CardHeader>
  <CardContent>
    <Table>
      <TableHeader>...</TableHeader>
      <TableBody>...</TableBody>
    </Table>
  </CardContent>
</Card>

<!-- 表单对话框 (Dialog + Form + Input + Select) -->
<Dialog v-model:open="open">
  <DialogTrigger as-child>
    <Button>新建</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>新建项目</DialogTitle>
    </DialogHeader>
    <form @submit.prevent="handleSubmit">
      <FormField v-slot="{ componentField }" name="name">
        <FormLabel>项目名称</FormLabel>
        <Input v-bind="componentField" />
      </FormField>
    </form>
  </DialogContent>
</Dialog>
```

## 状态管理选择

| 复杂度 | 方案 | 场景 |
|--------|------|------|
| 低 | Props + Emits | 父子组件通信 |
| 中 | Provide/Inject | 深层组件树 |
| 中 | Composable + ref | 跨组件共享状态 |
| 高 | Pinia | 全局状态、模块化 |
| 服务端 | TanStack Query (VueQuery) | 服务端状态缓存 |

## 常见反模式

| 反模式 | 问题 | 正确做法 |
|--------|------|----------|
| 直接修改 props | 破坏单向数据流 | emit + computed getter/setter |
| 在 watch 中修改 watch 的源 | 无限循环 | computed 替代 watch |
| 不做类型声明 | 失去 TS 类型检查 | defineProps<T>() |
| 深层嵌套 provide/inject | 调试困难 | Pinia 或组合函数 |
| 用 ref 替代 reactive 存对象 | 失去响应性 | reactive 用于对象, ref 用于原始值 |
