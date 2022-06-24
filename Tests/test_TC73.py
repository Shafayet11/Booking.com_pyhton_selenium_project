from Pages.CarRental_Page import CarPage
from Tests.BasePage import BasePage
import time


class PickLocTest(BasePage):
    def test_PICKLOC(self):
        pklc = CarPage(self.driver)
        pklc.click_on_car_rental()
        pklc.click_dif_loc()
        time.sleep(3)
        pklc.set_pick_loc("Dhaka")
        time.sleep(3)
        pklc.set_drop_loc("Toronto")
