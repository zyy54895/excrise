#coding=utf-8

"""
1.class的基本定义

2.构造，析构函数

3.基本继承

"""

class test(object):

    a = 1
    def __init__(self,arg1,arg2):   #构造
        self.arg1 = arg1
        self.arg2 = arg2

    def func_1(self):
        pass

    def __del__(self):       #析构
        del self.arg1


#a被称为test的属性
#func_1被称为test的方法

t = test()
print(t.a)
