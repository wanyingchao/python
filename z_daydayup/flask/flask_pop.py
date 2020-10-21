from flask import Flask, request
import os, sys, time
import xlrd
import requests
import datetime
from flask import render_template
from log.logger import *
url = 'https://www.jzcdsc.com/charge/device/pop'
interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)  # 将当前文件的父目录加入临时系统变量


def pop_flask(deviceid, slot, text):
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
    logger.info(result)
    text.append(result)


def pop_loop(deviceid, text):
    if deviceid[4] + deviceid[5] == '06':
        for slot in range(1, 7):
            pop_flask(deviceid, slot, text)
            if slot == 6:
                text.append('---------------------------------------------------------------------------------------')
    elif deviceid[4] + deviceid[5] == '09':
        for slot in range(1, 10):
            pop_flask(deviceid, slot, text)
            if slot == 9:
                text.append('---------------------------------------------------------------------------------------')
    else:
        for slot in range(1, 13):
            pop_flask(deviceid, slot, text)
            if slot == 12:
                text.append('---------------------------------------------------------------------------------------')


server = Flask(__name__, static_folder='static')  # Flask必须创建程序实例，Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名
# 需要自己在同级 创建一个名为 static 的文件夹来存放上传的文件


@server.route('/pop', methods=['post'])  # 文件路径/pop，方法post
def pop_all():
    file = request.files['excel']  # 获取上传的文件
    if file:
        t = time.strftime('%Y%m%d%H%M%S')
        new_file = 'static/' + t + file.filename
        file.save(new_file)
        text = []
        wb = xlrd.open_workbook(filename=new_file)
        sheet = wb.sheet_by_index(0)
        cols = sheet.col_values(0)
        for deviceid in cols:
            pop_loop(deviceid, text)
        return render_template('index.html', text=text)
    else:
        text = []
        slots_list = request.form['slot']
        deviceid = request.form['data']
        if len(slots_list) == 0:
            pop_loop(deviceid, text)
        else:
            slots = slots_list.split(',')
            for slot in slots:
                pop_flask(deviceid, slot, text)
        # 需要在同级目录创建templates文件存放index.html
        return render_template('index.html', text=text)


server.run(host='192.168.0.93', port=8888)
