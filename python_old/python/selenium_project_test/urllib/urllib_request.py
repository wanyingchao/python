import urllib.request


response = urllib.request.urlopen('http://172.16.1.188:8888/budget/pages/main')

html = response.read().decode('utf-8')

print(html)
