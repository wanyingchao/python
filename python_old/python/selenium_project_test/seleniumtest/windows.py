from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

sreach_windows = driver.current_window_handle  #获得当前窗口的句柄

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

all_handles = driver.window_handles    #获得当前打开的所有窗口的句柄

driver.switch_to_window(all_handles[1])  #切换到第二个窗口，handles[]默认为0，即第一个
driver.find_element_by_name("userName").send_keys("username")
driver.find_element_by_name("phone").send_keys("15708420051")
driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("password")
time.sleep(2)

driver.switch_to_window(all_handles[0])   #切换到第一个窗口
driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()  #关闭弹窗
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

# 利用for循环判断当前窗口并进入

# for handle in all_handles:
#     if handle != sreach_windows:
#         driver.switch_to_window(handle)
#         driver.find_element_by_name("userName").send_keys("username")
#         driver.find_element_by_name("phone").send_keys("15708420051")
#         driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("password")
#         time.sleep(2)

# for handle in all_handles:
#     if handle == sreach_windows:
#         driver.switch_to_window(handle)
#         driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
#         driver.find_element_by_id("kw").send_keys("selenium")
#         driver.find_element_by_id("su").click()
#         time.sleep(2)

driver.close()
time.sleep(2)
driver.quit()