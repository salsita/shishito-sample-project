# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Contextual (slide-in) help feature test
"""
from unittestzero import Assert
import pytest
from salsa_webqa.library.logic.auth.auth import log_in
from conftest import get_test_info

from pages.google_search import GoogleSearch
from library.google_lib import GoogleControl
from pages.google_doodles import GoogleDoodles

from salsa_webqa.library.support.selenium_support import TestSelenium


@pytest.mark.usefixtures("test_status")
class TestMainPage():
    """ Contextual help test """
    def setup_class(self):
        self.tc = GoogleControl()
        self.driver = self.tc.start_browser()

        self.ts = TestSelenium(self.driver)

        self.search_page = GoogleSearch(self.driver)
        self.doodles = GoogleDoodles(self.driver)

    def teardown_class(self):
        self.tc.stop_browser(self)

    def setup_method(self, method):
        self.tc.start_test()

    def teardown_method(self, method):
        test_info = get_test_info()
        self.tc.stop_test(test_info)

    ### Tests ###
    @pytest.mark.smoke
    def test_google_search(self):
        """ test google search """
        self.ts.click_and_wait(self.search_page.luck)
        Assert.equal(self.doodles.header.text, 'Doodles')

    def test_failing(self):
        """ test google title """
        log_in(self.search_page.search_field, 'email', self.search_page.search_field, 'password')
        Assert.equal(self.driver.title, 'Yahoo')

    def test_good_title(self):
        """ test google title """
        Assert.not_equal(self.driver.title, 'Apple')