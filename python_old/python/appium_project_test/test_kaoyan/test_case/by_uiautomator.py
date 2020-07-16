# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


desired_caps = {"platformName": "Android",
                "deviceName": "621QECQ63KZTB",
                "platformVersion": "7.0",
                "noReset":True,
                # apk包名
                "appPackage": "com.tal.kaoyan",
                # apk的launcherActivity
                "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
                "unicodeKeyboard": True,
                "resetKeyboard": True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(2)


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

driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id("com.tal.kaoyan:id/login_email_edittext"))     # 显示等待
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').clear()
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys("自学网测试")
# driver.find_element_by_android_uiautomator('new UiSelector().text("请输入用户名")').send_keys("自学网测试")
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText")').send_keys("自学网测试")
