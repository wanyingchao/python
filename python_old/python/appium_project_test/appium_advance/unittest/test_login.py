from appium_advance.unittest.myunit import StartEnd
from appium_advance.page_object.loginView import LoginView
import unittest


class TestLogin(StartEnd):

    def test_login_zxwcs(self):
        l = LoginView(self.driver)
        l.login_actiopn("自学网测试", "wyc1063983073")

    def test_login_zxw2017(self):
        l = LoginView(self.driver)
        l.login_actiopn("自学网2017", "zxw2017")

    def test_login_error(self):
        l = LoginView(self.driver)
        l.login_actiopn("595659", "236232")

if __name__ == '__main__':
    unittest.main()
