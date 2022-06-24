from Pages.RegisterPages import RegisterPages
from Tests.BasePage import BasePage
import time


class GoogleTest(BasePage):
    def test_reg_page(self):
        regpage = RegisterPages(self.driver)
        regpage.click_on_register()
        time.sleep(3)
        regpage.click_more_ways_btn()
        time.sleep(3)
        regpage.click_apple_btn()