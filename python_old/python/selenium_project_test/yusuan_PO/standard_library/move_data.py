from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *


class MoveData(Page):
    one_data_loc = (By.XPATH, '//*[@id="q"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/input')  # 其中一条数据（成都：人工：成本）
    lib_save_loc = (By.ID, 'lib_save')  # 保存
    lib_nonstandard_loc = (By.ID, 'lib_nonstandard')   # 移入非标准库
    unstandaard_button_loc = (By.LINK_TEXT, '非标准库')  # 非标准库按钮
    lib_discard_loc = (By.ID, 'lib_discard')    # 作废
    discard_list_loc = (By.LINK_TEXT, '作废记录')   # 作废记录按钮
    lib_start_loc = (By.ID, 'lib_start')   # 移入标准库

    def select_name(self,name):
        rows = self.find_elements(By.XPATH, './/div[contains(@class,"b_con4")]')
        for row in rows:
            pro_name = row.find_element_by_class_name('omit_2').text
            if name == pro_name:
                global curr_row
                curr_row = row
                break
        curr_row.find_element(By.CLASS_NAME, 'omit_2').click()

    def re_write_data(self):
        self.send_keys(self.one_data_loc, '100')
        self.click_button(self.lib_save_loc)
        self.alert_accept()

    def move_to_unstandard(self):
        self.click_button(self.lib_nonstandard_loc)
        self.alert_accept()

    def unstandaard_button(self):
        self.click_button(self.unstandaard_button_loc)

    def lib_discard(self):
        sleep(2)
        self.click_button(self.lib_discard_loc)
        self.alert_accept()

    def discard_list(self):
        self.click_button(self.discard_list_loc)

    def lib_start(self):
        self.click_button(self.lib_start_loc)
        self.alert_accept()

def test_move(driver,name):
    t = MoveData(driver)
    t.select_name(name)
    t.re_write_data()
    t.select_name(name)
    t.move_to_unstandard()
    t.unstandaard_button()
    t.select_name(name)
    t.lib_discard()
    t.discard_list()
    t.select_name(name)
    t.lib_start()

