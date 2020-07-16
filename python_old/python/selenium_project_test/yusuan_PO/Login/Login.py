from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *


class Login(Page):
    url = '/'

    username_loc = (By.ID, 'username')  # 账号
    submit_loc = (By.ID, 'button')  # 登录按钮

    def type_username(self, username):
        logger.info('输入账户名')
        self.send_keys(self.username_loc, username)

    def type_submit(self):
        logger.info('点击确认')
        self.click_button(self.submit_loc)


# with open("E://python/yusuan_PO/Login/login_arguments.yaml") as file:
#     data = yaml.load(file)


def test_user_login(driver, username='12033330008'):
    login_page = Login(driver)

    login_page.type_username(username)
    login_page.type_submit()

