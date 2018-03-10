#-*- coding: UTF-8 -*-

#1.定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：
# （注：列表里面的元素为偶数）。
def get_num(*num_list):
    try:
        for i in range(len(num_list)):
            assert type(num_list[i]) == int
        return [x for x in num_list if x % 2 == 0]
    except AssertionError as e:
        return e

result1 = get_num(*[1,2,4,'asd',6,3,4,33,55,66,90])

#2.定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
def get_page(url):
    import requests
    response = requests.get(url)
    response.encoding = ('utf-8')
    return response.text

result2 = get_page('http://www.baidu.com')

#3.定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def find_max_s(*input_list):
    try:
        int_list = [int(i) for i in input_list]
        return max(int_list)
    except TypeError as e:
        return e
    except ValueError as v:
        return v

def find_max_all(*source_list):
    try:
        for i in source_list:
            assert type(i) == list
        max_list = [find_max_s(*x) for x in source_list]
        return max(max_list)
    except AssertionError as e:
        return e
    except TypeError as v:
        return v
result3 = find_max_all(*[[1,3,67.9,23,32.2],[1,2,3,8,4,3],[9,6,5,4,3],[10,12,23,1]])

#4.定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
def get_dir(f):
    import os
    try:
        output_list = []
        for i in os.listdir(f):
            if os.path.isdir(f + '/' + i):
                output_list.append(os.path.abspath(f + '/' + i))
        assert len(output_list) > 0
        return output_list
    except AssertionError:
        return 'Not dir'


result4 = get_dir('D:\\test')
