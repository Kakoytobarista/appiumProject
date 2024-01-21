import abc

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractBaseElement(abc.ABC):
    @abc.abstractmethod
    def find_element_by(self, by: AppiumBy, selector: str) -> WebElement:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def click_on_element(element: WebElement):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def send_keys(element: WebElement):
        raise NotImplementedError


class BaseElement(AbstractBaseElement):
    ACCESSIBILITY_ID = None

    def __init__(self, driver, timeout=5):
        self.driver: webdriver = driver
        self.timeout = timeout
        self.element = self.wait_for_element_presence(
            by=AppiumBy.ACCESSIBILITY_ID, selector=self.ACCESSIBILITY_ID
        )

    def wait_for_element_presence(self, by, selector):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def find_element_by(self, by, selector):
        return self.element.find_element(by, selector)

    @staticmethod
    def click_on_element(element):
        element.click()

    @staticmethod
    def send_keys(element):
        element.send_keys()
