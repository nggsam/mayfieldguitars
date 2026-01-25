import os
from playwright.sync_api import sync_playwright

def verify_toggle():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/mayfieldguitars.com/output/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Check initial state (should be collapsed)
        nav = page.locator("nav.navbar-collapse")
        # Class check
        classes = nav.get_attribute("class")
        print(f"Initial classes: {classes}")

        # Click toggle
        btn = page.locator("#btn-toggle-nav")
        btn.click()

        # Wait for transition
        page.wait_for_timeout(600)

        # Check new state
        classes_after = nav.get_attribute("class")
        print(f"Classes after click: {classes_after}")

        # Screenshot
        page.screenshot(path="verification_toggle.png")

        browser.close()

if __name__ == "__main__":
    verify_toggle()
