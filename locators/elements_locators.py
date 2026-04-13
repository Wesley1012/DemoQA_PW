class ElementsLocators:
    TEXT_BOX = "#item-0"
    CHECK_BOX = "#item-1"
    RADIO_BUTTON = "#item-2"
    WEB_TABLES = "#item-3"
    BUTTONS = "#item-4"
    LINKS = "#item-5"
    BROKEN_LINKS_IMAGES = "#item-6"
    UPLOAD_AND_DOWNLOAD = "#item-7"
    DYNAMIC_PROPERTIES = "#item-8"

class TextBoxLocators:
    """Локаторы для страницы Text Box"""
    FULL_NAME = "#userName"
    EMAIL = "#userEmail"
    CURRENT_ADDRESS = "#currentAddress"
    PERMANENT_ADDRESS = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    OUTPUT = "#output"

class CheckBoxLocators:
    """ Локаторы для страницы Check Box"""
    #Folders
    HOME_CHECKBOX = "[aria-label='Select Home']"
    DESKTOP_CHECKBOX = "[aria-label='Select Desktop']"
    DOCUMENTS_CHECKBOX = "[aria-label='Select Documents']"
    WORKSPACE_CHECKBOX = "[aria-label='Select WorkSpace']"
    OFFICE_CHECKBOX = "[aria-label='Select Office']"
    DOWNLOADS_CHECKBOX = "[aria-label='Select Downloads']"

    ALL_FOLDERS_CHECKBOX = (HOME_CHECKBOX, DESKTOP_CHECKBOX, DOCUMENTS_CHECKBOX, WORKSPACE_CHECKBOX, OFFICE_CHECKBOX, DOWNLOADS_CHECKBOX)

    #files
    NOTES_CHECKBOX = "[aria-label='Select Notes']"
    COMMANDS_CHECKBOX = "[aria-label='Select Commands']"
    ANGULAR_CHECKBOX = "[aria-label='Select Angular']"
    VEU_CHECKBOX = "[aria-label='Select Veu']"
    PUBLIC_CHECKBOX = "[aria-label='Select Public']"
    PRIVATE_CHECKBOX = "[aria-label='Select Private']"
    CLASSIFIED_CHECKBOX = "[aria-label='Select Classified']"
    GENERAL_CHECKBOX = "[aria-label='Select General']"
    WORD_CHECKBOX = "[aria-label='Select Word File.doc']"
    EXCEL_CHECKBOX = "[aria-label='Select Excel File.doc']"

    ALL_FILES_CHECKBOX = (NOTES_CHECKBOX, COMMANDS_CHECKBOX, ANGULAR_CHECKBOX, VEU_CHECKBOX, PUBLIC_CHECKBOX, PRIVATE_CHECKBOX, CLASSIFIED_CHECKBOX, GENERAL_CHECKBOX, WORD_CHECKBOX, EXCEL_CHECKBOX)

    HOME_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'Home')]]//span[contains(@class,'rc-tree-switcher')]"
    DESKTOP_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'Desktop')]]//span[contains(@class,'rc-tree-switcher')]"
    DOCUMENTS_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'Documents')]]//span[contains(@class,'rc-tree-switcher')]"
    WORKSPACE_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'WorkSpace')]]//span[contains(@class,'rc-tree-switcher')]"
    OFFICE_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'Office')]]//span[contains(@class,'rc-tree-switcher')]"
    DOWNLOADS_SWITCHER = "//div[contains(@class,'rc-tree-treenode') and .//span[contains(text(),'Downloads')]]//span[contains(@class,'rc-tree-switcher')]"

    ALL_SWITCHERS = (HOME_SWITCHER, DESKTOP_SWITCHER, DOCUMENTS_SWITCHER, WORKSPACE_SWITCHER, OFFICE_SWITCHER, DOWNLOADS_SWITCHER)

    RESULT = "#result"

class RadioButtonLocators:

    YES_BUTTON = "#yesRadio"
    IMPRESSIVE_BUTTON = "#impressiveRadio"
    SELECTED_INPUT = ".text-success"

class WebTablesLocators:

    #add
    ADD_BUTTON = "#addNewRecordButton"

    FIRST_NAME = "#userForm #firstName"
    LAST_NAME = "#userForm #lastName"
    USER_EMAIL = "#userForm #userEmail"
    AGE = "#userForm #age"
    SALARY = "#userForm #salary"
    DEPARTMENT = "#userForm #department"
    SUBMIT = "#userForm #submit"

    #search
    SEARCH_BOX = "#searchBox"
    SEARCH_BUTTON = "#basic-addon2"

    #table titles last added
    TABLE_FIRST_NAME = "tbody tr:last-child td:first-child"
    TABLE_LAST_NAME = "tbody tr:last-child td:nth-child(2)"
    TABLE_AGE = "tbody tr:last-child td:nth-child(3)"
    TABLE_EMAIL = "tbody tr:last-child td:nth-child(4)"
    TABLE_SALARY = "tbody tr:last-child td:nth-child(5)"
    TABLE_DEPARTMENT = "tbody tr:last-child td:nth-child(6)"