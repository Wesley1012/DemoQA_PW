import pytest
from pages.form_page import FormsPage
import allure
from faker import Faker

fake = Faker()

class TestForms:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = FormsPage(page)
        self.page.navigate('automation-practice-form')

    @pytest.mark.parametrize("Gender",
                             ["Male", "Female", "Other"])
    def test_gender(self, Gender: str):
        self.page.choose_gender(Gender)
        if Gender == "Other":
            assert self.page.get_checked_gender() in ("Other", None)
        else:
            assert self.page.get_checked_gender() == Gender

    #fake.numerify('###-###-####')
    def test_number(self):
        self.page.fill_number("4444444444")
        assert self.page.get_number() == "4444444444"

    def test_date(self):
        self.page.fill_data()
        assert self.page.get_data() == "01 May 2026"''

    @allure.title("Выбрать хобби {hobby}")
    @pytest.mark.parametrize('hobby',
                             ["Sport", "Reading", "Music"])
    def test_choice_hobby(self, hobby: str):
        self.page.choice_hobby(hobby)

    def test_upload_picture(self, tmp_path, file_name=f'{fake.words()}.png'):
        self.page.upload_picture(tmp_path, file_name=file_name)

    # def test_text(self):
    #     print(self.page.get_picture_text())

class TestSubjects(TestForms):
    OPTIONS = ('Commerce', 'Economics', 'English', 'Chemistry', 'Arts',
               'Computer Science', 'Social Studies', 'Accounting', 'Maths',
               'Hindi', 'History', 'Civics', 'Biology', 'Physics')

    @allure.title("Проверка соответствия выбранной опции")
    @pytest.mark.parametrize('option',
                             OPTIONS)
    def test_select_option(self, option: str):
        self.page.select_option(option)
        assert self.page.get_option() == option

    @allure.title("Проверка вариантов вывода опций по букве")
    @pytest.mark.parametrize('letter, option_input',
                            (('a', ['Maths', 'Accounting', 'Arts', 'Social Studies']),
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
                            ('y', ['Physics', 'Chemistry', 'Biology', 'History'])))

    def test_all_letter(self, letter: str, option_input: list):
        self.page.select_option(letter)
        assert self.page.get_all_options() == option_input


    @allure.title("Выбрать предмет")
    @pytest.mark.parametrize('subject',
                             OPTIONS)
    def test_select_and_delete_subject(self, subject: str):
        self.page.fill_subject(subject)

        with allure.step('Проверить, что выбраный предмет отобразился'):
            self.page.assert_subject_is_visible(subject)

