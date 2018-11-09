from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class LoginPage(BasePage):
    """login form page object."""
    _login_form = By.CSS_SELECTOR, 'form'
    _heading = By.CSS_SELECTOR, 'h2'
    _username = By.CSS_SELECTOR, 'input#inputEmail'

    _password = By.CSS_SELECTOR, 'input#inputPassword'

    _invalid_inputs = By.CSS_SELECTOR, 'input:invalid'

    _submit_button = By.CSS_SELECTOR, 'button[type="submit"]'
    _warning_label = By.CSS_SELECTOR, 'div.form-error'
    _successful_login_label = By.CSS_SELECTOR, 'div'
    _remember_me_checkbox = By.CSS_SELECTOR, 'input[type="checkbox"]'
    _forgot_pwd = By.CSS_SELECTOR, 'div.clearfix a'

    @property
    def is_form_visible(self)->bool:
        return bool(len(self.find_elements(*self._login_form)))

    @property
    def heading(self)->str:
        return self.find_element(*self._heading).text

    @property
    def username(self) -> WebElement:
        return self.wait_for_element(*self._username)

    @property
    def password(self) -> WebElement:
        return self.wait_for_element(*self._password)

    @property
    def submit_button(self) -> WebElement:
        return self.wait_for_element(*self._submit_button)

    @property
    def count_invalid_inputs(self) -> int:
        """
        Use in case chrome built-in form validation is implemented.
        https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation#Using_built-in_form_validation
        :return amount of invalid fields:
        """
        return len(self.find_elements(*self._invalid_inputs))

    @property
    def name_warning_text(self) -> str:
        return self.wait_for_element(*self._warning_label).text

    @property
    def name_placeholder(self) -> str:
        return self.find_element(*self._username).get_attribute('placeholder')

    @property
    def password_placeholder(self) -> str:
        return self.find_element(*self._password).get_attribute('placeholder')

    @property
    def successful_login(self) -> str:
        """:return text which is present only in case of successful login."""
        return self.find_element(*self._successful_login_label).text

    @property
    def remember_me(self)-> WebElement:
        return self.find_element(*self._remember_me_checkbox)

    @property
    def remember_me_visible(self)->bool:
        return self.remember_me.is_displayed()

    @property
    def forgot_password_visible(self):
        self.find_element(*self._forgot_pwd).is_displayed()

    def select_remember_me(self):
        self.remember_me.click()

    def open_forgot_password(self):
        self.find_element(*self._forgot_pwd).click()

    def login(self, usr: str, pwd: str):
        """fill in login form name and password. then hit submit form.
        :param usr: user name
        :param pwd: password"""
        self.username.send_keys(usr)
        self.password.send_keys(pwd)
        self.submit_button.click()
