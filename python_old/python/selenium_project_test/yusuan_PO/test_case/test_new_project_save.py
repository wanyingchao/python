from yusuan_PO.Login.Login import *
from yusuan_PO.NewProject.new_project import *
from yusuan_PO.auditor.auditor import *
from yusuan_PO.NewProject.save_project import *


with open("../test_case/data.yaml", "r", encoding="utf8") as file:
    data = yaml.load(file)


class NewSave(unittest.TestCase):
    '''新建预算保存再保存待发再提交'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(3)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://172.16.3.83:8080/budget/pages/main"

    def test_new_pro_save(self):
        '''新建预算保存'''
        driver = self.driver
        driver.get(self.base_url + '/')
        pid = data['pid_two']
        test_user_login(driver)
        test_new_project_save(driver, pid)
        test_save_again(driver, pid)
        test_save_project_auditor(driver, pid)
        driver.find_element(By.LINK_TEXT, '退出').click()
        test_user_login(driver, username='12077770551')
        test_check_approve(driver, pid)

    def test_new_pro(self):
        '''编制人员编制提交审核'''
        driver = self.driver
        driver.get(self.base_url+'/')
        pid = data['pid_one']
        test_user_login(driver)
        test_new_project_submit(driver, pid)
        driver.find_element(By.LINK_TEXT, '退出').click()
        test_user_login(driver, username='12077770551')
        test_check_approve(driver, pid)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
