import os
from playwright.sync_api import sync_playwright

def test_navbar_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index page
        # Assuming the build output is in mayfieldguitars.com/output/index.html
        cwd = os.getcwd()
        url = f"file://{cwd}/mayfieldguitars.com/output/index.html"
        print(f"Loading {url}")
        page.goto(url)

        # Set viewport to mobile size to show the toggle button
        page.set_viewport_size({"width": 375, "height": 667})

        # Check initial state
        nav_collapse = page.locator("nav.navbar-collapse")
        # Initially it should be hidden (display: none via CSS for .collapse without .in)
        # Note: Playwright's to_be_visible checks if it takes up space.
        # If display: none, it is not visible.

        # Get the toggle button
        toggle_btn = page.locator("#btn-toggle-nav")

        # Screenshot before click
        page.screenshot(path="before_click.png")

        # Click the toggle button
        toggle_btn.click()

        # Wait for potential class change
        page.wait_for_timeout(500) # Wait a bit for JS execution

        # Screenshot after click
        page.screenshot(path="after_click.png")

        # Check if class 'in' is added
        class_attr = nav_collapse.get_attribute("class")
        print(f"Class attribute after click: {class_attr}")

        if "in" in class_attr:
            print("SUCCESS: 'in' class added to nav.")
        else:
            print("FAILURE: 'in' class NOT added to nav.")

        browser.close()

if __name__ == "__main__":
    test_navbar_toggle()
