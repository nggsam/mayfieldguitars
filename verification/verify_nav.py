import os
import re
from playwright.sync_api import sync_playwright, expect

def test_mobile_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        url = "file:///app/mayfieldguitars.com/output/index.html"
        print(f"Navigating to {url}")
        page.goto(url)

        # Check if toggle button is visible
        toggle_btn = page.locator("#btn-toggle-nav")
        expect(toggle_btn).to_be_visible()

        print("Clicking toggle button...")
        toggle_btn.click()

        # Check if navbar gets the class 'in'
        navbar = page.locator("nav.navbar-collapse")
        expect(navbar).to_have_class(re.compile(r"in"))

        # Wait a bit for transition
        page.wait_for_timeout(500)

        print("Taking screenshot...")
        os.makedirs("verification", exist_ok=True)
        page.screenshot(path="verification/nav_toggled.png")

        browser.close()

if __name__ == "__main__":
    test_mobile_nav()
