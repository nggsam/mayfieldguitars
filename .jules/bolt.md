## 2025-01-21 - [Generated Asset Consistency]
**Learning:** Manually editing generated assets (like `bnw-generated.css`) is a maintenance trap. Changes are lost when the source (`bnw.less`) is recompiled.
**Action:** Always modify the source file (LESS/SASS) and recompile. If the build pipeline is manual, ensure the compilation step is part of the verification process.

## 2025-01-21 - [Hardcoded Asset URLs]
**Learning:** Hardcoding external asset URLs (like Google Fonts TTF files) bypasses content negotiation and creates version coupling.
**Action:** Use the official API (e.g., Google Fonts CSS link) which handles format negotiation (WOFF2 vs TTF) and caching correctly.

## 2025-01-21 - [jQuery Removal Strategy]
**Learning:** Removing a library like jQuery from a Nikola theme requires checking multiple places:
1. `scripts.js` (refactor code)
2. `bundles` (remove from bundle definition)
3. `templates` (remove CDN fallbacks and script tags)
4. The actual file system (delete the file)
**Action:** Use `grep` to ensure no stray references remain in templates.
