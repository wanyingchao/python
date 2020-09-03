from flask import Flask
import time


server = Flask(__name__)  # Flask必须创建程序实例，Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名


@server.route('/time', methods=['post', 'get'])  # 文件路径/time，方法post和get
def get_time():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    return '当前时间是：%s' % now


server.run(port=8888)
