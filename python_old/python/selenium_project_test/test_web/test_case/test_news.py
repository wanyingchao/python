from selenium import webdriver
from time import sleep,ctime
import unittest
import login_function


class News(unittest.TestCase):
    '''测试消息通知'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_news(self):
        '''执行测试用例'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_id("animation").click()
        sleep(2)
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='u4096_text']/p/span[1]").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()