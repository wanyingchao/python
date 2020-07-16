from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.common.keys import Keys
import unittest
import login_function


class Search(unittest.TestCase):
    '''测试搜索框和搜索按钮'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_projectlist(self):
        '''项目列表页的搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver,phone="18583965785")

        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='u70']/p").click()  # 筛选进行中
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u71']/p").click()  # 筛选已完工
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u73']/p").click()  # 筛选全部
        sleep(5)

        driver.find_element_by_id("u586").send_keys("测试店", Keys.ENTER)  # 搜索框
        sleep(5)
        driver.find_element_by_id("u586").clear()
        driver.find_element_by_id("u586").send_keys(Keys.ENTER)
        sleep(2)

    def test_missionlist(self):
        '''任务列表页搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u341']/p").click()   # 整改中
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u342']/p").click()  # 施工中
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u346']/p").click()  # 待申请
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u343']/p").click()  # 验收中
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u344']/p").click()  # 验收通过
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u345']/p").click()  # 全部
        sleep(2)

        driver.find_element_by_id("u586").send_keys("平面图")
        driver.find_element_by_id("u332").click()
        sleep(2)
        driver.find_element_by_id("u586").clear()
        driver.find_element_by_id("u332").click()
        sleep(2)

    def test_loglist(self):
        '''日志列表页搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[5]/div[2]/div[2]/div/div[1]").click()  # 任务列表页第一个任务
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[2]/div[2]/div[1]/span[2]").click()  # 日志
        sleep(1)
        driver.find_element_by_xpath("//*[@id='js-choice-list']/div[2]/span").click()  # 进行中
        sleep(2)
        driver.find_element_by_xpath("//*[@id='js-choice-list']/div[3]/span").click()  # 突发
        sleep(2)
        driver.find_element_by_xpath("//*[@id='js-choice-list']/div[4]/span").click()  # 整改
        sleep(2)
        driver.find_element_by_xpath("//*[@id='js-choice-list']/div[5]/span").click()  # 监理
        sleep(2)
        driver.find_element_by_xpath("//*[@id='js-choice-list']/div[1]/span").click()  # 全部
        sleep(2)

        # driver.find_element_by_id("u60_text").send_keys("其它事项",Keys.ENTER)
        # sleep(2)
        # driver.find_element_by_id("u60_text").clear()
        # driver.find_element_by_id("u60_text").send_keys(Keys.ENTER)
        # sleep(2)

    def test_workgrouplist(self):
        '''工作组列表搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[5]/div[2]/div[2]/div[1]/div[1]").click()  # 任务列表页第一个任务
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[2]/div[3]/div[1]/div[1]/div/span[2]").click()  # 工作组
        driver.find_element_by_id("u1065_input").send_keys("5785", Keys.ENTER)  # 工作组搜索框
        sleep(2)
        driver.find_element_by_id("u1065_input").clear()
        driver.find_element_by_id("u1065_input").send_keys(Keys.ENTER)
        sleep(2)

    def test_partnerlist(self):
        '''伙伴列表的搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='u27_text']/p/span").click()  # 我的伙伴
        sleep(2)
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_id("u39_input").send_keys("5785",Keys.ENTER)
        sleep(2)
        driver.find_element_by_id("u39_input").clear()
        driver.find_element_by_id("u39_input").send_keys(Keys.ENTER)
        sleep(2)

    def test_memberliest(self):
        '''公司成员列表搜索'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='u25_text']/p/span").click()
        sleep(1)
        driver.switch_to.frame("indexFrame")
        text = driver.find_element_by_xpath("//*[@id='u2848_text']/p/span").text
        self.assertEqual(text, "当前账号：18583965785")
        sleep(1)
        driver.find_element_by_xpath("//*[@id='u2864_text']/p/span[2]").click()
        driver.find_element_by_xpath("//*[@id='box-1']/div/div/div[3]/div[1]/p/span[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='u3071']/div/input").send_keys("5785",Keys.ENTER)
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u3071']/div/input").clear()
        driver.find_element_by_xpath("//*[@id='u3071']/div/input").send_keys(Keys.ENTER)
        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()