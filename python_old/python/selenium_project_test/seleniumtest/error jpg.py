from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

driver.get_screenshot_as_file("E:/python/screenshot/screenshot.png")   #最后一个是截图文件名，以.png结尾

driver.quit()