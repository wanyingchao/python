# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep


desired_caps = {"platformName":"Android",
                "deviceName":"127.0.0.1:62001",
                "platformVersion":"4.4.2",
                 # apk包名
                "appPackage":"com.cn.player",
                # apk的launcherActivity
                "appActivity":"com.cn.player.MainActivity",
                "unicodeKeyboard":True,
                "resetKeyboard":True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(5)
print(driver.contexts)