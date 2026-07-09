// Bundle entry point — passed to @remotion/bundler bundle(). registerRoot wires
// the bridge composition into Remotion. (RFC-08 §5)
import { registerRoot } from 'remotion';
import { RemotionRoot } from './Root';

registerRoot(RemotionRoot);
