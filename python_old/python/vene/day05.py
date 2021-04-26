'''
def stu(*args):
    print("hello,大家好：")
    for qqq in args:
        print(qqq)
stu("daoge",20,"四川仁寿","单身")
stu("蛋蛋")
'''
'''
def stu(**kwargs):
    print("hello,大家好：")
    for q,w in kwargs.items():
        print(q,"++++",w)
stu(name = "daoge",addr = "四川仁寿",age = "20")
print("*" * 20)
stu(name = "蛋蛋")
'''
'''
a1 = 100
def fun():
    print(a1)
    print("i am in fun")
    a2 = 99
    print(a2)
print(a1)
fun()
'''
'''
a = 1
b = 2
def fun(c,d):
    e = 3
    print("locals=",locals())
    print("globals=",globals())
fun(10,20)
'''
'''
x = 10
y = 20
z1 = x + y
z2 = eval("x + y")
z3 = exec("x + y")
z4 = exec("print ('x + y =',x + y)")
print(z1)
print(z2)
print(z3)
print(z4)
'''
'''
x = 0
def fun():
    global x
    x += 1
    print(x)
    if x == 10:
        return
    fun()
fun()
'''
# 斐波那契数列：1，1，2，3，5，8，13，。。。，n = (n-1) + (n-2)
'''
def fib(n):
    if n == 1:
        return 1
    if n == 2 :
        return 1
    return fib(n-1) +fib(n-2)
print(fib(4))
'''
'''
list = [5,1,2,3,4,2,9]  #从左往右，第一位默认为0；从右往左，第一位默认为-1
print(list[0])
print(list[2:5])
print(list[5:])
print(list[2:7:2])  #后面那个冒号表示步长
print(list[-2:-4])
print(list[-4:-2])   #默认都是从左往右取，所以正常情况下坐下标小于右下标
print(list[-2:-4:-1]) #步长选择负数可以从右往左取，但是取出的值按取值顺序排列
print(list[::-1])
'''
