from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *
from selenium.webdriver.support.ui import Select


class StandardLibrary(Page):

    standard_button_loc = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/input[1]')   # 标准库按钮
    unstandard_button_loc = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/input[2]')  # 非标准库
    lib_add_loc = (By.ID, 'lib-add')     # 新建
    type_lib_item_loc = (By.ID, 'lib_item')  # 类别
    lib_unit_loc = (By.ID, 'lib_unit')     # 单位
    lib_note_loc = (By.ID, 'lib_note')     # 备注
    lib_name_loc = (By.ID, 'lib_name')     # 名称
    lib_save_loc = (By.ID, 'lib_save')     # 保存

    def standard_button(self):
        logger.info('点击标准库按钮')
        self.click_button(self.standard_button_loc)

    def unstandard_button(self):
        logger.info('点击非标准库')
        self.click_button(self.unstandard_button_loc)

    def lib_add(self):
        logger.info('点击新建')
        self.click_button(self.lib_add_loc)

    def type_lib_item(self, value):
        logger.info('选择类别')
        Select(self.find_element(*self.type_lib_item_loc)).select_by_value(value)

    def lib_unit(self,value):
        logger.info('选择单位')
        Select(self.find_element(*self.lib_unit_loc)).select_by_value(value)

    def lib_note(self, note):
        logger.info('填写备注')
        self.send_keys(self.lib_note_loc, note)

    def lib_name(self, name):
        logger.info('填写名称')
        self.send_keys(self.lib_name_loc, name)

    def input_lib_data(self):
        logger.info('填写数据')
        cost_1 = self.find_elements(By.XPATH, '//input[contains(@lib-price,"cost_1")]')
        for i, c1 in enumerate(cost_1):
            c1.send_keys(i + 1)
        price_1 = self.find_elements(By.XPATH, '//input[contains(@lib-price,"price_1")]')
        for i, c1 in enumerate(price_1):
            c1.send_keys(i + 2)
        cost_2 = self.find_elements(By.XPATH, '//input[contains(@lib-price,"cost_2")]')
        for i, c1 in enumerate(cost_2):
            c1.send_keys(i + 3)
        price_2 = self.find_elements(By.XPATH, '//input[contains(@lib-price,"price_2")]')
        for i, c1 in enumerate(price_2):
            c1.send_keys(i + 4)

    def lib_save(self):
        logger.info('点击保存')
        self.click_button(self.lib_save_loc)
        self.alert_accept()


# 新建标准库
def test_standard_lib(driver,value,note,name):
    lib = StandardLibrary(driver)

    lib.standard_button()
    lib.lib_add()
    lib.type_lib_item(value)
    lib.lib_unit(value)
    lib.lib_note(note)
    lib.lib_name(name)
    lib.input_lib_data()
    lib.lib_save()


# 新建非标准库
def test_unstandard_lib(driver,value,note,name):
    lib = StandardLibrary(driver)

    lib.unstandard_button()
    lib.lib_add()
    lib.type_lib_item(value)
    lib.lib_unit(value)
    lib.lib_note(note)
    lib.lib_name(name)
    lib.input_lib_data()
    lib.lib_save()
