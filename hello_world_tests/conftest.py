import os

from dotenv import load_dotenv

from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options

from appiumFramework.capabilities import IOSCapabilities as capabilities

load_dotenv()

KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')


lambda_test_url = 'https://heydevaslan:VULkGOjKRWDIAz9HnkmQTPugOVLytC01IPEWvkRM4eTkSaBmqa@mobile-hub.lambdatest.com/wd/hub'
testing_bot_url = f'http://{KEY}:{SECRET}@hub.testingbot.com/wd/hub'
local_appium_url = 'http://127.0.0.1:4723'


@pytest.fixture
def appium_driver(request):
    capabilities_options = UiAutomator2Options().load_capabilities(
        capabilities.DESIRED_CAPABILITIES_EMULATOR_HELLO_WORLD  # Here you can add capability that responsible for your task
    )
    driver = webdriver.Remote(command_executor=testing_bot_url, options=capabilities_options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
