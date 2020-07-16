from appium_szb.baseview.BaseView import *
from time import sleep
from appium_szb.LoginPage.login import *


class new_client(BaseView):
    client_button_loc = (By.LINK_TEXT, '客户')   # 客户
    new_button_loc = (By.ID, 'com.cn.szb.customer:id/page_header_layout_more')  # 新增

    def new_client(self):
        self.click_button(self.client_button_loc)
        sleep(1)
        self.click_button(self.new_button_loc)
