## 2025-12-28 - [Optimized Google Fonts Loading]
**Learning:** Nikola themes often use @import in CSS/LESS files for fonts, which blocks rendering. Moving these to HTML <link> tags with preconnect significantly improves performance.
**Action:** Always check theme CSS/LESS files for @import statements when optimizing Nikola sites.
