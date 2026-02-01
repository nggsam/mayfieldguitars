## 2025-02-01 - jQuery Removal and CSS Transitions
**Learning:** The 'bnw' theme in this project requires manual compilation of LESS files (`lessc bnw.less bnw-generated.css`). This step is not automated in the Nikola build process and requires `less` to be installed (`npm install -g less`).
**Action:** Always check for source files (LESS/SASS) and compilation instructions when modifying theme styles. If `less` is missing, install it.

**Learning:** Asset bundles defined in `themes/bnw/bundles` can persist old dependencies (like jQuery) even if the memory/instructions suggest they are removed.
**Action:** Verify bundle contents by reading the `bundles` file and the generated output to ensure dependencies are truly removed.

**Learning:** Replacing jQuery `slideToggle` with CSS transitions and Vanilla JS class toggling is a viable pattern for this project, improving performance by removing a large dependency (~90KB).
**Action:** Prefer CSS transitions for simple UI animations over JS libraries.
