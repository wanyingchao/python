from flask import Flask, request
import json
import mysql_connect

server = Flask(__name__)


@server.route('/login', methods=['post'])
def login():
    name = request.values.get('xm')
    pwd = request.values.get('pwd')
    if name and pwd:
        sql = "select * from name where xm= '%s' and pwd='%s';" % (name, pwd)
        result = mysql_connect.my_db(sql)
        if result:
            res = {'error_code': 1000, 'msg': '登录成功'}
        else:
            res = {'error_code': 3000, 'msg': '账号或密码错误'}
    else:
        res = {'error_code': 3001, 'msg': '必填参数未填'}
    return json.dumps(res, ensure_ascii=False)


server.run(port=9999)
