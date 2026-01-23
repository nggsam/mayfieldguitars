## 2025-01-23 - [Template Logic Anti-pattern]
**Learning:** The theme's `zzz_helper.tmpl` had broken logic for `use_cdn`, where enabling CDN would result in `scripts.js` (core logic) NOT being loaded at all.
**Action:** When auditing dependencies in Nikola templates, always check all conditional branches (`if/else`) to ensure core application scripts are included in every valid configuration, not just the default one.
