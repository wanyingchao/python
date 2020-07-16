from Login.BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PersonalCertificate(Page):

    personal_loc = (By.LINK_TEXT, "个人管理")                      # 个人管理
    operation_loc = (By.CLASS_NAME, "operation_btn_item ")       # 申请认证
    name_loc = (By.ID, "name")                                     # 姓名
    number_loc = (By.ID, "certificateNumber")                     # 证件号码
    email_loc = (By.ID, "email")                                   # 邮箱
    type_loc = (By.ID, "certificateType")                         # 证件类型



    def personal_management(self):
        self.click_button(self.personal_loc)

    def operation_button(self):                     # 两个页面同一class，两次调用，第二次处理警告框
        self.click_button(self.operation_loc)
        sleep(2)
        try:
            text = self.alert_text()
            if text is None:
                pass
            else:
                self.alert_accept()
        except:
            pass


    def certificate_name(self,name):
        self.send_keys(self.name_loc, name)

    def certificate_number(self,number):
        self.send_keys(self.number_loc, number)

    def certificate_email(self,email):
        self.send_keys(self.email_loc, email)

    def certificate_type(self,value):
        Select(self.find_element(*self.type_loc)).select_by_value(value)


def test_personal_certificate(driver,name,number,email,value):
    certificate_page = PersonalCertificate(driver)

    certificate_page.personal_management()
    certificate_page.operation_button()
    certificate_page.certificate_name(name)
    certificate_page.certificate_number(number)
    certificate_page.certificate_email(email)
    certificate_page.certificate_type(value)
    certificate_page.operation_button()
