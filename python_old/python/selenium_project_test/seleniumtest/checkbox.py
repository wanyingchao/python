from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("checkbox.html")  #调html文件的位置
driver.get(file_path)

# inputs = driver.find_elements_by_tag_name("input")
#
# for i in inputs:
#     if i.get_attribute("type") == "checkbox":  #遍历复选框
#         i.click()
#         time.sleep(1)
#
# driver.quit()

checkboxes = driver.find_elements_by_xpath("//*[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)
print(len(checkboxes))   #len()方法计算元素的个数

driver.find_elements_by_xpath("//*[@type='checkbox']").pop().click()
# pop()方法用于获取列表中的一个元素（默认为最后一个元素），并返回该元素的值。
# pop()或pop(-1)：       默认获取一组元素中的最后一个
# pop(0)：               默认获取一组元素中的第一个
# pop(1)：               默认获取一组元素中的第二个