from ILIKETEST.appium.BASE.BASE import *
from ILIKETEST.appium.BASE.LOGGER import *
from ILIKETEST.appium.adb_start_appium.adb_start_appium import *


class Login(Page):

    phonenum_loc = (By.ID, 'com.xiaomai.ageny:id/et_tel')
    pwd_loc = (By.ID, 'com.xiaomai.ageny:id/et_password')
    login_btn_loc = (By.ID, 'com.xiaomai.ageny:id/bt_login')
    # 验证码登录
    code_login_loc = (By.ID, 'com.xiaomai.ageny:id/bt_code_login')
    code_input_loc = (By.ID, 'com.xiaomai.ageny:id/et_vercode')
    layout_center_loc = (By.ID, 'com.xiaomai.ageny:id/layout_center')   # 个人中心

    def input_phone(self, phonenum):
        logger.info('输入手机号')
        self.send_keys(self.phonenum_loc, phonenum)

    def input_pwd(self, pwd):
        logger.info('输入密码')
        self.send_keys(self.pwd_loc, pwd)

    def click_login_button(self):
        logger.info('点击登录按钮')
        self.click_button(self.login_btn_loc)
        time.sleep(1)

    def click_code_login_button(self):
        logger.info('点击验证码登录')
        self.click_button(self.code_login_loc)

    def input_code(self, code):
        logger.info('输入验证码')
        self.send_keys(self.code_input_loc, code)


def login_pwd(driver, phonenum, pwd):
    login_page = Login(driver)
    login_page.input_phone(phonenum)
    login_page.input_pwd(pwd)
    login_page.click_login_button()


def login_code(driver, phonenum, code):
    login_page = Login(driver)
    login_page.click_code_login_button()
    login_page.input_phone(phonenum)
    login_page.input_code(code)
    login_page.click_login_button()


def assert_login_center(driver):
    time.sleep(2)
    if driver.find_element_by_id('com.xiaomai.ageny:id/layout_center'):
        return True
    else:
        return False


def assert_login_hint(driver):
    return driver.find_element_by_id('com.xiaomai.ageny:id/tv_hint').text


if __name__ == '__main__':
    adb_start_appium().appium_start()
    driver = adb_start_appium().desired_caps()
    time.sleep(8)
    login_pwd(driver, phonenum='15708448535', pwd='123456')
