from Pages.StaysPage import StaysPage
from Tests.BasePage import BasePage
import time


class DateTest(BasePage):
    def test_date_input(self):
        datetest = StaysPage(self.driver)
        datetest.click_on_date()
        datetest.set_checkin_date()
        time.sleep(3)
        datetest.set_Checkout_date()
        time.sleep(3)
