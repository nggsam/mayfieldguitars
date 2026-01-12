from playwright.sync_api import sync_playwright
import os

def test_mobile_nav_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Emulate a mobile device to ensure the toggle button is visible
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()

        # Load the local index.html
        cwd = os.getcwd()
        url = f"file://{cwd}/mayfieldguitars.com/output/index.html"
        print(f"Loading {url}")
        page.goto(url)

        # Wait for script to be ready (DOMContentLoaded is handled by browser, but we can wait a bit)
        page.wait_for_load_state("networkidle")

        # Locate the toggle button
        toggle_btn = page.locator("#btn-toggle-nav")

        # Check if button is visible (it should be on mobile)
        if not toggle_btn.is_visible():
            print("Toggle button not visible. Trying to force display block for verification or check CSS.")
            # It might be hidden by CSS if viewport emulation didn't trigger media query correctly or if CSS isn't loading.
            # But we set viewport to 375px.

        # Take screenshot before click
        page.screenshot(path="/home/jules/verification/before_toggle.png")

        # Click the toggle
        print("Clicking toggle button...")
        toggle_btn.click()

        # Wait for class toggle. Since we removed animation, it should be instant.
        # Check if 'in' class is added to nav.navbar-collapse
        nav_collapse = page.locator("nav.navbar-collapse")

        # Verify class 'in' is present
        # We can wait for it
        try:
            nav_collapse.wait_for(state="visible", timeout=2000) # It should become visible because of .in class
            # Or explicitly check class
            classes = nav_collapse.get_attribute("class")
            print(f"Nav classes after click: {classes}")

            if "in" in classes.split():
                print("SUCCESS: 'in' class added.")
            else:
                print("FAILURE: 'in' class NOT added.")

        except Exception as e:
            print(f"Error waiting for nav visible: {e}")

        # Take screenshot after click
        page.screenshot(path="/home/jules/verification/after_toggle.png")

        browser.close()

if __name__ == "__main__":
    try:
        os.makedirs("/home/jules/verification", exist_ok=True)
        test_mobile_nav_toggle()
    except Exception as e:
        print(f"Test failed: {e}")
