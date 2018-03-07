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

result2 = find_longest_len(*('s', 'qweqsawe', 'dfsd', 'as'))

#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
# 例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
def get_doc(module_name):
    try:
        exec('import ' + module_name)
        print(help(module_name))
    except ModuleNotFoundError as e:
        print(e)
get_doc('sys')

#4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f='C:/Users'):
    import win32ui
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir('C:/Users')  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    f = dlg.GetPathName()  # 获取选择的文件名称
    return f
result4 = get_text()

#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。
# 提示（可以了解python的glob模块）
def get_dir(folder):
    import glob
    return glob.glob(folder+'./*')

result5 = get_dir('C:/Users')