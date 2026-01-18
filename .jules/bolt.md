## 2024-05-21 - Removing jQuery from Legacy Themes
**Learning:** Legacy themes often bundle jQuery for simple interactions like navbar toggles. Replacing these with Vanilla JS can save ~90KB of bundle size.
**Action:** Always check `bundles` and `scripts.js` for "low hanging fruit" library removals.
