import time
from pages.basepage import BasePage
from locators.elements_locators import *
from playwright.sync_api import expect
from dotenv import load_dotenv
from faker import Faker
import allure
import os

load_dotenv()
fake = Faker()

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

    def get_first_name(self):
        return self.get_input_value(self.FIRST_NAME)

    def fill_last_name(self, last_name: str):
        self.fill(self.LAST_NAME, last_name)
        return self

    def get_last_name(self):
        return self.get_input_value(self.LAST_NAME)

    def fill_email(self, email: str):
        self.fill(self.USER_EMAIL, email)
        return self

    def get_email(self):
        return self.get_input_value(self.USER_EMAIL)

    def choose_gender(self, gender="male"):
        if gender.lower() == 'male':
            self.click(self.GENDER_MALE)
        elif gender.lower() == 'female':
            self.click(self.GENDER_FEMALE)
        elif gender.lower() == 'other':
            self.click(self.GENDER_OTHER)
        else:
            raise ValueError(f"Некорректное значение пола: '{gender}'."
                             f" Допустимые значения: 'male', 'female', 'other'")

        return self

    def fill_number(self, number="5555555555"):
        str_number = str(number)
        if len(str(number)) == 10:
            self.fill(self.USER_NUMBER, number)
        else:
            print(f"WARNING: Номер {number} имеет {len(str_number)} цифр (должно быть 10)")
            self.fill(self.USER_NUMBER, str_number)

    def get_number(self):
        return self.get_input_value(self.USER_NUMBER)

    def fill_data(self, day = "01",
                        month = "May",
                        year = "2026"):
        date = " ".join((day, month, year))
        link = self.locator(self.DATE_OF_BIRTH)
        link.fill(date)

        return self

    def get_data(self) -> str:
        form_input = self.locator(self.DATE_OF_BIRTH)
        return form_input.get_attribute('value')