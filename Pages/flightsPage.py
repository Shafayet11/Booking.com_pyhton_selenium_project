from Locators.Locators import FlightLocators
from Pages.HomePage import HomePage
import time


class FlightsPage(HomePage):

    def __init__(self, driver):
        self.locator = FlightLocators
        self.driver = driver
        super(FlightsPage, self).__init__(driver)

    def click_on_flights(self):
        self.find_element(*self.locator.FLIGHTS_BTN).click()

    def click_on_trip(self):
        self.find_element(*self.locator.CLICK_TRIP).click()

    def click_on_Oneway(self):
        self.find_element(*self.locator.CLICK_ONEWAY).click()

