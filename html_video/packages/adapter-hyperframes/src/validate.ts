import { existsSync } from 'node:fs';
import type { TemplateRef, ValidationError, ValidationResult } from '@html-video/core';
import { capabilities } from './capabilities.js';

/**
 * Validate a template against the Hyperframes adapter capabilities.
 * Cheap & read-only per RFC-01.
 */
export function validate(template: TemplateRef): ValidationResult {
  const errors: ValidationError[] = [];
  const warnings: ValidationError[] = [];

  if (template.engine !== 'hyperframes') {
    errors.push({
      code: 'engine-mismatch',
      message: `Template engine "${template.engine}" is not "hyperframes"`,
      fix: `Use the @html-video/adapter-${template.engine} adapter instead`,
    });
    return { ok: false, errors, warnings };
  }

  if (!template.sourcePath) {
    errors.push({
      code: 'missing-source',
      message: 'Template has no sourcePath',
    });
  } else if (!existsSync(template.sourcePath)) {
    errors.push({
      code: 'source-not-found',
      message: `Template source not found: ${template.sourcePath}`,
      fix: 'Check that the template directory contains the file declared in source_entry',
    });
  }

  // Sanity: max resolution from caps
  const cap = capabilities;
  if (cap.maxResolution.width < 1920) {
    warnings.push({
      code: 'low-max-resolution',
      message: `Adapter max resolution is ${cap.maxResolution.width}x${cap.maxResolution.height}`,
    });
  }

  return {
    ok: errors.length === 0,
    errors,
    warnings,
  };
}
