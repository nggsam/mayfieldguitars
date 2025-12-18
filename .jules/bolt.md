## 2024-05-23 - Static Site Font Loading
**Learning:** In Nikola static sites with asset bundling enabled (`USE_BUNDLES = True`), modifying CSS files (`bnw-generated.css`, `style.css`) directly is effective, but these changes are often shadowed by LESS source files if a compilation step exists. Always update both the generated CSS and the source LESS files (e.g., `bnw.less`) to ensure consistency and future-proofing.
**Action:** When optimizing CSS in this project, check for corresponding `.less` files in `themes/bnw/less/` and apply changes there as well.
