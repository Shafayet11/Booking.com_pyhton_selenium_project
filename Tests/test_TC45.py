from Pages.AirTaxiPage import AirTaxiPage
from Tests.BasePage import BasePage
import time


class AirTaxiTest(BasePage):
    def test_Air_Taxi_page(self):
        airtaxi = AirTaxiPage(self. driver)
        airtaxi.click_Air_Taxi()
        time.sleep(3)