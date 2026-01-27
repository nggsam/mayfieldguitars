from playwright.sync_api import sync_playwright, expect
import re
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        try:
            page.goto("http://localhost:8001")

            # Click toggle
            print("Clicking toggle button...")
            page.click("#btn-toggle-nav")

            # Wait for transition (0.3s)
            page.wait_for_timeout(500)

            # Verify 'in' class
            nav = page.locator("nav.navbar-collapse")
            expect(nav).to_have_class(re.compile(r"in"))
            print("Nav has 'in' class.")

            # Take screenshot
            output_path = "/home/jules/verification/mobile_menu.png"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            page.screenshot(path=output_path)
            print(f"Screenshot saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")
            # Take screenshot on error
            os.makedirs("/home/jules/verification", exist_ok=True)
            page.screenshot(path="/home/jules/verification/error.png")
            raise e
        finally:
            browser.close()

if __name__ == "__main__":
    run()
