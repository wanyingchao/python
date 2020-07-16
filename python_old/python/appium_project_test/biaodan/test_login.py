from selenium import webdriver
from time import sleep




def wyc(name="18583965785",password="1"):
    return name,password
def mazi(name="12055116631",password=""):
    return name,password
def  login_xj(driver,phone="",password=""):
    # driver = webdriver.Chrome()
    # driver.get("https://www.91szb.com")
    sleep(2)
    driver.find_element_by_id("loginBtn-text").click()
    driver.switch_to.frame("indexFrame")
    sleep(2)
    driver.find_element_by_id("js-phone-num").send_keys(phone)
    driver.find_element_by_id("js-get-code").click()
    sleep(2)
    driver.find_element_by_id("js-code-val").send_keys(password)
    driver.find_element_by_id("js-login-event").click()