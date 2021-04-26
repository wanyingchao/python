import time
import requests
import xlrd


file = 'E:/python/z_daydayup/finishOrder.xlsx'
wb = xlrd.open_workbook(filename=file, file_contents=None)
sheet = wb.sheet_by_index(0)
nrows = sheet.nrows

url1 = 'http://192.168.0.106:8080/mark/finishOrderKc'
for i in range(nrows):  # 循环行数
    row_vals = sheet.row_values(i)
    par = {
        'orderid': row_vals[0],
        'money': row_vals[1]
    }

    body = {
        'Content-Type': 'application/json;charset=utf-8',
    }
    r = requests.post(url1, par, body, verify=True)
    print(row_vals[0] + '  ' + row_vals[1] + r.text)


time.sleep(5)


url2 = 'http://192.168.0.106:8080/mark/testDis'
for i in range(nrows):  # 循环行数
    row_vals = sheet.row_values(i)
    par = {
        'orderid': row_vals[0]
    }
    body = {


        'Content-Type': 'application/json;charset=utf-8',
    }
    r = requests.post(url2, par, body, verify=True)
    print(row_vals[0] + '  ' + row_vals[1] + r.text)


