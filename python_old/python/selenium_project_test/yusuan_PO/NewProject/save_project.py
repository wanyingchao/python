from yusuan_PO.BasePage.BasePage import *
from yusuan_PO.BasePage.logger import *
from selenium.webdriver.support.ui import Select


class SaveProject(Page):
    all_button_loc = (By.LINK_TEXT, '全部')    # 点击全部
    project_list_loc = (By.CLASS_NAME, 'list-over-effect')   # 项目列表
    open_loc = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/span')  # 全部展开
    delete_loc = (By.XPATH, '//*[@id="project"]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div[2]/a')  # 删除商业展柜其它工程的第一条数据
    close_loc = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span')  # 全部收起
    edit_submit_loc = (By.ID, 'edit_submit_audit')  # 提交审批
    save_button_loc = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/span')
    save_to_momentum_loc = (By.CLASS_NAME, 'save_item')  # 保存待发
    assessor_loc = (By.ID, 'butget_assessor')   #选择审核人
    assessor_submit_loc = (By.XPATH, '//*[@id="q"]/div/div[3]/input[1]')   # 提交审核，弹窗确认

    # 点击全部
    def all_button(self):
        logger.info('点击全部')
        self.click_button(self.all_button_loc)

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
        curr_row.find_element(By.CLASS_NAME,"text-effect").click()  # 编辑按钮

    def all_open(self):
        sleep(2)
        logger.info('全部展开')
        self.find_element(*self.open_loc).click()
        sleep(2)
        logger.info('滑动到底部')
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def delete(self):
        sleep(2)
        logger.info('删除一项数据')
        self.find_element(*self.delete_loc).click()

    def all_close(self):
        sleep(2)
        logger.info('滑动到顶部')
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('全部收起')
        self.find_element(*self.close_loc).click()

    def edit_submit(self, text):
        logger.info('点击提交审核')
        self.find_element(*self.edit_submit_loc).click()
        Select(self.find_element(*self.assessor_loc)).select_by_visible_text(text)
        self.find_element(*self.assessor_submit_loc).click()

    def save_button(self):
        logger.info('点击保存')
        self.find_element(*self.save_button_loc).click()

    # i=0保存待发，i=1保存模板
    def save_to_momentum(self, i):
        self.find_elements(*self.save_to_momentum_loc)[i].click()
        if i == 0:
            sleep(2)
            self.alert_accept()


# 提交审批
def test_save_project_auditor(driver,pid,text='黑桃K'):
    save_project = SaveProject(driver)

    save_project.all_button()
    save_project.edit_button(pid)
    save_project.all_open()
    save_project.all_close()
    save_project.edit_submit(text)


# 再次保存
def test_save_again(driver,pid,i=0):
    save_project = SaveProject(driver)

    save_project.all_button()
    save_project.edit_button(pid)
    save_project.all_open()
    save_project.delete()
    save_project.all_close()
    save_project.save_button()
    save_project.save_to_momentum(i)
