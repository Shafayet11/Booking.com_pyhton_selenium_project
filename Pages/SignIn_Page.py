from Locators.Locators import SigninLocators
from Pages.HomePage import HomePage
import time


class SigninPage(HomePage):

    def __init__(self, driver):
        self.locator = SigninLocators
        self.driver = driver
        super(SigninPage, self).__init__(driver)

    def click_signin(self):
        self.find_element(*self.locator.SIGNIN_BTN).click()

    def set_email(self, email):
        self.find_element(*self.locator.INPUT_EMAIL).send_keys(email)

    def click_continue(self):
        self.find_element(*self.locator.CONTINUE_EMAIL).click()

    def set_password(self, password):
        self.find_element(*self.locator.ENTER_PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(*self.locator.CLICK_SIGNIN).click()
