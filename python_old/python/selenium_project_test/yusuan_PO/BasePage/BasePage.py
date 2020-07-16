import os
import time
from selenium.webdriver.common.by import By
import yaml
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import configparser
from PIL import ImageGrab
import logging


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://172.16.1.188:8888/budget/pages/main'

    def _open(self, url):
        url_ = self.base_url + url
        self.driver.get(url_)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未找到%s 元素" % (self, loc))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_screenshot(self, screenshot_name):
        x = self.driver.get_window_size()
        width = x['width']
        height = x['height']
        size = self.driver.set_window_size(width, height)
        img = ImageGrab.grab(size)

        now = time.strftime("%Y-%m-%d %H-%M-%S ")
        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = base_path + "/Report/screenshot/" + now + screenshot_name + ".png"
        return img.save(file_path)

    def clear_keys(self, loc):
        self.find_element(*loc).clear()

    def send_keys(self, loc, value):
        self.clear_keys(loc)
        self.find_element(*loc).send_keys(value)

    def click_button(self, loc):
        self.find_element(*loc).click()

    def alert_accept(self):
        sleep(2)
        return self.driver.switch_to_alert().accept()

    def alert_text(self):
        sleep(2)
        return self.driver.switch_to_alert().text