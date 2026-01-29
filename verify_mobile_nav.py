from playwright.sync_api import sync_playwright
import os

# Path to the build output
output_dir = os.path.abspath("mayfieldguitars.com/output")
index_file = os.path.join(output_dir, "index.html")
file_url = f"file://{index_file}"

def verify_mobile_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        print(f"Navigating to {file_url}")
        page.goto(file_url)

        # Verify button exists
        btn = page.locator("#btn-toggle-nav")
        if not btn.is_visible():
            print("Toggle button not visible!")
            page.screenshot(path="verification_failure.png")
            browser.close()
            return

        print("Toggle button found.")

        # Initial state: menu should be hidden (max-height 0)
        nav = page.locator("nav.navbar-collapse")

        # Check if 'in' class is absent
        assert "in" not in nav.get_attribute("class").split()
        print("Menu is initially collapsed (no 'in' class).")

        # Click toggle
        btn.click()
        print("Clicked toggle.")

        # Check if 'in' class is present
        page.wait_for_timeout(600) # Wait for transition
        assert "in" in nav.get_attribute("class").split()
        print("Menu is expanded ('in' class added).")

        # Screenshot expanded
        page.screenshot(path="verification_expanded.png")

        # Click toggle again
        btn.click()
        print("Clicked toggle again.")

        # Check if 'in' class is absent
        page.wait_for_timeout(600) # Wait for transition
        assert "in" not in nav.get_attribute("class").split()
        print("Menu is collapsed again.")

        browser.close()

if __name__ == "__main__":
    verify_mobile_nav()
