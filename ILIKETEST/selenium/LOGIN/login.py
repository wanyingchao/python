from BASE import *
from LOGGER import *


class Login(Page):
    # 元素定位
    username_loc = (By.ID, 'user')
    pwd_loc = (By.ID, 'password')
    login_button_loc = (By.XPATH, '//*[@id="root"]/div/div/ul/li[2]/form/button')
    assert_name_loc = (By.CLASS_NAME, 'name___2eduw')

    def input_username(self, username):
        logger.info('输入电话号码')
        self.send_keys(self.username_loc, username)

    def input_pwd(self, pwd):
        logger.info('输入密码')
        self.send_keys(self.pwd_loc, pwd)

    def click_login_button(self):
        logger.info('点击登录')
        self.click_button(self.login_button_loc)


def user_login(driver, username, pwd):
    login_page = Login(driver)
    login_page.input_username(username)
    login_page.input_pwd(pwd)
    login_page.click_login_button()


def assert_login(driver):
    return driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/div[1]').text


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://test.jzcdsc.com/bms/#/login')
    user_login(driver, username='13011114444', pwd='123456')
