import pymysql
import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def getcontent():
    inputdata = request.values.get("inputdata")
    conn = pymysql.connect(host='192.168.0.140', user='root', password='root123', db='data', charset='utf8', autocommit=True)
    cur = conn.cursor()
    sql = "SELECT * FROM name WHERE id = '%s';" % (inputdata)
    cur.execute(sql)
    data = cur.fetchone()
    result = {'id': data[0], 'xm': data[1], 'xb': data[2], 'csny': data[3]}
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)
