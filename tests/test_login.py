
import pytest

from tests.base_test import BaseTest
from data.test_data import users


@pytest.mark.usefixtures("test_status")
class TestLoginForm(BaseTest):

    def test_e2e_login_success(self):
        """verify positive scenario of login, visibility of expected elements."""
        assert self.login_page.heading == 'Log in'
        assert self.login_page.name_placeholder == 'Username'
        assert self.login_page.password_placeholder == 'Password'
        assert self.login_page.submit_button.text == 'Log in'
        assert self.login_page.remember_me_visible
        assert self.login_page.forgot_password_visible

        self.login_page.login(users['admin']['login_name'], users['admin']['password'])

        assert self.login_page.successful_login == 'Confirmation\nForm submitted successfully. It\'s just for testing purpose, ' \
                                         'data not saved.'

    def test_e2e_login_validation_warnings(self):
        """fill wrong login values and check warnings and invalid input style."""
        self.login_page.login('', '')

        assert self.login_page.count_invalid_inputs() == 2

        self.login_page.login('JohnDoe2', '')

        assert self.login_page.count_invalid_inputs() == 1

        # assert self.login_page.warning_text == "wrong name or password"

    def test_e2e_login_enter_and_tab(self):
        """Verify that keyboard shortcut ENTER trigger submitting form. TAB change active cursor."""

        self.login_page.fill_username()
        self.login_page.hit_tab()
        self.login_page.fill_password()
        self.login_page.hit_enter()

        assert self.login_page.successful_login == 'Confirmation\nForm submitted successfully. It\'s just for testing purpose, ' \
                                                   'data not saved.'

    def test_e2e_back_button_dont_logout_user(self):
        """Verify that clicking on browser back button after successful login should not take User to log out mode"""

        self.login_page.login(users['admin']['login_name'], users['admin']['password'])
        assert self.login_page.successful_login == 'Confirmation\nForm submitted successfully. It\'s just for testing purpose, ' \
                                                   'data not saved.'

        self.driver.back()

        assert not self.login_page.is_form_visible()
