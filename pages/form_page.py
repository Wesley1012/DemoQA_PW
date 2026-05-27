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


    #First name
    def fill_first_name(self, first_name: str):
        self.fill(self.FIRST_NAME, first_name)
        return self

    def get_first_name(self):
        return self.get_input_value(self.FIRST_NAME)

    #Last name
    def fill_last_name(self, last_name: str):
        self.fill(self.LAST_NAME, last_name)
        return self

    def get_last_name(self):
        return self.get_input_value(self.LAST_NAME)

    #Mail
    def fill_email(self, email: str):
        self.fill(self.USER_EMAIL, email)
        return self

    def get_email(self):
        return self.get_input_value(self.USER_EMAIL)

    #Gender
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

    def get_checked_gender(self) -> str:
        if self.page.is_checked(self.GENDER_MALE):
            return "Male"
        elif self.page.is_checked(self.GENDER_FEMALE):
            return "Female"
        elif self.page.is_checked(self.GENDER_OTHER):
            return "Other"
        return None


    #Fill number
    def fill_number(self, number="5555555555"):
        str_number = str(number)
        if len(str(number)) == 10:
            self.fill(self.USER_NUMBER, number)
        else:
            print(f"\nWARNING: Номер {number} имеет {len(str_number)} цифр (должно быть 10)")
            self.fill(self.USER_NUMBER, str_number)

    def get_number(self):
        return self.get_input_value(self.USER_NUMBER)

    #Data
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

    #Subjects

    def select_option(self, input_option):
        self.page.fill(self.SUBJECTS, input_option)
        self.page.wait_for_selector(selector=".subjects-auto-complete__option",
                                    state='visible',
                                    timeout=500
                                    )
        return self

    def fill_subject(self, input_sub: str):

        self.page.wait_for_timeout(500)
        self.click(self.SUBJECTS)
        self.page.fill(self.SUBJECTS, {input_sub})
        self.page.wait_for_selector('.subjects-auto-complete__option.subjects-auto-complete__option--is-focused.css-d7l1ni-option')

        self.page.wait_for_timeout(500)

        sub = self.locator(self.SUBJECTS)
        sub.press("Enter")
        sub.press("Control")

        return self

    def assert_subject_is_visible(self, name: str):
        try:
            if self.locator(".subjects-auto-complete__multi-value__label"):
                # subject = self.page.locator(".subjects-auto-complete__multi-value__label.css-9jq23d")
                # expect(subject).to_be_visible(timeout=3000)
                return True
        except:
            return False


    def get_last_subject(self):
        subject = self.locator(".subjects-auto-complete__multi-value__label")
        subject.last.wait_for(state="attached", timeout=500)
        print('\n', subject.count(), '\n', subject.text_content())
        return subject.nth(-1).text_content()

    def remove_subject_by_text(self, text: str):
        try:
            # self.fill(self.SUBJECTS, text)
            # options = self.page.locator(".subjects-auto-complete__option")
            # options.first.click()

            remove_btn = self.locator(f".subjects-auto-complete__multi-value__remove[aria-label='Remove {text.title()}']")
            remove_btn.click()
            return self
        except Exception as ex:
            print(f'Exception: {ex}')


    def subjects(self) -> bool:
        try:
            aria_expanded = self.page.get_attribute("#subjectsInput",
                                                    "aria-expanded") == 'true'
            options = self.page.locator(".subjects-auto-complete__option")
            has_options = options.count() > 0 and options.first.is_visible()
            print("\n", options.count())
            return aria_expanded and has_options
        except:
            return False

    def get_option(self):
        option = self.locator(".subjects-auto-complete__option")
        return option.text_content()


    def get_all_options(self):
        option = self.page.locator(".subjects-auto-complete__option")
        option.first.wait_for(state="attached", timeout=5000)
        return option.all_text_contents()

    def fill_all_letters_and_get_options(self):
        try:
            options_set = set()

            for i in 'abcdefghijklmnopqrstuvwxyz':
                self.fill(self.SUBJECTS, i)
                self.page.wait_for_timeout(200)

                options = self.page.locator(".subjects-auto-complete__option")
                if options.count():
                    all_options = options.all_text_contents()
                    print(f"\n({i}, {all_options}),")
                    options_set.update(all_options)
                else:
                    print(f"\n({i}, 'Nothing to output'),")

            print(f'\nLen :{len(options_set)}\n{options_set}')
            return options_set
        except Exception as ex:
            print(f"\nEXCEPTION: {ex}")

    def clear_subjects(self):
        clear_btn = self.locator(".subjects-auto-complete__indicator")
        clear_btn.click()
        return self


    # Hobbies

    @allure.title("Выбрать хобби спорт")
    def select_sport(self):
        self.page.wait_for_timeout(300)
        self.click(self.HOBBIES_SPORTS)
        self.page.wait_for_selector("#hobbies-checkbox-1.form-check-input:checked")
        return self


    @allure.title("Выбрать хобби чтение")
    def select_reading(self):
        self.page.wait_for_timeout(300)
        self.click(self.HOBBIES_READING)
        self.page.wait_for_selector("#hobbies-checkbox-2.form-check-input:checked")
        return self


    @allure.title("Выбрать хобби музыку")
    def select_music(self):
        self.page.wait_for_timeout(300)
        self.click(self.HOBBIES_MUSIC)
        self.page.wait_for_selector("#hobbies-checkbox-3.form-check-input:checked")
        return self

    @allure.step("Выбрать хобби {hobby} и проверить")
    def choice_hobby(self, hobby: str):
        self.page.wait_for_timeout(300)

        if hobby.lower() == "sport":
            self.click(self.HOBBIES_SPORTS)
            self.page.wait_for_selector("#hobbies-checkbox-1.form-check-input:checked")
            return self

        elif hobby.lower() == "reading":
            self.click(self.HOBBIES_READING)
            self.page.wait_for_selector("#hobbies-checkbox-2.form-check-input:checked")
            return self

        elif hobby.lower() == "music":
            self.click(self.HOBBIES_MUSIC)
            self.page.wait_for_selector("#hobbies-checkbox-3.form-check-input:checked")
            return self

    # Picture

    @allure.step("Загрузить картинку")
    def upload_picture(self, tmp_path, file_name="test_picture.png"):
        test_file = tmp_path / f"{file_name}"
        test_file.write_bytes(b'test_content')
        self.locator(self.UPLOAD_PICTURE).set_input_files(str(test_file))

        return self

    def get_picture_path(self):
        text = self.locator(self.UPLOAD_PICTURE).input_value()
        return text

    # Address

    @allure.step("Звполнить адрес")
    def fill_address(self, text):
        self.fill(self.CURRENT_ADDRESS, text)
        return self

    def get_address(self):
        text = self.locator('#currentAddress').input_value()
        return text

    # State and city

    def select_state_and_city(self, state: str, city: str):
        self.click(self.STATE_SELECT)
        if state.lower() == "ncr":
            self.click("#state #react-select-3-option-0")
            self.click("#city")
            if city.lower() == "delhi":
                self.click("#city #react-select-4-option-0")
            elif city.lower() == "gurgaon":
                self.click("#city #react-select-4-option-1")
            elif city.lower() == "noida":
                self.click("#city #react-select-4-option-2")
            else:
                raise f"NCR dont have city: {city}"

        elif state.lower() == "uttar Pradesh":
            self.click("#state #react-select-4-option-0")
            self.click("#city")
            if city.lower() == "agra":
                self.click("#city #react-select-4-option-0")
            elif city.lower() == "lucknow":
                self.click("#city #react-select-4-option-1")
            elif city.lower() == "merrut":
                self.click("#city #react-select-4-option-2")
            else:
                raise Exception(f"Uttar Pradesh dont have city: {city}")

        elif state.lower() == "haryana":
            self.click("#state #react-select-3-option-2")
            self.click("#city")
            if city.lower() == "karnal":
                self.click("#city #react-select-4-option-0")
            elif city.lower() == "panipat":
                self.click("#city #react-select-4-option-1")
            else:
                raise Exception(f"Haryana dont have city: {city}")

        elif state.lower() == "rajasthan":
            self.click("#state #react-select-3-option-3")
            self.click("#city")
            if city.lower() == "jaipur":
                self.click("#city #react-select-4-option-0")
            elif city.lower() == "jaiselmer":
                self.click("#city #react-select-4-option-1")
            else:
                raise Exception(f"Rajasthan dont have city: {city}")

        else:
            raise Exception(f"No this state in list: {state}")

    def get_selected_state(self):
        state = self.locator('#state .css-1dimb5e-singleValue').text_content()
        return state

    def get_selected_city(self):
        city = self.locator('#city .css-1dimb5e-singleValue').text_content()
        return city
