from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *
from selenium.webdriver.support.ui import Select


class NewProject(Page):
    all_button_loc = (By.LINK_TEXT, '全部')
    project_list = (By.CLASS_NAME, 'list-over-effect')  # 项目列表
    new_button_loc = (By.CLASS_NAME, 'text-effect')   # 【新建】按钮
    popup_loc = (By.XPATH, '//*[@id="q"]/div/div[2]/div[3]/div[1]/label/input')
    submit_button_loc = (By.XPATH, '//*[@id="q"]/div/div[3]/input[1]')
    offer_area_loc = (By.CLASS_NAME, 'ht_52_1')
    area_loc = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[7]/div[3]/div[1]/span')
    regular_project_new = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[2]/a')  # 常规项目的新增
    design_part_loc = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[3]/div[1]/span')  # 设计部分
    live_decoration_loc = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[3]/div[2]/span')  # 现场装修部分
    showcase_part_loc = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[3]/div[3]/span')    # 商业展柜部分
    design_part_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[2]/a')  # 设计部分新增
    design_button_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/span')  # 设计
    design_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[1]/div[3]/a')  # 设计新增
    save_loc = (By.ID, 'create_save')   # 保存
    submit_loc = (By.ID, 'create_submit_aduit')  # 提交审批
    assessor_loc = (By.ID, 'butget_assessor')  # 选择审核人
    assessor_submit_loc = (By.ID, 'btnOk')  # 提交审核，弹窗确认
    ceiling_engineering_button = (By.XPATH, '//*[contains(@class,third_new_add) and @create-item="7"]')

    # 点击全部
    def all_button(self):
        logger.info('点击全部')
        self.click_button(self.all_button_loc)

    # 点击新建
    def new_button(self, pid):
        rows = self.find_elements(*self.project_list)
        for row in rows:
            projectId = row.find_element_by_xpath('.//div[contains(@class,"w_15")]').text
            if pid == projectId:
                global curr_row
                curr_row = row
                break
        sleep(2)
        logger.info('找到项目id，点击新建')
        curr_row.find_element(By.CLASS_NAME,"text-effect").click()  # 编辑按钮

    # 点击弹窗完全新建
    def popup(self):
        logger.info('点击弹窗完全新建')
        self.click_button(self.popup_loc)

    # 点击确认
    def submit_button(self):
        logger.info('点击弹窗确认')
        self.click_button(self.submit_button_loc)

    # 点击报价区域：成都
    def offer_area(self):
        # 鼠标点击报价区域
        logger.info('点击报价区域')
        self.click_button(self.offer_area_loc)
        time.sleep(1)
        logger.info('选择成都')
        self.click_button(self.area_loc)

    # 点击常规项目新增
    def regular_new(self):
        logger.info('点击常规项目新增')
        self.click_button(self.regular_project_new)
        sleep(1)

    # 点击设计部分
    def design_part(self):
        logger.info('点击设计部分')
        self.click_button(self.design_part_loc)

    # 点击设计部分新增
    def design_part_new(self):
        logger.info('点击设计部分新增')
        self.click_button(self.design_part_new_loc)
        sleep(1)

    # 点击设计
    def design_button(self):
        logger.info('点击设计')
        self.click_button(self.design_button_loc)

    # 点击设计新增
    def design_new(self):
        for i in range(2):        # 新增两条
            logger.info('点击设计新增，两条')
            self.click_button(self.design_new_loc)
            sleep(1)

    # 完善设计资料
    def complete_design_information(self):         # 完善设计资料
        logger.info('完善设计资料')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('设计1')            # 第一个设计名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/input')\
            .send_keys('10')           # 预算数量
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/input')\
            .send_keys('10')           # 报价
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[1]/input')\
        #     .send_keys('9')            # 含税价

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input[1]')\
            .send_keys('设计2')  # 第二个设计名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input')\
            .send_keys('10')  # 预算数量
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input')\
            .send_keys('10')  # 报价
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[4]/div[1]/input')\
        #     .send_keys('9')  # 含税价

    # 收起设计模块
    def packup_design(self):
        logger.info('收起设计模块')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[1]/div[2]/div/div[1]/div[1]/span').click()

    # 点击现场装修部分
    def live_decoration(self):
        logger.info('点击现场装修部分')
        self.click_button(self.live_decoration_loc)

    # 点击现场装修部分新增
    def live_decoration_new(self):
        logger.info('点击现场装修部分新增')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/a').click()
        print(self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/a').text)
        sleep(2)

    # 点击天棚工程
    def ceiling_engineering(self):
        logger.info('点击天棚工程')
        self.click_button(self.ceiling_engineering_button)

    # 点击天棚工程新增
    def ceiling_engineering_new(self):
        for i in range(2):
            logger.info('点击天棚工程新增，两条')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[1]/div[3]/a').click()
            sleep(1)

    # 完善天棚工程资料
    def complete_ceiling_engineering(self):
        logger.info('完善天棚工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('天棚工程1')           # 天棚工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[1]/input')\
            .send_keys('这是天棚1备注信息')      # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('天棚工程2')           # 天棚工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[3]')\
            .click()                         # 单位:m
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div[1]/input')\
            .send_keys('这是天棚2备注信息')      # 备注

    # 收起天棚模块
    def packup_ceiling(self):
        logger.info('收起天棚工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/span').click()

    # 点击地面工程
    def flooring_work(self):
        logger.info('点击地面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[2]/span').click()

    # 点击地面工程新增
    def flooring_work_new(self):
        for i in range(2):
            logger.info('点击地面工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善地面工程的信息
    def complete_flooring_work(self):
        logger.info('完善地面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('地面工程1')           # 地面工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/input')\
            .send_keys('这是地面1备注信息')      # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('地面工程2')           # 地面工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[3]')\
            .click()                         # 单位:m
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/input')\
            .send_keys('这是地面2备注信息')      # 备注

    # 收起地面模块
    def packup_flooring(self):
        logger.info('收起地面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/span').click()

    # 点击墙面工程
    def metope_engineering(self):
        logger.info('点击墙面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[3]/span').click()

    # 点击墙面工程新增
    def metope_engineering_new(self):
        for i in range(2):
            logger.info('点击墙面工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善墙面工程信息
    def complete_metope_engineering(self):
        logger.info('完善墙面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('墙面工程1')      # 墙面工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是墙面1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('墙面工程2')      # 墙面工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是墙面2备注信息')  # 备注

    # 收起墙面模块
    def packup_metope(self):
        logger.info('收起墙面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/span').click()

    # 点击水电工程
    def waterpower_engineering(self):
        logger.info('点击水电工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[4]/span').click()

    # 点击水电工程新增
    def waterpower_engineering_new(self):
        for i in range(2):
            logger.info('点击水电工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善水电工程信息
    def complete_waterpower_engineering(self):
        logger.info('完善地面工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('水电工程1')           # 水电工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[4]/div[1]/input')\
            .send_keys('这是水电1备注信息')      # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('水电工程2')           # 水电工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:m
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[4]/div[1]/input')\
            .send_keys('这是水电2备注信息')      # 备注

    # 收起水电模块
    def packup_waterpower(self):
        logger.info('收起水电工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/span').click()

    # 点击店招工程
    def signage_engineering(self):
        logger.info('点击店招工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[5]/span').click()

    # 点击店招工程新增
    def signage_engineering_new(self):
        for i in range(2):
            logger.info('点击店招工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善店招工程信息
    def complete_signage_engineering(self):
        logger.info('完善店招工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('店招工程1')           # 店招工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[4]/div[1]/input')\
            .send_keys('这是店招1备注信息')      # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('店招工程2')           # 店招工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]')\
            .click()                         # 单位:m
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[1]/div[3]/input')\
            .send_keys('10')                  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')\
        #     .send_keys('10')                  # 材料报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input')\
            .send_keys('10')                  # 材料报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/input')\
        #     .send_keys('10')                  # 人工报价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')                  # 人工报价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input')\
        #     .send_keys('9')  # 材料成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input')\
            .send_keys('9')  # 材料成本实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/input')\
        #     .send_keys('9')  # 人工成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/input')\
            .send_keys('9')  # 人工成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div[4]/div[1]/input')\
            .send_keys('这是店招2备注信息')      # 备注

    # 收起店招模块
    def packup_signage(self):
        logger.info('完善店招工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[1]/div[1]/span').click()

    # 点击拆除建渣工程
    def demolition_engineering(self):
        logger.info('点击拆除建渣工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[6]/span').click()

    # 点击拆除建渣工程新增
    def demolition_engineering_new(self):
        for i in range(2):
            logger.info('点击拆除建渣工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善拆除建渣工程资料
    def complete_demolition_engineering(self):
        logger.info('完善拆除建渣工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('拆除建渣工程1')      # 拆除建渣工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是拆除建渣工程1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('拆除建渣工程2')      # 拆除建渣工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是拆除建渣2备注信息')  # 备注

    # 收起拆除建渣
    def packup_demolition(self):
        logger.info('收起拆除建渣工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[1]/div[1]/span').click()

    # 其它工程
    def other_projects(self):
        logger.info('点击其它工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[7]/span').click()

    # 其他工程新增
    def other_projects_new(self):
        for i in range(2):
            logger.info('点击其它工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善其它工程资料
    def complete_other_projects(self):
        logger.info('完善其它工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('其它工程1')      # 其它工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是其它工程1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('其它工程2')      # 其它工程名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是其它工程2备注信息')  # 备注

    # 收起其它工程模块
    def packup_live_other(self):
        logger.info('完善其它工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[1]/div[1]/span').click()

    # 收起现场装修模块
    def packup_live(self):
        logger.info('收起现场装修模块')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[1]/span').click()

    # 点击商业展柜部分
    def showcase_part(self):
        logger.info('点击商业展柜部分')
        self.click_button(self.showcase_part_loc)

    # 点击商业展柜部分新增
    def showcase_part_new(self):
        logger.info('点击商业展柜部分新增')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/a').click()
        sleep(1)

    # 点击展柜制作
    def under_production(self):
        logger.info('点击商业展柜制作')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[1]/div[3]/div[1]/div[3]/div[1]/span').click()

    # 点击展柜制作新增
    def under_production_new(self):
        for i in range(2):
            logger.info('点击商业展柜制作新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[1]/div[3]/a').click()
            sleep(1)

    # 完善展柜制作资料
    def complete_under_production(self):
        logger.info('完善商业展柜')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('展柜制作1')      # 展柜制作名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是展柜制作1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('展柜制作2')      # 展柜制作名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是展柜制作2备注信息')  # 备注

    # 收起展柜制作模块
    def packup_under_production(self):
        logger.info('收起商业展柜')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/span').click()

    # 点击美工制作
    def artists_create(self):
        logger.info('点击美工制作')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[1]/div[3]/div[1]/div[3]/div[2]/span').click()

    # 点击美工制作新增
    def artists_create_new(self):
        for i in range(2):
            logger.info('点击美工制作新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善美工制作资料
    def complete_artists_create(self):
        logger.info('完善美工制作')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('美工制作1')      # 美工制作名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是美工制作1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('美工制作2')      # 美工制作名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是美工制作2备注信息')  # 备注

    # 收起美工制作模块
    def packup_artists(self):
        logger.info('收起美工制作')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/span').click()

    # 点击商业展柜其它工程
    def showcase_other(self):
        logger.info('点击其它工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[1]/div[3]/div[1]/div[3]/div[3]/span').click()

    # 点击商业展柜其它新增
    def showcase_other_new(self):
        for i in range(2):
            logger.info('点击其它工程新增')
            self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[1]/div[3]/a').click()
            sleep(1)

    # 完善商业展柜其它资料
    def complete_showcase_other(self):
        logger.info('完善其它工程')
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')\
            .send_keys('商业展柜其它1')      # 商业展柜其它名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[4]/div[1]/input') \
            .send_keys('这是商业展柜其它1备注信息')  # 备注

        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')\
            .send_keys('商业展柜其它2')      # 商业展柜其它名称
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[2]') \
            .click()  # 单位:平方米
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[3]/input') \
            .send_keys('10')  # 预算数量
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input') \
        #     .send_keys('10')  # 单价标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input') \
            .send_keys('10')  # 单价实际
        # self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/input') \
        #     .send_keys('9')  # 成本标准
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/input') \
            .send_keys('9')  # 成本实际
        self.find_element(By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[4]/div[1]/input') \
            .send_keys('这是商业展柜其它2备注信息')  # 备注

    # 全部收起、展开、滑动查看
    def all_open_close(self):
        sleep(2)
        self.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/span').click()
        sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        sleep(2)
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        sleep(2)
        self.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span').click()

    # 添加品牌
    def add_brand(self):
        self.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/span').click()  # 添加品牌
        self.find_element(By.ID, 'brand_auto').send_keys('周大生')
        sleep(1)
        self.find_element(By.XPATH, '//*[@id="brand_list"]/div/div[1]').click()
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/a').click()  # 品牌新增
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/span').click()  # 新增设计部分
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[2]/a').click()  # 设计部分新增
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/span').click()  # 点击设计
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/a').click()

        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/input[1]')\
            .send_keys('品牌设计')            # 品牌设计名称
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/input')\
            .send_keys('10')           # 预算数量
        self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/input')\
            .send_keys('10')           # 报价
        # self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[1]/input')\
        #     .send_keys('9')            # 含税价

    # 保存
    def save(self):
        self.find_element(*self.save_loc).click()
        self.alert_accept()

    # 提交审批
    def submit(self, text):
        self.find_element(*self.submit_loc).click()
        Select(self.find_element(*self.assessor_loc)).select_by_visible_text(text)
        self.find_element(*self.assessor_submit_loc).click()


def test_new_project_base(driver, pid):
    new_page = NewProject(driver)
    # 设计
    new_page.all_button()
    new_page.new_button(pid)
    new_page.popup()
    new_page.submit_button()
    new_page.offer_area()
    new_page.regular_new()
    new_page.design_part()
    new_page.design_part_new()
    new_page.design_button()
    new_page.design_new()
    new_page.complete_design_information()
    new_page.packup_design()

    new_page.regular_new()
    new_page.live_decoration()
    # 天棚
    new_page.live_decoration_new()
    new_page.ceiling_engineering()
    new_page.ceiling_engineering_new()
    new_page.complete_ceiling_engineering()
    new_page.packup_ceiling()
    # 地面
    new_page.live_decoration_new()
    new_page.flooring_work()
    new_page.flooring_work_new()
    new_page.complete_flooring_work()
    new_page.packup_flooring()
    # 墙面
    new_page.live_decoration_new()
    new_page.metope_engineering()
    new_page.metope_engineering_new()
    new_page.complete_metope_engineering()
    new_page.packup_metope()
    # 水电
    new_page.live_decoration_new()
    new_page.waterpower_engineering()
    new_page.waterpower_engineering_new()
    new_page.complete_waterpower_engineering()
    new_page.packup_waterpower()
    # 店招
    new_page.live_decoration_new()
    new_page.signage_engineering()
    new_page.signage_engineering_new()
    new_page.complete_signage_engineering()
    new_page.packup_signage()
    # 拆除建渣
    new_page.live_decoration_new()
    new_page.demolition_engineering()
    new_page.demolition_engineering_new()
    new_page.complete_demolition_engineering()
    new_page.packup_demolition()
    # 其它
    new_page.live_decoration_new()
    new_page.other_projects()
    new_page.other_projects_new()
    new_page.complete_other_projects()
    new_page.packup_live_other()
    new_page.packup_live()

    new_page.regular_new()
    new_page.showcase_part()
    # 展柜制作
    new_page.showcase_part_new()
    new_page.under_production()
    new_page.under_production_new()
    new_page.complete_under_production()
    new_page.packup_under_production()
    # 美工制作
    new_page.showcase_part_new()
    new_page.artists_create()
    new_page.artists_create_new()
    new_page.complete_artists_create()
    new_page.packup_artists()
    # 其它
    new_page.showcase_part_new()
    new_page.showcase_other()
    new_page.showcase_other_new()
    new_page.complete_showcase_other()

    new_page.all_open_close()
    new_page.add_brand()


# 保存
def test_new_project_save(driver, pid):
    new_page = NewProject(driver)
    test_new_project_base(driver, pid)
    new_page.save()


# 提交审核
def test_new_project_submit(driver, pid, text='黑桃K'):
    new_page = NewProject(driver)
    test_new_project_base(driver, pid)
    new_page.submit(text)
