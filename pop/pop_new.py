import requests


url = 'https://test.jzcdsc.com/charge/device/pop'


id = 'JZCB121907000916,'\
'JZCB121907000613,'\
'JZCB121907001553,'\
'JZCB121907001218,'\
'JZCB121907000813'

idlist = id.split(',')

for deviceid in idlist:
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
            print(deviceid, r.text)
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
            print(deviceid, r.text)
