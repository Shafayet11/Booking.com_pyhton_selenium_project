from Pages.flightsPage import FlightsPage
from Tests.BasePage import BasePage
import time


class FlightsTest(BasePage):
    def test_signin_page(self):
        flightPage = FlightsPage(self.driver)
        flightPage.click_on_flights()
        time.sleep(3)