import requests
import datetime
import xlrd
url = 'https://www.jzcdsc.com/charge/device/pop'
file_logs = open('E:\python\pop\POP_LOGS.txt', 'a', encoding='utf8')


def pop(deviceid, slot):
    par = {
        'deviceid': deviceid,
        'slot': slot
    }
    body = {
        'Content-Type': 'application/json;charset=utf-8',
    }
    r = requests.post(url, par, body, verify=True)
    result = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + deviceid + " " + str(slot) + "口" + r.text
    print(result)
    file_logs.write(result + '\n')


def pop_one(deviceid, slots):
    for slot in slots:
        pop(deviceid, slot)


def pop_all():
    # file = 'E:\python\pop\pop.xlsx'
    # wb = xlrd.open_workbook(filename=file)
    # sheet = wb.sheet_by_index(0)
    # cols = sheet.col_values(0)
    # for deviceid in cols:
        deviceid = 'JZCB121907000953'
        if deviceid[4] + deviceid[5] == '06':
            for slot in range(1, 7):
                pop(deviceid, slot)
        elif deviceid[4] + deviceid[5] == '09':
            for slot in range(1, 10):
                pop(deviceid, slot)
        else:
            for slot in range(1, 13):
                pop(deviceid, slot)


# pop_one('JZCB061904000179', '6')
pop_all()

file_logs.close()
