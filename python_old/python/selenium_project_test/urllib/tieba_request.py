from urllib import parse
import urllib.request


def loadPage(url, filename):

    print('正在下载' + filename)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/67.0.3396.99 Safari/537.36'}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()

def writefile(html, filename):

    print('正在储存' + filename)
    with open(filename, 'w') as f:
        f.write(html)
    print('-'*20)

def tiebaSpider(url, beginPage, endPage):

    for page in range(beginPage, endPage+1):
        pn = (page-1)*50
        filename = "第" + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        print(fullurl)
        print(filename)

        html = loadPage(fullurl, filename)
        writefile(html, filename)

if __name__ == '__main__':
    kw = input('请输入需要爬取的贴吧')
    beginPage = int(input('请输入起始页：'))
    endPage = int(input('请输入终止页：'))
    url = 'http://tieba.baidu.com/f?'
    key = parse.urlencode({'kw': kw})

    url = url + key
    print(url)
    tiebaSpider(url, beginPage, endPage)
