import urllib.request


request = urllib.request.Request('http://172.16.1.188:8888/budget/pages/main')
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
