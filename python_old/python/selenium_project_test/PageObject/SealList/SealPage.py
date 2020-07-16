from Login.BasePage import *
from selenium.webdriver.common.by import By


class SealList(Page):

    seallist_loc = (By.LINK_TEXT, '印章列表')              # 印章列表
    addseal_loc = (By.LINK_TEXT, '添加印章')               # 添加印章
    sealname_loc = (By.ID, 'sealName')                    # 印章名称
    sealfile_loc = (By.ID, 'submitFile')                  # 选择文件
    submit_loc = (By.CLASS_NAME, 'seal_name_right')       # 上传和保存（两个按钮相同）
    delete_loc = (By.XPATH, '/html/body/div/div[3]/div[2]/div/div[3]')     # 删除

    def seal_list(self):
        self.click_button(self.seallist_loc)

    def add_seal(self):
        self.click_button(self.addseal_loc)

    def seal_name(self,sealname):
        self.send_keys(self.sealname_loc, sealname)

    def seal_file(self,fileloc):
        self.send_keys(self.sealfile_loc, fileloc)

    def submit_file(self,i):               # 同一页面两个按钮相同class,两次调用，i区分
        self.find_elements(*self.submit_loc)[i].click()
        # 添加上传失败的断言
        self.alert_accept()

    def delete_seal(self):
        sleep(2)
        self.click_button(self.delete_loc)
        self.alert_accept()

def test_seal_list(driver,name,fileloc,i):
    seal_page = SealList(driver)

    seal_page.seal_list()
    seal_page.add_seal()
    seal_page.seal_name(name)
    seal_page.seal_file(fileloc)
    seal_page.submit_file(i[0])
    seal_page.submit_file(i[1])
    seal_page.delete_seal()

