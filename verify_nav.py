import os
from playwright.sync_api import sync_playwright

def verify_mobile_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        # Load the index page
        index_path = os.path.abspath("mayfieldguitars.com/output/index.html")
        page.goto(f"file://{index_path}")

        # 1. Take initial screenshot (menu collapsed)
        page.screenshot(path="/home/jules/verification/1_collapsed.png")

        # 2. Click the toggle button
        # The button has id 'btn-toggle-nav'
        page.locator("#btn-toggle-nav").click()

        # 3. Wait for the class 'in' to be added to nav.navbar-collapse
        # This confirms the JS logic works
        page.locator("nav.navbar-collapse").wait_for(state="visible")

        # Take screenshot of expanded menu
        page.screenshot(path="/home/jules/verification/2_expanded.png")

        # 4. Check that jQuery is not loaded
        # We can check window.$
        jquery_check = page.evaluate("typeof window.$")
        print(f"jQuery check: {jquery_check}")

        if jquery_check != "undefined":
            print("FAILURE: jQuery is still present!")
        else:
            print("SUCCESS: jQuery is undefined.")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("/home/jules/verification"):
        os.makedirs("/home/jules/verification")
    verify_mobile_nav()
