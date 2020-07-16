import subprocess
from time import ctime
from appium import webdriver
import yaml


class adb_start_appium(object):
    def __init__(self):
        with open('E://python/adb_start_appium/config/desired_caps.yaml') as file:
            self.data = yaml.load(file)

    def appium_start(self):
        cmd = 'start /b appium -a ' + str(self.data['host'])+ ' -p '+ str(self.data['port']) + ' -U ' + self.data['deviceName']

        print('%s at %s' % (cmd, ctime()))
        subprocess.Popen(cmd,shell=True,stdout=open('E://python/adb_start_appium/appium_log/'+str(self.data['port'])+'.log','a'),stderr=subprocess.STDOUT)

    def desired_caps(self):
        desired_caps = {}
        desired_caps["platformName"] = self.data["platformName"]
        desired_caps["deviceName"] = self.data["deviceName"]
        desired_caps["platformVersion"] = self.data["platformVersion"]
        desired_caps["appPackage"] = self.data["appPackage"]
        desired_caps["appActivity"] = self.data["appActivity"]
        desired_caps["noReset"] = self.data["noReset"]
        desired_caps["unicodeKeyboard"] = self.data["unicodeKeyboard"]
        desired_caps["resetKeyboard"] = self.data["resetKeyboard"]

        driver = webdriver.Remote("http://" + str(self.data["host"]) + ":" + str(self.data["port"]) + "/wd/hub", desired_caps)
        return driver


if __name__ == '__main__':
    t = adb_start_appium()
    t.appium_start()
    t.desired_caps()
