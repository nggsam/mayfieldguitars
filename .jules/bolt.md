## 2025-01-27 - Removing jQuery from Nikola Themes
**Learning:** Nikola themes (like `bnw`) often hardcode jQuery dependencies in `bundles` AND template helpers (e.g., `zzz_helper.tmpl` logic for `late_load_js`). Removing it requires cleaning up both the bundle config and the conditional loading logic in templates to avoid accidental re-inclusion or broken fallbacks.
**Action:** When removing a library, grep for all occurrences in `themes/` and check `bundles` files explicitly.
