from pages.basepage import BasePage
from locators.elements_locators import *
from playwright.sync_api import expect
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