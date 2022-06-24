from Locators.Locators import StaysLocators
from Pages.HomePage import HomePage
import time


class StaysPage(HomePage):

    def __init__(self, driver):
        self.locator = StaysLocators
        self.driver = driver
        super(StaysPage, self).__init__(driver)

    def click_on_stays(self):
        self.find_element(*self.locator.STAYS_BTN).click()

    def set_Where_are_u_Going(self, place):
        self.find_element(*self.locator.PLACE_INPUT).send_keys(place)

    def click_on_date(self):
        self.find_element(*self.locator.DATE_INPUT).click()

    def set_checkin_date(self):
        self.find_element(*self.locator.PICK_CHECKIN_DATE).click()

    def set_Checkout_date(self):
        self.find_element(*self.locator.PICK_CHECKOUT_DATE).click()

    def click_dropdown(self):
        self.find_element(*self.locator.CLICK_DROPDOWN).click()

    def click_adult_pos(self):
        self.find_element(*self.locator.CLICK_ADULT_POS).click()

    def click_adult_neg(self):
        self.find_element(*self.locator.CLICK_ADULT_NEG).click()

    def click_child_pos(self):
        self.find_element(*self.locator.CLICK_CHILD_POS).click()

    def click_child_neg(self):
        self.find_element(*self.locator.CLICK_CHILD_NEG).click()

    def click_rooms_pos(self):
        self.find_element(*self.locator.CLICK_ROOMS_POS).click()

    def click_room_neg(self):
        self.find_element(*self.locator.CLICK_ROOMS_NEG).click()





