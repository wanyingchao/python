import urllib.request


url = "http://172.16.1.188:8888/budget/pages/main"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/67.0.3396.99 Safari/537.36"}
request = urllib.request.Request(url)
request.add_header('Connection', 'keep-alive')
print(request.get_header(header_name='Connection'))

response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
