import unittest,time
from HTMLTestRunner import HTMLTestRunner


test_dir = "../test_case"
report_dir = "../reports"

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")

now = time.strftime("%Y-%m-%d %H-%M-%S")
report_name = report_dir + "/" + now + "  result.html"

with open(report_name, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="考研帮测试用例", description="用例执行情况")
    runner.run(discover)