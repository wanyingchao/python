import xlrd
import requests
import datetime

file = 'E:\python\pop\pop.xlsx'
wb = xlrd.open_workbook(filename=file)
sheet = wb.sheet_by_index(0)
cols = sheet.col_values(0)
file_logs = open('E:\python\pop\POP_LOGS.txt', 'a', encoding='utf8')
url = 'https://www.jzcdsc.com/charge/device/pop'


def pop():
    par = {
        'deviceid': deviceid,
        'slot': slot
    }
    body = {
        'Content Type': 'application.json;charset=utf-8',
    }
    r = requests.post(url, par, body, verify=True)
    result = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + str(slot) + "口" + r.text
    print(result)
    file_logs.write(result + '\n')


for deviceid in cols:
    if deviceid[4] + deviceid[5] == '06':
        for slot in range(1, 7):
            pop()
    elif deviceid[4] + deviceid[5] == '09':
        for slot in range(1, 10):
            pop()
    else:
        for slot in range(1, 13):
            pop()

file_logs.close()
