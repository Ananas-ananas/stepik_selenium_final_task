from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fill_input(*LoginPageLocators.REGISTER_EMAIL, email)
        self.fill_input(*LoginPageLocators.REGISTER_PWD, password)
        self.fill_input(*LoginPageLocators.REGISTER_CONFIRM_PWD, password)

        self.click_element(*LoginPageLocators.REGISTER_BUTTON)
           
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Word 'login' not in URL "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
        
