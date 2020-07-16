from Login.LoginPage import *
from selenium import webdriver
import yaml
from SealList.SealPage import *
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

with open("../SealList/seal_list.yaml", "r", encoding="utf8") as file:
    data = yaml.load(file)

username = data["username"]
password = data["password"]
name = data["name"]
fileloc = data["fileloc"]
i = data["i"]


test_user_login(driver, username, password)
test_seal_list(driver,name,fileloc,i)
