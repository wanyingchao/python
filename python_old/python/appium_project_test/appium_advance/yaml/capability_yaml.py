from appium import webdriver
import yaml

file = open("desired_caps.yaml", "r")
data = yaml.load(file)

desired_caps = {"platformName": data['platformName'],
                "deviceName": data["deviceName"],
                "platformVersion": data['platformVersion'],
                "appPackage": data["appPackage"],
                "appActivity": data["appActivity"]}


driver = webdriver.Remote("http://" + str(data["ip"]) + ":" + str(data["port"]) + "/wd/hub", desired_caps)