'''for row in range(1,10):
    for col in range(1,row + 1):
        print(row * col,end="  ")
    print(" ")'''
'''def printline(row):
    for col in range(1,row + 1):
        print(row * col, end="  ")
    print(" ")
for row in range(1,10):
    printline(row)'''
'''for row in range(1,10):
    for k in range(1,row):
        print(end="")
    for col in range(row,10):
        print("{0}*{1}={2}".format(row,col,row*col),end="  ")
    print(" ")'''
'''for row in range(1,10):
    for k in range(1,row):
        print(end="")
    for col in range(row,10):
        print("%s * %s = %s"%(col,row,row*col),end="   ")
    print(" ")'''
'''for row in range(1,10):
    for col in range(1,row+1):
        print(col,"*",row,"=",row*col,end="   ")
    print(" ")'''
'''row = 1
while row <=9:
    col = 1
    while col <= row:
        print(col,"*",row,"=",col*row,end="   ")
        col = col + 1
    print()
    row = row + 1'''
'''def qwer(name,age,gender="male"):
    if gender =="male":
        print("{0} is {1},and he is a good student".format(name,age))
    else:
        print("{0} is {1},and she is a good student".format(name,age))
qwer("xiaoluo",22)
qwer("xiaohong",20,"female")'''