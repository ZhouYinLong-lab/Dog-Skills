/**
 * Stable error codes per RFC-01 + RFC-05.
 */

export type ErrorCode =
  | 'engine-not-installed'
  | 'engine-not-registered'
  | 'template-invalid'
  | 'template-not-found'
  | 'render-failed'
  | 'render-timeout'
  | 'output-corrupt'
  | 'disk-full'
  | 'cancelled'
  | 'asset-not-found'
  | 'project-not-found'
  | 'invalid-input';

export class HtmlVideoError extends Error {
  override readonly name = 'HtmlVideoError';
  constructor(
    public readonly code: ErrorCode,
    message: string,
    public readonly retryable = false,
    public readonly context: Record<string, unknown> = {},
  ) {
    super(message);
  }

  toJSON(): Record<string, unknown> {
    return {
      name: this.name,
      code: this.code,
      message: this.message,
      retryable: this.retryable,
      context: this.context,
    };
  }
}
