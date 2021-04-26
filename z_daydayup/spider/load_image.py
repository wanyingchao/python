import urllib
import urllib.request
import re       # 正则表达


def load_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def get_image(html):
    regx = 'http://[\S]*jpg'   # 正则表达式
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))
    num = 1
    for img in get_image:
        image = load_page(img)
        with open('E:/python/z_daydayup/spider/photo/%s.jpg' % num, 'wb') as fb:
            fb.write(image)
            print('正在下载第%s张图片' % num)
            num += 1
    print('下载完成')


if __name__ == '__main__':
    url = 'http://p.weather.com.cn/2019/10/3248439.shtml'
    html = load_page(url)
    get_image(html)
