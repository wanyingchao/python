import xlrd
import requests
import datetime

file = 'E:\python\pop\pop.xlsx'
wb = xlrd.open_workbook(filename=file)
sheet = wb.sheet_by_index(0)
cols = sheet.col_values(0)

file_logs = open('E:\python\pop\POP_LOGS.txt', 'a')

url = 'https://www.jzcdsc.com/charge/device/pop'

for deviceid in cols:
    if deviceid[4] == '0':
        for slot in range(1, 7):
            par = {
                'deviceid': deviceid,
                'slot': slot
            }
            body = {
                'Content Type': 'application.json;charset=utf-8',
            }
            r = requests.post(url, par, body, verify=True)
            print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + r.text)
            file_logs.write(
                str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + r.text + '\n')
    else:
        for slot in range(1, 13):
            par = {
                'deviceid': deviceid,
                'slot': slot
            }
            body = {
                'Content Type': 'application.json;charset=utf-8',
            }
            r = requests.post(url, par, body, verify=True)
            print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + r.text)
            file_logs.write(
                str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + r.text + '\n')

file_logs.close()










