from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep,ctime

driver = webdriver.Chrome()
driver.get("http://pt.91szb.com:8011/seeyon/main.do")

driver.find_element_by_id("login_username").send_keys("肖进")
driver.find_element_by_id("login_password").send_keys("123456abc")
driver.find_element_by_id("login_button").click()

sleep(2)
abc = driver.find_element_by_link_text("售前")
ActionChains(driver).move_to_element(abc).perform()

sleep(2)
above = driver.find_element_by_xpath("//*[@id='583653230694583949']/span[2]")   #合同管理悬停
ActionChains(driver).move_to_element(above).perform()

sleep(2)
driver.find_element_by_xpath("//*[@id='511434448425470192']").click()    #业务合同登记表

driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0002_span']/img").click()  #项目编码
driver.find_element_by_id("search-inputEl").send_keys("2018090993")
driver.find_element_by_id("search-inputEl").send_keys(Keys.ENTER)
sleep(2)
driver.find_element_by_class_name("x-grid-row-checker").click()
sleep(1)
driver.find_element_by_link_text("确定").click()

sleep(2)
driver.find_element_by_id("field0005").send_keys("测试")   #合同名称

driver.find_element_by_xpath("//*[@id='field0010_span']/img").click()  #付款客户
sleep(1)
driver.find_element_by_id("search-inputEl").send_keys("饮水机")
driver.find_element_by_id("search-inputEl").send_keys(Keys.ENTER)
sleep(1)
driver.find_element_by_class_name("x-grid-row-checker").click()
driver.find_element_by_link_text("确定").click()

sleep(1)
driver.find_element_by_id("field0023").send_keys("abc")  #签单负责人

# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0067').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0067").send_keys("否")    #免收一期款
driver.find_element_by_id("field0067").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='field0030_span']/span").click()   #合同签订日期
driver.find_element_by_link_text("确定").click()

sleep(1)
driver.find_element_by_xpath("//*[@id='field0031_span']/span").click()   #合同开始时间
driver.find_element_by_link_text("确定").click()

sleep(1)
driver.find_element_by_xpath("//*[@id='field0032_span']/span").click()   #合同结束时间
# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0032').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0032").send_keys("2018-12-15")
driver.find_element_by_id("field0032").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_id("field0026").send_keys("abc")   #预算负责人

sleep(1)
driver.find_element_by_id("field0047").send_keys("abc")   #收款负责人

sleep(1)
driver.find_element_by_id("field0048").send_keys("abc")   #跟单负责人

sleep(1)
driver.find_element_by_xpath("//*[@id='field0043_span']/span").click()  #客户经理
driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #选取操作的iframe
driver.find_element_by_id("670869647114347-anchor").click()    #点击商装宝公司
driver.find_element_by_id("q").send_keys("肖进")     #搜索人员
driver.find_element_by_id("q").send_keys(Keys.ENTER)
sleep(1)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()  #双击
driver.switch_to.default_content()   #返回最外层iframe
driver.find_element_by_link_text("确定").click()   #点击确定

driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0045_span']/img").click()  #公司代码
driver.find_element_by_class_name("x-grid-row-checker").click()
sleep(1)
driver.find_element_by_link_text("确定").click()

sleep(1)
driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")

# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0042').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0042").send_keys("正常")   #合同标记金额
driver.find_element_by_id("field0042").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='field0080_span']/span").click()  #施工图计划员
driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #选取操作的iframe
driver.find_element_by_id("670869647114347-anchor").click()    #点击商装宝公司
driver.find_element_by_id("q").send_keys("肖进1")     #搜索人员
driver.find_element_by_id("q").send_keys(Keys.ENTER)
sleep(1)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()  #双击
driver.switch_to.default_content()   #返回最外层iframe
driver.find_element_by_link_text("确定").click()   #点击确定

driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")

