from contract_po.basepage.basepage import *
from contract_po.basepage.logger import *
from selenium.webdriver.common.action_chains import ActionChains
import os


class Business(Page):
    project_list_loc = (By.ID, 'toProjectList')         # 项目列表按钮
    project_list_all = (By.CLASS_NAME, 'table_content_item')      # 循环项目列表
    key_word_loc = (By.ID, 'keyWord')             # 搜索框
    search_btn_loc = (By.CLASS_NAME, 'search_btn_query')    # 查询按钮
    new_contract_loc = (By.CLASS_NAME, 'new_contract')     # 新建合同按钮
    paper_contract_loc = (By.XPATH, '//*[@id="confirm"]/div/div[2]/div/input[2]')    # 选择纸质合同
    button_agree_loc = (By.XPATH, './/button[contains(@class,"btnAgree")]')         # 确定按钮
    contract_amount_loc = (By.ID, 'contractAmount')   # 合同金额
    budget_total_loc = (By.ID, 'budgetTotal')   # 预算报价
    start_time_loc = (By.ID, 'startTime')   # 合同开始时间
    end_time_loc = (By.ID, 'endTime')    # 合同结束时间
    part_A_loc = (By.ID, 'partA')   # 甲方
    selecct_part_loc = (By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[2]/ul/li')
    review_time_loc = (By.ID, 'reviewTime')   # 合同审批截止时间
    contract_name_loc = (By.ID, 'contractName')  # 合同名称
    contract_design_loc = (By.ID, 'design')   # 设计签单金额
    budget_design_loc = (By.ID, 'budgetDesign')  # 预算设计报价
    contract_scene_loc = (By.ID, 'scene')    # 现场金额
    budget_scene_loc = (By.ID, 'budgetScene')   # 预算现场报价
    contract_counter_loc = (By.ID, 'counter')  # 柜台金额
    budget_counter_loc = (By.ID, 'budgetCounter')   # 预算柜台报价
    first_amount_loc = (By.ID, 'firstAmount')    # 一期款
    second_amount_loc = (By.ID, 'secondAmount')   # 二期款
    third_amount_loc = (By.ID, 'thirdAmount')      # 三期款
    first_time_loc = (By.ID, 'firstTime')    # 一期款收款日期
    second_time_loc = (By.ID, 'secondTime')   # 二期款收款日期
    third_time_loc = (By.ID, 'thirdTime')      # 三期款收款日期
    add_approving_loc = (By.CLASS_NAME, 'add_approving')     # 添加审批方
    approve_id_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/div[1]/input')    # 审批方sh
    contract_pic_loc = (By.CLASS_NAME, 'upload_contract_pic')    # 上传合同图片


    def to_project_list(self):
        self.click_button(self.project_list_loc)

    '''
    # 列表循环查找项目
    def new_button(self, pid):
        rows = self.find_elements(*self.project_list_all)
        for row in rows:
            projectId = row.find_element_by_xpath('.//div[contains(@class,"projectId")]').text
            if pid == projectId:
                global curr_row
                curr_row = row
                break
        sleep(2)
        logger.info('找到项目id，点击新建')
        curr_row.find_element(By.CLASS_NAME, "new_contract").click()  # 编辑按钮
        '''
    def new_button(self, pid):
        self.send_keys(self.key_word_loc, pid)
        self.click_button(self.search_btn_loc)
        sleep(2)
        self.click_button(self.new_contract_loc)

    def paper_contract(self):
        self.click_button(self.paper_contract_loc)
        self.click_button(self.button_agree_loc)

    def complete_congtract(self, start_time, end_time, partA, review_time, contract_name):
        amount = self.find_element(*self.budget_total_loc).text
        self.send_keys(self.contract_amount_loc, str(amount))
        js = "$('input').removeAttr('readonly')"
        self.driver.execute_script(js)
        self.send_keys(self.start_time_loc, start_time)
        self.send_keys(self.end_time_loc, end_time)
        self.send_keys(self.part_A_loc, partA)
        self.click_button(self.selecct_part_loc)
        self.send_keys(self.review_time_loc, review_time)
        self.send_keys(self.contract_name_loc, contract_name)

    def contract_amount(self,first_time, second_time, third_time):
        design_amount = self.find_element(*self.budget_design_loc).text
        self.send_keys(self.contract_design_loc, str(design_amount))
        scene_amount = self.find_element(*self.budget_scene_loc).text
        self.send_keys(self.contract_scene_loc, str(scene_amount))
        counter_amount = self.find_element(*self.budget_counter_loc).text
        self.send_keys(self.contract_counter_loc, str(counter_amount))

        self.send_keys(self.first_amount_loc, design_amount)
        self.send_keys(self.second_amount_loc, scene_amount)
        self.send_keys(self.third_amount_loc, counter_amount)
        self.send_keys(self.first_time_loc, first_time)
        self.send_keys(self.second_time_loc, second_time)
        self.send_keys(self.third_time_loc, third_time)

        x = self.driver.get_window_size()
        width = x['width']
        height = x['height']

        move = ActionChains(self.driver).move_by_offset(width * 0.9, height * 0.9)
        move.click()
        move.perform()

    def add_approve(self):
        self.click_button(self.add_approving_loc)
        self.click_button(self.approve_id_loc)
        self.click_button(self.button_agree_loc)

    def upload_contract_pic(self):
        self.click_button(self.contract_pic_loc)
        os.system('E:\python\Autolt\contract.exe')


def test_business(driver, pid, start_time, end_time, partA, review_time, contract_name, first_time, second_time, third_time):
    business_page = Business(driver)

    business_page.to_project_list()
    business_page.new_button(pid)
    business_page.paper_contract()
    business_page.complete_congtract(start_time, end_time, partA, review_time, contract_name)
    business_page.contract_amount(first_time, second_time, third_time)
    business_page.add_approve()
    business_page.upload_contract_pic()
