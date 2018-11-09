import logging

import pytest
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.remote_connection import LOGGER

from helpers.mock_client import MockClient
from pages.app_page import App
from pages.login_page import LoginPage

from shishito.conf.conftest import get_test_info
from shishito.runtime.shishito_support import ShishitoSupport
from shishito.ui.selenium_support import SeleniumTest


class BaseTest:

    @pytest.fixture(autouse=True)
    def analytics_setup(self):
        self.mock_api_url = ShishitoSupport().get_opt('at_server_url')
        self.mock_client = MockClient(self.mock_api_url)


    @pytest.fixture(autouse=True)
    def class_variables(self, create_base_url, test_control):
        self.tc = test_control
        self.base_url = create_base_url

        self.mock_client.clear_analytics_events(origin=self.base_url)
        self.mock_client.clear_analytics_pages(origin=self.base_url)

        self.driver = self.tc.start_browser(self.base_url + '/app/bom')  # type: WebDriver

        # Pages
        self.app = App(self.driver)
        self.homepage = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

        # Stripe integration
        self.stripe = stripe
        self.stripe.api_key = 'sk_test_gtgjM7SwAnjGg9wBQ5UWahTY'

    @pytest.fixture(autouse=True)
    def setup(self, request):
        LOGGER.setLevel(logging.WARNING)

        self.ts = SeleniumTest(self.driver)

        # Pretend that DigiKey is logged in
        self.api_settings_url = self.base_url + '/app/api/settings'
        self.backoffice_url = self.base_url + '/backoffice'

        settings = {
            "distributor": "digikey",
            "settings": {"login": 2}
        }
        r = requests.post(self.api_settings_url, json=settings)

        yield

        console_events = self.driver.get_log('browser')
        self.tc.stop_test(get_test_info(), debug_events=console_events)
        print(self.mock_client.get_events_data(origin=self.base_url))
        print(self.mock_client.get_pages_data(origin=self.base_url))
        self.tc.stop_browser(driver=self.driver)