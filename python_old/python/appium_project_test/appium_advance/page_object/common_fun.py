from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Common(BaseView):
    cancelBtn = (By.ID, "android:id/button2")
    skipBtn = (By.ID, "com.tal.kaoyan:id/tv_skip")

    def check_cancelBtn(self):
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            print("no cancelBtn")
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            print("no skipBtn")
        else:
            skipBtn.click()

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()