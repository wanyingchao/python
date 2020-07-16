from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *


class Check(Page):
    url = '/'

    all_button_loc = (By.LINK_TEXT, '全部')  # 全部
    wait_conform_loc = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/label')   # 待审核
    project_list_loc = (By.CLASS_NAME, 'list-over-effect')
    approve_button_loc = (By.ID, 'edit_audit_pass')   # 审核通过
    submit_loc = (By.XPATH, '//*[@id="q"]/div/div[3]/input[1]')  # 审核通过弹窗确认
    unapprove_button_loc = (By.ID, 'edit_audit_failure')  # 审核不通过


    def all_button(self):
        logger.info('点击全部')
        self.find_element(*self.all_button_loc).click()

    def wait_conform(self):
        logger.info('点击待审核')
        self.find_element(*self.wait_conform_loc).click()
        sleep(2)

    def auditor_button(self,pid):
        rows = self.find_elements(*self.project_list_loc)
        sleep(2)
        for row in rows:
            projectId = row.find_element_by_xpath('.//div[contains(@class,"w_15")]').text
            if pid == projectId:
                global curr_row
                curr_row = row
                break
        sleep(2)
        logger.info('找到项目编码，点击审核')
        curr_row.find_element(By.CLASS_NAME, "text-effect").click()  # 审核按钮

    def approve_button(self):
        sleep(2)
        logger.info('点击审核通过')
        self.find_element(*self.approve_button_loc).click()
        sleep(2)
        logger.info('点击弹窗确认')
        self.find_element(*self.submit_loc).click()  # 确认按钮

    def unapprove_button(self):
        sleep(2)
        logger.info('点击审核不通过')
        self.find_element(*self.unapprove_button_loc).click()
        # 未完待续（不通过原因，文件）


def test_check_base(driver,pid):
    check_page = Check(driver)
    check_page.open()

    check_page.all_button()
    check_page.wait_conform()
    check_page.auditor_button(pid)


# 审核通过
def test_check_approve(driver,pid):
    check_page = Check(driver)
    test_check_base(driver,pid)
    check_page.approve_button()


# 审核不通过
def test_check_unapprove(driver,pid):
    check_page = Check(driver)
    test_check_base(driver,pid)
    check_page.unapprove_button()

