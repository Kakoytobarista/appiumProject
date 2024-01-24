import abc

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from appium.webdriver import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appiumFramework.logs import logger


class ElementNotFound(Exception):
    """
    Error class of Element Exception
    """
    pass


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
    def send_keys(element: WebElement, text: str) -> None:
        pass


class BasePage(AbstractBasePage):
    def __init__(self, driver, timeout: int = 5):
        self.driver: webdriver = driver
        self.timeout = timeout
        self.driver.implicitly_wait(self.timeout)

    def find_element_by(self, by, selector):
        try:
            element = self.driver.find_element(by, selector)
            logger.debug(f'Found the element {element}, by selector: {selector}, by {by}')
            return element
        except Exception as e:
            raise ElementNotFound(f'Error while finding element: {e}')

    def wait_for_element_presence(self, by, selector):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            logger.debug(f'Found the element {element}, by selector: {selector}, by {by}')
            return element
        except Exception as e:
            raise ElementNotFound(
                f'Error while finding element: {e}, by: {by}, {selector} '
                f'with presence_of_element_located'
            )

    def wait_for_element_visibility(self, by, selector):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, selector))
            )
            logger.debug(f'Found the element {element}, by selector: {selector}, by {by}')
            return element
        except Exception as e:
            raise ElementNotFound(
                f'Error while finding element: {e}, by: {by}, {selector} '
                f'with visibility_of_element_located'
            )

    def wait_for_element_clickable(self, by, selector):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            logger.debug(f'Found the element {element}, by selector: {selector}, by {by}')
            return element
        except Exception as e:
            raise ElementNotFound(
                f'Error while finding element: {e}, by: {by}, {selector} '
                f'with element_to_be_clickable'
            )

    @staticmethod
    def click_on_element(element):
        logger.debug(f'Click to element {element}')
        element.click()

    @staticmethod
    def send_keys(element, text):
        logger.debug(f'Set value: {text}, to {element}')
        element.send_keys(text)

    def swipe_left(self):
        start_x = 400
        start_y = 500
        end_x = 50
        end_y = 400
        TouchAction(self.driver).press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()
