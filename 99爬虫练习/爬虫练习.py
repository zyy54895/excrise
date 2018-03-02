#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def get_html(url, headers, proxies):
#     import requests
#     response = requests.get(url, headers=headers, proxies=proxies)
#     # response.encoding = 'utf-8'
#     return response.text
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
proxies = {"https": "https://122.114.31.177:808"}
html = requests.get('http://www.xicidaili.com/nn', headers=headers).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

table = soup.find_all('tr')
cloumn = str(table[0].text).replace('\n', ',')[1:-1].split(',')
cloumn_dict = dict(zip(cloumn, range(len(cloumn))))

def divice_elements(table):
    #country = table.find_all('td')[0].contents[0]
    ip_address = table.find_all('td')[1].text
    port = table.find_all('td')[2].text
    serve_address = str(table.find_all('td')[3].text).replace('\n', ',')[1:-1]
    unknown = table.find_all('td')[4].text
    types = table.find_all('td')[5].text
    speed = table.find_all('td')[6].contents[1].attrs['title']
    commit_time = table.find_all('td')[7].contents[1].attrs['title']
    exiting_time = table.find_all('td')[8].text
    prove_time = table.find_all('td')[9].text
    return (ip_address, port, serve_address, unknown, types, speed, commit_time, exiting_time, prove_time)

table_list = [divice_elements(table[i]) for i in range(1,len(table))]

# country = table[1].find_all('td')[0].contents[0].attrs['alt']
# ip_address = table[1].find_all('td')[1].text
# port = table[1].find_all('td')[2].text
# serve_address = str(table[1].find_all('td')[3].text).replace('\n', ',')[1:-1]
# unknown = table[1].find_all('td')[4].text
# types = table[1].find_all('td')[5].text
# speed = table[1].find_all('td')[6].contents[1].attrs['title']
# commit_time = table[1].find_all('td')[7].contents[1].attrs['title']
# exiting_time = table[1].find_all('td')[8].text
# prove_time = table[1].find_all('td')[9].text