from Pages.StaysPage import StaysPage
from Tests.BasePage import BasePage
import time


class StaysTest(BasePage):
    def test_stays_page(self):
        staypage = StaysPage(self.driver)
        staypage.click_on_stays()
        time.sleep(3)
