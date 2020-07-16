class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def clear_keys(self, loc):
        self.find_element(*loc).clear()

    def send_keys(self, loc, value):
        self.clear_keys(loc)
        self.find_element(*loc).send_keys(value)

    def click_button(self, loc):
        self.find_element(*loc).click()

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)