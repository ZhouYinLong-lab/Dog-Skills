import type { AgentDef } from '../types.js';

/**
 * GitHub Copilot CLI def (`copilot`, by GitHub).
 *
 * This is the standalone agentic `copilot` binary (npm `@github/copilot`,
 * GA 2026-02), NOT the deprecated `gh copilot` gh-cli extension.
 *
 * Headless: `-p`/`--prompt` runs one prompt and exits; stdin is also accepted.
 * We pipe the prompt via stdin and pass `-p` with no value to force prompt
 * mode, plus `--allow-all-tools` so the agent doesn't stall waiting for a
 * tool-approval prompt during a non-interactive run. Default stdout carries
 * some session metadata; the studio extractor still finds the fenced
 * ```html``` block, so plain mode is fine. (If metadata ever pollutes output
 * we can add `-s`/silent — left off until confirmed against an installed bin.)
 */
export const copilot: AgentDef = {
  id: 'copilot',
  name: 'GitHub Copilot CLI',
  bin: 'copilot',
  versionArgs: ['--version'],
  buildArgs(_prompt, _ctx) {
    // Prompt via stdin; --allow-all-tools avoids interactive approval stalls.
    return ['--allow-all-tools'];
  },
  streamFormat: 'plain',
  promptViaStdin: true,
  installUrl: 'https://github.com/github/copilot-cli',
};
