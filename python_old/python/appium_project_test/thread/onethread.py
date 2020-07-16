from time import sleep,ctime

# 听音乐任务
def music():
    print("i was listening to music! %s" % ctime())
    sleep(2)

# 看电影任务
def movie():
    print("i was at the movies! %s" % ctime())
    sleep(5)

if __name__ == "__main__":
    music()
    movie()
    print("all end:",ctime())