# conding=utf-8

import requests
import chardet
import re
from bs4 import BeautifulSoup
from multiprocessing import Process,Queue,Pool
import os,time,random
def trans_int(num):
    CN_NUM = {'〇': 0, '一': 1, '二': 2, '三': 3, '四': 4,
              '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
              '零': 0, '壹': 1, '贰': 2, '叁': 3, '肆': 4,
              '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9,
              '貮': 2, '两': 2, }

    CN_UNIT = {'十': 10, '拾': 10, '百': 100,
               '佰': 100, '千': 1000, '仟': 1000, '万': 10000,
               '萬': 10000, '亿': 100000000, '億': 100000000, '兆': 1000000000000}
    pos0 = 0
    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0
    pos5 = 0
    pos6 = 0
    for i in range(len(num)):
        if num[i] in CN_UNIT.keys():
            if num[i] == '十':
                pos1 = CN_NUM[num[i - 1]] * CN_UNIT['十']
            if num[i] == '百':
                pos2 = CN_NUM[num[i - 1]] * CN_UNIT['百']
            if num[i] == '千':
                pos3 = CN_NUM[num[i - 1]] * CN_UNIT['千']
            if num[i] == '万':
                pos4 = CN_NUM[num[i - 1]] * CN_UNIT['万']
            if num[i] == '亿':
                pos5 = CN_NUM[num[i - 1]] * CN_UNIT['亿']
            if num[i] == '兆':
                pos6 = CN_NUM[num[i - 1]] * CN_UNIT['兆']
        elif num[-1] not in CN_UNIT.keys():
            pos0 = CN_NUM[num[-1]]
    return (pos0 + pos1 + pos2 + pos3 + pos4 + pos5 + pos6)


def get_article(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.encoding = chardet.detect(response.content)['encoding']
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.h1.string
    title_s = re.findall('第(.*?)章.*?', title, re.S)
    try:
        title_num = int(title_s[0])
    except:
        title_num = trans_int(title_s[0])
    finally:
        if title_num >= 100:
            title_num = str(title_num)
        elif title_num >= 10:
            title_num = '0' + str(title_num)
        elif title_num >= 1:
            title_num = '00' + str(title_num)
    title = re.sub('第.*章', '第'+title_num+'章', title)
    article = str(soup.find(id="content"))
    with open('D:/soft/test/' + title + '.htm', 'w', encoding='utf-8') as file:
        file.write(article)
        print('%s done' % title)

if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    origin_url = 'http://www.biquge.info/10_10218/'
    response = requests.get(origin_url, headers=headers)
    response.encoding = chardet.detect(response.content)['encoding']
    html = response.text
    lists = re.findall('<dd.*?href="(.*?)".*?>(.*?)</a></dd>', html, re.S)
    contents = dict(zip([lists[i][1] for i in range(len(lists))], [lists[i][0] for i in range(len(lists))]))
    p = Pool(processes=5)
    for key in contents.keys():
        p.apply_async(get_article, args=(origin_url+contents[key], ))
    p.close()
    p.join()