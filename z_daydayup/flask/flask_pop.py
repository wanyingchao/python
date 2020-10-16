from flask import Flask, request
import requests
import datetime
from flask import render_template
url = 'https://www.jzcdsc.com/charge/device/pop'


def pop(deviceid, slot, text):
    par = {
        'deviceid': deviceid,
        'slot': slot
    }
    body = {
        'Content-Type': 'application/json;charset=utf-8',
    }
    r = requests.post(url, par, body, verify=True)
    result = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + str(
        slot) + "口" + r.text
    text.append(result)


server = Flask(__name__)  # Flask必须创建程序实例，Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名


@server.route('/pop', methods=['post'])  # 文件路径/pop，方法post
def pop_all():
    text = []
    slots_list = request.form['slot']
    cols = request.form['data']
    col = cols.split(',')
    if len(slots_list) == 0:
        for deviceid in col:
            if deviceid[4] + deviceid[5] == '06':
                for slot in range(1, 7):
                    pop(deviceid, slot, text)
                    if slot == 6:
                        text.append('---------------------------------------------------------------------------------------')
            elif deviceid[4] + deviceid[5] == '09':
                for slot in range(1, 10):
                    pop(deviceid, slot, text)
                    if slot == 9:
                        text.append('---------------------------------------------------------------------------------------')
            else:
                for slot in range(1, 13):
                    pop(deviceid, slot, text)
                    if slot == 12:
                        text.append('---------------------------------------------------------------------------------------')

    else:
        slots = slots_list.split(',')
        for slot in slots:
            pop(deviceid=cols, slot=slot, text=text)
    return render_template('index.html', text=text)


server.run(host='192.168.0.93', port=8888)
