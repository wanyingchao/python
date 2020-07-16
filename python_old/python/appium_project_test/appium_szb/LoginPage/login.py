from appium_szb.desired_caps.desired_caps import *
from appium_szb.baseview.BaseView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginView(BaseView):
    login_username_loc = (By.ID, 'com.cn.szb.customer:id/ali_login_username')
    login_pwd_loc = (By.ID, 'com.cn.szb.customer:id/ali_login_pwd')
    login_button_loc = (By.ID, 'com.cn.szb.customer:id/ali_login_btn')

    def login_button(self, username, pwd):
        self.send_keys(self.login_username_loc, username)
        self.send_keys(self.login_pwd_loc, pwd)
        self.click_button(self.login_button_loc)


def test_user_login(username, pwd):
    driver = appium_desired()
    login = LoginView(driver)

    login.login_button(username, pwd)

test_user_login(username='销售001', pwd='123456')
