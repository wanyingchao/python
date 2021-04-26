# 类的常用魔术方法
# 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
# 魔术方法的统一的特征，方法名被前后各两个下划线包裹
    # __init__：构造函数
'''
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")
a = A()
'''
    # __new__:对象实例化函数，此函数较特殊，一般不用
    # __call__:对象当函数使用的时候触发
'''
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")
    def __call__(self, *args, **kwargs):
        print("我被调用了again")
a = A()
a()
'''
    # __str__:当对象被当作字符串使用的时候调用
'''
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")
    def __call__(self, *args, **kwargs):
        print("我被调用了again")
a = A()
a()

    # __repr__:返回字符串
# 描述符相关：
    # __set__
    # __get__
    # __delete__
# 属性操作相关的：
    # __getattr__:访问一个不存在的属性时触发
# 三大方法
class Person():
# 实例方法
    def eat(self):
        print(self)
        print("Eating....")

# 类方法        第一个参数一般命名为cls，区别于self
    def play(cls):
        print(cls)
        print("Playing....")

# 静态方法      不需要用第一个参数表示自身或者类
    def say():
        print("Saying....")

dandan = Person()
# 实例方法
dandan.eat()
# 类方法
Person.play(Person)
dandan.play()
# 静态方法
Person.say()
'''

# 抽象
class Animel():
    def sayHello(self):
        pass
class Dog(Animel):
    def sayHello(self):
        print("闻一下")
class Person(Animel):
    def sayHello(self):
        print("亲一下")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

