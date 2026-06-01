import pytest
from pages.form_page import FormsPage
import allure
import random
from faker import Faker

fake = Faker()
random_data = f'{fake.day_of_month()} {fake.month_name()} {fake.year()}'
OPTIONS = ['Commerce', 'Economics', 'English', 'Chemistry', 'Arts',
           'Computer Science', 'Social Studies', 'Accounting', 'Maths',
           'Hindi', 'History', 'Civics', 'Biology', 'Physics']


STATE_CITY_PAIRS = [
    # (state, city)
    ('NCR', 'Delhi'),
    ('NCR', 'Gurgaon'),
    ('NCR', 'Noida'),
    ('Uttar Pradesh', 'Agra'),
    ('Uttar Pradesh', 'Lucknow'),
    ('Uttar Pradesh', 'Merrut'),
    ('Haryana', 'Karnal'),
    ('Haryana', 'Panipat'),
    ('Rajasthan', 'Jaipur'),
    ('Rajasthan', 'Jaiselmer'),
]
selected_pair = random.choice(STATE_CITY_PAIRS)

class TestForms:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = FormsPage(page)
        self.page.navigate('automation-practice-form')

    @allure.title('Заполнить всю форму и подтвердить')
    @pytest.mark.parametrize('first_name, last_name, email, gender, number, data,\
                              subject, hobby, picture, address, state, city', [(
                              fake.first_name(),
                              fake.last_name(),
                              fake.email(),
                              random.choice(["Male", "Female", "Other"]),
                              fake.numerify("##########"),
                              random_data,
                              random.choice(OPTIONS),
                              random.choice(["Sport", "Reading", "Music"]),
                              f'{fake.word()}.png',
                              fake.address(),
                              selected_pair[0],  # state
                              selected_pair[1]   # city
                                )])
    def test_form(self, tmp_path, first_name: str, last_name: str, email: str, gender: str, number: str, data: str,
                        subject: str, hobby: str, picture: str, address: str, state: str, city: str):
        self.page.fill_first_name(first_name)
        self.page.fill_last_name(last_name)
        self.page.fill_email(email)
        self.page.choose_gender(gender)
        self.page.fill_number(number)
        self.page.fill_data(data)
        self.page.fill_subject(subject)
        self.page.choose_hobby(hobby)
        self.page.upload_picture(tmp_path, picture)
        self.page.fill_address(address)
        self.page.select_state_and_city(state, city)
        self.page.submit_form()

        with allure.step('Проверить форму'):
            assert self.page.get_first_name() == first_name
            assert self.page.get_last_name() == last_name
            if gender == "Other":
                assert self.page.get_checked_gender() in ("Other", None)
            else:
                assert self.page.get_checked_gender() == gender
            assert self.page.get_number() == number
            assert self.page.get_data() == data
            self.page.assert_subject_is_visible(subject)
            assert self.page.get_picture_path() == f"C:\\fakepath\\{picture}"
            assert self.page.get_address() == address
            assert self.page.get_selected_state() == state, f"Штат не совпадает с выбранным: {state}"
            assert self.page.get_selected_city() == city, f"Город не совпадает с выбранным: {city}"


    def test_first_name(self, first_name=fake.first_name()):
        self.page.fill_first_name(first_name)

        assert self.page.get_first_name() == first_name

    def test_last_name(self, last_name=fake.last_name()):
        self.page.fill_first_name(last_name)

        assert self.page.get_first_name() == last_name

    @allure.title("Указать пол")
    @pytest.mark.parametrize("Gender",
                             ["Male", "Female", "Other"])
    def test_gender(self, Gender: str):
        self.page.choose_gender(Gender)
        if Gender == "Other":
            assert self.page.get_checked_gender() in ("Other", None)
        else:
            assert self.page.get_checked_gender() == Gender

    #fake.numerify('###-###-####')
    @allure.title("Ввести номер телефона")
    @pytest.mark.parametrize('number',
                             [fake.numerify("##########"),
                              "0000000000",
                              "9999999999"])
    def test_number(self, number: str):
        self.page.fill_number(number)
        with allure.step("Проверить, что номер отобразился корректно"):
            assert self.page.get_number() == number


    @allure.title("Ввести дату")
    @pytest.mark.parametrize("day, month, year",
                             [(fake.day_of_month(), fake.month_name(), fake.year())])
    def test_date(self, day: str, month: str, year: str):
        self.page.fill_data(day, month, year)
        assert self.page.get_data() == " ".join((day, month, year))


    @allure.title("Выбрать хобби {hobby}")
    @pytest.mark.parametrize('hobby',
                             ["Sport", "Reading", "Music"])
    def test_choice_hobby(self, hobby: str):
        self.page.choose_hobby(hobby)


    @allure.title("Загрузить фото")
    def test_upload_picture(self, tmp_path, file_name=f'{fake.word()}.png'):
        self.page.upload_picture(tmp_path, file_name=file_name)
        with allure.step('Проверть, что путь соответствует загруженному файлу'):
            assert self.page.get_picture_path() == f"C:\\fakepath\\{file_name}"


    @allure.title("Заполнить адрес")
    def test_fill_current_address(self, text=fake.address()):
        self.page.fill_address(text)
        assert self.page.get_address() == text

    @allure.title("Выбор штата и города")
    @pytest.mark.parametrize('state, city',
                             STATE_CITY_PAIRS)
    def test_state_and_city(self, state: str, city: str):
        self.page.select_state_and_city(state, city)
        with allure.step('Проверить, что штат и город совпадают'):
            assert self.page.get_selected_state() == state, f"Штат не совпадает с выбранным: {state}"
            assert self.page.get_selected_city() == city, f"Город не совпадает с выбранным: {city}"


