# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Contextual (slide-in) help feature test
"""
import time

from unittestzero import Assert
import pytest

from tests.conftest import get_test_info
from pages.google_search import GoogleSearch
from library.google_lib import GoogleControl
from pages.google_doodles import GoogleDoodles
from salsa_webqa.library.support.selenium_support import SeleniumTest
from salsa_webqa.library.support.jira_zephyr_api import ZAPI
import os

@pytest.mark.usefixtures("test_status")
class TestMainPage():
    """ Contextual help test """
    def setup_class(self):
        self.tc = GoogleControl()
        self.driver = self.tc.start_browser()
        self.ts = SeleniumTest(self.driver)
        self.search_page = GoogleSearch(self.driver)
        self.doodles = GoogleDoodles(self.driver)
        self.zapi= ZAPI()
        self.execution_id = None
        self.auth = self.tc.get_jira_auth()

    def teardown_class(self):
        self.tc.stop_browser(self)

    def setup_method(self, method):
        self.tc.start_test(True)

    def teardown_method(self, method):
        test_info = get_test_info()
        self.tc.stop_test(test_info, self.execution_id)
        self.execution_id=None

    ### Tests ###
    @pytest.mark.smoke
    def test_google_search(self):
        """ test google search """
        if self.auth:
            self.execution_id = self.tc.get_execution_id("MET-14")
        self.ts.click_and_wait(self.search_page.luck)
        self.ts.click_and_wait(self.doodles.doodle_archive)
        Assert.equal(self.driver.title, 'Google Doodles')

    def test_failing(self):
        """ test google title """
        if self.auth:
            self.execution_id = self.tc.get_execution_id("MET-11")
        Assert.equal(self.driver.title, 'Yahoo')

    def test_good_title(self):
        """ test google title """
        if self.auth:
            self.search_page.search_field.send_keys('Jaromir Jagr')
        time.sleep(3)
        Assert.equal(self.search_page.jagr_title.text, 'Jaromír Jágr'.decode('utf8'))