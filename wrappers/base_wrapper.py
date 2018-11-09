import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from utils import custom_expected_conditions

from shishito.runtime.shishito_support import ShishitoSupport


class BaseWrapper:

    def __init__(self, webelement: WebElement):
        self.webelement = webelement
        self.driver = self.webelement.parent  # type: WebDriver
        self.framework = ShishitoSupport()
        self.timeout = int(self.framework.get_opt('timeout'))

    def wait_for_element(self, *locator, timeout=None) -> WebElement:
        """
        Wait until the element is located in wrapper element.

        :param locator: element locator (tuple)
        :param timeout: seconds to wait before failing (int)
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            custom_expected_conditions.presence_of_element_in_element_located(self.webelement, locator)
        )
        self.highlight(element)
        return element

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       element, s)

        original_style = element.get_attribute('style')
        apply_style("background: #ffcc66; border: 2px solid red;")
        time.sleep(.1)
        apply_style(original_style)

    def __getattr__(self, item):
        return getattr(self.webelement, item)