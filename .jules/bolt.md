# Bolt's Journal

## 2024-05-22 - [Optimizing Nikola Theme Assets]
**Learning:** Nikola themes often rely on jQuery for simple interactions (like mobile nav toggles). In the `bnw` theme, jQuery is bundled (`assets/js/all-nocdn.js`) but only used for `slideToggle`. Replacing this with Vanilla JS and CSS transitions can save ~30KB (minified/gzipped) and remove a dependency.
**Action:** Always check bundled scripts for "heavy" libraries used for trivial tasks. Verify CSS transition capabilities in LESS files before refactoring JS animations.

## 2024-05-22 - [LESS Compilation & Font Inlining]
**Learning:** `lessc` by default might inline `@import url(...)` as content if it resolves to a resource, especially with tilde `~` or if treated as a LESS import. This can lead to inlining 400KB+ of TTF fonts if compiling locally without careful import handling.
**Action:** Use `@import (css) url(...)` to force `lessc` to treat imports as standard CSS imports (keeping them as `@import` rules in the output) instead of inlining them.
