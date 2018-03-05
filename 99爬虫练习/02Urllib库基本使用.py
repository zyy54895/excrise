#!/usr/bin/python3.5


import requests
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests.get('http://222llll.com/xiaoshuo/jiqingwenxue/2017-06-01/29726.html', headers=headers)
response.enconding = 'ISO8859-1'
#print(response.encoding)
html = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
title = soup.title.string
text = str(soup.p)
# text = soup.p.encode('gbk', 'ignore')
# text1 = text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
# print(text1)
# print(type(text1))

f = open(title+'.txt', 'w', encoding='gbk')
f.write(text)
f.close()

# response1 = requests.get('http://222llll.com/xiaoshuo/jiqingwenxue')
# response1.encoding='utf-8'
# print(response1.text)
