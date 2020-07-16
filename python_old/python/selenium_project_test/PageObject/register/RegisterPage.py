from Login.BasePage import *
from register import get_code
import random
from selenium.webdriver.common.by import By
import yaml


class RegisterPage(Page):
    url = '/'

    register_loc = (By.LINK_TEXT, '立即注册')
    phone_loc = (By.ID, 'phone')
    getcode_loc = (By.CLASS_NAME, 'getCode')          # 获取验证码按钮
    phonecode_loc = (By.ID, 'phoneCode')              # 输入验证码
    checkagree_loc = (By.ID, 'chk')                   # 已阅读且同意
    nextbutton_loc = (By.ID, 'phoneNextBt')           # 下一步
    accounttype_loc = (By.ID, 'accountType')          # 账号类型
    accountname_loc = (By.ID, 'accountName')          # 输入账号
    password_loc = (By.ID, 'pwd')                      # 输入密码
    surepwd_loc = (By.ID, 'surePwd')                   # 确认密码
    nextstep_loc = (By.CLASS_NAME, 'next_step')        # 填写账号信息后的下一步

    def test_register(self):
        self.click_button(self.register_loc)

    def test_phone(self,phone):
        self.send_keys(self.phone_loc, phone)

    def test_get_code(self):
        self.click_button(self.getcode_loc)

    def test_phone_code(self,phone):
        try:
            db = get_code.GetCode()
            res = db.get_phone_code(phone)

            self.send_keys(self.phonecode_loc, res)
        except:
            pass

    def check_agree(self):
        self.click_button(self.checkagree_loc)

    def next_button(self):
        self.click_button(self.nextbutton_loc)
        sleep(5)

    def account_type(self,type):
        self.send_keys(self.accounttype_loc, type)

    def account_name(self,name):
        self.send_keys(self.accountname_loc, name)

    def test_password(self,pwd):
        self.send_keys(self.password_loc, pwd)

    def test_surepwd(self,surepwd):
        self.send_keys(self.surepwd_loc, surepwd)

    def next_step(self):
        self.click_button(self.nextstep_loc)


with open("E:/python/PageObject/register/register.yaml",'r',encoding='utf8') as file:
    data = yaml.load(file)


def test_register(driver,phone=str(random.randint(15708400000, 15708499999)),name=str(random.randint(1, 1000)),
                  type=data["type"],pwd=data["pwd"],surepwd=data["surepwd"]):
    register_account = RegisterPage(driver)
    register_account.open()

    register_account.test_register()
    register_account.test_phone(phone)
    register_account.test_get_code()
    register_account.test_phone_code(phone)
    register_account.check_agree()
    register_account.next_button()
    # register_account.account_type(type)
    # register_account.account_name(name)
    # register_account.test_password(pwd)
    # register_account.test_surepwd(surepwd)
    # register_account.next_step()


def test_register2(driver, phone=str(random.randint(15708400000, 15708499999)),name=str(random.randint(1, 1000)),
                   type=data["type"], pwd=data["pwd"], surepwd=data["surepwd"]):
    register_account = RegisterPage(driver)
    register_account.open()

    register_account.test_register()
    register_account.test_phone(phone)
    register_account.test_get_code()
    sleep(10)
    register_account.test_phone_code(phone)
    register_account.check_agree()
    register_account.next_button()
    register_account.account_type(type)
    register_account.account_name(name)
    register_account.test_password(pwd)
    register_account.test_surepwd(surepwd)
    register_account.next_step()
