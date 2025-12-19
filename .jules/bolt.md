# Bolt's Journal

## 2025-05-18 - [Static Site Generator Template Performance]
**Learning:** Even in static sites built with Python tools like Nikola, frontend performance patterns like font loading must be manually optimized in templates. Generated CSS files often contain blocking `@import` statements if the original LESS/SASS files were not optimized.
**Action:** Always check the source templates and stylesheet pre-processor files (LESS/SASS) for blocking imports, not just the output HTML.
