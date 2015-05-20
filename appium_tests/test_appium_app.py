# -*- coding: utf-8 -*-
import pytest
import time
from unittestzero import Assert

from shishito.runtime.shishito_support import ShishitoSupport
from tests.conftest import get_test_info


@pytest.mark.usefixtures("test_status")
class TestAppiumApp():
    """ Contextual help test """

    def setup_class(self):
        self.tc = ShishitoSupport().get_test_control()
        self.driver = self.tc.start_browser()

    def teardown_class(self):
        self.tc.stop_browser()

    def setup_method(self, method):
        self.tc.start_test(True)

    def teardown_method(self, method):
        test_info = get_test_info()
        self.tc.stop_test(test_info)

    ### Tests ###
    @pytest.mark.smoke
    def test_ios_app(self):
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAToolbar[1]/UIATextField[2]").click()
        self.driver.find_element_by_name("Clear text").click()

        # loads Google homepage
        bar = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAToolbar[1]/UIATextField[1]")
        bar.click()
        bar.send_keys("www.google.com")
        self.driver.find_element_by_name("Go").click()

        time.sleep(5)

        google_input = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAElement[1]')
        tested_test = 'try to find this'
        google_input.send_keys(tested_test)
        Assert.equal(google_input.get_attribute('value'), tested_test)

    @pytest.mark.smoke
    def test_android_app(self):
        el = self.driver.find_element_by_accessibility_id("New note")
        el.click()

        el = self.driver.find_element_by_class_name("android.widget.EditText")
        el.send_keys("This is a new note!")

        el = self.driver.find_element_by_accessibility_id("Save")
        el.click()

        els = self.driver.find_elements_by_class_name("android.widget.TextView")
        Assert.equal(els[2].text, "This is a new note!")
