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
        self._search_field = (By.ID, 'lst-ib')
        self._luck = (By.NAME, 'btnI')
        self._jagr_title = (By.CLASS_NAME, 'kno-ecr-pt')
        self._search_button = (By.NAME, 'btnG')

    @property
    def search_field(self):
        return self.driver.find_element(*self._search_field)

    @property
    def luck(self):
        return self.driver.find_element(*self._luck)

    @property
    def jagr_title(self):
        return self.driver.find_element(*self._jagr_title)

    @property
    def search_button(self):
        return self.driver.find_element(*self._search_button)
