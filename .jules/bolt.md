## 2025-01-28 - Nikola Theme Asset Bundling
**Learning:** Nikola themes (like `bnw`) can include heavy dependencies like jQuery in their `bundles` configuration file (`themes/bnw/bundles`) and fallback conditionals in templates (`zzz_helper.tmpl`), even if the site config (`conf.py`) disables CDNs.
**Action:** When optimizing Nikola sites, always check the theme's `bundles` file and helper templates for hidden dependencies, not just the site configuration.
