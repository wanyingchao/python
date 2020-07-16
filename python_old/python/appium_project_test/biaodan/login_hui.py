from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep,ctime

def login(driver,phone="",password=""):
    driver.find_element_by_id("loginBtn-text").click()
    driver.switch_to.frame("indexFrame")
    driver.find_element_by_id("js-phone-num").clear()
    sleep(2)
    driver.find_element_by_id("js-phone-num").send_keys(phone)
    driver.find_element_by_id("js-get-code").click()
    sleep(2)
    driver.find_element_by_id("js-code-val").send_keys(password)
    driver.find_element_by_id("js-login-event").click()

def login_out(driver):
    driver.find_element_by_xpath("//*[@id='u545']/p/span").click()  # 退出