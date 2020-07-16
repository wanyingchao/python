from appium import webdriver
import yaml


def appium_desired():
    with open('E://python/jinzhu/jinzhu_agent/desired_caps/desired_caps.yaml') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = data["noReset"]
    desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
    desired_caps["resetKeyboard"] = data["resetKeyboard"]

    driver = webdriver.Remote("http://" + str(data["ip"]) + ":" + str(data["port"]) + "/wd/hub", desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    appium_desired()
