from selenium import webdriver
from contract_po.basepage.basepage import *
from contract_po.basepage.logger import *


class Login(Page):
    url = '/'

    account_name_loc = (By.ID, 'accountName')
    pwd_loc = (By.ID, 'pwd')
    login_button_loc = (By.CLASS_NAME, 'login_in')

    def type_accountname(self, accountname):
        logger.info('输入登录名')
        self.send_keys(self.account_name_loc, accountname)

    def type_pwd(self, pwd):
        logger.info('输入登录密码')
        self.send_keys(self.pwd_loc, pwd)

    def login_button(self):
        logger.info('点击登录按钮')
        self.click_button(self.login_button_loc)


def test_login(driver, accountname='xs', pwd='1'):
    login_page = Login(driver)
    login_page.type_accountname(accountname)
    login_page.type_pwd(pwd)
    login_page.login_button()
