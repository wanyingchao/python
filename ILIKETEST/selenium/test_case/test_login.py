from login import *
import unittest


class WebLogin(unittest.TestCase, Page):
    """登录测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://rainbow.mynatapp.cc//bms/#/login')
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)

    def test_login_success(self):
        """成功登录"""
        driver = self.driver
        user_login(driver, username='18500001113', pwd='123456')
        logger.info('断言，判断页面是否登录成功')
        time.sleep(0.5)
        # 获取登录成功后飘窗的文本信息
        self.assertEqual(assert_login(driver), '登录成功！')
        self.get_screenshot('登录成功')

    def test_login_username_null(self):
        """用户名为空登录"""
        driver = self.driver
        user_login(driver, username='', pwd='123456')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        # 获取飘窗的文本信息
        self.assertEqual(assert_login(driver), '登录名不能为空')
        self.get_screenshot('登录名为空')

    def test_login_pwd_null(self):
        """密码为空登录"""
        driver = self.driver
        user_login(driver, username='18500001113', pwd='')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login(driver), '密码不能为空')
        self.get_screenshot('密码为空')

    def test_login_both_null(self):
        """用户名和密码都为空登录"""
        driver = self.driver
        user_login(driver, username='', pwd='')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login(driver), '登录名不能为空')
        self.get_screenshot('登录名为空')

    def test_login_fail(self):
        """错误账号登录"""
        driver = self.driver
        user_login(driver, username='623232', pwd='216616')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login(driver), '用户名或者密码错误')
        self.get_screenshot('用户名或者密码错误')

    def tearDown(self):
        time.sleep(3)
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
