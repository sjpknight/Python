__author__ = 'sknight'

import unittest
import pywinauto
import time
# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import page


class printTestWithIELogin(unittest.TestCase):
    # create the pywinauto object
    PWA_APP = pywinauto.Application()

    def setUp(self):
        self.driver = webdriver.Ie()

    def test_all_non_login_prints_in_IE(self):
        with open('data/barnetPrintURLsShort.txt', 'r') as urls:
            for line in urls:
                print ('going to: ' + line)
                page.HomePage(self.driver).goto_args_page_IE(line)
                print ('attempting to print: ' + line)
                page.HomePage(self.driver).print_screen()
                # need to shutdown the browser and have a bit of a rest between each cycle
                self.driver.quit()
                time.sleep(5)
                # need to setup the driver again for this test
                self.driver = webdriver.Ie()

    def test_all_login_prints_in_IE(self):
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_benefits()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Ie()
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_bins()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Ie()
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_council_tax()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Ie()
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_libraries()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Ie()
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_report_a_problem()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Ie()
        page.HomePage(self.driver).goto_home_page_IE()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_parking()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()