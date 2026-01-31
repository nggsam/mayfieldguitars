## 2025-01-31 - [Nikola Bundle Logic]
**Learning:** Nikola's `USE_BUNDLES` and `USE_CDN` logic in templates can be tricky. When `USE_CDN=False`, it uses `all-nocdn.js`. Removing a library (like jQuery) requires updating both the `bundles` file AND the template (`zzz_helper.tmpl`) to remove fallback or explicit loading logic.
**Action:** When removing dependencies in Nikola, always `grep` the templates for manual inclusions and check the `bundles` file. Verify the final build output (`output/index.html`) to ensure the script is truly gone.
