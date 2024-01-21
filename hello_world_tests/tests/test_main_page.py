import allure
from appiumFramework.assertions import Assertions
from hello_world_tests.page_objects.main_page_object import MainPageObject


class TestMainPage:

    @allure.feature('File Creation')
    @allure.story('Create new file with plus button')
    def test_create_new_file_with_plus_btn(self, appium_driver):
        """Test creating a new file via the plus button"""
        with allure.step('Open the main page'):
            main_page = MainPageObject(driver=appium_driver)

        with allure.step('Create a new file'):
            main_page.create_new_file()

        with allure.step('Get file text'):
            file_text = main_page.get_file_text()

        with allure.step('Verify file text'):
            Assertions.assert_are_equal(
                expected_result=file_text,
                actual_result='Hello, world!')
