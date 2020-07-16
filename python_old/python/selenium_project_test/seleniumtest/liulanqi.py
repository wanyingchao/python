from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.set_window_size(480,800)   #控制浏览器的大小
sleep(2)
driver.refresh()
sleep(2)
driver.maximize_window()      #浏览器全屏
sleep(2)

driver.get("https://www.baidu.com")

sleep(1)

driver.back()    #浏览器后退

sleep(1)

driver.forward()  #浏览器前进
driver.quit()