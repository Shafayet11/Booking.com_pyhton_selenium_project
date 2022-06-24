from Locators.Locators import RegisterLocators
from Pages.HomePage import HomePage
import time


class RegisterPages(HomePage):

    def __init__(self, driver):
        self.locator = RegisterLocators
        self.driver = driver
        super(RegisterPages, self).__init__(driver)

    def click_on_register(self):
        self.find_element(*self.locator.REG_BTN).click()

    def set_email(self, email):
        self.find_element(*self.locator.SET_EMAIL).send_keys(email)

    def click_continue(self):
        self.find_element(*self.locator.CONTINUE_EMAIL).click()

    def new_password(self, password):
        time.sleep(3)
        self.find_element(*self.locator.NEW_PASSWORD).send_keys(password)

    def confirm_password(self, password):
        self.find_element(*self.locator.CONFIRM_PASSWORD).send_keys(password)

    def click_create_ac(self):
        self.find_element(*self.locator.CREATE_ACCOUNT).click()

    def click_fb_btn(self):
        self.find_element(*self.locator.FB_BTN).click()

    def click_google_btn(self):
        self.find_element(*self.locator.GOOGLE_BTN).click()

    def click_more_ways_btn(self):
        self.find_element(*self.locator.MORE_WAYS_BTN).click()

    def click_apple_btn(self):
        self.find_element(*self.locator.APPLE_BTN).click()

