from Login.NewContract import *
from register.RegisterPage import *
from Login.logger import *


class TestNewContract(unittest.TestCase, Page):
    '''新建合同'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)

    def test_newcontract(self):
        '''新建未上传合同文件'''
        driver = self.driver

        logger.info('登录销售账号')
        test_user_login(driver)
        logger.info('新建合同')
        test_contract(driver)
        logger.info('不上传合同文件')
        sleep(1)
        self.get_screenshot("未上传合同文件截图")
        logger.info('截图')
        sleep(2)
        logger.info('断言')
        text = self.alert_text()
        self.assertEqual(text, "请先上传合同文件")

    def test_newcontract2(self):
        '''正常新建'''
        driver = self.driver

        logger.info('登录销售账号')
        test_user_login(driver)
        logger.info('新建合同')
        test_contract2(driver)
        sleep(1)
        self.get_screenshot("上传了合同文件截图")
        logger.info('截图')
        sleep(2)
        self.alert_accept()

    def tearDown(self):
        sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                self.get_screenshot(case_name)
                logger.error(method_name)
                logger.error(error)

        self.driver.quit()
        test_name = self._testMethodName + '>>>>>>>>>>>>>>完成用例'
        logger.info(test_name)


if __name__ == '__main__':
    unittest.main()
