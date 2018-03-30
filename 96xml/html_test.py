# conding=utf-8


import requests
import chardet
# from bs4 import BeautifulSoup
import re
origin_url = 'http://www.biquke.com/bq/23/23727/'
response = requests.get(origin_url)
response.encoding = chardet.detect(response.content)['encoding']
html = response.text
# soup = BeautifulSoup(html, 'lxml')
# results = str(soup.find_all(id='list')[0])
lists = re.findall('<dd.*?href="(.*?)".*?title="(.*?)".*?</dd>', html, re.S)
content = dict(zip([lists[i][1] for i in range(len(lists))], [lists[i][0] for i in range(len(lists))]))
