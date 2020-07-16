from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep,ctime

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("成都决赛圈见")   #id定位
driver.find_element_by_id("su").click()

sleep(1)  #休眠时间

driver.find_element_by_id("kw").clear()

driver.find_element_by_name("wd").send_keys("成都")  #name定位
driver.find_element_by_id("su").click()

sleep(2)

driver.find_element_by_xpath("//*[@id='s_tab']/div/a[2]").click() #xpath定位(知道)
# driver.find_element_by_xpath("//*[@id='s_tab']/div/a[3]").click()

sleep(2)

driver.find_element_by_link_text("网页").click()  #返回百度网页
driver.find_element_by_id("kw").clear()

sleep(1)

driver.find_element_by_class_name("toindex").click()  #返回到百度首页

   # class定位 _class_name
driver.find_element_by_class_name("s_ipt").send_keys("格调")
driver.find_element_by_id("su").click()

sleep(2)
driver.find_element_by_class_name("toindex").click()  #返回到百度首页

   # link定位，专门用于定位文本链接
driver.find_element_by_link_text("新闻").click()

sleep(1)
driver.find_element_by_link_text("网页").click()  #返回百度网页

driver.find_element_by_link_text("贴吧").click()

sleep(1)
driver.find_element_by_link_text("网页").click()  #返回百度网页

driver.find_element_by_link_text("视频").click()

sleep(1)
driver.find_element_by_link_text("网页").click()  #返回百度网页

   # partial link定位，对link定位的补充，文本链接过长，选取其中一部分
# driver.find_element_by_partial_link_text("京公网").click()  #这是一个弹出窗

   # xpath定位
      # 找元素的绝对路径   div[n]表示第n个div标签
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/form/span/input").send_keys("格调")
driver.find_element_by_id("su").click()

sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/form/span/input").clear()

      # 使用元素的属性值定位,元素的任意属性值都可以使用，只要能唯一的标识一个元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("红河")
driver.find_element_by_xpath("//*[@class='bg s_btn_wr']").click()

sleep(1)
driver.find_element_by_xpath("//input[@id='kw']").clear()
driver.find_element_by_xpath("//input[@id='kw']").send_keys("格调")

   # 层级与属性结合使用：元素本身没有可以唯一标识的属性，找上一级元素
driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()

sleep(1)
driver.find_element_by_xpath("//input[@id='kw']").clear()

   # 使用逻辑运算符and连接属性来唯一标识一个元素

   # CSS定位
       # 通过class属性定位,"."表示通过class属性来定位
driver.find_element_by_css_selector(".s_ipt").send_keys("红河")
       # 通过id属性定位，"#"表示通过id属性来定位
driver.find_element_by_css_selector("#su").click()
       #通过标签名来定位，不需要任何符号标识，但标签名重复概率大，很难唯一标识
# 例如：driver.find_element_by_css_selector("input")

sleep(1)
driver.find_element_by_css_selector(".s_ipt").clear()

       #通过父子关系定位,
driver.find_element_by_css_selector("span>input").send_keys("ysl")  #父元素span下所有叫input的子元素
driver.find_element_by_id("su").click()

sleep(1)
driver.find_element_by_css_selector("span>input").clear()

       #通过属性定位
driver.find_element_by_css_selector("[name='wd']").send_keys("iphone")   #属性值引号可不加
driver.find_element_by_css_selector("[type='submit']").click()

sleep(1)
driver.find_element_by_css_selector("[name='wd']").clear()

       #组合定位
driver.find_element_by_css_selector("form > span.bg.s_ipt_wr.quickdelete-wrap>input.s_ipt").send_keys("紫罗兰")
driver.find_element_by_css_selector("[type='submit']").click()

sleep(1)
driver.find_element_by_css_selector("form > span.bg.s_ipt_wr.quickdelete-wrap>input.s_ipt").clear()

sleep(2)
driver.find_element_by_class_name("toindex").click()  #返回到百度首页

size = driver.find_element_by_id("kw").size   #获得输入框的尺寸
print(size)
text = driver.find_element_by_id("s-bottom-layer-right").text   #返回底部备案信息
print(text)

sleep(1)
driver.quit()