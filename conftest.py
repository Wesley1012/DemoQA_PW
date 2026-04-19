from playwright.sync_api import sync_playwright, Page
import datetime, os
import pytest


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:

        browser = playwright.firefox.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        yield browser

        browser.close()
        playwright.stop()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True,
        extra_http_headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0", #Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )

    yield context

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    yield page

os.makedirs("screenshots", exist_ok=True)


@pytest.fixture
def auto_screenshot(page: Page, request):
    yield page

    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

        try:
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"\nСкриншот падения: {screenshot_path}")
        except Exception as e:
            print(f"\nНе удалось создать скриншот: {e}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
