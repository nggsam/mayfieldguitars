## 2025-01-26 - jQuery Removal
**Learning:** The project had a massive (~90KB) dependency on jQuery solely for a simple navbar toggle animation. The memory indicated it was already removed, but the codebase proved otherwise.
**Action:** Replaced the jQuery toggle with a simple Vanilla JS class toggle. The "slide" animation was sacrificed for a ~90KB size reduction, which is a worthwhile trade-off for performance. When optimizing, always verify if "heavy" dependencies are actually pulling their weight.
