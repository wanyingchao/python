from Login.BasePage import *


class LoginPage(Page):
    url = '/'

    username_loc = (By.ID, 'accountName')         # 账号
    password_loc = (By.ID, 'pwd')                  # 密码
    submit_loc = (By.CLASS_NAME, 'login_in')       # 登录按钮
    newcontract_loc = (By.LINK_TEXT, '新建合同')

    def type_username(self, username):
        self.send_keys(self.username_loc, username)

    def type_password(self, password):
        self.send_keys(self.password_loc, password)

    def type_submit(self):
        self.click_button(self.submit_loc)

    def loginpass(self):
        try:
            if self.find_element(*self.newcontract_loc) is not None:
                return True
            else:
                self.alert_accept()
                return False
        except:
            pass


with open("E:/python/PageObject/Login/arguments.yaml","r",encoding='utf8') as file:
    data = yaml.load(file)


def test_user_login(driver,username=data["username"],password=data["password"]):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()
    return login_page.loginpass()