class TestSubjects(TestForms):

    @allure.title("Выбрать предмет")
    @pytest.mark.parametrize('subject',
                             OPTIONS)
    def test_select_subject(self, subject: str):
        self.page.fill_subject(subject)

        with allure.step('Проверить, что выбраный предмет отобразился'):
            self.page.assert_subject_is_visible(subject)

    @allure.title("Проверка соответствия выбранной опции")
    @pytest.mark.parametrize('option',
                             OPTIONS)
    def test_select_option(self, option: str):
        self.page.select_option(option)
        assert self.page.get_option() == option

    @allure.title("Проверка вариантов вывода опций по букве")
    @pytest.mark.parametrize('letter, option_input',
                            [('a', ['Maths', 'Accounting', 'Arts', 'Social Studies']),
                            ('b', ['Biology']),
                            ('c', ['Physics', 'Chemistry', 'Computer Science', 'Commerce', 'Accounting', 'Economics', 'Social Studies', 'Civics']),
                            ('d', ['Hindi', 'Social Studies']),
                            ('e', ['English', 'Chemistry', 'Computer Science', 'Commerce', 'Economics', 'Social Studies']),
                            ('g', ['English', 'Biology', 'Accounting']),
                            ('h', ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'History']),
                            ('i', ['Hindi', 'English', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Accounting', 'Economics', 'Social Studies', 'History', 'Civics']),
                            ('l', ['English', 'Biology', 'Social Studies']),
                            ('m', ['Maths', 'Chemistry', 'Computer Science', 'Commerce', 'Economics']),
                            ('n', ['Hindi', 'English', 'Computer Science', 'Accounting', 'Economics']),
                            ('o', ['Biology', 'Computer Science', 'Commerce', 'Accounting', 'Economics', 'Social Studies', 'History']),
                            ('p', ['Physics', 'Computer Science']),
                            ('r', ['Chemistry', 'Computer Science', 'Commerce', 'Arts', 'History']),
                            ('s', ['English', 'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']),
                            ('t', ['Maths', 'Chemistry', 'Computer Science', 'Accounting', 'Arts', 'Social Studies', 'History']),
                            ('u', ['Computer Science', 'Accounting', 'Social Studies']),
                            ('v', ['Civics']),
                            ('y', ['Physics', 'Chemistry', 'Biology', 'History'])])

    def test_all_letter(self, letter: str, option_input: list):
        self.page.select_option(letter)
        assert self.page.get_all_options() == option_input





