from Pages.AttractionsPage import AttractionsPage
from Tests.BasePage import BasePage
import time


class AttractionsTest(BasePage):
    def test_Attr_page(self):
        AttrPage = AttractionsPage(self.driver)
        AttrPage.click_on_AttrBTN()
        time.sleep(3)
