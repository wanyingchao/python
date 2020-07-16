import unittest
import time
from HTMLTestRunner import HTMLTestRunner


test_dir = "E:/python/ILIKETEST/selenium/test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "E:/python/ILIKETEST/selenium/Report/html/" + now+" result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况：")
    runner.run(discover)
    fp.close()
