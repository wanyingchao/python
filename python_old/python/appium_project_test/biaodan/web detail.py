from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import os
import login_hui


driver = webdriver.Chrome()
driver.get("https://www.91szb.com")
sleep(1)
driver.maximize_window()
driver.implicitly_wait(10)
login_hui.login(driver,phone="18583965785",password="1")
sleep(5)

driver.switch_to.default_content()
driver.switch_to_frame("indexFrame")
driver.find_element_by_xpath("//*[@id='u70']/p").click()  #筛选进行中
sleep(5)
driver.find_element_by_xpath("//*[@id='u71']/p").click()  #筛选已完工
sleep(5)
driver.find_element_by_xpath("//*[@id='u73']/p").click()  #筛选全部
sleep(5)

driver.find_element_by_id("u586").send_keys("2018090953",Keys.ENTER)  #搜索框
sleep(5)
driver.find_element_by_id("u586").clear()
driver.find_element_by_id("u586").send_keys(Keys.ENTER)
sleep(5)

driver.find_element_by_xpath("//*[@id='projectAll']/div[1]/div[1]").click()   #项目列表页第一个项目

driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='js-radio']/input[2]").click()   #实施业务
driver.find_element_by_xpath("//*[@id='js-add-firm']/div/div/div[3]/div[1]").click()   #确定

driver.switch_to.default_content()
driver.switch_to.frame("indexFrame")
sleep(2)
driver.find_element_by_id("jump-file-sys").click()   #文件系统
sleep(2)

search_window = driver.current_window_handle    #切换到第二个窗口
all_handles = driver.window_handles
driver.switch_to_window(all_handles[1])

sleep(2)
driver.find_element_by_xpath("//*[@id='ion-file-type-opt']/select/option[5]").click()   #文件类型
sleep(2)
driver.find_element_by_xpath("//*[@id='ss']/input").click()    #选择文件
sleep(2)
os.system("E:\python\Autolt\\upfile_file_system.exe")  #调用Autolt
sleep(2)

driver.find_element_by_xpath("//*[@id='ion-file-submit-btn']/input[1]").click()   #提交
sleep(10)
driver.find_element_by_link_text("确定").click()   #弹窗确定
sleep(2)

driver.find_element_by_xpath("//*[@id='update-accordion']/div[4]/div[1]/div[2]/a[2]").click()   #展开
sleep(2)
driver.find_element_by_xpath("//*[@id='update-accordion']/div[4]/div[1]/div[3]").click()   #下载
sleep(5)
driver.close()

# sleep(2)
# driver.find_element_by_xpath("//body/div[1]/div[2]/div[1]/div[4]/p").click()

driver.switch_to_window(all_handles[0])
driver.switch_to_frame("indexFrame")
driver.find_element_by_id("u586").send_keys("平面图任务",Keys.ENTER)  #搜索框
sleep(2)
driver.find_element_by_id("u586").clear()
driver.find_element_by_id("u586").send_keys(Keys.ENTER)
sleep(2)
driver.find_element_by_xpath("//*[@id='base']/div[5]/div[2]/div[2]/div[1]/div[1]").click()  #任务列表页第一个任务

sleep(2)
driver.find_element_by_xpath("//*[@id='base']/div[2]/div[3]/div[1]/div[1]/div/span[2]").click()  #工作组
driver.find_element_by_id("u1065_input").send_keys("5785",Keys.ENTER)  #工作组搜索框
sleep(2)
driver.find_element_by_id("u1065_input").clear()
driver.find_element_by_id("u1065_input").send_keys(Keys.ENTER)
sleep(2)

sleep(2)
driver.find_element_by_xpath("//*[@id='u1184_text']/p/span[2]").click()   # 添加工作组
sleep(2)
driver.find_element_by_xpath("//*[@id='u1441_text']/p/span[2]").click()  # 批量添加
sleep(2)
driver.find_element_by_xpath("//*[@id='u1617_text']/p/div/ins").click()  #全选
driver.find_element_by_id("u1615").click()   #提交
sleep(2)

driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()   #确定

driver.switch_to.default_content()
driver.switch_to_frame("indexFrame")
sleep(2)
driver.find_element_by_xpath("//*[@id='u1075']/div/div[3]").click()   #列表第三个
sleep(2)
driver.find_element_by_id("u1208").click()  #移除工作组
driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='confirm']/div/div/div[3]/div[1]").click()

driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='u541']/p/span").click()    #系统消息
sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame("indexFrame")
driver.find_element_by_xpath("//*[@id='u4096_text']/p/span[1]").click()  #全部标记已读
sleep(2)

driver.find_element_by_xpath("//*[@id='pageLimit']/li[11]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='pageLimit']/li[11]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='pageLimit']/li[12]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='pageLimit']/li[2]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='pageLimit']/li[2]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='pageLimit']/li[1]/a").click()
sleep(2)

driver.switch_to.default_content()
driver.find_element_by_xpath("//*[@id='u467']/p[1]/span").click()
sleep(2)
text1 = driver.find_element_by_xpath("//*[@id='u473']/p/span").text
text2 = driver.find_element_by_xpath("//*[@id='u471']/p[4]/span").text
text3 = driver.find_element_by_xpath("//*[@id='u471']/p[2]/span").text
text4 = driver.find_element_by_xpath("//*[@id='u471']/p[3]/span").text
print(text1)
print(text2)
print(text3)
print(text4)