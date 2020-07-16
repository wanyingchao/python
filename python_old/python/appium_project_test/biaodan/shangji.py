from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import login

driver = webdriver.Chrome()
driver.get("http://pt.91szb.com:8011/seeyon/main.do")

# 登录
login.login_A8(driver, name="万应超", password="123456abc")

sleep(2)

# 鼠标悬停售前
abc = driver.find_element_by_link_text("售前")
ActionChains(driver).move_to_element(abc).perform()

sleep(2)

# 鼠标悬停商机管理
bbc = driver.find_element_by_xpath("//*[@id='5049337705759985130']")
ActionChains(driver).move_to_element(bbc).perform()

sleep(2)

# 鼠标点击商机登记信息
driver.find_element_by_xpath("//*[@id='1331574756786129903']").click()

sleep(2)

# 定位商机登记信息表单
driver.switch_to_frame("main")
driver.find_element_by_xpath("//*[@id='fr-btn-CustomToolBarButton']/div/em/button").click()

sleep(5)

# 切换窗口
sreach_window = driver.current_window_handle
all_handles = driver.window_handles
driver.switch_to_window(all_handles[1])

# 商机来源
driver.find_element_by_id("nicheSource").click()
driver.find_element_by_xpath("//*[@id='nicheSource']/option[3]").click()

sleep(2)


# q = driver.find_element_by_xpath("//*[@id='province']/option[5]") #省
# w = driver.find_element_by_xpath("//*[@id='city']/option[8]")    #市
# e = driver.find_element_by_xpath("//*[@id='county']/option[3]")  #县

driver.find_element_by_id("province").click()
driver.find_element_by_xpath("//*[@id='province']/option[5]") #省
sleep(2)
driver.find_element_by_id("city").click()
driver.find_element_by_xpath("//*[@id='city']/option[8]")    #市
sleep(2)
driver.find_element_by_id("county").click()
driver.find_element_by_xpath("//*[@id='county']/option[3]")  #县

# # 省
# driver.find_element_by_id("province").click()
# ActionChains(driver).click(q).perform()
#
# sleep(2)
#
# # 市
# driver.find_element_by_id("city").click()
# ActionChains(driver).click(w).perform()
#
# sleep(2)
#
# # 县
# driver.find_element_by_id("county").click()
# ActionChains(driver).click(e).perform()

sleep(2)

# 资料完善
driver.find_element_by_id("street").send_keys("青啤大道测试")
driver.find_element_by_id("build_name").send_keys("脚本")
driver.find_element_by_id("shop_name").send_keys("测试")
driver.find_element_by_id("nicheIndustry").click()
driver.find_element_by_xpath("//*[@id='nicheIndustry']/option[6]").click()
driver.find_element_by_id("main_contacts").send_keys("脚本")
driver.find_element_by_id("phone").send_keys("12055116631")

sleep(2)

# 新增商机
driver.find_element_by_id("save-info").click()

sleep(2)

# 接受警告框
driver.switch_to_alert().accept()
