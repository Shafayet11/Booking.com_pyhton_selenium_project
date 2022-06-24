from Pages.CarRental_Page import CarPage
from Tests.BasePage import BasePage
import time


class SameLocTest(BasePage):
    def test_SMLOC(self):
        smlc = CarPage(self.driver)
        smlc.click_on_car_rental()
        time.sleep(3)
        smlc.click_sm_loc()
