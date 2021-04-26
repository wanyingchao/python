import requests
from lxml import etree

url = 'http://s.manmanbuy.com/Default.aspx?key=苹果8'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
          'Cookie': 'Hm_lvt_30453b7c2dfa67a6c69b52556ce8eaef=1618300205; _ga=GA1.2.784751914.1618300206; _gid=GA1.2.641471189.1618300206; mmb_search_userid=b8d8c30089e64f41b8b55eb0b669a54c; MMBUserAreaN=%7B%22Area%22%3A%22510104%22%2C%22Zone%22%3A5%2C%22PerName%22%3A%22%25u56DB%25u5DDD%22%2C%22CityName%22%3A%22%25u6210%25u90FD%25u5E02%22%2C%22CountyName%22%3A%22%25u9526%25u6C5F%25u533A%22%2C%22User%22%3A%22dae3b0e2-6fd2-2a60-1c8f-5f494bfa727f%22%2C%22IsUsed%22%3A1%7D; Hm_lvt_85f48cee3e51cd48eaba80781b243db3=1618300205,1618383304,1618474580; log-uid=e44670d76bda4b2d9e0e3d19e4387615; ASP.NET_SessionId=qdej1hvm2dv1zcxtmnicpqo5; usersearcherid=bf0da34851644190bb00585c67bd995d; mmbp=mmbp; mmb_search_pageid=eafed1a4636e4b81bf47cd7d398f69c0; uibdfq=3; Hm_lpvt_85f48cee3e51cd48eaba80781b243db3=1618475225; Hm_lvt_313c599bcf6e44393cebef6a2629f81e=1618300214,1618383304,1618474590,1618475225; Hm_lpvt_313c599bcf6e44393cebef6a2629f81e=1618475225'}
html = requests.get(url, headers=header).text
dom = etree.HTML(html)
data = dom.xpath('/html/body/div[1]/div[5]/div[3]/div[4]/div[4]/div[2]/div/div[2]/div[3]/div[1]/span[1]/text()')
print(data)
