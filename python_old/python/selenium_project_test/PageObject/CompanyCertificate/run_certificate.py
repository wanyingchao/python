from Login.LoginPage import *
from CompanyCertificate.Certificate import *
from selenium import webdriver
import yaml


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

with open("../CompanyCertificate/certificate.yaml", "r", encoding="utf8") as file:
    data = yaml.load(file)

username = data["username"]
password = data["password"]

name = data["name"]
number = data["number"]
email = data["email"]
contact_name = data["contact_name"]
contact_phone = data["contact_phone"]


test_user_login(driver,username,password)
test_company_certificate(driver,name,email,number,contact_name,contact_phone)
