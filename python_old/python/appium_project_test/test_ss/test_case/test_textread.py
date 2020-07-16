# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep, ctime
import appium_config
import unittest


class SSLogin(unittest.TestCase):
    '''测试今日头条'''
    def setUp(self):
        self.driver = appium_config.appium_start()

    def test_login(self):
        '''评论需登录'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/title")[0].click()  # 推荐页第一条新闻
        sleep(2)
        for i in range(5):
            driver.swipe(300, 600, 300, 100)  # 模拟手指向上滑动，5次
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_view_comment").click()  # 点击进入评论区
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/content")[0].click()  # 评论第一条
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/update_item_digg_layout").click()  # 点赞
        sleep(2)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/点赞截图.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回
        sleep(1)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)  # 滑动评论区
        driver.find_element_by_id("com.ss.android.article.news:id/write_comment_layout").click()  # 写评论
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/btn_qzone").click()  # qq账号登录
        sleep(3)
        driver.find_element_by_class_name("android.widget.Button").click()  # 登录按钮
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/ss_share_text").send_keys("我只是来做测试的")  # 输入框输入
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/publish_btn").click()  # 发表
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/评论截图.png")
        driver.find_element_by_id("com.ss.android.article.news:id/delete").click()  # 删除评论
        sleep(1)
        driver.find_element_by_id("android:id/button1").click()  # 确定按钮
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_favor").click()  # 收藏
        sleep(2)
        driver.find_element_by_id("android:id/button2").click()  # 不转发
        driver.find_element_by_id("com.ss.android.article.news:id/action_favor").click()  # 取消收藏
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_repost").click()  # 分享
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/cancel_btn").click()  # 取消分享
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/top_more_title").click()  # 更多
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[0].click()  # 查看头条号
        sleep(5)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回上级
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/top_more_title").click()  # 更多
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[1].click()  # 夜间模式
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[1].click()  # 日间模式
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[2].click()  # 显示设置
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/cancel_btn").click()  # 返回
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/icon")[3].click()  # 举报
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回上一级
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回上一级
        sleep(1)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[1].click()  # 热点
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[3].click()  # 视频
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[4].click()  # 图片
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_elements_by_id("com.ss.android.article.news:id/category_text")[6].click()  # 科技
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_category").click()  # 页面右上角+号
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_collapse").click()  # 页面右上角*号
        sleep(2)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[0].click()  # 刷新

    def test_topic(self):
        '''测试话题'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[1].click()  # 话题
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/reply_notify").click()  # 消息
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/btn_qzone").click()
        sleep(3)
        driver.find_element_by_class_name("android.widget.Button").click()  # 登录按钮
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/reply_notify").click()  # 消息
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/消息截图.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/add_topic_btn").click()  # 搜索
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").click()  # 搜索框
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").send_keys("英雄联盟s8")  # 输入
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_btn_search").click()  # 搜索按钮
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/话题搜索结果.png")
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # 返回
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # 返回

    def test_video(self):
        '''测试视频'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[2].click()  # 视频
        sleep(2)
        for i in range(3):
            driver.swipe(300, 600, 300, 300)
        driver.find_element_by_id("com.ss.android.article.news:id/icon_category").click()  # 搜索
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/search_input").send_keys("英雄联盟s8")  # 输入
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_btn_search").click()  # 搜索按钮
        sleep(3)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/视频搜索结果.png")
        driver.find_element_by_id("com.ss.android.article.news:id/search_cancel").click()  # 返回
        driver.swipe(300, 300, 600, 600)
        sleep(2)

    def test_mine(self):
        '''测试我的账号'''
        driver = self.driver
        driver.find_element_by_id("com.ss.android.article.news:id/ok_btn").click()
        sleep(2)
        driver.find_element_by_id("android:id/button1").click()
        sleep(5)
        driver.find_elements_by_id("com.ss.android.article.news:id/indicator_title")[3].click()  # 我的
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_btn").click()
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_input").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/mobile_input").send_keys("18583965785")
        driver.find_element_by_id("com.ss.android.article.news:id/password_input").send_keys("abc123456")
        driver.find_element_by_id("com.ss.android.article.news:id/login_btn").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/user_name_tv").click()  # 我的账号
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_text").click()  # 设置
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/account_head_image").click()  # 头像
        driver.find_elements_by_id("android:id/text1")[0].click()           # 从相册选择
        sleep(2)
        driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")[2].click()  # 选择一张图片
        sleep(2)
        driver.find_element_by_id("com.android.gallery3d:id/filtershow_done").click()  # 保存
        sleep(3)
        driver.find_element_by_id("com.ss.android.article.news:id/account_name_text").click()  # 修改昵称
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("退货单号给你徒弟")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # 确定
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/account_desc_text").click()  # 签名
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("漫长的测试之路")
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # 确定
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/手机号登录修改名称.png")
        driver.find_element_by_id("com.ss.android.article.news:id/logout").click()  # 退出登录
        sleep(0.5)
        driver.find_element_by_id("android:id/button1").click()  # 确认退出
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回
        # qq登录
        driver.find_element_by_id("com.ss.android.article.news:id/qzone_btn").click()
        sleep(2)
        driver.find_element_by_class_name("android.widget.Button").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/my_friend_update_layout").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/publish_topic").click()
        driver.find_element_by_id("com.ss.android.article.news:id/input_content").send_keys("这首歌写给你听")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/right_text").click()
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/update_item_digg_layout").click()
        sleep(1)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/动态发表截图.png")
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()
        driver.find_element_by_id("com.ss.android.article.news:id/user_name_tv").click()  # 我的账号
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/action_text").click()  # 设置
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/account_head_image").click()  # 头像
        driver.find_elements_by_id("android:id/text1")[0].click()  # 从相册选择
        sleep(2)
        driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")[3].click()  # 选择一张图片
        sleep(2)
        driver.find_element_by_id("com.android.gallery3d:id/filtershow_done").click()  # 保存
        sleep(3)
        driver.find_element_by_id("com.ss.android.article.news:id/account_name_text").click()  # 修改昵称
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("团队内部那么后面")
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # 确定
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/account_desc_text").click()  # 签名
        sleep(1)
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").clear()
        driver.find_element_by_id("com.ss.android.article.news:id/edit_user_info").send_keys("漫长的测试之路")
        driver.find_element_by_id("com.ss.android.article.news:id/confirm_user_info").click()  # 确定
        sleep(5)
        driver.get_screenshot_as_file("E:/python/test_ss/screenshot/qq号登录修改名称.png")
        driver.find_element_by_id("com.ss.android.article.news:id/logout").click()  # 退出登录
        sleep(0.5)
        driver.find_element_by_id("android:id/button1").click()  # 确认退出
        sleep(2)
        driver.find_element_by_id("com.ss.android.article.news:id/back").click()  # 返回    

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()