import os
import re
from playwright.sync_api import sync_playwright, expect

def verify_mobile_nav():
    output_dir = os.path.abspath("mayfieldguitars.com/output")
    index_path = f"file://{output_dir}/index.html"

    with sync_playwright() as p:
        # Use mobile viewport to trigger mobile layout
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        print(f"Navigating to {index_path}")
        page.goto(index_path)

        # Check initial state (collapsed)
        nav = page.locator("nav.collapse")

        print("Checking initial state...")
        # Should not have 'in' class
        classes = nav.get_attribute("class") or ""
        if "in" in classes.split():
            raise AssertionError(f"Expected nav NOT to have 'in' class initially, found: {classes}")

        # Take screenshot of collapsed state
        if not os.path.exists("/home/jules/verification"):
            os.makedirs("/home/jules/verification")
        page.screenshot(path="/home/jules/verification/nav_collapsed.png")

        # Click the toggle button
        print("Clicking toggle button...")
        toggle_btn = page.locator("#btn-toggle-nav")
        toggle_btn.click()

        # Wait for transition (approx 0.5s)
        page.wait_for_timeout(600)

        # Check expanded state
        print("Checking expanded state...")
        classes = nav.get_attribute("class") or ""
        print(f"Classes after toggle: {classes}")

        if "in" not in classes.split():
             raise AssertionError(f"Expected 'in' class after toggle, found: {classes}")

        # Take screenshot of expanded state
        page.screenshot(path="/home/jules/verification/nav_expanded.png")
        print("Verification complete. Screenshots saved.")

        browser.close()

if __name__ == "__main__":
    verify_mobile_nav()
