import requests
import re
import pandas as pd

url_first = 'http://www.zei8.org/mh/2017/0121/94170.html/'

head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu '
                   'Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36'}
html = requests.get(url_first, headers=head, cookies=cookies)
cookies = {'cookie': '你自己的cookie'}  # 也就是找到你的账号对应的cookie