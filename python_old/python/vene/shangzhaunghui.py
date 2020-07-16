

from random import randint
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.91szb.com/")

driver.find_element_by_id('loginBtn-text').click()
sleep(8)

driver.switch_to_frame("indexFrame")

driver.find_element_by_id("js-phone-num").send_keys("18398929673")
driver.find_element_by_id("js-get-code").click()
driver.find_element_by_xpath(".//*[@id='js-code-val']").send_keys("12345")
driver.find_element_by_id("js-login-event").click()

driver.quit()
