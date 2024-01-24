import allure

from appiumFramework.assertions import Assertions
from appiumFramework.testing_bot import TestingBotStatus
from hello_world_tests.page_objects.recent_page_object import RecentPageObject


class TestRecentsPage:
    @allure.feature('Resents page')
    @allure.story('Resents document page actions')
    def test_recent_document_data(self, appium_driver):
        """Test creating a new file via the plus button"""
        with allure.step('Open the main page'):
            recent_page = RecentPageObject(driver=appium_driver)

        with allure.step('Get name of the page'):
            page_name = recent_page.get_name_of_page()

        with allure.step('Check is page name correct'):
            Assertions.assert_are_equal(
                expected_result='TestDocument',
                actual_result=page_name
            )
        TestingBotStatus().set_status(session_id=recent_page.driver.session_id)
