from selenium import webdriver
from time import sleep, ctime
import unittest

class WebLogin(unittest.TestCase):
    '''测试web登录'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_login1(self):
        '''手机号和验证码都为空的截图'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("loginBtn-text").click()
        driver.switch_to.frame("indexFrame")
        driver.find_element_by_id("js-phone-num").clear()
        driver.find_element_by_id("js-code-val").clear()
        driver.find_element_by_id("js-phone-num").send_keys("")
        # driver.find_element_by_id("js-get-code").click()
        sleep(2)
        driver.find_element_by_id("js-code-val").send_keys("")
        driver.find_element_by_id("js-login-event").click()
        sleep(1)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/p").text
        self.assertEqual(text,"手机号码有误，请重填")
        driver.get_screenshot_as_file("E:\\python\\test_web\\error\\手机号和验证码都为空的截图.png")

    def test_login2(self):
        '''验证码为空的截图'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("loginBtn-text").click()
        driver.switch_to.frame("indexFrame")
        driver.find_element_by_id("js-phone-num").clear()
        driver.find_element_by_id("js-code-val").clear()
        driver.find_element_by_id("js-phone-num").send_keys("18583965785")
        # driver.find_element_by_id("js-get-code").click()
        sleep(2)
        driver.find_element_by_id("js-code-val").send_keys("")
        driver.find_element_by_id("js-login-event").click()
        sleep(1)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/p").text
        self.assertEqual(text,"请输入验证码！")
        driver.get_screenshot_as_file("E:\\python\\test_web\\error\\验证码为空的截图.png")

    def test_login3(self):
        '''验证码错误的截图'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("loginBtn-text").click()
        driver.switch_to.frame("indexFrame")
        driver.find_element_by_id("js-phone-num").clear()
        driver.find_element_by_id("js-code-val").clear()
        driver.find_element_by_id("js-phone-num").send_keys("18583965785")
        # driver.find_element_by_id("js-get-code").click()
        sleep(2)
        driver.find_element_by_id("js-code-val").send_keys("123456")
        driver.find_element_by_id("js-login-event").click()
        sleep(1)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/p").text
        self.assertEqual(text,"错误:验证码不存在！")
        driver.get_screenshot_as_file("E:\\python\\test_web\\error\\验证码错误的截图.png")

    def test_login4(self):
        '''正常登录的截图'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("loginBtn-text").click()
        driver.switch_to.frame("indexFrame")
        driver.find_element_by_id("js-phone-num").clear()
        driver.find_element_by_id("js-code-val").clear()
        driver.find_element_by_id("js-phone-num").send_keys("18583965785")
        driver.find_element_by_id("js-get-code").click()
        sleep(1)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/p").text
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_id("js-code-val").send_keys(text)
        driver.find_element_by_id("js-login-event").click()
        driver.get_screenshot_as_file("E:\\python\\test_web\\error\\正常登录的截图.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()