from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options

from appiumFramework.capabilities import IOSCapabilities


@pytest.fixture
def appium_driver(request):
    capabilities_options = UiAutomator2Options().load_capabilities(
        IOSCapabilities.DEBUG_CAPABILITIES  # Here you can add capability that responsible for your task
    )
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capabilities_options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
