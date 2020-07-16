import pymysql


# 获取短信验证码
class GetCode():

    def __init__(self):
        self.connection = pymysql.connect(host='172.16.3.81',
                                     user='root',
                                     password='root',
                                     db='szbDB',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

    def get_phone_code(self, phone):
        cur = self.connection.cursor()

        sql = "SELECT t.phoneCode FROM szb_phone_code t where t.phone=" + phone + " ORDER BY id DESC"
        try:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                phone_code = row['phoneCode']
                return phone_code
                # print(org_id)
        except:
            print('Error:unable to fetch data')

        self.connection.close()


if __name__ == '__main__':
    db = GetCode()
    res = db.get_phone_code('18398929673')
    print(res)
