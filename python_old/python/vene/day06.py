##########汉诺塔
'''
def hano(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
        return None
    if n == 2:
        print(a,"-->",b)
        print(a,"-->",c)
        print(b,"-->",c)
        return None
    hano(n-1,a,c,b)
    print(a,"-->",c)
    hano(n-1,b,a,c)
a = "A"
b = "B"
c = "C"
n = 3
hano(n,a,b,c)
'''
###成员资格
'''
a = [1,2,3,4,5,6]
b = 8
c = b in a
print(c)
d = b not in a
print(d)
for i in a:
    print(i)
'''
### while循环访问list
'''
a = [1,2,3,4,5,6]
length = len(a)
indx = 0
while indx < length:
    print(a[indx])
    indx += 1
'''
#  双层列表循环
'''
a = [["one",1],["two",2],["three",3]]
for k,v in a:
    print(k,"----",v)
'''
'''
a = [["one",1,"汪"],["two",2,"凸"],["three",3,"税"]]
for k,v,w in a:
    print(k,"----",v,"----",w)
'''
'''
# 列表内涵：list content
a = ["a","b","c"]
b = [i for i in a]
print(b)
c = [1,2,3,4,5]
d = [m * 2 for m in c]
print(d)
'''
'''
# 过滤原来的list中的内容
a = [ x for x in range(1,30) if x % 2 == 0]
print(a)
b = [i for i in range(1,4)]
print(b)
c = [i for i in range(100,400) if i % 100 == 0]
print(c)
d = [m+n for m in b for n in c]
print(d)
'''
# 关于列表的常用函数
'''
a = [x for x in range(1,100)]
print(len(a))    # 求列表长度
print(max(a))    # 求列表最大值
b = ["bbb","xilmkokomo","man"]  # 打印的应该是首字母排序再最后的那个
print(max(b))
'''
'''
a = "how are you"
print(list(a))
print(list(range(1,6)))
'''
a = [i for i in range(1,5)]
print(a)
a.append(100)  # 在末尾追加一个内容
print(a)
# a.insert(index,data)   在指定位置插入，位置是index前面
a.insert(2,999)
print(a)
# del  删除
# pop 把最后一个元素取出来
m = a.pop()
print(m)
print(a)