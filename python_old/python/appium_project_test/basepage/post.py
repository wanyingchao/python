import requests


url = 'https://mapi.kyboye.com/club/topic/list?tid=9308943&type=1&skip=0&psize=20&pid=&_t=1552031515818'
# data = {
#     'tid': '9308943',
#     'type': '1',
#     'skip': '0',
#     'psize': '20',
#     'pid': '',
#     '_t': '1552031515818'
# }


res = requests.post(url, verify=False)
print(res.json())



