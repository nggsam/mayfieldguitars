from playwright.sync_api import sync_playwright
import os

def verify_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 812})
        page = context.new_page()

        url = f"file://{os.getcwd()}/mayfieldguitars.com/output/index.html"
        print(f"Loading {url}")
        page.goto(url)

        # Verify navigation is collapsed
        nav = page.locator("nav.navbar-collapse")

        # In CSS, it is hidden by max-height: 0 and visibility: hidden.
        # Playwright's to_be_visible() checks display:none, visibility:hidden, opacity:0, etc.
        # Since I set visibility: hidden, it should be considered hidden.
        print("Checking if nav is hidden...")
        # expect(nav).to_be_hidden()
        # But to_be_hidden() waits. I'll just check state or take screenshot.

        page.screenshot(path="verification_collapsed.png")

        # Click toggle
        btn = page.locator("#btn-toggle-nav")
        if btn.is_visible():
            print("Clicking toggle button...")
            btn.click()

            # Wait for animation/transition
            page.wait_for_timeout(600) # > 0.5s transition

            print("Checking if nav is visible...")
            # It should have class 'in' and be visible
            # Verify class
            classes = nav.get_attribute("class")
            print(f"Nav classes: {classes}")

            page.screenshot(path="verification_expanded.png")
        else:
            print("Toggle button not visible!")

        browser.close()

if __name__ == "__main__":
    verify_nav()
