# #Urllib
#
# #urlopen
#
# #urllib.request.urlopen(url,data=None,[timeout]*,cafile=None.capath=None,cadefault=False,context=None)
#
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# #print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
#
#
#
#
# import urllib.parse
#
#
# #data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# #response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# #print(response.read())
#
#
# #import socket
# #import urllib.request
# #import urllib.error
#
# #try:
#  #   response = urllib.request.urlopen('http://httpbin.org/get')
# #except urllib.error.URLError as e:
# #    if isinstance(e.reason, socket.timeout):
#  #       print('TIME OUT')

def get_html(url, headers, proxies):
    import requests
    response = requests.get(url, headers=headers, proxies=proxies)
    response.encoding = 'utf-8'
    return response.text

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
proxies = {"https": "https://110.73.53.198:8123"}
html = get_html('http://222llll.com/xiaoshuo/jiqingwenxue/2017-06-01/29726.html', headers=headers, proxies=proxies)


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
title = soup.title.string
text = str(soup.p)
# text = soup.p.encode('gbk', 'ignore')
# text1 = text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
# print(text1)
# print(type(text1))

f = open(title+'.txt', 'w', encoding='utf-8')
f.write(text)
f.close()

# response1 = requests.get('http://222llll.com/xiaoshuo/jiqingwenxue')
# response1.encoding='utf-8'
# print(response1.text)