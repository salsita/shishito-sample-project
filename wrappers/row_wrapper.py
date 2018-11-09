from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from wrappers.base_wrapper import BaseWrapper


class RowGroup(BaseWrapper):
    """
    Represents the radio button groups (custom implementation)
    """


    def is_row_selected(self) -> bool:
        return 'checked' in self.webelement.get_attribute('class')
        # return opt.find_element_by_xpath('../input').get_attribute('checked')

    @property
    def color(self):
        """get color of webelement"""
        return self.webelement.value_of_css_property('color')

    def __getattr__(self, item):
        # will be called if the object attribute (method, variable) cannot be obtained through the normal mechanism
        return getattr(self.webelement, item)
