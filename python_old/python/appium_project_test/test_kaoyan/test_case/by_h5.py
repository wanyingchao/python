# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_caps = {"platformName": "Android",
                "deviceName": "127.0.0.1:52001",
                "platformVersion": "4.4.2",
                # "noReset":True,
                # "automationName":"uiautomator2",
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
check_skipBtn()


def login():
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("自学网测试")
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("wyc1063983073")
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()


try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()
    login()

driver.find_element_by_id("com.tal.kaoyan:id/tv_agree").click()
driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_bx").click()
time.sleep(2)
driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_bx").click()
