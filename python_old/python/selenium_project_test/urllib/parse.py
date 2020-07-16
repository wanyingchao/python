from urllib import parse
import urllib.request


url = 'http://172.16.1.188:8888/budget/pages/main'
wd = {'wd': '传智播客'}
pw = parse.urlencode(wd)
print(pw)

wd1 = {'wd1': '传'}
pw1 = parse.urlencode(wd1)
print(pw1)

wd2 = {'wd2': '智'}
pw2 = parse.urlencode(wd2)
print(pw2)

wd3 = {'wd3': '播'}
pw3 = parse.urlencode(wd3)
print(pw3)

wd4 = {'wd4': '客'}
pw4 = parse.urlencode(wd4)
print(pw4)

print(parse.unquote('wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2'))
