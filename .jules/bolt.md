## 2025-02-03 - Removed jQuery from static site
**Learning:** Legacy themes often bundle jQuery for trivial tasks like a navbar toggle. Removing it can save ~90KB (~30KB gzipped) with minimal effort by refactoring to Vanilla JS and CSS transitions.
**Action:** Always audit bundled assets in static site themes. Check `bundles` files and template helpers for "default" libraries that aren't actually needed.
