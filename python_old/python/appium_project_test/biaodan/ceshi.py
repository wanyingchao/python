from calculator import Count
import unittest

'''
class TestCount:
    def test_add(self):
        try:
            j = Count(2,3)
            add = j.add()
            assert(add == 5),"error"
        except ArithmeticError as msg:
            print(msg)
        else:
            print("pass")

mytest = TestCount()
mytest.test_add()
'''

class MyTest(unittest.TestCase):      #封装
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

class TestAdd(MyTest):

    def test_add(self):
        j = Count(2,3)
        # assertEqual(first,second,msg)   断言第一个参数和第二个参数是否相等，不相等测试失败，返回msg的信息
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(41,76)
        self.assertNotEqual(j.add(),107,msg="出错了")

class TestSub(MyTest):

    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = Count(70,50)
        self.assertNotEqual(j.sub(),10,msg="相等")

if __name__ == "__main__":
    unittest.main()




''' 
if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_sub2"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''