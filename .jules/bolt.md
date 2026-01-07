# Bolt's Journal

## 2024-05-22 - Asset Bundling
**Learning:** Nikola's asset bundling (`USE_BUNDLES`) is highly effective but requires careful configuration of bundle files. It's easy to miss including a file in the bundle, which can lead to it being loaded separately or not at all.
**Action:** Always verify bundle contents against the source files and the generated output.

## 2024-05-22 - External Assets
**Learning:** Relying on external CDNs (like for Google Fonts) can be a significant performance bottleneck due to blocking render.
**Action:** Self-hosting fonts or using `preconnect` and non-blocking loading strategies is crucial for FCP.

## 2024-05-22 - Image Optimization
**Learning:** Nikola has built-in support for image optimization via filters, but it requires external tools (like `jpegoptim`) to be installed in the environment.
**Action:** Check for available system tools before enabling filters in `conf.py`.
