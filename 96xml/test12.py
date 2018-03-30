
import re
import os

origin_path = 'C:/Users/zyy/66eeee.com/xiaoshuo/jiqingwenxue/'

files = os.listdir(origin_path.encode('utf-8'))
html_files = [str(files[i])[2:-1] for i in range(len(files))][4:]
contents = []
for i in range(len(html_files)):
    with open(origin_path + html_files[i], 'r', encoding='utf-8') as file:
        text = file.read()
    lists = re.findall('<li>.*?href="(.*?)".*?title="(.*?)".*?</li>', text, re.S)
    contents.extend(lists)
contents_dict = dict(zip([contents[i][1] for i in range(len(contents))], [contents[i][0] for i in range(len(contents))]))

from bs4 import BeautifulSoup
for key in contents_dict.keys():
    try:
        with open(origin_path + contents_dict[key], 'r', encoding='utf-8') as html_read:
            text1 = html_read.read()
            soup = BeautifulSoup(text1, 'lxml')
            title = soup.title.string
            article = str(soup.find(class_="vod_content"))

        with open('D:/soft/test/' + title + '.htm', 'w', encoding='utf-8') as html_write:
            html_write.write(article)
    except OSError as e:
        pass
    except UnicodeDecodeError as u:
        pass

