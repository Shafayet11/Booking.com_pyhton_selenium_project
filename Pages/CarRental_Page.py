from Locators.Locators import CarRentalLocators
from Pages.HomePage import HomePage


class CarPage(HomePage):

    def __init__(self, driver):
        self.locator = CarRentalLocators
        self.driver = driver
        super(CarPage, self).__init__(driver)

    def click_on_car_rental(self):
        self.find_element(*self.locator.CAR_BTN).click()

    def click_sm_loc(self):
        self.find_element(*self.locator.RET_SM_LOC).click()

    def click_dif_loc(self):
        self.find_element(*self.locator.RET_DF_LOC).click()

    def set_pick_loc(self, location):
        self.find_element(*self.locator.PICKUP_LOC).send_keys(location)

    def set_drop_loc(self, location):
        self.find_element(*self.locator.DROPUP_LOC).send_keys(location)

    def click_date(self):
        self.find_element(*self.locator.CLICK_DATE).click()

    def set_date(self):
        self.find_element(*self.locator.DATE_SET_FROM).click()

    def set_date_to(self):
        self.find_element(*self.locator.DATE_SET_TO).click()