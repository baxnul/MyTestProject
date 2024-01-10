from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'In URL ABSENT LOGIN word'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        reg_email = self.get_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_passw1 = self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        reg_passw2 = self.get_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        reg_submit_button = self.get_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        reg_email.send_keys(email)
        reg_passw1.send_keys(password)
        reg_passw2.send_keys(password)
        reg_submit_button.click()
