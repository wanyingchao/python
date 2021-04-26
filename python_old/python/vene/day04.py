'''a = [1,2,3]
b = a[:]
if b is a:
    print("true")
else:
    print("false")
print(b)
if b == a:
    print("lala")
else:
    print("wawa")
print(id(a))
print(id(b))'''
'''i = 1
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)'''
'''i = 1           #for i in range(1,11)
while i < 10:             #if i % 2 == 0:
    i += 1                     # print(i)
    if i % 2 ==0:
        print(i)'''
'''
var = 1
while var == 1:
    num = input("你脑袋里想到的是:")
    if num == "0":
        print("结束了")
        break
    print("你输入了：",num)
'''
'''
c = 0
while c < 5:
    print(c)
    c += 1
else:
    print(c,"漫出来了")

b = 1
while b < 10:
    print(b)
    b += 1
else:
    print()
'''
'''
f = 1
while (f): print("ture")     # 无限循环，相当于f == 1
'''
'''
for l in "pathon":
    print(l)
o = ["香蕉","苹果","梨子"]
for b in o :
    print(b)
'''
'''
for n in range(10,20):
    for i in range(2,n):
        if n % i == 0 :
            j = n / i
            if i > j:
                break
            print(n,"等于",i,"*",j)
            break
    else:
        print(n,"是一个质数")
'''
'''
i = 2
while i < 50:
    j = 2
    while j <= (i / j):
        if i % j == 0:
            break
        j = j + 1
    if j > (i / j):
        print(i,"是素数")
    i = i + 1
'''
'''
for q in "iphone":
    if q == "o":
        break
    print("当前字母：",q)
v = 10
while v > 0:
    print("当前数字：",v)
    v -= 1
    if v == 5:
        break
'''
'''
for q in "iphone":
    if q == "o":
        continue
    print("当前字母：",q)
v = 10
while v > 0:
    v -= 1
    if v == 5 or v == 2:
        continue
    print("当前数字：", v)
'''