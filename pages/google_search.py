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

    @property
    def search_field(self):
        return self.driver.find_element(By.ID, 'lst-ib')

    @property
    def luck(self):
        return self.driver.find_element(By.NAME, 'btnI')

    @property
    def jagr_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'kno-ecr-pt')

    @property
    def search_button(self):
        return self.driver.find_element(By.NAME, 'btnG')
