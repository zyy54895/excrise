#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def get_html(url, headers, proxies):
#     import requests
#     response = requests.get(url, headers=headers, proxies=proxies)
#     # response.encoding = 'utf-8'
#     return response.text
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
proxies = {"https": "https://61.135.217.7:80"}
try:
    html = requests.get('http://www.xicidaili.com/nn', headers=headers, proxies=proxies).text
except:
    html = 'error'

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

table = soup.find_all('tr')
cloumn = str(table[0].text).replace('\n', ',')[1:-1].split(',')
cloumn_dict = dict(zip(cloumn, range(len(cloumn))))

def divice_elements(table):
    try:
        country = table.find_all('td')[0].contents[0].attrs('alts')
    except:
        country = 'error'
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
    return (country, ip_address, port, serve_address, unknown, types, speed, commit_time, exiting_time, prove_time)

table_list = [divice_elements(table[i]) for i in range(1,len(table))]

import xlrd
import xlwt
# from xlutils.copy import copy
workbook =xlwt.Workbook('encoding = utf-8')
worksheet = workbook.add_sheet('sheet1')

#写入第一行：
for i in range(len(cloumn)):
    worksheet.write(0, i, cloumn[i])

#写入采集内容
for i in range(len(table_list)):
    for j in range(len(table_list[i])):
        worksheet.write(i+1, j, table_list[i][j])
workbook.save('test.xls')