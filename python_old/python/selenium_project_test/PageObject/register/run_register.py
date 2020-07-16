from RegisterPage import *
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


test_register2(driver)
