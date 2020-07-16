from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.youdao.com")

driver.find_element_by_id("translateContent").send_keys("hello")

sleep(1)

driver.find_element_by_id("translateContent").submit()

sleep(2)

driver.quit()