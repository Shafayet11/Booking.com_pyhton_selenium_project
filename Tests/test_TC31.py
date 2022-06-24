from Pages.SignIn_Page import SigninPage
from Tests.BasePage import BasePage
import time


class SigninTest(BasePage):
    def test_signin_page(self):
        signinpage = SigninPage(self.driver)
        signinpage.click_signin()
        signinpage.set_email("mipam523@jooffy.com")
        signinpage.click_continue()
        time.sleep(3)
        signinpage.set_password("Qups123456")
        signinpage.click_login()
        time.sleep(3)
