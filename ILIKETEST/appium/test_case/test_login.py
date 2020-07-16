from ILIKETEST.appium.LOGIN.login import *
import unittest


class AppLogin(unittest.TestCase, Page):
    """登录测试用例"""
    def setUp(self):
        adb_start_appium().appium_start()
        self.driver = adb_start_appium().desired_caps()
        self.driver.implicitly_wait(10)
        test_name = self._testMethodName + '>>>>>>>>>>>>>>开始用例'
        logger.info(test_name)

    def test_login_success(self):
        """成功登录"""
        driver = self.driver
        login_pwd(driver, phonenum='15708448535', pwd='123456')
        logger.info('断言，判断页面是否登录成功')
        self.assertTrue(assert_login_center(driver))
        self.get_screenshot('登录成功')

    def test_login_phone_null(self):
        """用户名为空登录"""
        driver = self.driver
        login_pwd(driver, phonenum='', pwd='123456')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '密码和电话不能为空')
        self.get_screenshot('登录名为空')

    def test_login_pwd_null(self):
        """密码为空登录"""
        driver = self.driver
        login_pwd(driver, phonenum='15708448535', pwd='')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '密码和电话不能为空')
        self.get_screenshot('密码为空')

    def test_login_both_null(self):
        """用户名和密码都为空登录"""
        driver = self.driver
        login_pwd(driver, phonenum='', pwd='')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '密码和电话不能为空')
        self.get_screenshot('登录名和密码都为空')

    def test_login_phone_wrong(self):
        """错误账号登录"""
        driver = self.driver
        login_pwd(driver, phonenum='10086', pwd='123456')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '手机号码为11位')
        self.get_screenshot('错误账号登录')

    def test_login_phone_non_existent(self):
        """不存在账号登录"""
        driver = self.driver
        login_pwd(driver, phonenum='15708448536', pwd='123456')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '该用户不存在')
        self.get_screenshot('不存在账号登录')

    def test_login_pwd_wrong(self):
        """错误账号登录"""
        driver = self.driver
        login_pwd(driver, phonenum='15708448535', pwd='111111')
        logger.info('断言，判断页面是否登录失败')
        time.sleep(0.5)
        self.assertEqual(assert_login_hint(driver), '密码错误')
        self.get_screenshot('错误密码登录')

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
