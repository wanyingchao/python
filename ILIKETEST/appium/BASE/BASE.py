from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import time
from selenium.webdriver.common.by import By


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):       # 查找单个元素
        try:
            WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未找到%s 元素" % (self, loc))

    def find_elements(self, *loc):      # 查找元素组
        return self.driver.find_elements(*loc)

    def clear_keys(self, loc):          # 清空输入框
        self.find_element(*loc).clear()

    def send_keys(self, loc, value):    # 清空输入框，查找元素，输入值
        self.clear_keys(loc)
        self.find_element(*loc).send_keys(value)

    def click_button(self, loc):       # 查找元素，点击
        self.find_element(*loc).click()

    def click_buttons(self, loc, n):   # 点击元素组中的一个
        self.find_elements(*loc)[n].click()

    def get_window_size(self):         # 获取屏幕尺寸
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):       # 屏幕滑动
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def alert_accept(self):     # 接受弹窗
        sleep(2)
        return self.driver.switch_to_alert().accept()

    def alert_text(self):     # 获取弹窗文本
        sleep(2)
        return self.driver.switch_to_alert().text

    # 获取屏幕的宽高
    def get_size(self):
        size = self.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.swipe(x1, y1, x1, y, 2000)

    # 向下滑动
    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.swipe(x1, y1, x1, y, 2000)

    def get_screenshot(self, screenshot_name):
        now = time.strftime("%Y-%m-%d %H-%M-%S ")
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = base_path + "/Report/screenshots/" + now + screenshot_name + ".png"
        return self.driver.get_screenshot_as_file(file_path)
