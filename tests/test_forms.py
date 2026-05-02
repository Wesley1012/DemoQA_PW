import pytest
from pages.form_page import FormsPage
import allure

class TestForms:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = FormsPage(page)
        self.page.navigate('automation-practice-form')

    def test_gender(self):
        self.page.choose_gender('Female')
        assert self.page.get_checked_gender() == "Female"

    def test_number(self):
        self.page.fill_number("4444444444")
        assert self.page.get_number() == "4444444444"

    def test_date(self):
        self.page.fill_data()
        assert self.page.get_data() == "01 May 2026"''

    def test_subjects(self):
        self.page.fill_subject("c")
        assert self.page.subjects()