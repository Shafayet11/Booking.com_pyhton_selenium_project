from Locators.Locators import AirportTaxisLocators
from Pages.HomePage import HomePage


class AirTaxiPage(HomePage):

    def __init__(self, driver):
        self.locator = AirportTaxisLocators
        self.driver = driver
        super(AirTaxiPage, self).__init__(driver)

    def click_Air_Taxi(self):
        self.find_element(*self.locator.AIRTAXI_BTN).click()