from Locators.Locators import AttractionsLocators
from Pages.HomePage import HomePage


class AttractionsPage(HomePage):

    def __init__(self, driver):
        self.locator = AttractionsLocators
        self.driver = driver
        super(AttractionsPage, self).__init__(driver)

    def click_on_AttrBTN(self):
        self.find_element(*self.locator.ATTR_BTN).click()

    def set_search(self, srch):
        self.find_element(*self.locator.SET_SEARCH).send_keys(srch)
