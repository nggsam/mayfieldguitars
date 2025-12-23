## 2024-05-23 - Removed jQuery for Vanilla JS
**Learning:** Legacy jQuery usage for simple UI interactions (like slideToggle) can be replaced with Vanilla JS and CSS transitions, significantly reducing bundle size.
**Action:** When auditing dependencies, check if "heavy" libraries like jQuery are only used for trivial tasks that modern CSS/JS can handle natively. In this case, we saved ~90KB by replacing `slideToggle` with a CSS `max-height` transition and a few lines of JS.
