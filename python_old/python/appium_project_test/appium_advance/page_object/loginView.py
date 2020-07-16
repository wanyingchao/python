from appium_advance.page_object.common_fun import Common
from appium_advance.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By


class LoginView(Common):
    username_type = (By.ID, "com.tal.kaoyan:id/login_email_edittext")
    password_type = (By.ID, "com.tal.kaoyan:id/login_password_edittext")
    loginBtn = (By.ID, "com.tal.kaoyan:id/login_login_btn")

    def login_actiopn(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        self.driver.find_element(*self.username_type).send_keys(username)

        self.driver.find_element(*self.password_type).send_keys(password)

        self.driver.find_element(*self.loginBtn).click()

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_actiopn("自学网测试", "wyc1063983073")
