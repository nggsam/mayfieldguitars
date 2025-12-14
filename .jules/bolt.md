## 2025-02-17 - Google Fonts Performance Optimization
**Learning:** Using `@import` in CSS files to load Google Fonts blocks the browser from downloading fonts in parallel with the stylesheet, delaying text rendering.
**Action:** Always load Google Fonts using `<link>` tags in the HTML `<head>` with `preconnect` and `display=swap` to enable parallel downloading and avoid blocking.
