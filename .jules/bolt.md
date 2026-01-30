## 2025-01-30 - Unexpected Behavior of Less Compiler with URLs
**Learning:** `lessc` (standard npm version) treats `@import url(...)` as something to process/inline if it can resolve it, or at least it changed behavior here replacing imports with `@font-face` blocks when targeting Google Fonts. This broke the intended linking strategy.
**Action:** Always use `@import (css) url(...)` when importing remote CSS files in LESS to force the compiler to treat them as standard CSS imports and preserve them in the output.
