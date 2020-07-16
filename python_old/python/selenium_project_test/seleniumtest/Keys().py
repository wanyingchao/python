from selenium import webdriver
# 引入Keys模块
from selenium.webdriver.common.keys import Keys   #最后的Keys大写的K
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm") #输入框输入
sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE) #回退

driver.find_element_by_id("kw").send_keys(Keys.SPACE)  #空格
driver.find_element_by_id("kw").send_keys("教材")

sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a") #全选  （CONTROL,“小写的字母”）

sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")  #剪切

sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")  #粘贴

driver.find_element_by_id("kw").send_keys(Keys.ENTER)   #回车

sleep(2)

driver.quit()

'''
send_keys(Keys.BACK_SPACE)                  删除
send_keys(Keys.SPACE)                       空格
send_keys(Keys.TAB)                         制表（Tab）
send_keys(Keys.ESCAPE)                      回退
send_keys(Keys.ENTER)                       回车
send_keys(Keys.CONTORL,"a/c/x/v")           全选/复制/剪切/粘贴
send_keys(Keys.F1)                          键盘F1
......
send_keys(Keys.F2)                          键盘F12
'''
