from selenium import webdriver
import time

def login_A8(driver,name="肖进",password="123456abc"):
    driver.find_element_by_id("login_username").send_keys(name)
    driver.find_element_by_id("login_password").send_keys(password)
    driver.find_element_by_id("login_button").click()