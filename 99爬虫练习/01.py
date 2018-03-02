import requests
response = requests.get('https://ss3.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/super/pic/item/8ad4b31c8701a18b9968cd6b922f07082838fe17.jpg')
print(response.content)
with open('1.gif','wb') as f:
    f.write(response.content)
    f.close()                           #下载图片，二进制文件抓取

from selenium import webdriver
import os
chromeDriver = '‪D:\Anaconda3\chromedriver.exe'

os.environ["webdriver.chrome.driver"] = chromeDriver
driver = webdriver.Chrome(chromeDriver)
driver.get('http://www.zhihu.com/')




