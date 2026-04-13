from pages.basepage import BasePage
from locators.elements_locators import *
import allure
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv('BASE_URL')


class TextBoxPage(ElementsPage):

    @allure.step('Заполнить все поля значениями и подтвердить')
    def fill_form_text_box(self,
                           name,
                           email,
                           current_address,
                           permanent_address):
        self.fill(TextBoxLocators.FULL_NAME, name)
        self.fill(TextBoxLocators.EMAIL, email)
        self.fill(TextBoxLocators.CURRENT_ADDRESS, current_address)
        self.fill(TextBoxLocators.PERMANENT_ADDRESS, permanent_address)
        self.click(TextBoxLocators.SUBMIT_BUTTON)

        return self

    @allure.step("Проверить корректность вывода")
    def assert_output_text_box(self,
                               name,
                               email,
                               current_address,
                               permanent_address):
        assert self.get_text("#output #name").replace("Name:", "").strip() == name
        assert self.get_text("#output #email").replace("Email:", "").strip() == email
        assert self.get_text("#output #currentAddress").replace("Current Address :", "").strip() == current_address
        assert self.get_text("#output #permanentAddress").replace("Permananet Address :", "").strip() == permanent_address

    def get_element_title(self):
        return self.get_text('.text-center')


class CheckBoxPage(ElementsPage):

    @allure.step('Нажать все чекбоксы')
    def click_all_checkbox(self):
        self.click(CheckBoxLocators.HOME_CHECKBOX)
        return self

    @allure.step('Нажать все свичи')
    def click_all_switcher(self):

        for switcher in CheckBoxLocators.ALL_SWITCHERS:
            self.click(switcher)

        return self

    def get_result_checkbox_text(self):
        RESULT = self.get_text(CheckBoxLocators.RESULT)

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

class RadioButtonPage(ElementsPage):

    @allure.step('Кликнуть кнопку "Yes"')
    def click_yes(self):
        self.click(RadioButtonLocators.YES_BUTTON)
        return self

    @allure.step('Кликнуть кнопку "Impressive"')
    def click_impressive(self):
        self.click(RadioButtonLocators.IMPRESSIVE_BUTTON)
        return self

    def get_result(self):
        return self.get_text(RadioButtonLocators.SELECTED_INPUT)

class WebTablesPage(ElementsPage):

    @allure.step(f"Ввести значения в поля таблицы")
    def fill_new_user_and_submit(self, first_name, last_name, email, age, salary, departament):
        self.click(WebTablesLocators.ADD_BUTTON)
        self.fill(WebTablesLocators.FIRST_NAME, first_name)
        self.fill(WebTablesLocators.LAST_NAME, last_name)
        self.fill(WebTablesLocators.USER_EMAIL, email)
        self.fill(WebTablesLocators.AGE, age)
        self.fill(WebTablesLocators.SALARY, salary)
        self.fill(WebTablesLocators.DEPARTMENT, departament)
        self.click(WebTablesLocators.SUBMIT)

        with allure.step("Проверить, что пользователь корректно добавился в таблицу"):
            assert self.get_text(WebTablesLocators.TABLE_FIRST_NAME) == first_name
            assert self.get_text(WebTablesLocators.TABLE_LAST_NAME) == last_name
            assert self.get_text(WebTablesLocators.TABLE_EMAIL) == email
            assert self.get_text(WebTablesLocators.TABLE_AGE) == age
            assert self.get_text(WebTablesLocators.TABLE_SALARY) == salary
            assert self.get_text(WebTablesLocators.TABLE_DEPARTMENT) == departament
