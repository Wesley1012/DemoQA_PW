import time
from pages.basepage import BasePage
from locators.elements_locators import *
from playwright.sync_api import expect
from dotenv import load_dotenv
import allure
import os

load_dotenv()

class FormsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv('BASE_URL')

    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    USER_EMAIL = "#userEmail"
    USER_NUMBER = "#userNumber"
    DATE_OF_BIRTH = "#dateOfBirthInput"
    SUBJECTS = "#subjectsInput"
    CURRENT_ADDRESS = "#currentAddress"

    GENDER_MALE = "#gender-radio-1"
    GENDER_FEMALE = "#gender-radio-2"
    GENDER_OTHER = "#gender-radio-3"

    HOBBIES_SPORTS = "#hobbies-checkbox-1"
    HOBBIES_READING = "#hobbies-checkbox-2"
    HOBBIES_MUSIC = "#hobbies-checkbox-3"

    UPLOAD_PICTURE = "#uploadPicture"
    STATE_SELECT = "#state"
    CITY_SELECT = "#city"
    SUBMIT_BTN = "#submit"

    def fill_first_name(self, first_name: str):
        self.fill(self.FIRST_NAME, first_name)
        return self

    def fill_last_name(self, last_name: str):
        self.fill(self.LAST_NAME, last_name)
        return self

    def fill_email(self, email: str):
        self.fill(self.USER_EMAIL, email)
        return self