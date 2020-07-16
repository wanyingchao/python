# coding=utf-8
from util.read_init import ReadIni


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        print(self.driver)
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except Exception as e:
            print(str(e))
            return None