driver.find_element_by_xpath("//*[@id='field0079_span']/span").click()    #工厂计划
sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))  #切换到进入工厂计划的表单
driver.find_element_by_xpath("//*[@class='hand']/tr/td[1]/div/input").click()  #选择计划
sleep(2)
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()   #确定按钮


driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0076_span']/span").click()   #工厂计划人员
sleep(1)
driver.switch_to.default_content()
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #切换表单
driver.find_element_by_id("670869647114347-anchor").click()         #点击商装宝公司
sleep(1)
driver.find_element_by_id("q").send_keys("肖进2")
driver.find_element_by_id("q").send_keys(Keys.ENTER)
sleep(1)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()    #双击人员选择
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()


driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")

driver.find_element_by_xpath("//*[@id='field0077_span']/span").click()    #现场计划
sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))  #切换到进入现场计划的表单
driver.find_element_by_xpath("//*[@class='hand']/tr/td[1]/div/input").click()  #选择计划
sleep(2)
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()   #确定按钮

driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0078_span']/span").click()   #现场计划人员
sleep(1)
driver.switch_to.default_content()
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #切换表单
driver.find_element_by_id("670869647114347-anchor").click()         #点击商装宝公司
sleep(1)
driver.find_element_by_id("q").send_keys("肖进4")
driver.find_element_by_id("q").send_keys(Keys.ENTER)
sleep(1)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()    #双击人员选择
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()


driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")

# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0052').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0052").send_keys("一期款")
driver.find_element_by_id("field0052").send_keys(Keys.ENTER)
driver.find_element_by_id("field0053").send_keys("2")
driver.find_element_by_id("field0054").send_keys("2018-09-20",Keys.ENTER)
driver.find_element_by_id("field0056").send_keys("协议应付")

sleep(1)
driver.find_element_by_id("field0052").click()
sleep(2)
driver.find_element_by_id("addEmptyImg").click()
# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementsByName('field0052')[1].style.display='block'"
driver.execute_script(js)
driver.find_elements_by_id("field0052")[1].send_keys("二期款")
driver.find_elements_by_id("field0052")[1].send_keys(Keys.ENTER)
driver.find_elements_by_id("field0053")[1].send_keys("3")
driver.find_elements_by_id("field0054")[1].send_keys("2018-09-20",Keys.ENTER)
driver.find_elements_by_id("field0056")[1].send_keys("协议应付")

sleep(1)
driver.find_elements_by_id("field0052")[1].click()
driver.find_element_by_id("addEmptyImg").click()
# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementsByName('field0052')[2].style.display='block'"
driver.execute_script(js)
driver.find_elements_by_id("field0052")[2].send_keys("三期款")
driver.find_elements_by_id("field0052")[2].send_keys(Keys.ENTER)
driver.find_elements_by_id("field0053")[2].send_keys("5")
driver.find_elements_by_id("field0054")[2].send_keys("2018-09-20",Keys.ENTER)
driver.find_elements_by_id("field0056")[2].send_keys("协议应付")

sleep(2)
driver.find_element_by_xpath("//*[@id='field0063_span']/span[2]").click()
driver.switch_to.default_content()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))
driver.find_element_by_xpath("//*[@class='hand']/tr/td[1]/div/input").click()
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()

driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0058').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0058").send_keys("现场",Keys.ENTER)
driver.find_element_by_id("field0060").send_keys("10")
driver.find_element_by_id("field0062").send_keys("协议应付")

sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.find_element_by_id("sendId").click()

# driver.switch_to.default_content()
# driver.switch_to_frame("workflow_dialog_showWorkFlowMatchResultPage_Id_main_iframe_content")
# # js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
# js = "document.getElementById('node_15145199969450_peoples').style.display='block'"
# driver.execute_script(js)
# driver.find_element_by_id("node_15145199969450_peoples").send_keys("肖进1",Keys.ENTER)
# driver.switch_to.default_content()
# driver.find_element_by_link_text("确定").click()


# sleep(5)
# # driver.quit()