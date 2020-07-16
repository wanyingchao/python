from selenium import webdriver
import unittest
from time import sleep,ctime


def login_regular(driver,phone="18583965785"):
    driver.find_element_by_id("loginBtn-text").click()
    driver.switch_to.frame("indexFrame")
    driver.find_element_by_id("js-phone-num").clear()
    driver.find_element_by_id("js-code-val").clear()
    driver.find_element_by_id("js-phone-num").send_keys(phone)
    driver.find_element_by_id("js-get-code").click()
    sleep(1)
    driver.switch_to.default_content()
    text = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/p").text
    driver.switch_to_frame("indexFrame")
    driver.find_element_by_id("js-code-val").send_keys(text)
    driver.find_element_by_id("js-login-event").click()
    sleep(10)

def login_test(driver,phone="12055116631"):
    driver.find_element_by_id("loginBtn-text").click()
    driver.switch_to.frame("indexFrame")
    driver.find_element_by_id("js-phone-num").clear()
    driver.find_element_by_id("js-code-val").clear()
    driver.find_element_by_id("js-phone-num").send_keys(phone)
    driver.find_element_by_id("js-get-code").click()
    sleep(1)
    driver.find_element_by_id("js-login-event").click()
    sleep(10)