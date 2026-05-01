import pytest
from pages.form_page import FormsPage
import allure

class TestForms:
    @pytest.fixture(autouse=True)
    def setup_method(self, page, auto_screenshot):
        self.page = FormsPage(page)
        self.page.navigate('automation-practice-form')

    def test_number(self):
        self.page.fill_number("4444444444")
        assert self.page.get_number() == "4444444444"

    def test_date(self):
        self.page.fill_data()
        assert self.page.get_data() == "01 May 2026"
