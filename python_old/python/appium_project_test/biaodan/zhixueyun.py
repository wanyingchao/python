from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://xinqlfangao.zhixueyun.com")
sleep(2)

driver.find_element_by_id("D49login").click()
sleep(5)
driver.find_element_by_id("D25username").send_keys("904060")
driver.find_element_by_id("D25pword").send_keys("xql904060")
driver.find_element_by_id("D25login").click()
sleep(5)
driver.find_element_by_id("D48menu-2939f209-75d0-4f87-a465-d95b3d108197").click()
sleep(2)
abc = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/div/div/div[2]/div[2]/ul/li[1]/div/div[1]/a/div[1]/img")
ActionChains(driver).move_to_element(abc).perform()
sleep(1)
driver.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/div/div/div[2]/div[2]/ul/li[1]/div/div[1]/a/div[2]/div").click()
sleep(2)
serach_window = driver.current_window_handle
all_hanles = driver.window_handles
driver.switch_to_window(all_hanles[1])
