from contract_po.login.login import *
from contract_po.business.business import *
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://110.185.169.136:29090/contract/')
driver.maximize_window()
driver.implicitly_wait(5)
pid = "62101900003"
start_time = '2018-10-01'
end_time = '2019-03-30'
partA = '测试股份有限公司'
review_time = '2019-02-22'
contract_name = '脚本纸质合同'
first_time = '2019-01-01'
second_time = '2019-01-02'
third_time = '2019-01-03'


test_login(driver)
test_business(driver, pid, start_time, end_time, partA, review_time, contract_name, first_time, second_time, third_time)
