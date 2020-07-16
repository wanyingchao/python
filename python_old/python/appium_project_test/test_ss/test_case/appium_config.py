# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep, ctime


def appium_start():
    desired_caps = {"platformName": "Android",
                    "deviceName": "127.0.0.1:62001",
                    "platformVersion": "4.4.2",
                    # apk包名
                    "appPackage": "com.ss.android.article.news",
                    # apk的launcherActivity
                    "appActivity": "com.ss.android.article.news.activity.SplashActivity",
                    "unicodeKeyboard": True,
                    "resetKeyboard": True}
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
