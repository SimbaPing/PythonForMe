import urllib.request
import urllib.parse

try:
    url = 'http://pythonprogramming.net/'
    values = {
        's': 'basic',
        'submit': 'search'
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    print(data)

    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    respData = response.read()
    print(respData)
    saveFile = open('withoutheader.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
