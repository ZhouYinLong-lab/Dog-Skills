---
name: cc-dispatch
description: >
  Codex 与 Claude Code 协作的分发协议。当你（Codex）需要将实现任务委托给 Claude Code 执行时，使用此 skill 生成结构化任务包（Task Package），并根据 Claude Code 返回的完成报告（Completion Report）执行验收。

  核心目标：让每个任务包足够精确，使 Claude Code 无需反复确认即可一次性执行正确；让每份完成报告足够结构化，使你无需阅读所有代码改动即可快速验收。

  **触发时机**：
  - 用户提出需求，你需要拆解并交给 Claude Code 实现
  - 你收到 Claude Code 的完成报告，需要执行验收
  - 需要对已完成任务提出修改意见并生成 Change Request
metadata:
  category: development
---

# Codex ↔ Claude Code 协作协议

这是一套异步任务分发协议，像票据系统而非对话。你（Codex）作为 PM，负责需求拆解、任务包生成和最终验收；Claude Code 负责执行实现。

---

## 阶段一：生成任务包

### 任务包的核心原则

- **自包含**：Claude Code 拿到任务包后无需任何追问就能开始执行
- **精确而非冗长**：用文件路径引用代码，不要粘贴大段内容
- **验收前置**：验收标准在任务包里定义好，而不是事后补充
- **边界清晰**：明确说明哪些东西不能动

### 任务包模板

````markdown
## Task Package

**Task ID**: `TASK-<项目缩写>-<序号>`（如 `TASK-AUTH-042`）
**Title**: 一句话描述任务
**Priority**: P0 / P1 / P2
**Estimated Scope**: 小（< 50 行）/ 中（50-200 行）/ 大（> 200 行）

---

### Context

<!-- 1-3 句话说明背景：为什么要做这个，当前状态是什么 -->

相关文件：
- `src/auth/login.ts` — 当前登录逻辑
- `src/types/user.ts` — User 类型定义

<!-- 只列出 Claude Code 需要理解的文件路径，不要粘贴内容 -->

---

### Requirements

<!-- 编号的具体要求列表，每条都是可执行的动作 -->

1. 在 `src/auth/login.ts` 中，将 token 过期时间从硬编码的 3600 改为读取 `config.tokenTtl`
2. 在 `src/config.ts` 中新增 `tokenTtl` 配置项，默认值 3600，类型 `number`
3. 为修改后的登录逻辑新增单元测试，覆盖 token 过期的边界情况

---

### Constraints

<!-- 告诉 Claude Code 什么不能做 -->

- 不要修改 `src/auth/logout.ts` 和任何 middleware 文件
- 不要改变 `login()` 函数的公共签名
- 保持现有测试全部通过，不允许删除或跳过任何测试
- 代码风格遵循项目 ESLint 配置

---

### Acceptance Criteria

<!-- 可验证的完成条件，Claude Code 必须在报告中逐条标注 PASS/FAIL -->

- [ ] AC-1：`config.tokenTtl` 存在且有默认值 3600
- [ ] AC-2：`login()` 使用 `config.tokenTtl` 而非硬编码值
- [ ] AC-3：新增测试覆盖 tokenTtl 为 0、负数、正常值三种情况
- [ ] AC-4：`npm test` 全部通过，无新增 warning

---

### Test Expectations

<!-- Claude Code 需要运行哪些测试命令 -->

```bash
npm test -- --testPathPattern=auth
npm run lint
```
````

---

### 任务拆解指南

**何时拆分任务**：如果一个任务涉及超过 3 个不相关模块，或预计改动超过 300 行，考虑拆成多个 Task Package。

**拆分原则**：
- 按模块边界拆，而不是按代码行数拆
- 有依赖关系的任务要注明 `Depends on: TASK-XXX`
- 每个子任务都要有独立可验证的 AC

**节省额度的关键**：Requirement 写得越精确，Claude Code 越不需要猜测，出错后返工的概率越低。与其写"优化登录逻辑"，不如写"将第 47 行的 if 判断提取为 `isTokenValid()` 函数"。

