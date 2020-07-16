from selenium import webdriver
from time import sleep
import os,time

driver = webdriver.Chrome()
driver.get("https://www.91szb.com")

driver.find_element_by_id("loginBtn-text").click()

# 找到iframe的id或name，使用switch_to_frame（）直接取
driver.switch_to_frame("indexFrame")
# 如果iframe没有可用的id或name，先用xpath定位到iframe，再将定位传给switch_to_frame（）
# iframe = driver.find_element_by_xpath("//*[@id='indexFrame']")
# driver.switch_to_frame(iframe)

driver.find_element_by_id("js-phone-num").send_keys("12055116631")
driver.find_element_by_id("js-get-code").click()
sleep(2)
driver.find_element_by_id("js-login-event").click()

# 如果完成了当前表单上的操作，则可以通过switch_to.parent_congent()方法跳出当前一级表单
# 该方法默认对应于离它最近的switch_to.frame()方法
# 在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面