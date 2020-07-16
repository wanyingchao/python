from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *
from selenium.webdriver.support.ui import Select
import json


class ApproveNewPro(Page):
    all_button_loc = (By.LINK_TEXT, '全部')
    approve_pass_loc = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[4]/label')  # 审核通过
    project_list_loc = (By.CLASS_NAME, 'list-over-effect')  # 项目列表
    clear_all_loc = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[2]/p/a')  # 常规项目清空
    regular_project_new = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[2]/a')  # 常规项目新增
    design_part_loc = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[3]/div[1]/span')  # 设计部分
    design_part_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[2]/a')  # 设计部分新增
    design_button_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/span')  # 设计
    design_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[2]/div/div[1]/div[3]/a')  # 设计新增
    live_decoration_lco = (By.XPATH, '//*[@id="project"]/div[1]/div[3]/div[1]/div[3]/div[2]/span')  # 现场装修部分
    live_decoration_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/a')  # 现场装修部分新增

    ceiling_engineering_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]/span')
    flooring_work_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[2]/span')
    metope_engineering_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[3]/span')
    water_power_engineering_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[4]/span')
    signage_engineering_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[5]/span')
    slag_works_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[6]/span')
    other_works_loc = (By.XPATH, '//*[@id="project"]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[7]/span')

    ceiling_engineering_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/a')
    flooring_work_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/a')
    metope_engineering_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/a')
    water_power_engineering_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[3]/a')
    signage_engineering_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[1]/div[3]/a')
    slag_works_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[1]/div[3]/a')
    other_works_new_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[1]/div[3]/a')

    close_design_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[1]/div[2]/div/div[1]/div[1]/span')
    close_ceiling_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/span')
    close_flooring_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/span')
    close_metope_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/span')
    close_water_power_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/span')
    close_signage_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[5]/div[1]/div[1]/span')
    close_slag_works_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[6]/div[1]/div[1]/span')
    close_other_works_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[2]/div[2]/div[7]/div[1]/div[1]/span')

    edit_submit_audit_loc = (By.ID, 'edit_submit_audit')     # 提交审核
    butget_assessor_loc = (By.ID, 'butget_assessor')          # 选择审核人员
    last_submit_loc = (By.XPATH, '//*[@id="q"]/div/div[3]/input[1]')   # 选择审核人员后的确认

    def get_budget_datas(self):
        with open("E:/python/yusuan_PO/config/budget_datas.json", 'r', encoding="utf-8") as load_f:
            self.budget_datas = json.load(load_f)

    def get_project(self):
        self.get_budget_datas()
        return self.find_element(By.XPATH, '//div[contains(@class,"project")]')

    def get_item1(self, item_val):
        project = self.get_project()
        item1s = project.find_elements_by_xpath('.//div[contains(@class,"item1_statistics")]')
        for item in item1s:
            create_item = item.get_attribute("create-item")
            if create_item == item_val:
                return item

    def get_item2(self, item1):
        return item1.find_element_by_xpath('.//div[contains(@class,"item2_statistics")]')

    def get_item3(self, item1, item_val):
        item2 = self.get_item2(item1)
        item3s = item2.find_elements_by_xpath('.//div[contains(@class,"item3_statistics")]')
        for item3 in item3s:
            create_item = item3.get_attribute("create-item")
            if create_item == item_val:
                return item3

    def get_input_rows_1(self, item3):
        return item3.find_elements_by_xpath('.//div[contains(@class,"early-2")]')

    def get_input_rows_2(self, item3):
        return item3.find_elements_by_xpath('.//div[contains(@class,"tp-3")]')

    def input_datas(self, rows, item_val):
        for i, row in enumerate(rows):
            data = self.budget_datas[item_val][i]
            self.input_data(row, data)

    def input_data(self, input_row, data):
        butget_name = input_row.find_element_by_xpath('.//input[contains(@class,"butget_name")]')
        self.set_data(butget_name, data['name'])
        try:
            butget_unit = Select(input_row.find_element_by_class_name('butget_unit')).select_by_value('1')
            self.set_butget_unit(butget_unit)
        except:
            pass
        try:
            butget_num = input_row.find_element_by_xpath('.//input[contains(@class,"butget_num")]')
            self.set_data(butget_num, data['num'])
        except:
            pass
        try:
            materials_actual_price = input_row.find_element_by_xpath(
                './/input[contains(@class,"materials_actual_price")]')
            self.set_data(materials_actual_price, data['materials_actual_price'])
        except:
            pass
        try:
            person_actual_price = input_row.find_element_by_xpath('.//input[contains(@class,"person_actual_price")]')
            self.set_data(person_actual_price, data['person_actual_price'])
        except:
            pass
        try:
            materials_actual_cost = input_row.find_element_by_xpath(
                './/input[contains(@class,"materials_actual_cost")]')
            self.set_data(materials_actual_cost, data['materials_actual_cost'])
        except:
            pass
        try:
            person_actual_cost = input_row.find_element_by_xpath('.//input[contains(@class,"person_actual_cost")]')
            self.set_data(person_actual_cost, data['person_actual_cost'])
        except:
            pass
        try:
            butget_note = input_row.find_element_by_xpath('.//input[contains(@class,"butget_note")]')
            self.set_data(butget_note, data['butget_note'])
        except:
            pass
        try:
            tax_price = input_row.find_element_by_xpath('.//input[contains(@class,"tax_price")]')
            self.set_data(tax_price, data['tax'])
        except:
            pass

    # def find_input_set_data(self, input_row, classname):
    #     try:
    #         tax_price = input_row.find_element_by_xpath('.//input[contains(@class,' + classname + ')]')
    #         self.set_tax_price(tax_price)
    #     except:
    #         pass

    def set_data(self, ele, val):
        if ele is None:
            return
        ele.send_keys(val)

    # def set_budget_name(self, ele, val):
    #     if ele is None:
    #         return
    #     ele.send_keys(val)

    def set_butget_unit(self, ele):
        if ele is None:
            return

    # def set_butget_num(self, ele, val):
    #     if ele is None:
    #         return
    #     ele.send_keys(val)
    #
    # def set_materials_actual_price(self, ele):
    #     if ele is None:
    #         return
    #
    # def set_person_actual_price(self, ele):
    #     if ele is None:
    #         return
    #
    # def set_materials_actual_cost(self, ele):
    #     if ele is None:
    #         return
    #
    # def set_person_actual_cost(self, ele):
    #     if ele is None:
    #         return
    #
    # def set_butget_note(self, ele):
    #     if ele is None:
    #         return
    #
    # def set_tax_price(self, ele):
    #     if ele is None:
    #         return

    def all_button(self):
        logger.info('点击全部')
        self.find_element(*self.all_button_loc).click()

    def approve_pass(self):
        logger.info('点击审核通过')
        self.find_element(*self.approve_pass_loc).click()

    # 点击编辑
    def edit_button(self, pid):
        rows = self.find_elements(*self.project_list_loc)
        for row in rows:
            projectId = row.find_element_by_xpath('.//div[contains(@class,"w_15")]').text
            if pid == projectId:
                global curr_row
                curr_row = row
                break
        sleep(2)
        logger.info('点击编辑')
        curr_row.find_element(By.CLASS_NAME, "text-effect").click()  # 编辑按钮

    def clear_all(self):
        sleep(1)
        logger.info('清空所有数据')
        self.find_element(*self.clear_all_loc).click()
        sleep(1)

    # 点击常规项目新增
    def regular_new(self):
        logger.info('点击常规项目新增')
        self.click_button(self.regular_project_new)
        sleep(1)

    # 点击设计部分
    def design_part(self):
        self.regular_new()
        logger.info('点击设计部分')
        self.click_button(self.design_part_loc)

    # 点击设计部分新增
    def design_part_new(self):
        self.design_part()
        logger.info('点击设计部分新增')
        self.click_button(self.design_part_new_loc)
        sleep(1)

    # 点击设计
    def design_button(self):
        self.design_part_new()
        logger.info('点击设计')
        self.click_button(self.design_button_loc)

    # 点击设计新增
    def design_new(self):
        self.design_button()
        logger.info('点击设计新增，两条')
        for i in range(2):  # 新增两条
            self.click_button(self.design_new_loc)
            sleep(1)

    def live_decoration(self):
        self.regular_new()
        logger.info("点击现场装修部分")
        self.click_button(self.live_decoration_lco)

    def live_decoration_new(self):
        logger.info('点击现场装修部分新增')
        self.click_button(self.live_decoration_new_loc)

    def ceiling_engineering(self):
        self.live_decoration_new()
        logger.info('点击天棚工程')
        self.click_button(self.ceiling_engineering_loc)

    def ceiling_engineering_new(self):
        self.ceiling_engineering()
        logger.info('天棚工程新增两条')
        for i in range(2):
            self.click_button(self.ceiling_engineering_new_loc)
            sleep(1)

    def flooring_work(self):
        self.live_decoration_new()
        logger.info('点击地面工程')
        self.click_button(self.flooring_work_loc)

    def flooring_work_new(self):
        self.flooring_work()
        logger.info('地面工程新增两条')
        for i in range(2):
            self.click_button(self.flooring_work_new_loc)
            sleep(1)

    def metope_engineering(self):
        self.live_decoration_new()
        logger.info('点击墙面工程')
        self.click_button(self.metope_engineering_loc)

    def metope_engineering_new(self):
        self.metope_engineering()
        logger.info('墙面工程新增两条')
        for i in range(2):
            self.click_button(self.metope_engineering_new_loc)
            sleep(1)

    def water_power_engineering(self):
        self.live_decoration_new()
        logger.info('点击水电工程')
        self.click_button(self.water_power_engineering_loc)

    def water_power_engineering_new(self):
        self.water_power_engineering()
        logger.info('水电工程新增两条')
        for i in range(2):
            self.click_button(self.water_power_engineering_new_loc)
            sleep(1)

    def signage_engineering(self):
        self.live_decoration_new()
        logger.info('点击店招工程')
        self.click_button(self.signage_engineering_loc)

    def signage_engineering_new(self):
        self.signage_engineering()
        logger.info('店招工程新增两条')
        for i in range(2):
            self.click_button(self.signage_engineering_new_loc)
            sleep(1)

    def slag_works(self):
        self.live_decoration_new()
        logger.info('点击拆除建渣工程')
        self.click_button(self.slag_works_loc)

    def slag_works_new(self):
        self.slag_works()
        logger.info('拆除建渣工程新增两条')
        for i in range(2):
            self.click_button(self.slag_works_new_loc)
            sleep(1)

    def other_works(self):
        self.live_decoration_new()
        logger.info('点击其它工程')
        self.click_button(self.other_works_loc)

    def other_works_new(self):
        self.other_works()
        logger.info('其它工程新增两条')
        for i in range(2):
            self.click_button(self.other_works_new_loc)
            sleep(1)

    def close_design(self):
        self.click_button(self.close_design_loc)

    def close_ceiling(self):
        self.click_button(self.close_ceiling_loc)

    def close_flooring(self):
        self.click_button(self.close_flooring_loc)

    def close_metope(self):
        self.click_button(self.close_metope_loc)

    def close_water_power(self):
        self.click_button(self.close_water_power_loc)

    def close_signage(self):
        self.click_button(self.close_signage_loc)

    def close_slag_works(self):
        self.click_button(self.close_slag_works_loc)

    def close_other_works(self):
        self.click_button(self.close_other_works_loc)

    def edit_submit_audit(self, value):
        self.click_button(self.edit_submit_audit_loc)
        sleep(1)
        Select(self.find_element(*self.butget_assessor_loc)).select_by_visible_text(value)
        sleep(1)
        self.click_button(self.last_submit_loc)
        sleep(2)
        self.alert_accept()


def test(driver, pid, value='黑桃K'):
    t = ApproveNewPro(driver)

    t.all_button()
    t.approve_pass()
    t.edit_button(pid)
    t.clear_all()
    t.design_new()

    design = t.get_item1('1')
    design_item = t.get_item3(design, '6')
    rows = t.get_input_rows_1(design_item)
    t.input_datas(rows, '6')
    t.close_design()

    t.live_decoration()
    t.ceiling_engineering_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '7')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '7')
    t.close_ceiling()

    t.flooring_work_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '8')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '8')
    t.close_flooring()

    t.metope_engineering_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '9')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '9')
    t.close_metope()

    t.water_power_engineering_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '11')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '11')
    t.close_water_power()

    t.signage_engineering_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '12')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '12')
    t.close_signage()

    t.slag_works_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '17')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '17')
    t.close_slag_works()

    t.other_works_new()
    design = t.get_item1('2')
    design_item = t.get_item3(design, '18')
    rows = t.get_input_rows_2(design_item)
    t.input_datas(rows, '18')
    t.close_other_works()

    t.edit_submit_audit(value)
