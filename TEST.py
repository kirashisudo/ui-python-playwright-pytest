from playwright.sync_api import sync_playwright


def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        context = browser.new_context(viewport={"width": 910, "height": 1080})
        page = context.new_page()
        page.goto("https://playwright.dev")
        page.pause()
        print(page.title())
        browser.close()
