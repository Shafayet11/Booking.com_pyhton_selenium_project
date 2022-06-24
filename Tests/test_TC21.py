from Pages.RegisterPages import RegisterPages
from Tests.BasePage import BasePage
import time


class RegTest(BasePage):
    def test_reg_page(self):
        regpage = RegisterPages(self.driver)
        regpage.click_on_register()
        time.sleep(2)
        regpage.set_email("qups12@gmail.com")
        regpage.click_continue()
        regpage.new_password("Qups12345678")
        regpage.confirm_password("Qups12345678")
        time.sleep(3)
        regpage.click_create_ac()


