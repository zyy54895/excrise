#coding = utf-8

import requests
import re
import chardet
import threading
import random,time
from multiprocessing import Process,Queue
origin_url = 'http://www.mmjpg.com/hot/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
def find_max_num(*lists):
    i = 0
    for max_num in lists:
        if int(max_num) > i:
            i = int(max_num)
    return [j for j in range(1, i+1)]

def url_analize(q, urls):
    for url in urls:
        response = requests.get(url, headers=headers)
        response.encoding = chardet.detect(response.content)['encoding']
        html = response.text
        nums = re.compile('<a.*?(\d+)</a>')
        num_list = find_max_num(*nums.findall(html))
        urls_dict = {}
        for i in num_list:
            if i > 1:
                r = requests.get(url+'/'+str(i), headers=headers)
                r.encoding = chardet.detect(r.content)['encoding']
                html1 = r.text
            elif i == 1:
                r = requests.get(url, headers=headers)
                r.encoding = chardet.detect(r.content)['encoding']
                html1 = r.text
            try:
                jpg_url = str(re.findall('data-img="(.*?)"', html1)[0])
                title = str(re.findall('<h2>(.*?)</h2>', html1)[0])
                urls_dict[title] = jpg_url
                print('%s链接已保存' %title)
            except:
                print('存储出错')
        q.put(urls_dict)
        time.sleep(random.random())

def recv_data(q):
    while True:
        urls_dict = q.get(True)
        try:
            for title in urls_dict.keys():
                pic_content = requests.get(urls_dict[title], headers=headers)
                pic_content.encoding = chardet.detect(pic_content.content)['encoding']
                with open('D:/soft/test/' + title + '.jpg', 'wb') as file:
                    file.write(pic_content.content)
                print('%s 下载完成' % title)
        except:
            print('%s error' % title)

def get_pic(url, title):
    try:
        pic_content = requests.get(url, headers=headers)
        with open('D:/soft/test/' + title + '.jpg', 'wb') as file:
            file.write(pic_content.content)
        print('%s done' % title)
    except:
        print('%s error' % title)


if __name__ == '__main__':
    response = requests.get(origin_url, headers=headers)
    response.encoding = chardet.detect(response.content)['encoding']
    html = response.text
    urls = re.compile('<a href="(http:.*?/\d+)".*?>')
    urls_list = list(set(urls.findall(html)))
    q1 = Queue()
    p1 = Process(target=url_analize, args=(q1, urls_list[0:int(len(urls_list)/2)]))
    proc_reader1 = Process(target=recv_data, args=(q1, ))
    q2 = Queue()
    p2 = Process(target=url_analize, args=(q2, urls_list[int(len(urls_list) / 2):-1]))
    proc_reader2 = Process(target=recv_data, args=(q2,))
    p1.start()
    proc_reader1.start()
    p2.start()
    proc_reader2.start()
    p1.join()
    p2.join()
    proc_reader1.terminate()
    proc_reader2.terminate()







