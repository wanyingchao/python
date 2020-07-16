import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number = input("输入一个数：")
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number,10,msg="你输入的不是10")

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()