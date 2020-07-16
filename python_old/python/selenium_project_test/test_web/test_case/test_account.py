from selenium import webdriver
from time import sleep,ctime
import unittest
import login_function


class Account(unittest.TestCase):
    '''测试帐号与设置'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_account(self):
        '''编辑账号信息'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='u25_text']/p/span").click()
        sleep(1)
        driver.switch_to.frame("indexFrame")
        text = driver.find_element_by_xpath("//*[@id='u2848_text']/p/span").text
        self.assertEqual(text,"当前账号：18583965785")

        driver.find_element_by_id("u2863").click()
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()
        driver.switch_to.default_content()
        driver.get_screenshot_as_file("E:\\python\\test_web\\error\\保存账号修改的截图.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()