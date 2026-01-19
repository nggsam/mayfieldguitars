## 2024-05-22 - Nikola Theme Dependency Management
**Learning:** Removing a JS dependency in a Nikola theme requires updating `bundles` configuration AND checking templates (like `zzz_helper.tmpl`) for fallback script tags. Disabling CDN in `conf.py` does not automatically remove CDN links from templates if they are hardcoded in `use_cdn` blocks.
**Action:** Always grep for the library name in the `themes/` directory after removing it from `bundles`.
