from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep,ctime

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")


# 鼠标拖放操作（未成功执行）
# element = driver.find_element_by_name("tj_trnews")
# target = driver.find_element_by_id("kw")
# ActionChains(driver).drag_and_drop(element,target).perform()
# driver.find_element_by_id("su").click()
# # driver.find_element_by_id("kw").submit()

# 显示等待
sleep(2)
driver.refresh()
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw"))) #located(())两个括号
    # WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
    # driver:浏览器驱动
    # timeout:最长超时时间，默认为秒
    # poll_frequency:检测的间隔时间（步长），默认为0.5秒
    # ignored_exceptions：超时后的异常信息
    # WebDriverWait()一般由 until()或 until_not()方法配合使用
element.send_keys("selenium")
sleep(1)
driver.find_element_by_id("kw").submit()

print(ctime())   #打印当前时间
for i in range(10):
    try:
        e = driver.find_element_by_id("kw22")
        if e.is_displayed():  #返回元素是否可见
            break
    except:pass
    sleep(1)
else:
    print("time out")

print(ctime())
driver.close()

# 隐式等待
# WebDriver提供了 implicitly_wait()方法来实现隐式等待，默认设置为0
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.close()
