from Pages.CarRental_Page import CarPage
from Tests.BasePage import BasePage
import time


class CarRentTest(BasePage):
    def test_car_rent_page(self):
        carRentpage = CarPage(self. driver)
        carRentpage.click_on_car_rental()
        time.sleep(3)