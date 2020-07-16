from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()  #鼠标悬停

driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)  #等待页面跳转，如未设置休眠时间，没有找到元素就进行下一步了

driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

driver.switch_to_alert().accept()

time.sleep(2)
driver.quit()

# 在webdriver中处理javascript所生成的alart、confirm以及prompt十分简单，用switch_to_alart()定位
# text:                        返回alart/confirm/prompt 中的文字信息
# accept():                    接受现有警告框
# dismiss():                   解散现有警告框
# send_keys(keysToSend):       发送文本至警告框