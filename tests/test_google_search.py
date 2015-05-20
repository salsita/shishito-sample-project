# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Contextual (slide-in) help feature test
"""
import time

from unittestzero import Assert
import pytest

from shishito.runtime.shishito_support import ShishitoSupport
from shishito.ui.selenium_support import SeleniumTest
from tests.conftest import get_test_info
from pages.google_search import GoogleSearch
from pages.google_doodles import GoogleDoodles


@pytest.mark.usefixtures("test_status")
class TestMainPage():
    """ Contextual help test """

    def setup_class(self):
        self.tc = ShishitoSupport().get_test_control()

        self.driver = self.tc.start_browser()
        self.ts = SeleniumTest(self.driver)

        # Page Objects
        self.search_page = GoogleSearch(self.driver)
        self.doodles = GoogleDoodles(self.driver)

    def teardown_class(self):
        self.tc.stop_browser()

    def setup_method(self, method):
        self.tc.start_test(True)

    def teardown_method(self, method):
        test_info = get_test_info()
        self.tc.stop_test(test_info)

    ### Tests ###
    @pytest.mark.smoke
    def test_google_search(self):
        """ test google search """
        self.ts.click_and_wait(self.search_page.luck)
        self.ts.click_and_wait(self.doodles.doodle_archive)
        Assert.equal(self.driver.title, 'Google Doodles')

    def test_failing(self):
        """ test google title """
        # self.execution_id = self.tc.get_execution_id("MET-11")
        Assert.equal(self.driver.title, 'Yahoo')

    def test_good_title(self):
        """ test google title """
        self.search_page.search_field.send_keys('Jaromir Jagr')
        self.ts.click_and_wait(self.search_page.search_button)
        time.sleep(3)
        Assert.equal(self.search_page.jagr_title.text, u'Jaromír Jágr')
