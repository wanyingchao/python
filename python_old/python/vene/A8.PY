# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class A8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pt.91szb.com:8011/seeyon/main.do"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_a8(self):
        driver = self.driver
        driver.get(self.base_url + "/seeyon/main.do;jsessionid=007C9152CBA6173120FB5D373FFBBB1F.tomcat1")
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys(u"肖进")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("123456abc")
        driver.find_element_by_id("login_button").click()
        driver.find_element_by_id("submit_button").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | main | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | IframeSectionTemplete | ]]
        driver.find_element_by_id("row1065921117663936949").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | ctpPopup1536033117676 | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=zwIframe | ]]
        driver.find_element_by_xpath("(//span[@name='field0042'])[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=42483419_main_iframe | ]]
        driver.find_element_by_id("sizcache0649646476859005").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=ctpPopup1536033117676 | ]]
        driver.find_element_by_id("2064887_btn42483419").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
