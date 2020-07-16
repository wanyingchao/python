from Login.LoginPage import *
from register.RegisterPage import *
from Login.logger import *


class TestLogin(unittest.TestCase, Page):
    '''登录'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)

    def test_assert_login(self):
        '''正常登录'''
        driver = self.driver
        logger.info('登陆')
        x = test_user_login(driver, username='xs', password='1')
        logger.info('登录成功')
        self.assertTrue(x)
        self.get_screenshot("登录正常截图")
        logger.info('正常登录截图')

    def test_assert_login1(self):
        '''账号为空'''
        driver = self.driver
        logger.info('登录输入空账号')
        x = test_user_login(driver, username='', password='1')
        logger.info('登录失败')
        self.assertFalse(x)
        self.get_screenshot("账号为空截图")

    def test_assert_login2(self):
        '''密码为空'''
        driver = self.driver
        logger.info('登录密码为空')
        x = test_user_login(driver, username='xs', password='')
        self.assertFalse(x)
        self.get_screenshot("密码为空截图")

    def test_assert_login3(self):
        '''账号、密码都为空'''
        driver = self.driver
        logger.info('登录账号、密码都为空')
        x = test_user_login(driver, username='', password='')
        self.assertFalse(x)
        logger.info('断言')
        self.get_screenshot("账号、密码都为空截图")
        logger.info('截图')

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
