from selenium import webdriver
# 导入提供鼠标操作的ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://yunpan.360.cn")

right_click = driver.find_element_by_name("password")
# context_click(right_click)模拟鼠标右键，perform执行操作
ActionChains(driver).context_click(right_click).perform()

sleep(3)

# move_to_element(move_to_element)模拟鼠标悬停
move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[1]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[2]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[3]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[4]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[5]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[6]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

move_to_element = driver.find_element_by_xpath("/html/body/dl/dd/span[7]")
ActionChains(driver).move_to_element(move_to_element).perform()

sleep(2)

#double_click模拟鼠标双击操作
double_click = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]")
ActionChains(driver).double_click(double_click).perform()

sleep(1)

driver.quit()

# 鼠标拖放操作，drag_and_drop(source,target)  见yuansudengdai.py
# element = driver.find_element_by_id("xx")
# target = driver.find_element_by_id("yy")   #把xx拖到yy里去
# ActionChains(driver).drag_and_drop(element,target).perform()
