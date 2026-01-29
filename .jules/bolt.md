## 2025-02-12 - Replicating slideToggle with CSS
**Learning:** When replacing jQuery's `slideToggle` with CSS transitions (using `max-height`), simply setting `max-height: 0` leaves the element in the accessibility tree and focusable.
**Action:** Always pair `max-height: 0` with `visibility: hidden` (and transition `visibility`) to ensure collapsed content is properly hidden from screen readers and tab order.

## 2025-02-12 - LESS Compiler Behavior
**Learning:** `lessc` may inline remote CSS imports (like Google Fonts) into `@font-face` definitions. This improves performance by reducing requests but hardcodes the font URLs, making them brittle to upstream changes.
**Action:** Be aware that compiling LESS might produce "hardcoded" assets in the output CSS. If this is undesirable, manage imports in HTML or configure LESS differently.
