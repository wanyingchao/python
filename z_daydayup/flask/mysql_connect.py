import pymysql


def my_db(sql):
    connect = pymysql.connect(
        host='192.168.0.140',
        user='root',
        password='root123',
        db='data',
        charset='utf8',
        autocommit=True  # 自动提交
    )
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标，默认返回二维数组，DictCursor指定返回字典
    cursor.execute(sql)  # execute执行sql
    result = cursor.fetchall()  # 拿到全部sql执行结果
    cursor.close()
    connect.close()
    return result
