t = (1,2,3,4)
t1 = [i * 2 for i in t]
print(t1)
# 字典遍历，for循环访问key
a = {"one":1,"two":2,"three":3}
for i in a.keys():
    print(i,a[i])
# for循环访问values
for k in a.values():
    print(k)
# 特殊用法
for k ,v in a.items():
    print(k,"---",v)