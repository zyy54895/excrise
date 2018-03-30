
import requests
import chardet
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
response = requests.get('http://222llll.com/xiaoshuo/jiqingwenxue/')
#if response.encoding == 'ISO-8859-1':

# print(chardet.detect(response.content))
response.encoding = 'utf-8'
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

# f = open(title+'.txt', 'w')
# f.write(text)
# f.close()

# response1 = requests.get('http://222llll.com/xiaoshuo/jiqingwenxue')
# response1.encoding='utf-8'
# print(response1.text)
