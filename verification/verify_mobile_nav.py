import re
from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        file_path = "file:///app/mayfieldguitars.com/output/index.html"
        print(f"Loading {file_path}")
        page.goto(file_path)

        toggle_btn = page.locator('#btn-toggle-nav')
        expect(toggle_btn).to_be_visible()

        nav_collapse = page.locator('nav.navbar-collapse')

        # Click
        print("Clicking toggle...")
        toggle_btn.click()

        # Wait
        page.wait_for_timeout(1000)

        # Verify 'in' class
        class_attr = nav_collapse.get_attribute("class")
        print(f"Class attribute: {class_attr}")
        if "in" not in class_attr.split():
             raise Exception("Class 'in' not found after toggle")

        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/mobile_nav_open.png")
        print("Screenshot saved.")
        browser.close()

if __name__ == "__main__":
    run()
