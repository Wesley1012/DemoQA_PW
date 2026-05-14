import pytest
from pages.form_page import FormsPage
import allure

class TestForms:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = FormsPage(page)
        self.page.navigate('automation-practice-form')

    def test_gender(self):
        self.page.choose_gender('Female')
        assert self.page.get_checked_gender() == "Female"

    #fake.numerify('###-###-####')
    def test_number(self):
        self.page.fill_number("4444444444")
        assert self.page.get_number() == "4444444444"

    def test_date(self):
        self.page.fill_data()
        assert self.page.get_data() == "01 May 2026"''

class TestSubjects(TestForms):
    OPTIONS = ('Commerce', 'Economics', 'English', 'Chemistry', 'Arts',
               'Computer Science', 'Social Studies', 'Accounting', 'Maths',
               'Hindi', 'History', 'Civics', 'Biology', 'Physics')

    def test_subjects(self):
        self.page.fill_subject("s")
        assert self.page.subjects()

    @pytest.mark.parametrize('option',
                             OPTIONS)
    def test_select_option(self, option):
        self.page.select_option(option)
        assert self.page.get_option() == option
    #
    # def test_get_all_options(self):
    #     self.page.fill_all_letters_and_get_options()

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

    def test_all_letter(self, letter, option_input):
        self.page.select_option(letter)
        assert self.page.get_all_options() == option_input


    def test_adds_and_delete_all_options(self):
        for option in self.OPTIONS:
            self.page.fill_subject(option)

            assert self.page.assert_subject_is_visible(option)

            self.page.remove_subject_by_text(option)

    @pytest.mark.parametrize('subject',
                             OPTIONS)
    def test_select_and_delete_subject(self, subject: str):
        self.page.fill_subject(subject)

        with allure.step('Проверить, что выбраный предмет отобразился'):
            self.page.assert_subject_is_visible(subject)

        self.page.remove_subject_by_text(subject)

        assert self.page.assert_subject_is_visible(subject) == False
