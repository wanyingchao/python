from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import login


driver = webdriver.Chrome()
driver.get("http://pt.91szb.com:8011/seeyon/main.do?method=main")

# 登录
login.login_A8(driver)

sleep(2)

# 鼠标悬停售前
abc = driver.find_element_by_link_text("售前")
ActionChains(driver).move_to_element(abc).perform()

sleep(2)


bbc = driver.find_element_by_xpath("//*[@id='-706461402249934041']/span[2]")
ActionChains(driver).move_to_element(bbc).perform()  #立项管理

sleep(2)

driver.find_element_by_xpath("//*[@id='7068347776013781835']").click()  #项目立项审核表

driver.switch_to_frame("main")  #最外层iframe
driver.switch_to_frame("zwIframe")  #下一层iframe

# js代码使不可见的元素可见（处理可输入的下拉框，输入值后不可见）
js = "document.getElementById('field0062').style.display='block'"
driver.execute_script(js)
driver.find_element_by_id("field0062").send_keys("测试数据")  #数据性质
driver.find_element_by_id("field0062").send_keys(Keys.ENTER)

driver.find_element_by_id("field0006_combox").click()  #省
driver.find_element_by_xpath("//*[@id='field0006_combox']/option[8]").click()
driver.find_element_by_id("field0007_combox").click()  #市
driver.find_element_by_xpath("//*[@id='field0007_combox']/option[6]").click()
driver.find_element_by_id("field0008_combox").click()  #县
driver.find_element_by_xpath("//*[@id='field0008_combox']/option[6]").click()

sleep(1)
driver.find_element_by_id("field0065").send_keys("青啤大道测试")  #街道
driver.find_element_by_id("field0069").send_keys("213")           #门牌
driver.find_element_by_id("field0066").send_keys("测试")          #名称

js = "document.getElementById('field0068').style.display='block'"    # js代码使不可见的元素可见
driver.execute_script(js)
driver.find_element_by_id("field0068").send_keys("四楼")
driver.find_element_by_id("field0068").send_keys(Keys.ENTER)

driver.find_element_by_name("field0067").send_keys("测试")  #主店名称
sleep(1)

js = "document.getElementById('field0029').style.display='block'"   # js代码使不可见的元素可见
driver.execute_script(js)
driver.find_element_by_id("field0029").send_keys("是")    #是否需要设计
driver.find_element_by_id("field0029").send_keys(Keys.ENTER)

driver.find_element_by_id("field0070").send_keys("123")   #备注
driver.find_element_by_id("field0009").click()      #项目地址
driver.find_element_by_id("field0012").send_keys("12055116631")  #主要联系人
sleep(1)

js = "document.getElementById('field0010').style.display='block'"  # js代码使不可见的元素可见
driver.execute_script(js)
driver.find_element_by_id("field0010").send_keys("珠宝")      #行业
driver.find_element_by_id("field0010").send_keys(Keys.ENTER)

js = "document.getElementById('field0014').style.display='block'"   # js代码使不可见的元素可见
driver.execute_script(js)
driver.find_element_by_id("field0014").send_keys("专卖店")   #类型
driver.find_element_by_id("field0014").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//span[@id='field0018_span']/span").click()  #开业时间
sleep(1)
driver.find_element_by_link_text("确定").click()   #确定按钮

sleep(1)
driver.find_element_by_id("field0017").send_keys("1")    #金额
driver.find_element_by_id("field0013").send_keys("1")    #面积
driver.find_element_by_id("field0022").send_keys("万应超")   #商机提供人员

driver.find_element_by_xpath("//*[@id='field0023_span']/span").click()  #量房人员
sleep(1)
driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #选取操作的iframe
sleep(1)
driver.find_element_by_id("670869647114347-anchor").click()    #点击商装宝公司
driver.find_element_by_id("q").send_keys("万应超")     #搜索人员
driver.find_element_by_id("q").send_keys(Keys.ENTER)

double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()  #双击

driver.switch_to.default_content()   #返回最外层iframe
driver.find_element_by_link_text("确定").click()   #点击确定

driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
sleep(1)
driver.find_element_by_xpath("//*[@id='field0033_span']/span").click()  #客户经理

driver.switch_to.default_content()   #返回最外层iframe
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #选取操作的iframe

driver.find_element_by_id("670869647114347-anchor").click()    #点击商装宝公司
driver.find_element_by_id("q").send_keys("肖进")     #搜索人员
driver.find_element_by_id("q").send_keys(Keys.ENTER)

double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()  #双击

driver.switch_to.default_content()   #返回最外层iframe
driver.find_element_by_link_text("确定").click()   #点击确定


driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0060_span']/img").click()  #公司代码
sleep(2)
driver.find_element_by_class_name("x-grid-row-checker").click()
sleep(1)
driver.find_element_by_link_text("确定").click()

sleep(1)
driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0075_span']/span").click()    #销售计划

sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))  #切换到进入销售计划的表单
driver.find_element_by_xpath("//*[@class='hand']/tr/td[1]/div/input").click()  #选择计划

sleep(2)
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()   #确定按钮

driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0079_span']/span").click()   #销售计划人员
sleep(1)
driver.switch_to.default_content()
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")   #切换表单
driver.find_element_by_id("670869647114347-anchor").click()         #点击商装宝公司
sleep(1)
driver.find_element_by_id("q").send_keys("肖进1")
driver.find_element_by_id("q").send_keys(Keys.ENTER)
sleep(1)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()    #双击人员选择
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()

driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")
driver.find_element_by_xpath("//*[@id='field0076_span']/span").click()  #设计计划
sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))
driver.find_element_by_xpath("//*[@class='hand']/tr/td[3]/div").click()
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()

sleep(2)
driver.switch_to.default_content()
driver.switch_to_frame("main")
driver.switch_to_frame("zwIframe")

driver.find_element_by_xpath("//*[@id='field0080_span']/span").click()   #设计计划人员
driver.switch_to.default_content()
driver.switch_to_frame("SelectPeopleDialog_main_iframe_content")
driver.find_element_by_id("670869647114347-anchor").click()
driver.find_element_by_id("q").send_keys("肖进2")
driver.find_element_by_id("q").send_keys(Keys.ENTER)
double_click = driver.find_element_by_xpath("//*[@id='memberDataBody']/option")
ActionChains(driver).double_click(double_click).perform()
sleep(1)
# driver.switch_to.default_content()
# driver.find_element_by_link_text("确定").click()

# sleep(2)
# driver.switch_to.default_content()
# driver.switch_to_frame("main")
# driver.find_element_by_id("sendId").click()
#
#
# sleep(5)
# driver.quit()