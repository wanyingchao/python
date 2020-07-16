from Login.LoginPage import *
from PersonalCertificate.Certificate import *
from selenium import webdriver
import yaml

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

with open("../PersonalCertificate/certificate.yaml", "r", encoding="utf8") as file:
    data = yaml.load(file)

username = data["username"]
password = data["password"]

name = data["name"]
number = data["number"]
email = data["email"]
value = data["value"]


test_user_login(driver, username, password)
test_personal_certificate(driver,name,number,email,value)
