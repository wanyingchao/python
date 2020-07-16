# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_caps = {"platformName": "Android",
                "deviceName": "621QECQ63KZTB",
                "platformVersion": "7.0",
                # "noReset":True,
                "automationName":"uiautomator2",
                # apk包名
                "appPackage": "com.tal.kaoyan",
                # apk的launcherActivity
                "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
                "unicodeKeyboard": True,
                "resetKeyboard": True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)


def check_cancelBtn():
    print("check_cancelBtn")

    try:
        cancelBtn = driver.find_element_by_id("android:id/button2")
    except NoSuchElementException:
        print("no cancelBtn")
    else:
        cancelBtn.click()

def check_skipBtn():
    print("check_skipBtn")

    try:
        skipBtn = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
    except NoSuchElementException:
        print("no skipBtn")
    else:
        skipBtn.click()


check_cancelBtn()
# check_skipBtn()

def get_size():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return x, y
l = get_size()
print(l)

def swipe_left():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1, y1, x2, y1, 1000)

for i in range(2):
    swipe_left()
    time.sleep(0.5)

def swipe_right():
    l = get_size()
    x1 = int(l[0]*0.1)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.9)
    driver.swipe(x1, y1, x2, y1, 1000)


for i in range(2):
    swipe_right()
    time.sleep(0.5)