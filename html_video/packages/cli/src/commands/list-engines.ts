import type { CliContext } from '../context.js';
import { ok } from '../output.js';

export async function listEngines(ctx: CliContext): Promise<void> {
  const engines = ctx.engines.list().map((a) => ({
    id: a.id,
    name: a.name,
    upstream_version: a.upstreamVersion,
    capabilities: a.capabilities,
  }));
  ok({ engines });
}
