from pages.basepage import BasePage
from dotenv import load_dotenv
from faker import Faker
import allure
import os

load_dotenv()
fake = Faker()

class WindowsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv('BASE_URL')

    NEW_TAB = "#tabButton"
    NEW_WINDOW = "#windowButton"
    NEW_WINDOW_MESSAGE = "#messageWindowButton"

    @allure.step("Открыть новую вкладку")
    def click_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.click(self.NEW_TAB)
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")

        return new_page


    @allure.step("Открыть новое окно")
    def click_new_window(self):
        self.click(self.NEW_WINDOW)
        self.page.wait_for_url('https://demoqa.com/browser-windows/sample')
        return self
    
    def click_new_window_message(self):
        self.click(self.NEW_WINDOW_MESSAGE)
        return self