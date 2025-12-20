## 2024-05-23 - Static Asset Compression
**Learning:** Enabling `GZIP_FILES` in Nikola significantly reduces asset size (~72% reduction for CSS, ~62% for JS).
**Action:** Always enable `GZIP_FILES` for static sites to leverage `gzip_static` in web servers (Nginx/Apache), saving CPU and reducing latency.
