from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, url=None):
        self.url = url
        self.page = page

    def navigate(self, path: str = ""):
        full_url = f"{self.url}{path}"
        self.page.goto(full_url, timeout=30000, wait_until="domcontentloaded")
        return self

    def find_locator(self, selector, timeout=30000):
        locator = self.page.locator(selector)
        locator.wait_for(state="attached", timeout=timeout)
        return locator

    def click(self, selector, timeout=30000):
        self.page.locator(selector).click(timeout=timeout, force=True)
        return self

    def fill(self, selector, text, timeout=30000):
        self.page.fill(selector, text, timeout=timeout)
        return self

    def get_text(self, selector) -> str:
        return self.page.text_content(selector)

    def get_attribute(self, selector, attribute) -> str:
        return self.page.get_attribute(selector, attribute)

    def get_current_url(self) -> str:
        return self.page.url

    def get_title(self):
        return self.page.title()

    def hover_and_check(self, selector: str) -> None:
        """Наводим и проверяем что не падает"""
        element = self.page.locator(selector)
        element.hover()  # Если тут ошибка - тест упадет
        self.page.wait_for_timeout(100)