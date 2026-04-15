import random
from pages.elements_page import RadioButtonPage, CheckBoxPage, TextBoxPage, WebTablesPage, ClickMeButtonsPage
from locators.elements_locators import *
import allure
from faker import Faker
import pytest
from time import sleep

random_age = str(random.randint(1, 100))
random_salary = str(random.randint(1, 10))+"000"
fake = Faker()

FULL_RESULT = ('home', 'desktop', 'documents', 'downloads', 'notes', 'commands', 'workspace', 'office', 'wordFile', 'excelFile', 'react', 'angular', 'veu', 'public', 'private', 'classified', 'general')

class TestTextBox:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = TextBoxPage(page)
        self.page.navigate('text-box')

    @allure.title("Форма Text Box")
    @pytest.mark.parametrize(
        "name, email, current_address, permanent_address", (
        (fake.name(), fake.email(), fake.address(), fake.address()),
        (fake.last_name(), fake.email(), fake.address(), fake.address()))
    )
    def test_text_box(self, name, email, current_address, permanent_address):
        self.page.fill_form_text_box(name, email, current_address, permanent_address)
        sleep(2)

        with allure.step('Проверить что значения есть на выходе'):
            assert self.page.get_element_title() == "Text Box"
            self.page.assert_output_text_box(name,
                                             email,
                                             current_address,
                                             permanent_address)
            
@allure.title("Форма Check Box и навигация")
class TestCheckBox:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = CheckBoxPage(page)
        self.page.navigate('checkbox')


    def test_all_check_box(self):
        self.page.navigate('checkbox')
        self.page.click_all_switcher()
        self.page.click_all_checkbox()


        for checkbox in CheckBoxLocators.ALL_FOLDERS_CHECKBOX + CheckBoxLocators.ALL_FILES_CHECKBOX:
            self.page.assert_checkbox_is_checked(checkbox)

        for switcher in CheckBoxLocators.ALL_SWITCHERS:
            self.page.assert_switcher_state(switcher)

        for item in FULL_RESULT:
            assert item in self.page.get_result_checkbox_text()


    def test_notes_checkbox(self):
        self.page.navigate('checkbox')
        sleep(1)
        self.page.click(CheckBoxLocators.HOME_SWITCHER)
        self.page.click(CheckBoxLocators.DESKTOP_SWITCHER)

        self.page.assert_switcher_state(CheckBoxLocators.DESKTOP_SWITCHER)
        self.page.assert_checkbox_is_checked(CheckBoxLocators.NOTES_CHECKBOX, False)
        # self.page.assert_switcher_or_checkbox_is_checked(CheckBox.DOCUMENTS_SWITCHER) == False

@allure.feature("Кнопки (Radio Button)")
class TestRadioButton:

    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = RadioButtonPage(page)
        self.page.navigate('radio-button')

    @allure.title("Radio Button")
    def test_radio_button(self):
        self.page.click_yes()
        with allure.step('Проверить, что результат "Yes"'):
            assert self.page.get_result() == "Yes"

        self.page.click_impressive()
        with allure.step('Проверить, что результат "Impressive"'):
            assert self.page.get_result() == "Impressive"


@allure.feature('Форма таблицы (Web Tables)')
class TestWebTables:

    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = WebTablesPage(page)
        self.page.navigate('webtables')

    @allure.title("Таблица пользователей")
    @allure.description("""
     Тест проверяет добавление пользователя в таблицу:
     1) Нажимает кнопку "Add".
     2) Заполняет все поля валидными значениями.
     3) Нажимает кнопку "Submit".
     4) Проверяет, что в таблице появился новый пользователь с ведёнными раннее значениями.
    """)
    @pytest.mark.parametrize('first_name, last_name, email, age, salary, department',[
                             (str(fake.first_name()), str(fake.last_name()), fake.email(), random_age, random_salary, fake.company())
                                ])
    def test_add_new_user(self, first_name, last_name, email, age, salary, department):

        self.page.fill_new_user_and_submit(first_name, last_name, email, age, salary, department)


@allure.feature('Кнопки с кликами (Buttons)')
class TestClickButtons:

    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = ClickMeButtonsPage(page)
        self.page.navigate('buttons')

    @allure.title("Двойной клик")
    def test_bouble_click_me(self):
        self.page.click_double_click_button()

    @allure.title("Правый клик")
    def test_right_click_me(self):
        self.page.click_right_click_button()

    @allure.title("Клик")
    def test_clime_me(self):
        self.page.click_clickMe_button()

