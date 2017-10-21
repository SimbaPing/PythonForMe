import urllib
import urllib.request


def get_image(url):
    request = urllib.request.Request(url)  # 构建请求
    response = urllib.request.urlopen(request)  # 获取服务器响应
    get_img = response.read()
    with open('001.jpg', 'wb') as fp:
        fp.write(get_img)
        print("图片下载完成")
    return


url = "http://p2.123.sogoucdn.com/imgu/2016/10/20161019124600_428.jpg"
get_image(url)
