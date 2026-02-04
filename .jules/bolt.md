## 2025-02-04 - Removing jQuery from Nikola Themes
**Learning:** Nikola themes often bundle assets (defined in a `bundles` file) and have fallback loading logic in templates (like `zzz_helper.tmpl`) that checks for `use_bundles` and `use_cdn`. Removing a library like jQuery requires updating all three: the source file removal, the bundle definition, and the template logic.
**Action:** When removing dependencies in Nikola, grep for the library name in `templates/` and `bundles` files, not just the asset directory.

## 2025-02-04 - CSS Transitions for "slidToggle" replacement
**Learning:** Replacing jQuery's `slideToggle` with Vanilla JS requires CSS transitions. Since `height: auto` cannot be transitioned, `max-height` is a robust alternative. To match accessibility of `display: none`, `visibility: hidden` should be used. The transition for visibility needs a delay on the "collapse" action to ensure the element remains visible while the height animates down.
**Action:** Use `transition: max-height 0.5s ease, visibility 0s 0.5s;` for the collapsing state and `visibility 0s` for the expanding state.
