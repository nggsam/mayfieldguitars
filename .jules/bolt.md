## 2025-01-24 - LESS Import Inlining
**Learning:** `lessc` by default inlines content from `@import url(...)`, even from remote URLs, which can lead to unintentional hardcoding of assets (like Google Fonts) and bloated CSS.
**Action:** Always use `@import (css) url(...)` in LESS files when referencing external CSS that should remain as an import statement, and verify the generated CSS output.
