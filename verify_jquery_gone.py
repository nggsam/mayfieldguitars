from playwright.sync_api import sync_playwright
import os

def test_homepage(page):
    # Navigate to the local file
    cwd = os.getcwd()
    page.goto(f"file://{cwd}/mayfieldguitars.com/output/index.html")

    # Check if jQuery is present
    # We can check window.jQuery
    is_jquery_present = page.evaluate("typeof window.jQuery !== 'undefined'")
    print(f"Is jQuery present? {is_jquery_present}")

    if is_jquery_present:
        raise Exception("jQuery should NOT be present!")

    # Check if Headroom is present and working (header should exist)
    header = page.locator('header')
    if header.count() == 0:
        raise Exception("Header not found!")

    # Check if our new script logic is working
    # We can't easily test the click because the navbar is hidden on desktop usually,
    # and in headless mode the viewport might be desktop size.
    # But we can verify the script loaded and ran by checking if the event listener is attached?
    # Hard to check event listeners in Playwright directly without firing event.

    # Let's try to set viewport to mobile
    page.set_viewport_size({"width": 375, "height": 812})

    # Find the toggle button
    btn = page.locator('#btn-toggle-nav')
    if btn.count() == 0:
        print("Button not found (maybe not visible or id wrong?)")
    else:
        print("Button found")
        # Click it
        btn.click()
        # Check if nav.navbar-collapse has class 'in'
        nav = page.locator('nav.navbar-collapse')
        if nav.count() > 0:
             # wait a bit for potential async (though ours is sync)
            page.wait_for_timeout(100)
            classes = nav.get_attribute('class')
            print(f"Nav classes after click: {classes}")
            if 'in' not in classes:
                raise Exception("Class 'in' not toggled on nav menu!")
        else:
            print("Nav menu not found")

    page.screenshot(path="/home/jules/verification/verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_homepage(page)
        finally:
            browser.close()
