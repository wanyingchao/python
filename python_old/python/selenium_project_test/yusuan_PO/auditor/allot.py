from yusuan_PO.BasePage.BasePage import *
from selenium.webdriver.support.ui import Select


class Auditor(Page):
    allot_loc = (By.XPATH, '//*[@id="order-list"]/div[1]/div[8]/a')   # 审核人第一条分配
    select_loc = (By.XPATH, '//*[@id="order-1"]/div[1]/div[10]/select')   # 分配编制人员
    select_auditor_loc = (By.XPATH, '//*[@id="tab-content1"]/div[2]/div[1]/div[10]/select')
    submit_loc = (By.XPATH, '//*[@id="order-1"]/div[1]/div[11]/a')

    def click_auditor(self):
        self.click_button(self.allot_loc)

    def select_auditor(self, value):
        Select(self.find_element(*self.select_auditor_loc)).select_by_visible_text(value)

    def click_submit(self):
        self.click_button(self.submit_loc)


def test_allot(driver, value='红桃K'):
    auditor = Auditor(driver)
    auditor.click_auditor()
    auditor.select_auditor(value)
    auditor.click_submit()
