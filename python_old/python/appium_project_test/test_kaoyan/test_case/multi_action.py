from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


desired_caps = {"platformName": "Android",
                "deviceName": "127.0.0.1:52001",
                "platformVersion": "4.4.2",
                # "noReset":False,
                # apk包名
                "appPackage": "com.baidu.BaiduMap",
                # apk的launcherActivity
                "appActivity": "com.baidu.baidumaps.WelcomeScreen",
                "unicodeKeyboard": True,
                "resetKeyboard": True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

x = driver.get_window_size()["width"]
y = driver.get_window_size()["height"]

WebDriverWait(driver,5).until(lambda x:x.find_element_by_id("com.baidu.BaiduMap:id/ok_btn"))
driver.find_element_by_id("com.baidu.BaiduMap:id/ok_btn").click()

driver.find_element_by_id("com.baidu.BaiduMap:id/btn_enter_map").click()
sleep(10)

def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    action1.press(x=x*0.2, y=y*0.2).wait(1000).move_to(x=x*0.4, y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8, y=y*0.8).wait(1000).move_to(x=x*0.6, y=y*0.6).wait(1000).release()

    pinch_action.add(action1,action2)
    print("start action....")
    pinch_action.perform()

def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    zoom_action.add(action1, action2)
    print("start action....")
    zoom_action.perform()

if __name__ == "__main__":
    for i in range(5):
        pinch()
    sleep(3)
    for i in range(3):
        zoom()
