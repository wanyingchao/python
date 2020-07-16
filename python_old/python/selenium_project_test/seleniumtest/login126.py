from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.126.com")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "x-URS-iframe")))
driver.switch_to_frame("x-URS-iframe")

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("a15708420051")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456aa")
driver.find_element_by_id("un-login").click()
driver.find_element_by_id("dologin").click()

sleep(1)

driver.quit()
