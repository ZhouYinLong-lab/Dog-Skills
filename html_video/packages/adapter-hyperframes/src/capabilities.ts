import type { EngineCapabilities } from '@html-video/core';

/**
 * Static capability declaration for Hyperframes.
 * v0.1: hard-coded; v0.2 may detect upstream version and adjust.
 */
export const capabilities: EngineCapabilities = {
  paradigms: ['html-css-gsap'],
  outputFormats: ['mp4', 'webm', 'webm-alpha', 'png-sequence'],
  maxResolution: { width: 3840, height: 2160 },
  alpha: true,
  audio: 'multi',
  subtitles: ['burn-in', 'sidecar'],
  renderTarget: ['local-chromium', 'lambda'],
  licensing: 'free-osi',
  renderSpeedHint: {
    resolution: '1080p',
    durationSec: 10,
    fps: 60,
    estimatedRenderSec: 18,
  },
  bestFor: [
    'social-shorts',
    'product-marketing',
    'logo-reveal',
    'gsap-animations',
    'ken-burns',
    'text-card',
  ],
  weaknesses: ['no-react-ecosystem', 'limited-3d-without-three.js'],
};
