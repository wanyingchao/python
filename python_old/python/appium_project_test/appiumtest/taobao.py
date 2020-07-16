# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep


desired_caps = {"platformName":"Android",
                "deviceName":"621QECQ63KZTB",
                "platformVersion":"4.4.2",
                 # apk包名
                "appPackage":"com.taobao.taobao",
                # apk的launcherActivity
                "appActivity":"com.taobao.tao.welcome.Welcome",
                "unicodeKeyboard":True,
                "resetKeyboard":True}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/uik_mdButtonDefaultPositive").click()
sleep(2)
driver.find_element_by_id("com.taobao.taobao:id/yes").click()
sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
sleep(2)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").clear()
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"鞋子")