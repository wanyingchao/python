from appium import webdriver
from appium_szb.desired_caps.desired_caps import *
from time import sleep
from selenium.webdriver.common.by import By

driver = appium_desired()
sleep(5)
driver.find_element(By.ID, 'com.cn.szb.customer:id/ali_login_username').send_keys('销售001')
sleep(1)
driver.find_element(By.ID, 'com.cn.szb.customer:id/ali_login_pwd').send_keys('123456')
sleep(1)
driver.find_element(By.ID, 'com.cn.szb.customer:id/ali_login_btn').click()
sleep(5)
driver.find_element(By.LINK_TEXT, '工作').click()
sleep(1)
driver.find_element(By.ID, 'com.cn.szb.customer:id/work_btn_name').click()
sleep(1)
driver.find_element(By.ID, 'com.cn.szb.customer:id/page_header_layout_more').click()

