from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from appiumFramework.base_page_object import BasePage


class RecentPageObject(BasePage):
    RECENT_PAGE_LABEL = 'TestDocument'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def get_name_of_page(self):
        file_input = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.RECENT_PAGE_LABEL
        )
        return file_input.text
