#  继承
#  在python中，任何类都有一个共同的父类叫object
'''
class Person():
    name = "NoName"
    age = 18
    def sleep(self):
        print("Sleeping .....")
#  父类写在括号中
class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(Teacher.name)
class Animel():
    def __init__(self):
        print("Anim")
class PaxingAnim(Animel):
    def __init__(self):
        print("Paxing Dongwu")
class Dog(PaxingAnim):
    def __init__(self):
        print("I am init in dog")
doudou = Dog()
class Cat(PaxingAnim):
    pass
c = Cat()
'''
'''
class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(B):
    pass
c = C()
'''
###   issubclass用于检测一个类是否是另一个类的子类
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B,A))
print(isinstance(C,A))
print(issubclass(C,object))
###  isinstanse用于检测一个对象是否是一个类的实例
class A():
    pass
a = A()
print(isinstance(a,A))
print(isinstance(A,A))
##  hasattr检测一个对象是否有成员
class A():
    name = "NoName"
a = A()
print(hasattr(a,"name"))
print(hasattr(a,"age"))