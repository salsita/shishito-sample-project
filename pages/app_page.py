import os
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage



class App(BasePage):
    _back_button = By.CSS_SELECTOR, '[data-qa-id="back-button"]'
    _next_button = By.CSS_SELECTOR, '[data-qa-id="next-button"]'
    _error_message = By.CSS_SELECTOR, '[data-qa-id="error_message"]'

    @property
    def back_button(self) -> WebElement:
        return self.wait_for_element(*self._back_button)

    @property
    def next_button(self) -> WebElement:
        return self.wait_for_element(*self._next_button)

    @property
    def error_messages(self) -> List[str]:
        err_msg_elements = self.find_elements(*self._error_message)
        return [err.text for err in err_msg_elements]

    def go_back_to_previous_step(self):
        self.back_button.click()

    def go_back_to_next_step(self):
        self.next_button.click()
