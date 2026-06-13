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

    def click_new_tab(self):
        self.click(self.NEW_TAB)
        return self

    @allure.step("Открыть новое окно")
    def click_new_window(self):
        self.click(self.NEW_WINDOW)
        return self
    
    def click_new_window_message(self):
        self.click(self.NEW_WINDOW_MESSAGE)
        return self