from Pages.StaysPage import StaysPage
from Tests.BasePage import BasePage
import time


class PlaceTest(BasePage):
    def test_place_input(self):
        placeinput = StaysPage(self.driver)
        placeinput.set_Where_are_u_Going("Uganda")
        time.sleep(3)

