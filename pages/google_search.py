# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
"""
from selenium.webdriver.common.by import By

from pages.page_base import Page


class GoogleSearch(Page):
    """ WorkspacesOverview page object """
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.driver = driver
        
        self._search_field_locator = (By.ID, 'gbqfq')
        self._luck_locator = (By.ID, 'gbqfbb')
        self._jagr_title = (By.CLASS_NAME, 'kno-ecr-pt')

    @property 
    def search_field(self):
        return self.driver.find_element(*self._search_field_locator)

    @property
    def luck(self):
        return self.driver.find_element(*self._luck_locator)

    @property
    def jagr_title(self):
        return self.driver.find_element(*self._jagr_title)
