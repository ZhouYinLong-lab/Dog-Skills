export const meta = {
  name: 'sync-skill-readme',
  description: 'After creating or copying a skill directory, update the root README.md — adds entries to Installation, Verification, Trigger Table, and Skills sections.',
  phases: [
    { title: 'Extract', detail: 'Read SKILL.md and extract metadata' },
    { title: 'Update', detail: 'Update README.md in all 4 sections' },
    { title: 'Verify', detail: 'Check README is consistent' },
  ],
}

// ── Schema for structured metadata extraction ──
const SKILL_SCHEMA = {
  type: 'object',
  properties: {
    name: { type: 'string', description: 'Skill name from YAML frontmatter (e.g. "my-skill")' },
    title: { type: 'string', description: 'Human-readable title from the first H1 heading after frontmatter (e.g. "My Skill — Does Amazing Things")' },
    shortDescription: { type: 'string', description: 'First sentence or line of the description field — used as the Purpose line' },
    fullDescription: { type: 'string', description: 'Full description text from YAML frontmatter, used to derive the Skills section body' },
    hasWorkflow: { type: 'boolean', description: 'Whether the skill has a multi-step workflow worth diagramming' },
    hasSubcommands: { type: 'boolean', description: 'Whether the skill uses subcommands' },
    hasPrerequisites: { type: 'boolean', description: 'Whether the skill lists prerequisites (Node.js, etc.)' },
    distFile: { type: 'string', description: 'Expected .skill filename in dist/ (e.g. "my-skill.skill")' },
    suggestedTriggerExamples: { type: 'string', description: 'Trigger examples derived from description keywords, formatted as: "中文示例" / "English example"' },
    suggestedInstallCmd: { type: 'string', description: 'Suggested install command, e.g. "npx skills add author/repo -g" or "Download dist/xxx.skill"' },
    suggestedInstallName: { type: 'string', description: 'Suggested install directory name for ~/.claude/skills/ (may differ from source dir name)' },
  },
  required: ['name', 'title', 'shortDescription']
}

// ── Phase 1: Extract metadata ──
phase('Extract')

const skillDir = args?.skillDir
if (!skillDir) {
  log('ERROR: args.skillDir is required. Usage: workflow("sync-skill-readme", { skillDir: "my-skill/" })')
  throw new Error('Missing required arg: skillDir')
}

log(`Reading SKILL.md from ${skillDir}...`)

const extractedMeta = await agent(
  `Read the file "${skillDir}/SKILL.md" (relative to the repo root).

Extract the following structured data:

1. **name**: The "name" field from YAML frontmatter (between --- lines at the top).
2. **title**: The text of the first markdown H1 heading after the frontmatter block.
   Strip the leading "# " — just the title text. If the title contains "—" or ":", include the full thing.
3. **shortDescription**: The FIRST sentence or line of the description field (before any line break).
4. **fullDescription**: The COMPLETE description field text.
5. **hasWorkflow**: true if the skill body describes a multi-step pipeline/phase workflow.
6. **hasSubcommands**: true if the skill uses CLI subcommands.
7. **hasPrerequisites**: true if the skill lists prerequisites (Node.js version, tools, etc.).
8. **distFile**: The likely .skill filename in dist/. Usually "{name}.skill". Look at the name field.
9. **suggestedTriggerExamples**: Based on the description's trigger keywords and the skill's purpose, suggest 2-4 trigger examples in the format: "中文触发词" / "English trigger phrase". Look for phrases like "Trigger keywords:", "触发词:", "Try saying...", or derive from the description's keyword list.
10. **suggestedInstallCmd**: Based on the skill content, suggest an install command. If the skill references npx, use that. Otherwise default to: 'Download \`dist/XXX.skill\` and drag it into Claude Code.'
11. **suggestedInstallName**: The name used for the ~/.claude/skills/ directory. Usually same as "name" field, but some skills differ (e.g. source dir "tutor" -> install as "exam-tutor"). Check if the skill body or metadata mentions an install name.

IMPORTANT: Read the actual file content carefully. Return accurate data.`,
  { label: `extract:${skillDir}`, schema: SKILL_SCHEMA }
)

if (!extractedMeta) {
  log('ERROR: Failed to extract metadata from SKILL.md')
  throw new Error('Metadata extraction failed')
}

log(`Extracted: name="${extractedMeta.name}", title="${extractedMeta.title}"`)

