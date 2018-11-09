"""
Custom "Expected Conditions" which are generally useful
within webdriver tests.
"""
from typing import Tuple

from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement


class number_of_elements_to_be():
    """
    An expectation for the number of located
    elements to be a certain value.
    """

    def __init__(self, locator, num_elements):
        self.locator = locator
        self.num_elements = num_elements

    def __call__(self, driver):
        elements = _find_elements(driver, self.locator)
        return len(elements) == self.num_elements

class text_not_to_be_present_in_element(object):
    """ An expectation for checking if the given text is not present in the
    specified element.
    WebElement, text
    """
    def __init__(self, element: WebElement, text_):
        self.element = element
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = self.element.text
            return self.text not in element_text
        except StaleElementReferenceException:
            return False

class presence_of_element_in_element_located:
    """ An expectation for checking that an element is present in another (parent) element.
    This does not necessarily mean that the element is visible.
    locator - used to find the element
    returns the WebElement once it is located
    """

    def __init__(self, parent_element: WebElement, locator):
        self.parent_element = parent_element
        self.locator = locator

    def __call__(self, driver):
        return _find_element_in_element(self.parent_element, self.locator)


def _find_element(driver, by):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_element_in_element(parent_element: WebElement, by: Tuple[str, str]):
    """Looks up an element in parent element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return parent_element.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e