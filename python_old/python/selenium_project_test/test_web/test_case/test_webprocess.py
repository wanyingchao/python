from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, ctime
import unittest
from selenium.webdriver.support.ui import Select
import os
import login_function


class WebProcess(unittest.TestCase):
    '''测试web主体流程'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.91szb.com/"

    def test_process1(self):
        '''接单员提交完工'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18398929673")

        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[5]/div[2]/div[2]/div[1]/div[1]").click()  # 任务列表页第一个任务
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[2]/div[2]/div[1]/span[2]").click()  # 日志
        sleep(2)
        driver.find_element_by_xpath("//*[@id='base']/div[2]/div[4]").click()  # 添加日志
        sleep(2)
        # Select(driver.find_elements_by_id("c2")[2]).select_by_value("888179385742")  #进度标签(进行中)
        Select(driver.find_elements_by_xpath("//*[@id='progress']/select[2]")[0]).select_by_visible_text("进行中")
        driver.find_element_by_id("u184_input").send_keys("日志说明")

        sleep(2)
        driver.find_element_by_xpath("//*[@id='u85']/div[2]/label").click()  # 添加附件(本地弹窗，使用Autolt实现文件上传)
        os.system("E:\python\Autolt\\upfile.exe")  # 调用Autolt

        sleep(10)
        driver.find_element_by_id("cache2").click()  # 确定
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定弹窗

        sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='base']/div[2]/div[4]").click()  # 添加日志
        sleep(2)
        # Select(driver.find_elements_by_id("c2")[2]).select_by_value("888179385728")  #进度标签(已完工)
        Select(driver.find_elements_by_xpath("//*[@id='progress']/select[2]")[0]).select_by_visible_text("已完工")
        driver.find_element_by_id("u184_input").send_keys("日志说明")

        sleep(2)
        driver.find_element_by_xpath("//*[@id='u85']/div[2]/label").click()  # 添加附件(本地弹窗，使用Autolt实现文件上传)
        os.system("E:\python\Autolt\\upfile.complate.exe")  # 调用Autolt

        sleep(10)
        driver.find_element_by_id("cache2").click()  # 确定
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定弹窗

        sleep(2)
        driver.find_element_by_xpath("//*[@id='sit-map-item']/a[3]").click()  # 回到上一层
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_id("u451_text").click()  # 提交完工
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定弹窗

        sleep(5)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='sit-map-item']/a[2]").click()  # 回到上一层
        sleep(2)
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='apply']/p/span").click()  # 申请验收
        driver.find_element_by_id("inputMask").click()  # 全选
        driver.find_element_by_xpath("//*[@id='submit']/p/span[2]").click()  # 点击提交
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定提交

        sleep(5)
        driver.find_element_by_xpath("//*[@id='u545']/p/span").click()  # 退出

    def test_process2(self):
        '''监理验收不通过'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_test(driver,phone="12077119995")

        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u795']/div/div[1]").click()  # 任务列表页第一个任务
        sleep(2)
        driver.find_element_by_id("u946").click()  # 验收不通过
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_id("js-textarea").send_keys("验收不通过原因")
        sleep(2)
        driver.find_element_by_xpath("//*[@id='js-add-firm']/div/div/div[3]/div[1]").click()

        sleep(2)
        driver.find_element_by_xpath("//*[@id='u545']/p/span").click()  # 退出

    def test_process3(self):
        '''接单员再次提交完工'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_regular(driver, phone="18583965785")

        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u249']/div[2]/div[2]/div[1]/div[1]").click()  # 任务列表页第一个任务

        driver.find_element_by_id("u451_text").click()  # 提交完工
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定弹窗

        sleep(5)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='sit-map-item']/a[2]").click()  # 回到上一层
        sleep(2)
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='apply']/p/span").click()  # 申请验收
        driver.find_element_by_id("inputMask").click()  # 全选
        driver.find_element_by_xpath("//*[@id='submit']/p/span[2]").click()  # 点击提交
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确定提交
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u545']/p/span").click()  # 退出

    def test_process4(self):
        '''监理验收通过'''
        driver = self.driver
        driver.get(self.base_url + "/")
        login_function.login_test(driver,phone="12077119995")

        driver.switch_to.default_content()
        driver.switch_to_frame("indexFrame")
        driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()  # 项目列表页第一个项目
        sleep(5)
        driver.find_element_by_xpath("//*[@id='u795']/div/div[1]").click()  # 任务列表页第一个任务

        # 验收通过
        sleep(2)
        driver.find_element_by_xpath("//*[@id='u945_text']/p/span[2]").click()  # 验收通过
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()  # 确认弹窗

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
