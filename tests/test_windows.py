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