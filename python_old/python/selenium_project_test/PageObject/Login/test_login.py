from Login.NewContract import *
from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(10)


test_user_login(driver)
# test_contract2(driver)
