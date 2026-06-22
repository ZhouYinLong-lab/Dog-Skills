/**
 * Generate NanE opening + ending videos.
 * Usage: node generate-nane-videos.js
 */

import { mkdtemp, mkdir, writeFile, cp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { existsSync } from 'node:fs';
import { bootstrap } from './packages/cli/dist/context.js';

const log = (msg) => process.stdout.write(`▸ ${msg}\n`);
const ok = (msg) => process.stdout.write(`  ✓ ${msg}\n`);

const OUTPUT_DIR = resolve(process.argv[2] || 'D:/Projects/html_video/output');
const LOGO_PATH = 'D:/Projects/NanE/assets/brand/logo.png';

// ─── Opening HTML: Matches ending background, with logo ───
function openingHtml(logoDataUri) {
  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<title>南易 · 开场</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Inter Tight', 'Noto Sans SC', system-ui, -apple-system, sans-serif;
    background: radial-gradient(circle at 50% 45%, #1a1530 0%, #08090c 70%);
    width: 1920px; height: 1080px;
    overflow: hidden;
    display: flex; align-items: center; justify-content: center;
  }

  /* Top ribbon */
  .ribbon {
    position: absolute; top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #6E0065, #b87cb5, #6E0065);
  }

  /* Subtle grain overlay */
  .grain {
    position: absolute; inset: 0;
    opacity: 0.04;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    background-size: 256px 256px;
    pointer-events: none;
  }

  /* Content */
  .content {
    position: relative; z-index: 2;
    text-align: center;
    display: flex; flex-direction: column; align-items: center;
    gap: 28px;
  }

  /* Logo */
  .logo-wrap {
    animation: logoIn 1s cubic-bezier(0.34,1.56,0.64,1) 0.3s both;
    filter: drop-shadow(0 0 40px rgba(110,0,101,0.5));
  }
  .logo-wrap img {
    width: 160px; height: 160px;
    object-fit: contain;
    border-radius: 28px;
  }

  @keyframes logoIn {
    0% { opacity: 0; transform: scale(1.3); }
    100% { opacity: 1; transform: scale(1); }
  }

  /* Label */
  .label {
    font-size: 20px; font-weight: 500;
    letter-spacing: 0.28em; text-transform: uppercase;
    color: rgba(245,243,237,0.55);
    animation: fadeUp 1s cubic-bezier(0.22,0.61,0.36,1) 0.1s both;
  }

  .headline {
    font-size: 150px; font-weight: 900;
    letter-spacing: -0.03em; line-height: 1.05;
    color: #f5f5f7;
    animation: fadeUp 1s cubic-bezier(0.22,0.61,0.36,1) 0.6s both;
    text-shadow: 0 0 80px rgba(184,124,181,0.35);
  }
  .headline .accent {
    color: #b87cb5;
  }

  .subheadline {
    font-size: 40px; font-weight: 400;
    color: rgba(245,243,237,0.65);
    letter-spacing: 0.04em;
    animation: fadeUp 1s cubic-bezier(0.22,0.61,0.36,1) 0.9s both;
  }

  .divider {
    width: 100px; height: 2px;
    background: linear-gradient(90deg, transparent, #6E0065, transparent);
    margin: 4px 0;
    animation: fadeUp 1s cubic-bezier(0.22,0.61,0.36,1) 1.1s both;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(50px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* Bottom bar */
  .bottom-bar {
    position: absolute; bottom: 48px; left: 0; right: 0;
    display: flex; justify-content: center; gap: 36px;
    font-size: 15px; font-weight: 400;
    letter-spacing: 0.14em;
    color: rgba(245,243,237,0.3);
    animation: fadeUp 1s cubic-bezier(0.22,0.61,0.36,1) 1.5s both;
  }
  .bottom-bar span { position: relative; }
  .bottom-bar span + span::before {
    content: '·'; position: absolute; left: -20px;
    color: rgba(245,243,237,0.2);
  }
</style>
</head>
<body>
  <div class="ribbon"></div>
  <div class="grain"></div>

  <div class="content">
    <div class="logo-wrap">
      <img src="${logoDataUri}" alt="南易 Logo" />
    </div>
    <div class="label">南京大学 · 校园互助平台</div>
    <h1 class="headline"><span class="accent">南</span>易</h1>
    <p class="subheadline">让闲置物资在楼栋间流动</p>
    <div class="divider"></div>
  </div>

  <div class="bottom-bar">
    <span>nane.zylatent.com</span>
    <span>免费互助</span>
    <span>赠人玫瑰，手有余香</span>
    <span>2026</span>
  </div>
</body>
</html>`;
}

// ─── Ending HTML: Logo outro with stable final frame ───
function endingHtml(logoDataUri) {
  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<title>南易 · 结尾</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Inter Tight', 'Noto Sans SC', system-ui, -apple-system, sans-serif;
    background: radial-gradient(circle at 50% 45%, #1a1530 0%, #08090c 70%);
    color: #f5f5f7;
    width: 1920px; height: 1080px;
    overflow: hidden;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
  }

  /* Top ribbon */
  .ribbon {
    position: absolute; top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #6E0065, #b87cb5, #6E0065);
  }

  /* Logo — larger, with animated entrance + glow */
  .logo-wrap {
    animation: logoIn 1s cubic-bezier(0.34,1.56,0.64,1) 0s both;
    filter: drop-shadow(0 0 40px rgba(110,0,101,0.5));
  }
  .logo-wrap img {
    width: 190px; height: 190px;
    object-fit: contain;
    border-radius: 28px;
  }

  @keyframes logoIn {
    0%   { opacity: 0; transform: scale(1.35); filter: drop-shadow(0 0 0 transparent); }
    60%  { filter: drop-shadow(0 0 70px rgba(110,0,101,0.7)); }
    100% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 36px rgba(110,0,101,0.45)); }
  }

  /* Brand name — solid color, no transparent-text trick; glow settles */
  .brand {
    margin-top: 52px;
    font-size: 120px; font-weight: 900;
    letter-spacing: -0.02em; line-height: 0.95;
    color: #f5f5f7;
    animation: brandIn 1.3s ease-out 0.8s both;
  }

  @keyframes brandIn {
    0%   { opacity: 0; transform: translateY(24px); text-shadow: 0 0 120px rgba(184,124,181,0.9); }
    55%  { text-shadow: 0 0 120px rgba(184,124,181,0.8); }
    100% { opacity: 1; transform: translateY(0); text-shadow: 0 0 28px rgba(184,124,181,0.25); }
  }

  /* Tagline */
  .tagline {
    margin-top: 18px;
    font-size: 34px; font-weight: 400;
    opacity: 0;
    animation: fadeUp 0.8s ease-out 1.4s forwards;
    color: #b87cb5;
  }

  /* Meta bar */
  .meta {
    margin-top: 52px;
    display: flex; align-items: center; gap: 28px;
    font-size: 14px; font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    opacity: 0;
    animation: fadeUp 0.6s ease-out 1.8s forwards;
    color: rgba(245,245,247,0.45);
  }
  .meta .dot { opacity: 0.4; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>
  <div class="ribbon"></div>

  <div class="logo-wrap">
    <img src="${logoDataUri}" alt="南易 Logo" />
  </div>

  <h1 class="brand">南易</h1>

  <p class="tagline">赠人玫瑰，手有余香</p>

  <div class="meta">
    <span>nane.zylatent.com</span>
    <span class="dot">·</span>
    <span>南大校园 · 免费互助</span>
    <span class="dot">·</span>
    <span>© 2026 南易</span>
  </div>
</body>
</html>`;
}

async function main() {
  const projectRoot = await mkdtemp(join(tmpdir(), 'hv-nane-'));
  await mkdir(join(projectRoot, '.html-video'), { recursive: true });
  log(`workdir: ${projectRoot}`);

  const monorepoRoot = resolve(import.meta.url.replace(/^file:\/\//, ''), '..');
  // Actually, use the current directory as monorepo root
  const actualRoot = 'D:/Projects/html_video';

  log('bootstrap context');
  const ctx = await bootstrap({ cwd: projectRoot });
  if (ctx.templates.list().length === 0) {
    await ctx.templates.scan(join(actualRoot, 'templates'));
  }
  ok(`engines: ${ctx.engines.list().map((e) => e.id).join(', ')}`);
  ok(`templates: ${ctx.templates.list().length} loaded`);

  // ─── Read logo once, convert to base64 data URI (file:// URLs blocked in headless Chromium) ───
  const { readFile: readLogo } = await import('node:fs/promises');
  const logoBuffer = await readLogo(LOGO_PATH);
  const logoDataUri = `data:image/png;base64,${logoBuffer.toString('base64')}`;
  ok(`logo encoded: ${(logoBuffer.length / 1024).toFixed(1)}KB → ${(logoDataUri.length / 1024).toFixed(1)}KB data URI`);

  // ─── 1. Opening video ───
  log('─── Generating OPENING video ───');

  const projOpen = await ctx.orchestrator.create({
    name: 'NanE Opening',
    intent: 'Opening hero video for NanE campus mutual-aid platform',
    preferences: { aspect: '16:9', resolution: { width: 1920, height: 1080 }, fps: 60 },
  });
  ok(`project: ${projOpen.id}`);

  // Set the template to get the engine
  let p = await ctx.orchestrator.setTemplate(projOpen.id, 'frame-liquid-bg-hero');
  ok(`template: ${p.templateId} engine: hyperframes`);

  // Write content graph with one node
  await ctx.orchestrator.writeContentGraph(projOpen.id, {
    schemaVersion: 1,
    intent: 'hero',
    synopsis: 'NanE platform opening hero',
    nodes: [{ id: 'opening', kind: 'text', text: '南易', durationSec: 6 }],
    edges: [],
  });
  ok('content-graph written');

  // Write the custom frame HTML (with logo)
  const openHtml = openingHtml(logoDataUri);
  await ctx.orchestrator.writeFrameHtml(projOpen.id, 'opening', openHtml);
  ok('frame HTML written');

  // Export MP4
  log('exporting MP4 (opening)...');
  const { outputPath: openPath } = await ctx.orchestrator.exportMp4({
    projectId: projOpen.id,
    onProgress: (pct, stage) => {
      if (pct === 0 || pct % 25 === 0) ok(`render ${stage} ${Math.round(pct)}%`);
    },
  });
  ok(`opening MP4: ${openPath}`);

  // ─── 2. Ending video ───
  log('─── Generating ENDING video ───');

  const projEnd = await ctx.orchestrator.create({
    name: 'NanE Ending',
    intent: 'Ending outro video for NanE campus mutual-aid platform',
    preferences: { aspect: '16:9', resolution: { width: 1920, height: 1080 }, fps: 60 },
  });
  ok(`project: ${projEnd.id}`);

  p = await ctx.orchestrator.setTemplate(projEnd.id, 'frame-logo-outro');
  ok(`template: ${p.templateId} engine: hyperframes`);

  await ctx.orchestrator.writeContentGraph(projEnd.id, {
    schemaVersion: 1,
    intent: 'outro',
    synopsis: 'NanE platform logo outro',
    nodes: [{ id: 'outro', kind: 'entity', props: { logo: 'nane' }, durationSec: 5 }],
    edges: [],
  });
  ok('content-graph written');

  const endHtml = endingHtml(logoDataUri);
  await ctx.orchestrator.writeFrameHtml(projEnd.id, 'outro', endHtml);
  ok('frame HTML written');

  // Export MP4
  log('exporting MP4 (ending)...');
  const { outputPath: endPath } = await ctx.orchestrator.exportMp4({
    projectId: projEnd.id,
    onProgress: (pct, stage) => {
      if (pct === 0 || pct % 25 === 0) ok(`render ${stage} ${Math.round(pct)}%`);
    },
  });
  ok(`ending MP4: ${endPath}`);

  // ─── Copy to output directory ───
  await mkdir(OUTPUT_DIR, { recursive: true });
  const finalOpen = join(OUTPUT_DIR, 'nane-opening.mp4');
  const finalEnd = join(OUTPUT_DIR, 'nane-ending.mp4');
  await cp(openPath, finalOpen);
  await cp(endPath, finalEnd);

  log('');
  log('✅ Both videos generated successfully!');
  log(`   Opening: ${finalOpen}`);
  log(`   Ending:  ${finalEnd}`);
}

main().catch((err) => {
  process.stderr.write(`\n❌ Failed: ${err.message ?? err}\n`);
  if (err.stack) process.stderr.write(err.stack + '\n');
  process.exit(1);
});
