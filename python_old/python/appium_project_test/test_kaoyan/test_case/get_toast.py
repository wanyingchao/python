# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_caps = {"platformName": "Android",
                "deviceName": "621QECQ63KZTB",
                "platformVersion": "7.0",
                "noReset":True,
                "automationName":"uiautomator2",
                # apk包名
                "appPackage": "com.tal.kaoyan",
                # apk的launcherActivity
                "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
                "unicodeKeyboard": True,
                "resetKeyboard": True}
driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)
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

# driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
# driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()

driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("自学网测试")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("wyc106398")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

error_message = "用户名或密码错误，你还可以尝试4次"
limit_message = "验证失败次数过多，请15分钟后再试"

message = "//*[@text=\'{}\']".format(error_message)
# message = "//*[@text=\'{}\']".format(limit_message)

toast_element = WebDriverWait(driver,10,0.1).until(lambda x:x.find_element_by_xpath(message))
time.sleep(2)
print(toast_element.text)
