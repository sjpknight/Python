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


class printTestWithChromeLogin(unittest.TestCase):
    # need to setup a webdriver profile so that the print dialog screen is skipped
    CHROME_OPTIONS = Options()
    CHROME_OPTIONS.add_argument("--disable-print-preview")
    # create the pywinauto object
    PWA_APP = pywinauto.Application()

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)

    def test_all_non_login_prints_in_chrome(self):
        with open('data/barnetPrintURLsShort.txt', 'r') as urls:
            for line in urls:
                print ('going to: ' + line)
                page.HomePage(self.driver).goto_args_page(line)
                print ('attempting to print: ' + line)
                page.HomePage(self.driver).print_screen()
                # need to shutdown the browser and have a bit of a rest between each cycle
                self.driver.quit()
                time.sleep(5)
                # need to setup the driver again for this test
                self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)

    def test_all_login_prints_in_chrome(self):
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_benefits()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_bins()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_council_tax()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_libraries()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_report_a_problem()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()
        time.sleep(5)
        # need to setup the driver again for this test
        self.driver = webdriver.Chrome(chrome_options=self.CHROME_OPTIONS)
        page.HomePage(self.driver).goto_home_page()
        page.HomePage(self.driver).login()
        page.HomePage(self.driver).goto_parking()
        page.HomePage(self.driver).print_screen()
        self.driver.quit()


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()