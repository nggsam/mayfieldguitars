## 2026-01-11 - Removing jQuery from Nikola Theme
**Learning:** Nikola themes often define asset bundles in a `bundles` file and have fallback script tags in templates (e.g., `zzz_helper.tmpl`). Removing a dependency requires updating the bundle definition, the template fallbacks, and the actual asset files.
**Action:** Always grep for the dependency name in `bundles` and `templates` before assuming it's gone.
