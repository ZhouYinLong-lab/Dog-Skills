export const meta = {
  name: 'bootstrap-skill',
  description: 'Create a new skill from scratch: scaffold the directory + SKILL.md template, then sync to the root README.',
  phases: [
    { title: 'Scaffold', detail: 'Create skill directory and SKILL.md from template' },
    { title: 'Sync', detail: 'Run sync-skill-readme to update README.md' },
  ],
}

// ── Phase 1: Scaffold the skill ──
phase('Scaffold')

const skillDir = args?.skillDir
const skillName = args?.name
const skillTitle = args?.title
const skillDescription = args?.description

if (!skillDir) {
  log('ERROR: args.skillDir is required (e.g. "my-skill/")')
  throw new Error('Missing required arg: skillDir')
}
if (!skillName) {
  log('ERROR: args.name is required (e.g. "my-skill")')
  throw new Error('Missing required arg: name')
}
if (!skillDescription) {
  log('ERROR: args.description is required')
  throw new Error('Missing required arg: description')
}

log(`Bootstrapping skill: ${skillName} in ${skillDir}`)

const scaffoldResult = await agent(
  `Create a new skill directory and SKILL.md file with the following data:

- Directory: ${skillDir}
- Skill name: ${skillName}
- Title: ${skillTitle || skillName}
- Description: ${skillDescription}

## Instructions

1. Create the directory "${skillDir}" if it doesn't exist.
2. Create "${skillDir}/SKILL.md" with this template:

\`\`\`markdown
---
name: ${skillName}
description: >
  ${skillDescription}
allowed-tools:
  - Read
  - Write
  - Edit
---

# ${skillTitle || skillName}

## Overview

[Brief overview of what this skill does]

## Workflow

[Describe the step-by-step workflow]

## Key Features

- Feature 1
- Feature 2

## Usage

[How to use this skill — trigger phrases, commands, etc.]

## References

- [Any references or attributions]
\`\`\`

3. Create "${skillDir}/LICENSE" with MIT license (standard MIT text).

## Rules
- Only create files if they don't already exist. If SKILL.md exists, report that and stop.
- Use the EXACT skill name and description provided.
- Write the SKILL.md in the same bilingual style as other skills in this repo (Chinese + English where appropriate).
- Derive a good title from the description if no explicit title is given.`,
  { label: `scaffold:${skillName}` }
)

log(`Scaffold done: ${scaffoldResult}`)

// ── Phase 2: Sync to README ──
phase('Sync')

log('Running sync-skill-readme to update README.md...')

const syncResult = await workflow('sync-skill-readme', {
  skillDir: skillDir,
  name: args.name,
  title: args.title,
  triggerExamples: args.triggerExamples,
  installName: args.installName,
  installCmd: args.installCmd,
  shortDescription: args.shortDescription,
})

log(`README sync done: ${syncResult?.summary || 'completed'}`)

return {
  skill: { name: skillName, dir: skillDir },
  sync: syncResult,
  status: 'done',
  summary: `Created "${skillName}" in ${skillDir} and synced to README.md.`,
}
