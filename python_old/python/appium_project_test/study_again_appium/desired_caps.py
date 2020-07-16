from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess
from time import ctime


cmd = 'start /b appium -a ' + '127.0.0.1' + ' -p ' + '4723' + ' -U ' + '127.0.0.1:52001'
print('%s at %s' % (cmd, ctime()))
subprocess.Popen(cmd, shell=True, stdout=open('./appium_log/' + '4723' + '.log', 'a'), stderr=subprocess.STDOUT)

time.sleep(3)
desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:52001',
    'platformVersion': '4.4.2',
    'appPackage': 'com.ss.android.article.news',
    'appActivity': 'com.ss.android.article.news.activity.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)
try:
    el = driver.find_element_by_id('com.ss.android.article.news:id/ok_btn')
    el.click()
    print('点击确定')
except NoSuchElementException:
    print('no such element!!!!!!!')

time.sleep(2)
try:
    el2 = driver.find_element_by_id('com.ss.android.article.news:id/content')
    text2 = el2.text
    if text2 == '您是否允许今日头条精选您关注的资讯及时推送?':
        driver.find_element_by_id('android:id/button1').click()
        print('点击允许')
    else:
        print('不明弹窗')
except NoSuchElementException:
    print('no such element!!!!')

time.sleep(10)
try:
    el3 = driver.find_element_by_id('com.ss.android.article.news:id/btn_left')
    text3 = el3.text
    if text3 == '忽略':
        el3.click()
        print('点击忽略')
    else:
        print('不明弹窗')
except NoSuchElementException:
    pass

time.sleep(2)
driver.find_elements_by_id('com.ss.android.article.news:id/indicator_icon')[3].click()
time.sleep(2)
driver.find_element_by_id('com.ss.android.article.news:id/qzone_btn').click()
time.sleep(2)
try:
    driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
    print('没有登录qq获取权限')
except:
    driver.find_element_by_class_name('android.widget.Button').click()
    print('登录了qq获取权限')
time.sleep(5)
try:
    el4 = driver.find_element_by_id('com.ss.android.article.news:id/user_name_tv')
    text4 = el4.text
    if text4 == '团队内部那么后面':
        print('登录成功')
        time.sleep(2)
        driver.find_elements_by_id('com.ss.android.article.news:id/indicator_icon')[0].click()

        size = driver.get_window_size()
        x = size['width']
        y = size['height']
        driver.swipe(x*0.5, y*0.2, x*0.5, y*0.8)
        time.sleep(5)
        driver.find_elements_by_id('com.ss.android.article.news:id/contents_wrapper')[0].click()
        time.sleep(2)
        for i in range(3):
            driver.swipe(x*0.5, y*0.8, x*0.5, y*0.5)
            time.sleep(1)
        driver.find_element_by_id('com.ss.android.article.news:id/write_comment_layout').click()
        driver.find_element_by_id('com.ss.android.article.news:id/ss_share_text').send_keys('路过')
        driver.find_element_by_id('com.ss.android.article.news:id/publish_btn').click()

    else:
        print('登录失败')
except NoSuchElementException:
    print('登录失败')


