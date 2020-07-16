from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from Login.LoginPage import *


class NewContact(Page):
    newcontract_loc = (By.LINK_TEXT, '新建合同')
    project_loc = (By.ID, 'projectSelect')              # 项目编码
    contractamount_loc = (By.ID, 'contractAmount')      # 合同金额
    starttime_loc = (By.ID, 'startTime')                # 合同开始时间
    endtime_loc = (By.ID, "endTime")                    # 合同结束时间
    contractname_loc = (By.ID, "contractName")          # 合同名称
    partname_loc = (By.ID, "partACode")                 # 甲方
    reviewtime_loc = (By.ID, "reviewTime")              # 合同截至时间
    contractfile_loc = (By.ID, "submitFile")            # 合同文件
    submitfile_loc = (By.XPATH, "//*[@id='pdfFile']/div/button")            # 上传
    remark_loc = (By.ID, "remark")                      # 备注
    approve_loc = (By.ID, "approveSelect")              # 审批
    operation_loc = (By.CLASS_NAME, "operation_btn_item")              # 送审和存草稿

    def test_new_contract(self):
        self.click_button(self.newcontract_loc)

    def test_edit_contract(self, value):
        Select(self.find_element(*self.project_loc)).select_by_value(value)

    def test_amount_contract(self,amount):   # 合同金额
        self.send_keys(self.contractamount_loc, amount)

    def test_time_contract(self,starttime,endtime):
        js = "$('input').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.send_keys(self.starttime_loc, starttime)

        self.send_keys(self.endtime_loc, endtime)

    def test_first_part(self,partvalue):
        Select(self.find_element(*self.partname_loc)).select_by_value(partvalue)

    def test_review_time(self,reviewtime):
        self.send_keys(self.reviewtime_loc, reviewtime)

    def test_name_contract(self,contractname):
        self.send_keys(self.contractname_loc, contractname)

    def test_file_contract(self,file_path):
        self.send_keys(self.contractfile_loc, file_path)
        sleep(2)
        x = self.driver.get_window_size()
        width = x['width']
        height = x['height']

        move = ActionChains(self.driver).move_by_offset(width * 0.9, height * 0.9)
        move.click()
        move.perform()

        self.click_button(self.submitfile_loc)
        sleep(2)

        self.alert_accept()

    def test_remark(self,remark):
        self.send_keys(self.remark_loc, remark)

    def test_approve(self,approvevalue=data["approvevalue"]):
        Select(self.find_element(*self.approve_loc)).select_by_value(approvevalue)

    def test_operation(self,i):
        self.find_elements(*self.operation_loc)[i].click()


with open("E:/python/PageObject/Login/arguments.yaml",'r',encoding='utf-8') as file:
    data = yaml.load(file)


# 不上传文件，点击存草稿
def test_contract(driver,value=data["value"],amount=data["amount"],
                  starttime=data["starttime"],endtime=data["endtime"],partvalue=data["partvalue"],
                  reviewtime=data["reviewtime"],contractname=data["contractname"],file_path=data['file_path'],
                  remark=data["remark"],approvevalue=data["approvevalue"],i=data["i"][1]):
    new_contract = NewContact(driver)

    new_contract.test_new_contract()
    new_contract.test_edit_contract(value)
    new_contract.test_amount_contract(amount)
    new_contract.test_time_contract(starttime,endtime)
    new_contract.test_first_part(partvalue)
    new_contract.test_review_time(reviewtime)
    new_contract.test_name_contract(contractname)
    # new_contract.test_file_contract(file_path)
    new_contract.test_remark(remark)
    new_contract.test_approve(approvevalue)
    new_contract.test_operation(i)


def test_contract2(driver,value=data["value"],amount=data["amount"],starttime=data["starttime"],
                   endtime=data["endtime"],partvalue=data["partvalue"],reviewtime=data["reviewtime"],
                   contractname=data["contractname"],file_path=data['file_path'],remark=data["remark"],
                   approvevalue=data["approvevalue"],i=data["i"][1]):
    new_contract = NewContact(driver)

    new_contract.test_new_contract()
    new_contract.test_edit_contract(value)
    new_contract.test_amount_contract(amount)
    new_contract.test_time_contract(starttime,endtime)
    new_contract.test_first_part(partvalue)
    new_contract.test_review_time(reviewtime)
    new_contract.test_name_contract(contractname)
    new_contract.test_file_contract(file_path)
    new_contract.test_remark(remark)
    new_contract.test_approve(approvevalue)
    new_contract.test_operation(i)
