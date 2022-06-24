from Pages.flightsPage import FlightsPage
from Tests.BasePage import BasePage
import time


class TripTest(BasePage):
    def test_trip(self):
        trip = FlightsPage(self.driver)
        trip.click_on_flights()
        time.sleep(5)
        trip.click_on_trip()
        time.sleep(2)
        trip.click_on_Oneway()
        time.sleep(3)

