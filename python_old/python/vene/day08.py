### 定义类
'''
class Student():
    pass  # 一个空类，pass代表跳过，pass必须有
### 定义对象
yueyue = Student()
class PythonStudent():
    name = None     # 用None给不确定的值赋值
    age = 18
    course = "Python"
    def doHomework(self):  # 注意def的缩进层级，系统默认有一个self参数
        print("I 在做作业")
        return None   # 推荐在末尾使用return语句
dongdong = PythonStudent()
print(dongdong.name)
print(dongdong.age)
dongdong.doHomework()
'''
'''
class Teacher():
    name = "duoduo"
    age = 20
    def say(self):     # 有self的是非绑定类的方法
        self.name = "henduo"
        self.age = 18
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    def sayAgain():    #  没有self的是绑定类方法
        print("Hllo Wold")
        print(Teacher.name)
        print(Teacher.age)

t = Teacher()
t.say()
Teacher.sayAgain()  # 调用绑定类函数使用类名
'''
'''
class A():
    name = "niuniu"
    age = 18
    def __init__(self):
        self.name = "aaa"
        self.age = 200
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbb"
    age = 50
a = A()
a.say()       # 系统默认将a作为第一个参数传入函数
A.say(a)      #self被a替换
A.say(A)      #把A作为参数传入
A.say(B)      #传入得是类B，因为B具有name和age属性
####  以上代码利用了鸭子模型
'''
class Person():
    name = "dandan"  # 公有成员
    __age = 18       # 私有成员
p = Person()
print(p.name)        # 可直接访问
print(Person.__dict__)  # 字典查询，实际是更改了私有成员得名称
print(p._Person__age)   # 运用更改后得名称可访问
print(p.__age)       #不能直接访问
