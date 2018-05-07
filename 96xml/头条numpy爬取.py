# conding=utf-8

import requests, chardet
import json
import re
origin_url = 'https://www.toutiao.com/search_content/'
params = {'offset': 0, 'format': 'json', 'keyword': 'numpy', 'autoload': 'true',
          'count': 20, 'cur_tab': 1, 'from': 'search_tab'}

response = requests.get(origin_url, params=params)

data = json.loads(response.text)['data']

lists = []
for i in range(len(data)):
    if 'title' in data[i].keys() :
        lists.append(data[i]['title'], data[i]['article_url'])






