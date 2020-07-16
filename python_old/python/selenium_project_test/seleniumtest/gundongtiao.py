from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(600,600)

driver.find_element_by_id("kw").send_keys("selenium")
sleep(1)
driver.find_element_by_id("su").click()

js = "window.scrollTo(100,400);"     #滚动条的位置

driver.execute_script(js)
sleep(2)

driver.quit()