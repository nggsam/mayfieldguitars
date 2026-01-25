## 2025-01-25 - jQuery Removal & LESS Compilation
**Learning:** The `bnw` theme relies on manual LESS compilation using `lessc`, not automated by Nikola. Changes to `.less` files require manual compilation to `.css` artifacts.
**Action:** Always install `less` and run `lessc` after modifying LESS files.

**Learning:** `zzz_helper.tmpl` had a logic bug where `use_cdn` + `use_bundles` excluded theme scripts.
**Action:** When refactoring template logic, check all conditional branches (CDN vs local) to ensure scripts are loaded correctly in all configurations.
