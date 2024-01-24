import allure

from appiumFramework.assertions import Assertions
from appiumFramework.testing_bot import TestingBotStatus
from hello_world_tests.page_objects.main_page_object import MainPageObject


class TestMainPage:
    @allure.feature('File Creation')
    @allure.story('Create new file with plus button')
    def test_create_new_file(self, appium_driver):
        """Test creating a new file via the plus button"""
        with allure.step('Open the main page'):
            main_page = MainPageObject(driver=appium_driver)

        with allure.step('Go to browse tab'):
            main_page.click_browse_button()

        with allure.step('Create a new file'):
            main_page.create_new_file()

        with allure.step('Come back to main page'):
            main_page.click_to_documents_btn()

        with allure.step('Get name of file'):
            file_text = main_page.get_name_of_file()

        with allure.step('Verify name of file with expected'):
            Assertions.assert_are_equal(
                expected_result=file_text,
                actual_result='Untitled')

        TestingBotStatus().set_status(session_id=main_page.driver.session_id)
