from Pages.CarRental_Page import CarPage
from Tests.BasePage import BasePage
import time


class DiffLocTest(BasePage):
    def test_DFLOC(self):
        dflc = CarPage(self.driver)
        dflc.click_on_car_rental()
        time.sleep(3)
        dflc.click_dif_loc()
