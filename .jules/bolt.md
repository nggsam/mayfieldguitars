## 2025-01-13 - Removing jQuery Dependency
**Learning:** Nikola bundle management configuration in `bundles` file is not the only place where dependencies are defined. Templates like `zzz_helper.tmpl` may manually inject scripts (especially for CDN fallbacks) that persist even if the file is removed from the bundle. When removing a core dependency like jQuery, it is critical to audit all templates for manual `<script>` tags to ensure complete removal.
**Action:** When removing dependencies in Nikola themes, always `grep` the template directory for the library name to catch manual injections.
