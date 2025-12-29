
## 2025-02-18 - Removed jQuery dependency
**Learning:** The project used jQuery (~90KB) solely for a simple toggle animation and document readiness check.
**Action:** Replaced with Vanilla JS (`classList.toggle`, `DOMContentLoaded`, `addEventListener`). This saved ~90KB of blocking JS and simplified the dependency chain. Always check usage before assuming a library is needed.
