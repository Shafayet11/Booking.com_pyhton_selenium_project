from Pages.StaysPage import StaysPage
from Tests.BasePage import BasePage
import time


class PersonTest(BasePage):
    def test_dropdown(self):
        dropdn = StaysPage(self.driver)
        dropdn.click_dropdown()
        dropdn.click_adult_pos()
        time.sleep(3)
        dropdn.click_adult_neg()
        time.sleep(5)
        dropdn.click_child_pos()
        time.sleep(5)
        dropdn.click_child_neg()
        time.sleep(2)
        dropdn.click_rooms_pos()
        time.sleep(2)
        dropdn.click_room_neg()
        time.sleep(3)

