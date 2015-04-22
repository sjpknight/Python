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
import page

QA2 = "https://barnet-qa2.technophobia.int/"
UAT = "https://barnet-gateway.technophobia.int/"
DESIRED_ENV = UAT


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def goto_home_page(self):
        self.driver.get(DESIRED_ENV + 'citizen-home/')

    def goto_home_page_IE(self):
        self.driver.get(DESIRED_ENV + 'citizen-home/')
        self.driver.execute_script("javascript:document.getElementById('overridelink').click()")

    def goto_args_page_IE(self, url):
        self.driver.get(DESIRED_ENV + url)
        self.driver.execute_script("javascript:document.getElementById('overridelink').click()")
        time.sleep(5)

    def login(self):
        login_link_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-link")))
        login_link_element.click()

        # gotta wait for the lightbox and fields to be visible
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "lightbox-modal")))
        except:
            print("lightbox fail")
        finally:
            print("lightbox success")
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "password")))
        except:
            print("password field fail")
        finally:
            print("password field success")

        email_field_element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "email")))
        email_field_element.send_keys("sknight-auto1@g2g3.digital")
        password_field_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "password")))
        password_field_element.send_keys("P@55w0rd", Keys.ENTER)

        # now we need to wait for the homepage to load
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "leaflet-zoom-animated")))
        except:
            print("homepage load fail")
        finally:
            print("homepage loaded")

    def print_screen(self):
        # setup pwyinauto
        PWA_APP = pywinauto.Application()
        # pwa_app = self.PWA_APP
        # execute javascript to print the page
        self.driver.execute_script("window.print()")
        # now use pywinauto to interact with the Windows dialog and click the print button
        a_check = lambda: pywinauto.findwindows.find_windows(title=u'Print', class_name='#32770')[0]
        try:
            dialog = pywinauto.timings.WaitUntilPasses(5, 1, a_check)
            window = PWA_APP.window_(handle=dialog)
            window.SetFocus()
            ctrl = window['&Print']
            ctrl.Click()
            # need an explicit wait to allow the print to go through so we can quit the browser instance
            time.sleep(5)
            #self.driver.quit()
        except:
            print("Something went wrong")
        finally:
            print("success!")

    def verify_page_title(self, title):
        driver = self.driver
        # verify we're on the right page
        try:
            titleElement = WebDriverWait(driver, 30).until(EC.title_is(title))
        finally:
            print("homepage load fail")

    def goto_parking(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "parking")))
        myWaitElement.click()
        #self.verify_page_title("Parking and Travel - barnet.gov.uk")

    def goto_council_tax(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "council-tax")))
        myWaitElement.click()
        #self.verify_page_title("Council Tax - barnet.gov.uk")

    def goto_benefits(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "benefits")))
        myWaitElement.click()
        #self.verify_page_title("Benefits - barnet.gov.uk")

    def goto_libraries(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "libraries")))
        myWaitElement.click()
        #self.verify_page_title("Libraries - barnet.gov.uk")

    def goto_report_a_problem(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Report a problem")))
        myWaitElement.click()
        #self.verify_page_title("Report a problem - barnet.gov.uk")

    def goto_bins(self):
        driver = self.driver
        #self.goto_home_page()
        myWaitElement = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "waste-collection")))
        myWaitElement.click()
        #self.verify_page_title("Bins & waste collection - barnet.gov.uk")
