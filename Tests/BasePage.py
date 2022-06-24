from selenium import webdriver
import time
import unittest


class BasePage(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="I:/Booking_Project/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.booking.com/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        print("Test Complete")
        cls.driver.quit()
