import abc

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractBasePage(abc.ABC):
    @abc.abstractmethod
    def find_element_by(self, by: AppiumBy, selector: str) -> WebElement:
        pass

    @staticmethod
    @abc.abstractmethod
    def click_on_element(element: WebElement) -> None:
        pass

    @staticmethod
    @abc.abstractmethod
    def send_keys(element: WebElement) -> None:
        pass


class BasePage(AbstractBasePage):
    def __init__(self, driver, timeout: int = 5):
        self.driver: webdriver = driver
        self.timeout = timeout
        self.driver.implicitly_wait(self.timeout)

    def find_element_by(self, by, selector):
        return self.driver.find_element(by, selector)

    def wait_for_element_presence(self, by, selector):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def wait_for_element_visibility(self, by, selector):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, selector))
        )

    def wait_for_element_clickable(self, by, selector):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, selector))
        )

    @staticmethod
    def click_on_element(element):
        element.click()

    @staticmethod
    def send_keys(element):
        element.send_keys()
