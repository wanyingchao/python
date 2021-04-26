import requests
from lxml import etree

url = 'https://movie.douban.com/chart'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html = requests.get(url, headers=header).text
html = etree.HTML(html)
# print(html)
datas = html.xpath('//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a/span/text()')
print(datas)
