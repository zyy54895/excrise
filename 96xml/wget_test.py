import wget
import requests
import re
import chardet


url = input('请输入网址：')
file_path = 'D:/soft/test/'

response = requests.get(url)
response.encoding = chardet.detect(response.content)['encoding']
html = response.text

pattern = re.compile('<title>([\s\S]*?)<\/title>')

title = re.findall(pattern, html)[0]
wget.download(url, out=file_path+title+'.html')