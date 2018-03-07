#!/usr/bin/python3.5
#-*- coding: UTF-8 -*-

#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。

def find_max_min_int(*input_list):
    try:
        int_list = [int(i) for i in input_list]
        return (max(int_list), min(int_list))
    except TypeError as e:
        return e
    except ValueError as v:
        return v
result1 = find_max_min_int(*(1, 'as', 3, 4, 5, 6, 7, 8, 9))

#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def find_longest_len(*input_str):
    try:
        maxlen = 0
        maxlen_str = ''
        for i in range(len(input_str)):
            assert type(input_str[i]) == str

            if int(len(input_str[i])) > int(maxlen):
                maxlen = len(input_str[i])
                maxlen_str = input_str[i]
        return (maxlen_str, maxlen)
    except AssertionError as e:
        return e

result2 = find_longest_len(*('s', 12, 'qweqsawe', 'dfsd', 'as'))

#

