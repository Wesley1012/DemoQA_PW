import pytest
from pages.windows_page import WindowsPage
import allure
import random
from faker import Faker

class TestWindows:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = WindowsPage(page)
        self.page.navigate('browser-windows')

    @allure.title("Открытие новой вкладки")
    def test_new_tab(self):
        new_page = self.page.click_new_tab()
        assert new_page.url == "https://demoqa.com/sample"

    def test_new_window(self):
        pass

    def test_new_window_message(self):
        pass