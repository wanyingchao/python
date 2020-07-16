import unittest
from appium_advance.page_object.desired_caps import appium_desired
from time import sleep


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = appium_desired()

    def tearDown(self):
        sleep(5)
        self.driver.close_app()