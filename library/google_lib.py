# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Google project-specific function library
"""
from salsa_webqa.library.test_control import TestControl


class GoogleControl(TestControl):

    def __init__(self):
        TestControl.__init__(self)

    def do_some_google_specific_stuff(self):
        print 'this is some google project specific text!'

    def start_browser(self, build_name=None, url=None, browser=None, width=None, height=None):
        """ Browser startup function.
         Initialize session over Browserstack or local browser. """
        # get default parameter values
        browser, height, url, width = self.get_default_browser_attributes(browser, height, url, width)

        self.do_some_google_specific_stuff()

        if browser.lower() == "browserstack":
            self.call_browserstack_browser(build_name)
        else:
            self.call_local_browser(browser)
            self.driver.set_window_size(width, height)

        self.test_init(url, browser)
        return self.driver