from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

desired_caps = {"platformName": "Android",
                "deviceName": "621QECQ63KZTB",
                "platformVersion": "7.0",
                "noReset":False,
                # apk包名
                "appPackage": "com.mymoney",
                # apk的launcherActivity
                "appActivity": "com.mymoney.biz.splash.SplashScreenActivity",
                "unicodeKeyboard": True,
                "resetKeyboard": True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)


a = ("//*[@text='允许']")
b = ("//*[@text='下一步']")
try:
    WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath(a))
    driver.find_element_by_xpath(a).click()
except:
    pass
try:
    WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(b))
    driver.find_element_by_xpath(b).click()
except:
    pass


def get_size():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return x, y


def swipe_left():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipe_up():
    l = get_size()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.95)
    y2 = int(l[1]*0.45)
    driver.swipe(x1, y1, x1, y2)

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/begin_finance_btn"))
for i in range(2):
    swipe_left()

driver.find_element_by_id("com.mymoney:id/begin_finance_btn").click()
try:
    WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(a))
    driver.find_element_by_xpath(a).click()
except:
    pass

driver.find_element_by_id("com.mymoney:id/nav_setting_btn").click()
for i in range(2):
    swipe_up()

driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("密码保护")').click()
driver.find_element_by_id("com.mymoney:id/content_container_ly").click()
driver.find_element_by_id("com.mymoney:id/ll_gesture_psd").click()

for i in range(2):
    TouchAction(driver).press(x=240, y=560).wait(2000)\
    .move_to(x=540, y=560).wait(1000)\
    .move_to(x=840, y=860).wait(1000)\
    .move_to(x=840, y=1150).wait(1000)\
    .release().perform()