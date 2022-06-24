import time

from Pages.CarRental_Page import CarPage
from Tests.BasePage import BasePage


class DateTest(BasePage):
    def test_Date(self):
        dt = CarPage(self.driver)
        dt.click_on_car_rental()
        dt.click_date()
        time.sleep(2)
        dt.set_date()
        dt.set_date_to()