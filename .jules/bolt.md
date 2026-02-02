## 2025-02-02 - jQuery Removal
**Learning:** Removing jQuery from a legacy theme like 'bnw' is a massive win (~90KB saved). It requires carefully checking bundles, templates, and script files.
**Action:** Always check `bundles` files in Nikola themes and look for hardcoded script tags in `zzz_helper.tmpl` or `base_helper.tmpl`.
