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
from google_test_runner import CYCLE_ID
cycle_id_base="5"


@pytest.mark.usefixtures("test_status")
class TestMainPage():
    """ Contextual help test """
    def setup_class(self):
        self.tc = GoogleControl()
        self.driver = self.tc.start_browser()

        self.ts = SeleniumTest(self.driver)

        self.search_page = GoogleSearch(self.driver)
        self.doodles = GoogleDoodles(self.driver)
        self.auth=self.tc.get_jira_auth()
        self.zapi= ZAPI()
        self.cycle_id=CYCLE_ID
        self.issue_id = None
        self.execution_id = None


    def teardown_class(self):
        self.tc.stop_browser(self)

    def setup_method(self, method):
        self.tc.start_test(True)

    def teardown_method(self, method):
        test_info = get_test_info()
        if self.issue_id is not None and self.execution_id is not None:
            if test_info.test_status == "failed_execution":
                self.zapi.update_execution_status(self.execution_id, "FAIL", self.auth)
            elif test_info.test_status == "passed":
                self.zapi.update_execution_status(self.execution_id, "PASS", self.auth)
        self.issue_id = None
        self.execution_id=None
        self.tc.stop_test(test_info)

    ### Tests ###
    @pytest.mark.smoke
    def test_google_search(self):
        """ test google search """
        self.issue_id = self.zapi.get_issueid(cycle_id_base,"MET-14", self.auth)
        self.execution_id = self.zapi.add_new_execution("Metros Testing", "First release", self.cycle_id, self.issue_id, self.auth)
        self.ts.click_and_wait(self.search_page.luck)
        self.ts.click_and_wait(self.doodles.doodle_archive)
        Assert.equal(self.driver.title, 'Google Doodles')

    def test_failing(self):
        """ test google title """
        self.issue_id = self.zapi.get_issueid(cycle_id_base,"MET-11", self.auth)
        self.execution_id = self.zapi.add_new_execution("Metros Testing", "First release", self.cycle_id, self.issue_id, self.auth)
        Assert.equal(self.driver.title, 'Yahoo')

    def test_good_title(self):
        """ test google title """
        self.search_page.search_field.send_keys('Jaromir Jagr')
        time.sleep(3)
        Assert.equal(self.search_page.jagr_title.text, 'Jaromír Jágr'.decode('utf8'))