---

## 阶段二：解读完成报告

Claude Code 执行完毕后应返回如下格式的完成报告。以下是你（Codex）应该重点关注的内容：

### 完成报告结构（Claude Code 的输出格式）

````markdown
## Completion Report

**Task ID**: `TASK-<ID>`
**Status**: ✅ DONE / ⚠️ PARTIAL / ❌ BLOCKED

---

### Summary

<!-- 1-2 句话说明做了什么 -->

---

### Files Modified

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/auth/login.ts` | 修改 | 将 token TTL 改为读取配置 |
| `src/config.ts` | 修改 | 新增 tokenTtl 配置项 |
| `src/auth/login.test.ts` | 新增 | token 过期边界测试 |

---

### Acceptance Criteria Status

- [x] AC-1：`config.tokenTtl` 存在且有默认值 3600 — **PASS**
- [x] AC-2：`login()` 使用 `config.tokenTtl` — **PASS**
- [x] AC-3：新增测试覆盖三种情况 — **PASS**
- [ ] AC-4：`npm test` 全部通过 — **FAIL**（见 Deviations）

---

### Test Results

```
PASS src/auth/login.test.ts
FAIL src/auth/session.test.ts
  ● session timeout › should expire after TTL
    Expected: 3600, Received: undefined
```

---

### Deviations

<!-- 任何偏离原始 Requirements 的地方，以及原因 -->

- AC-4 未通过：`session.test.ts` 中存在一个预先存在的 bug，与本次修改无直接关联，但暴露在测试中。该文件不在本任务 Scope 内，建议新开 `TASK-SESSION-FIX`。

---

### Open Questions

<!-- 执行中遇到的疑问，仅当 PARTIAL 或 BLOCKED 时填写 -->

（无）
````

---

## 阶段三：执行验收

### 验收决策框架

收到完成报告后，按以下顺序检查：

1. **Status 是否 DONE？** 若 PARTIAL/BLOCKED，直接看 Open Questions，决定是补充信息还是重新规划任务
2. **所有 AC 是否 PASS？** 有 FAIL 的，看 Deviations 判断是任务本身的问题还是范围外的 bug
3. **Deviations 是否可接受？** 判断偏离是否影响核心目标
4. **有无需要跟进的副作用？** 如报告中暴露的新 bug

### 验收结论格式

**接受（ACCEPT）**：
```
ACCEPT TASK-AUTH-042
验收通过。AC-4 的 session.test.ts 问题已记录，新建 TASK-SESSION-FIX 跟进。
```

**请求修改（CHANGE REQUEST）**：
生成一个新的 Task Package，在 Context 中引用原 Task ID，Requirements 只写增量变更：

```markdown
## Task Package

**Task ID**: `TASK-AUTH-042-CR1`
**Title**: 修复 login.ts 的 config 读取时序问题
**Depends on**: `TASK-AUTH-042`（已完成）

### Context
基于 TASK-AUTH-042 的完成报告，AC-2 虽标注 PASS，但 Code Review 发现
`config.tokenTtl` 在 config 模块初始化前被读取（见 `src/auth/login.ts:23`）。

### Requirements
1. 将 `config.tokenTtl` 的读取从模块顶层移至 `login()` 函数调用时

### Acceptance Criteria
- [ ] AC-1：`login()` 调用时才读取 `config.tokenTtl`，而非模块加载时
- [ ] AC-2：原有测试全部通过
```

---

## 快速参考：Task Package 质量检查

生成任务包前，自问：

- [ ] Claude Code 是否知道要修改哪些具体文件？
- [ ] 每个 Requirement 都是可执行的动作而非模糊目标？
- [ ] 已明确列出不能修改的内容？
- [ ] AC 是否可以被机械地验证（而不需要主观判断）？
- [ ] 测试命令是否明确？

如果以上有任何一条是否，先完善任务包再交出去。
