import flask, os, sys,time
import xlrd
from flask import request
interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)


server = flask.Flask(__name__, static_folder='static')


@server.route('/pop', methods=['post'])
def upload():
    file = request.files['excel']  #获取上传的文件
    if file:
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        new_file = 'static/' + t + file.filename
        file.save(new_file)
        wb = xlrd.open_workbook(filename=new_file)
        sheet = wb.sheet_by_index(0)
        cols = sheet.col_values(0)
        for deviceid in cols:
            print(deviceid)
        return '1'
    else:
        print(222)
        return '2'

server.run(port=8000)