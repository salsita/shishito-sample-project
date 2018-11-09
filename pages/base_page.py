import logging
import time
from typing import List

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from shishito.runtime.shishito_support import ShishitoSupport

from utils import custom_expected_conditions


class BasePage:
    """
    Class with shared methods / locators for extending Page Objects
    """

    def __init__(self, driver):
        self.driver = driver                # type: WebDriver
        self.framework = ShishitoSupport()
        self.timeout = int(self.framework.get_opt('timeout'))

    def wait_for_element(self, *locator, timeout=None) -> WebElement:
        """
        Wait until the element is located in DOM.
        :param locator: element locator (tuple)
        :param timeout: seconds to wait before failing (int)
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return element

    def find_element(self, *locator) -> WebElement:
        """
        Find web element on page
        (standard Selenium webdriver function, enahanced with the visual highlight of the element)
        :param locator: element locator (tuple)
        :return: webdriver element
        """
        element = self.driver.find_element(*locator)
        return element

    def find_elements(self, *locator) -> List[WebElement]:
        """
        Find web element on page
        (standard Selenium webdriver function, enahanced with the visual highlight of the element)
        :param locator: element locator (tuple)
        :return: webdriver element
        """
        elements = self.driver.find_elements(*locator)
        return elements

    def wait_for_element_visible(self, *locator, timeout=None) -> WebElement:
        """
        Wait until the element is located and displayed on page. It won't work for e.g. elements with opacity 0
        :param locator: element locator (tuple)
        :param timeout: seconds to wait before failing (int)
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element

    def wait_for_text_not_in_element(self, element:WebElement, unwanted_text: str, timeout=None) -> WebElement:
        """
        Wait until the element does not contain specified text
        :param locator: element locator (tuple)
        :param timeout: seconds to wait before failing (int)
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            custom_expected_conditions.text_not_to_be_present_in_element(element, unwanted_text)
        )
        return element

    def wait_for_number_of_elements(self, *locator, expected_number, timeout=None):
        """
        Wait until required number of specified elements is located in the page
        :param locator: element locator (tuple)
        :param expected_number: number of elements (int)
        :param timeout: seconds to wait before failing (int)
        :return: true if all elements found
        :raises: TimeoutException if elements not found within the time limit
        """
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            custom_expected_conditions.number_of_elements_to_be(locator, expected_number)
        )

    def click_on(self, *locator, retries: int = 2, timeout=None):
        """
        Wait for element and click on it.
        Handle StaleElement exception by retrying the operation
        :param locator: locator: element locator (tuple)
        :param retries: number of retries before failing (int)
        :param timeout: seconds to wait before failing (int)
        """
        attempts = 0
        while attempts < retries:
            try:
                self.wait_for_element(*locator, timeout=timeout).click()
                break
            except StaleElementReferenceException:
                pass
            attempts += 1

    def wait_for_element_clickable(self, *locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def wait_for_element_invisible(self, *locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def get_parent_element(self, child_element):
        return child_element.find_element(By.XPATH, '..')

    def get_child_elements(self, parent_element):
        return parent_element.find_elements(By.XPATH, '*')

    def refresh_page(self):
        self.driver.refresh()

    def get_node_text(self, element:WebElement)->str:
        text = element.text
        children_el = self.get_child_elements(element)
        for child in children_el:
            text = text.replace(child.text, "")
        return text

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)

    def log_performance(self, message):
        log = logging.getLogger()
        log.warning(message)

    def fill_form_field(self, form_element, value, request_clear=True):
        if type(form_element) is tuple:
            # Locator, not WebElement
            form_element = self.wait_for_element(*form_element)

        if request_clear:
            form_element.clear()

        form_element.send_keys(value)

    def scroll_to_element(self, element_locator, align_to_top=False):
        """
        Use Javascript to scroll current view to the element
        (must be done e.g. before clicking on checkboxes and radio boxes)
        :param element_locator: WebElement that should be scrolled onto
        :param align_to_top: should the element be visible at the top of the view? (bottom otherwise)
        """
        try:
            boolvalue_js = 'true' if align_to_top else 'false'
            self.driver.execute_script("arguments[0].scrollIntoView({});".format(boolvalue_js), element_locator)
        except:
            pass

    def scroll_top_by_px(self, px: int, querySelector: str):
        """:param px: how many px should be scrolled in +NEW dropdown to reach item.
        Because invisible elements don't exist yet it is not possible to scroll to element."""
        self.driver.execute_script(f"document.querySelector('{querySelector}').scrollTop+={px};")

    def form_field_value(self, form_element):
        return form_element.get_attribute("value")

    def check_checkbox(self, checkbox_element):
        if not checkbox_element.is_selected():
            checkbox_element.click()

    def uncheck_checkbox(self, checkbox_element):
        if checkbox_element.is_selected():
            checkbox_element.click()

    def select_in_dropdown(self, form_element, value):
        select = Select(form_element)
        select.select_by_value(value)

    def dropdown_selected_value(self, form_element):
        select = Select(form_element)
        return select.first_selected_option

    def form_file_upload(self, file_input_element: WebElement, file_path: str):
        self.driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.display='block'",
                                   file_input_element)
        file_input_element.send_keys(os.path.abspath(file_path))