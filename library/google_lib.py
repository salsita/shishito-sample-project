# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Vojtech Burian
@summary: Google project-specific function library
"""
from salsa_webqa.library.control_test import ControlTest


class GoogleControl(ControlTest):

    def __init__(self):
        ControlTest.__init__(self)

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
            self.call_browser(browser.lower())
            self.driver.set_window_size(width, height)

        self.test_init(url)
        return self.driver