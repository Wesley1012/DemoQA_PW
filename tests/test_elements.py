from pages.elements_page import ElementsPage
from locators.elements_locators import *
from faker import Faker
import pytest
from time import sleep

fake = Faker()

FULL_RESULT = ('home', 'desktop', 'documents', 'downloads', 'notes', 'commands', 'workspace', 'office', 'wordFile', 'excelFile', 'react', 'angular', 'veu', 'public', 'private', 'classified', 'general')

class TestTextBox:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = ElementsPage(page)
        self.page.navigate('text-box')

    @pytest.mark.parametrize(
        "name, email, currentAddress, permanentAddress", (
        (fake.name(), fake.email(), fake.address(), fake.address()),
        (fake.last_name(), fake.email(), fake.address(), fake.address()))
    )
    def test_text_box(self, name, email, currentAddress, permanentAddress):
        self.page.fill_form_text_box(name, email, currentAddress, permanentAddress)
        sleep(2)

        assert self.page.get_element_title() == "Text Box"
        self.page.assert_output_text_box(name,
                                         email,
                                         currentAddress,
                                         permanentAddress)

class TestCheckBox:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = ElementsPage(page)
        self.page.navigate('checkbox')


    # @pytest.mark.parametrize('Checkbox, Switchers',
    #                          (i for i in dir(CheckBox) if i.endswith('_CHECKBOX')),
    #                          )
    def test_all_check_box(self):
        self.page.navigate('checkbox')
        self.page.click_all_switcher()
        self.page.click_all_checkbox()


        for checkbox in CheckBox.ALL_FOLDERS_CHECKBOX + CheckBox.ALL_FILES_CHECKBOX:
            self.page.assert_checkbox_is_checked(checkbox)

        for switcher in CheckBox.ALL_SWITCHERS:
            self.page.assert_switcher_state(switcher)

        for item in FULL_RESULT:
            assert item in self.page.get_result_checkbox_text()

    def test_notes_checkbox(self):
        self.page.navigate('checkbox')
        sleep(1)
        self.page.click(CheckBox.HOME_SWITCHER)
        self.page.click(CheckBox.DESKTOP_SWITCHER)
        # self.page.click(CheckBox.NOTES_CHECKBOX)

        # assert 'notes' in self.page.get_result_checkbox_text()
        self.page.assert_switcher_state(CheckBox.DESKTOP_SWITCHER)
        self.page.assert_checkbox_is_checked(CheckBox.NOTES_CHECKBOX, False)
        # self.page.assert_switcher_or_checkbox_is_checked(CheckBox.DOCUMENTS_SWITCHER) == False
