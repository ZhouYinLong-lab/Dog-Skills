import type { AgentDef } from '../types.js';

export const cursorAgent: AgentDef = {
  id: 'cursor-agent',
  name: 'Cursor Agent',
  bin: 'cursor-agent',
  versionArgs: ['--version'],
  buildArgs(_prompt, _ctx) {
    return ['--print'];
  },
  streamFormat: 'plain',
  promptViaStdin: true,
  installUrl: 'https://cursor.com/cli',
};
