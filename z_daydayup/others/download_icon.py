from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.iconfont.cn/collections/detail?cid=22163')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="magix_vf_header"]/header/div/div[2]/ul/li[2]/a/i').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="body_dlg_122"]/div[3]/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_id('userId').send_keys('18583965785')
driver.find_element_by_id('passwd').send_keys('1234567887654321')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
time.sleep(5)
driver.refresh()
time.sleep(5)

for i in range(1, 80):
    ele = driver.find_element_by_xpath('//*[@id="magix_vf_main"]/div[2]/div[1]/div[1]/ul/li[%s]' %i)
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="magix_vf_main"]/div[2]/div[1]/div[1]/ul/li[%s]/div[2]/span[3]' %i).click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="mp-e2e-body"]/div[5]/span[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/span').click()
    time.sleep(1)
