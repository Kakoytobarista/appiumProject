from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from appiumFramework.base_page_object import BasePage


class MainPageObject(BasePage):
    CREATE_FILE_IDENTIFIER_BTN = 'FullDocumentManagerViewControllerNavigationBarCreateButtonIdentifier'
    FILE_INPUT_ELEM = 'inputField'
    CREATE_DOCUMENT_BTN = 'Create Document'
    BROWSE_BTN = 'Browse'  # Accessibility identifier for the "Browse" element
    DOCUMENTS_BTN = 'Documents'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def create_new_file(self):
        """Method creating new file and open it"""
        create_btn = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.CREATE_FILE_IDENTIFIER_BTN
        )
        self.click_on_element(element=create_btn)

    def get_file_text(self):
        file_input = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.FILE_INPUT_ELEM
        )
        return file_input.text

    def click_browse_button(self):
        browse_btn = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.BROWSE_BTN
        )
        self.click_on_element(element=browse_btn)

    def click_to_documents_btn(self):
        browse_btn = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.DOCUMENTS_BTN
        )
        self.click_on_element(element=browse_btn)
