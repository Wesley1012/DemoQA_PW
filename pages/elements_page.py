from pages.basepage import BasePage
from locators.elements_locators import *
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv('BASE_URL')

    def fill_form_text_box(self,
                           name,
                           email,
                           curAddress,
                           perAddress):
        self.fill(TextBox.FULL_NAME, name)
        self.fill(TextBox.EMAIL, email)
        self.fill(TextBox.CURRENT_ADDRESS, curAddress)
        self.fill(TextBox.PERMANENT_ADDRESS, perAddress)

        self.click(TextBox.SUBMIT_BUTTON)

        return self

    def assert_output_text_box(self,
                               name,
                               email,
                               curAddress,
                               perAddress):
        assert self.get_text("#output #name").replace("Name:", "").strip() == name
        assert self.get_text("#output #email").replace("Email:", "").strip() == email
        assert self.get_text("#output #currentAddress").replace("Current Address :", "").strip() == curAddress
        assert self.get_text("#output #permanentAddress").replace("Permananet Address :", "").strip() == perAddress

    def get_element_title(self):
        return self.get_text('.text-center')

    def click_all_checkbox(self):
        self.click(CheckBox.HOME_CHECKBOX)

        return self

    def click_all_switcher(self):

        for switcher in CheckBox.ALL_SWITCHERS:
            self.click(switcher)

        return self

    def get_result_checkbox_text(self):
        RESULT = self.get_text(CheckBox.RESULT)

        if 'You have selected :' in RESULT:
            result_text = RESULT.replace('You have selected :', '').strip()

        return result_text

    def assert_checkbox_is_checked(self, selector, expected_state=True):
        item = self.find_locator(selector)
        actural_state = item.get_attribute("aria-checked") == 'true'
        assert actural_state == expected_state

    def assert_switcher_state(self, selector, should_be_open=True):
        switcher = self.find_locator(selector)
        if should_be_open:
            assert "switcher_open" in switcher.get_attribute("class")
        else:
            assert "switcher_close" in switcher.get_attribute("class") or \
                    "switcher_noop" in switcher.get_attribute("class")