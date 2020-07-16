import os
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By


class Page:
    # driver 私有化
    def __init__(self, driver):
        self.driver = driver

    # 查找页面元素方法：查询某元素直到它出现，15秒超时
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未找到%s 元素" % (self, loc))

    # 查找元素组方法
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 截屏方法：获取当前页面尺寸，以此尺寸截屏加上时间戳并保存文件
    def get_screenshot(self, screenshot_name):
        x = self.driver.get_window_size()
        width = x['width']
        height = x['height']
        size = self.driver.set_window_size(width, height)
        img = ImageGrab.grab(size)

        now = time.strftime("%Y-%m-%d %H-%M-%S ")
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = base_path + "/Report/screenshots/" + now + screenshot_name + ".png"
        return img.save(file_path)

    # 输入框清楚方法
    def clear_keys(self, loc):
        self.find_element(*loc).clear()

    # 输入框输入方法
    def send_keys(self, loc, value):
        self.clear_keys(loc)
        self.find_element(*loc).send_keys(value)

    # 元素点击方法
    def click_button(self, loc):
        self.find_element(*loc).click()

    # 弹窗确定方法
    def alert_accept(self):
        sleep(2)
        return self.driver.switch_to_alert().accept()

    # 获取弹窗文本方法
    def alert_text(self):
        sleep(2)
        return self.driver.switch_to_alert().text
