from register.RegisterPage import *
from Login.logger import *


class TestRegister(unittest.TestCase, Page):
    '''注册'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)

    def test_assert_register(self):
        '''错误手机号注册'''
        driver = self.driver
        logger.info('注册输入错误手机号')
        test_register(driver, phone='14521645',name="")
        sleep(2)
        text = self.driver.switch_to_alert().text
        self.assertEqual(text, '验证码不正确')
        logger.info('断言')
        self.get_screenshot("验证码错误截图")
        logger.info('截图')

    def test_assert_register2(self):
        '''正常注册'''
        driver = self.driver
        logger.info('正常注册')
        test_register2(driver,phone=str(random.randint(15708400000, 15708499999)),name=str(random.randint(1,1000)))
        # 设置断言

    def tearDown(self):
        sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                self.get_screenshot(case_name)
                logger.error(method_name)
                logger.error(error)

        self.driver.quit()
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)


if __name__ == '__main__':
    unittest.main()
