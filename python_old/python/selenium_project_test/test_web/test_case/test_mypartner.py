from selenium import webdriver
from time import sleep,ctime
import unittest
import login_function


class MyPatner(unittest.TestCase):
    '''我的伙伴'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_addmypartner(self):
        '''添加伙伴'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver,phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='u27_text']/p/span").click()   #我的伙伴

        sleep(2)
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='u210']/p").click()    #添加伙伴
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_id("js-input-name").send_keys("12055116631")
        driver.find_element_by_id("js-input-phone").send_keys("12055116631")
        driver.find_element_by_xpath("//*[@id='js-add-firm']/div/div/div[3]/div[1]").click()

    def test_addmypartner2(self):
        '''伙伴同意邀请'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_test(driver,phone="12055116631")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  #同意邀请

    def test_submypartner(self):
        '''移除伙伴'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='u27_text']/p/span").click()  # 我的伙伴
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@class='partnerList']/div[1]").click()   #点击第一个伙伴
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u2810_text']/p/span[2]").click()  #移除按钮
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()