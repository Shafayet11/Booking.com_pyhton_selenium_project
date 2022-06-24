from Pages.RegisterPages import RegisterPages
from Tests.BasePage import BasePage
import time


class RegTest(BasePage):
    def test_reg_page(self):
        regpage = RegisterPages(self.driver)
        regpage.click_on_register()
        time.sleep(3)
        regpage.click_fb_btn()
