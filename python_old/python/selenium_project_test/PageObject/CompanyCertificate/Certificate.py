from Login.BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CompanyCertificate(Page):
    company_loc = (By.LINK_TEXT,"企业管理")       # 企业管理
    operation_loc = (By.CLASS_NAME,"operation_btn_item ")    # 申请认证
    name_loc = (By.ID,"companyName")                  # 企业名称
    email_loc = (By.ID,"companyEmail")                # 企业邮箱
    credit_loc = (By.ID,"creditNumber")               # 统一社会信用代码
    contact_name_loc = (By.ID,"contactName")          # 联系人
    contact_phone_loc = (By.ID,"contactPhone")        # 联系人手机



    def company_certificate(self):
        self.click_button(self.company_loc)

    def operation_button(self):           # 申请认证的两个按钮是同一个class,调用这个函数两次即可,第二次调用后处理警告框
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

    def company_name(self,name):
        self.send_keys(self.name_loc, name)

    def company_email(self,email):
        self.send_keys(self.email_loc, email)

    def credit_number(self,number):
        self.send_keys(self.credit_loc, number)

    def contact_name(self,contact_name):
        self.send_keys(self.contact_name_loc, contact_name)

    def contact_phone(self,contact_phone):
        self.send_keys(self.contact_phone_loc, contact_phone)


def test_company_certificate(driver,name,email,number,contact_name,contact_phone):
    certificate_page = CompanyCertificate(driver)

    certificate_page.company_certificate()
    certificate_page.operation_button()
    certificate_page.company_name(name)
    certificate_page.company_email(email)
    certificate_page.credit_number(number)
    certificate_page.contact_name(contact_name)
    certificate_page.contact_phone(contact_phone)
    certificate_page.operation_button()
