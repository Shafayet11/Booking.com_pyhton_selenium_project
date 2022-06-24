from Pages.AttractionsPage import AttractionsPage
from Tests.BasePage import BasePage
import time


class SearchTest(BasePage):
    def test_search(self):
        src = AttractionsPage(self.driver)
        src.click_on_AttrBTN()
        src.set_search("Greenland")
        time.sleep(3)