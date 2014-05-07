# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
"""
from selenium.webdriver.common.by import By

from pages.page_base import Page


class GoogleDoodles(Page):
    """ WorkspacesOverview page object """
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.driver = driver

        self._header = (By.TAG_NAME, 'h1')
        self._doodle_archive_locator = (By.LINK_TEXT, 'Doodles Archive')

    @property
    def header(self):
        return self.driver.find_element(*self._header)

    @property
    def doodle_archive(self):
        return self.driver.find_element(*self._doodle_archive_locator)