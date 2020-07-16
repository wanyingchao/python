# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep, ctime
import appium_config
import unittest


class SSLogin(unittest.TestCase):
    '''���Խ���ͷ��'''
    def setUp(self):
        self.driver = appium_config.appium_start()

    def test_login(self):
        '''�������¼'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/title")[0].click()  # �Ƽ�ҳ��һ������
        sleep(2)
        for i in range(5):
            driver.swipe(300, 600, 300, 100)  # ģ����ָ���ϻ�����5��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_view_comment").click()  # �������������
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/content")[0].click()  # ���۵�һ��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/update_item_digg_layout").click()  # ����
        sleep(2)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/���޽�ͼ.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ����
        sleep(1)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)  # ����������
        driver.find_element_by_id("com.ss.android.article.news:id/write_comment_layout").click()  # д����
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/btn_qzone").click()  # qq�˺ŵ�¼
        sleep(3)
        driver.find_element_by_class_name("android.widget.Button").click()  # ��¼��ť
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/ss_share_text").send_keys("��ֻ���������Ե�")  # ���������
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/publish_btn").click()  # ����
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/���۽�ͼ.png")
        driver.find_element_by_id("com.ss.android.article.news:id/delete").click()  # ɾ������
        sleep(1)
        driver.find_element_by_id("android:id/button1").click()  # ȷ����ť
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_favor").click()  # �ղ�
        sleep(2)
        driver.find_element_by_id("android:id/button2").click()  # ��ת��
        driver.find_element_by_id("com.ss.android.article.news:id/action_favor").click()  # ȡ���ղ�
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_repost").click()  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/cancel_btn").click()  # ȡ������
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/top_more_title").click()  # ����
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[0].click()  # �鿴ͷ����
        sleep(5)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # �����ϼ�
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/top_more_title").click()  # ����
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[1].click()  # ҹ��ģʽ
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[1].click()  # �ռ�ģʽ
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[2].click()  # ��ʾ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/cancel_btn").click()  # ����
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[3].click()  # �ٱ�
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ������һ��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ������һ��
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[1].click()  # �ȵ�
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[3].click()  # ��Ƶ
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[4].click()  # ͼƬ
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[6].click()  # �Ƽ�
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_category").click()  # ҳ�����Ͻ�+��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_collapse").click()  # ҳ�����Ͻ�*��
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[0].click()  # ˢ��

    def test_topic(self):
        '''���Ի���'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[1].click()  # ����
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/reply_notify").click()  # ��Ϣ
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/btn_qzone").click()
        sleep(3)
        driver.find_element_by_class_name("android.widget.Button").click()  # ��¼��ť
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/reply_notify").click()  # ��Ϣ
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/��Ϣ��ͼ.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/add_topic_btn").click()  # ����
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").click()  # ������
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").send_keys("Ӣ������s8")  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_btn_search").click()  # ������ť
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/�����������.png")
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # ����
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # ����

    def test_video(self):
        '''������Ƶ'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[2].click()  # ��Ƶ
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_category").click()  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").send_keys("Ӣ������s8")  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_btn_search").click()  # ������ť
        sleep(3)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/��Ƶ�������.png")
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # ����
        driver.swipe(300, 300, 600, 600)
        sleep(2)

    def test_mine(self):
        '''�����ҵ��˺�'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[3].click()  # �ҵ�
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_btn").click()
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_input").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_input").send_keys("18583965785")
        driver.find_element_by_id("com.ss.android.article.news:id/password_input").send_keys("abc123456")
        driver.find_element_by_id("com.ss.android.article.news:id/login_btn").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/user_name_tv").click()  # �ҵ��˺�
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_text").click()  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/account_head_image").click()  # ͷ��
        driver.find_elements_by_id("android:id/text1")[0].click()           # �����ѡ��
        sleep(2)
        driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")[2].click()  # ѡ��һ��ͼƬ
        sleep(2)
        driver.find_element_by_id("com.android.gallery3d:id/filtershow_done").click()  # ����
        sleep(3)
        driver.find_element_by_id("com.ss.android.article.news:id/account_name_text").click()  # �޸��ǳ�
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("�˻����Ÿ���ͽ��")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # ȷ��
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/account_desc_text").click()  # ǩ��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("�����Ĳ���֮·")
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # ȷ��
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/�ֻ��ŵ�¼�޸�����.png")
        driver.find_element_by_id("com.ss.android.article.news:id/logout").click()  # �˳���¼
        sleep(0.5)
        driver.find_element_by_id("android:id/button1").click()  # ȷ���˳�
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ����
        # qq��¼
        driver.find_element_by_id("com.ss.android.article.news:id/qzone_btn").click()
        sleep(2)
        driver.find_element_by_class_name("android.widget.Button").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/my_friend_update_layout").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/publish_topic").click()
        driver.find_element_by_id("com.ss.android.article.news:id/input_content").send_keys("���׸�д������")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_text").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/update_item_digg_layout").click()
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/��̬�����ͼ.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()
        driver.find_element_by_id("com.ss.android.article.news:id/user_name_tv").click()  # �ҵ��˺�
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_text").click()  # ����
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/account_head_image").click()  # ͷ��
        driver.find_elements_by_id("android:id/text1")[0].click()  # �����ѡ��
        sleep(2)
        driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")[3].click()  # ѡ��һ��ͼƬ
        sleep(2)
        driver.find_element_by_id("com.android.gallery3d:id/filtershow_done").click()  # ����
        sleep(3)
        driver.find_element_by_id("com.ss.android.article.news:id/account_name_text").click()  # �޸��ǳ�
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("�Ŷ��ڲ���ô����")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # ȷ��
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/account_desc_text").click()  # ǩ��
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("�����Ĳ���֮·")
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # ȷ��
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/qq�ŵ�¼�޸�����.png")
        driver.find_element_by_id("com.ss.android.article.news:id/logout").click()  # �˳���¼
        sleep(0.5)
        driver.find_element_by_id("android:id/button1").click()  # ȷ���˳�
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # ����    

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()