// Merge args overrides with extracted metadata
const skill = {
  name: args.name || extractedMeta.name,
  title: args.title || extractedMeta.title,
  shortDescription: args.shortDescription || extractedMeta.shortDescription,
  fullDescription: extractedMeta.fullDescription || extractedMeta.shortDescription,
  triggerExamples: args.triggerExamples || extractedMeta.suggestedTriggerExamples || '',
  installName: args.installName || extractedMeta.suggestedInstallName || extractedMeta.name,
  installCmd: args.installCmd || extractedMeta.suggestedInstallCmd || `Download \`dist/${extractedMeta.distFile || extractedMeta.name + '.skill'}\` and drag it into Claude Code.`,
  distFile: extractedMeta.distFile || (extractedMeta.name + '.skill'),
  hasWorkflow: extractedMeta.hasWorkflow || false,
  hasSubcommands: extractedMeta.hasSubcommands || false,
  hasPrerequisites: extractedMeta.hasPrerequisites || false,
  skillDir: skillDir,
}

log(`Skill config: ${JSON.stringify(skill, null, 2)}`)

// ── Phase 2: Update README ──
phase('Update')

await agent(
  `You are updating the root README.md to add a new skill. Here is the skill data:

${JSON.stringify(skill, null, 2)}

## What to do

Read the root README.md, then make ALL of the following edits. Each edit is independent in a different section of the file:

### Edit 1: Installation (Method 2) — add cp command

Find the code block under "### Method 2: Manual copy" that contains lines like:
  \`\`\`bash
  mkdir -p ~/.claude/skills
  cp -r cc-dispatch ~/.claude/skills/cc-dispatch
  ...
  \`\`\`

Add this line in ALPHABETICAL order among the other cp commands:
  cp -r ${skill.skillDir.replace(/\/$/, '')} ~/.claude/skills/${skill.installName}

### Edit 2: Verification — add to ls output

Find the code block under "### Verification" that shows:
  \`\`\`bash
  ls ~/.claude/skills/
  # baoyu-skills/  cc-dispatch/  ...
  \`\`\`

Add "${skill.installName}/" in ALPHABETICAL order in the comment line showing all skill directories.

### Edit 3: Trigger examples table — add row

Find the table under "### Trigger examples". Add a new row in ALPHABETICAL order by skill name:
  | \`${skill.name}\` | "${skill.triggerExamples}" |

If triggerExamples is empty, use: "Try ${skill.name}"

### Edit 4: Skills section — add new skill entry

Find the "## Skills" section. Each skill starts with "### \`...\` --- ..." and ends with "---".
Add a new entry BEFORE the "## Adding Skills" section, in ALPHABETICAL order by skill name.

Use this template:

---
### \`${skill.name}\` — ${skill.title}

**Purpose**: ${skill.shortDescription}

${skill.hasWorkflow ? `**Workflow**:

\`\`\`
[describe the workflow steps based on the fullDescription]
\`\`\`
` : ''}
**Key features**:
[Derive 3-6 bullet points from the fullDescription. Focus on what makes this skill useful.]

**Install**: ${skill.installCmd}

---

## Important rules
- Use the EXACT skill name from the data above
- Keep alphabetical order in all sections
- Match the existing README style exactly (bold labels, em-dash separators, etc.)
- If you're unsure about alphabetical order, compare character by character
- Make minimal, precise edits using the Edit tool — don't rewrite the whole file
- After all edits, verify the file still reads correctly`,
  { label: 'update-readme' }
)

log('README.md updated in all 4 sections.')

// ── Phase 3: Verify consistency ──
phase('Verify')

const verifyResult = await agent(
  `Verify that the root README.md is consistent after adding skill "${skill.name}".

Check:
1. The skill appears in the Installation cp commands (alphabetical order)
2. The skill appears in the Verification ls output (alphabetical order)
3. The skill has a row in the Trigger examples table (alphabetical order)
4. The skill has a full entry in the Skills section (alphabetical order)
5. The name is consistent across all 4 sections
6. No duplicate entries exist

Report PASS/FAIL for each check. If any FAIL, note what's wrong.`,
  { label: 'verify-readme' }
)

log(`Verification result:\n${verifyResult}`)

return {
  skill,
  status: 'done',
  summary: `Added "${skill.name}" to README.md in all 4 sections (Installation, Verification, Trigger Table, Skills).`,
}
