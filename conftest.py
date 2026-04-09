from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:

        browser = playwright.firefox.launch(
            headless=False,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        yield browser

        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )

    yield context

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    yield page