#  property
# 定义一个person类，具有name,age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数保存
# x = property(fget,fset,fdel,doc)
'''
class Person():
    def fget(self):      # 函数的名称可以任意
        return self._name
    def fset(self,name):
        self._name = name.upper()  # 所有输入的姓名以大写形式保存
    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
p1.name = "dandan"
print(p1.name)
'''
class Person():
    def fget(self):
        return self._age
    def fset(self,age):
        self._age = age
    def fdel(self):
        self._age = "NoAge"
    age = property(fget,fset,fdel,"操作属性")
p2 = Person()
p2.age = "20.1"
print(p2.age)
