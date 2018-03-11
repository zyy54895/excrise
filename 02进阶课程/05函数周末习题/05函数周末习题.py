#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

# def func_1(name):
#     try:
#         assert type(name) == str, '输入不是字符串'
#         l = [x for x in name]
#         if l[0].islower():
#             l[0] = l[0].upper()
#         return ''.join(l)
#     except AssertionError as e:
#         return e

def func_1(name):
    return name.capitalize()

assert func_1("lilei") == "Lilei"
assert func_1("hanmeimei") == "Hanmeimei"
assert func_1("Hanmeimei") == "Hanmeimei"
"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
import string
def func_2(name, callback=None):

        if callback == None:
            return name.capitalize()
        elif callback == string.ascii_lowercase:
            return name.lower()
        elif callback == string.ascii_uppercase:
            return name.upper()

assert func_2("lilei") == "Lilei"
assert func_2("LILEI",callback=string.ascii_lowercase) == "lilei"
assert func_2("lilei",callback=string.ascii_uppercase) == "LILEI"

"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6

"""
def func_3(*kargs):
    return kargs

l = func_3(1,2,3,4,5)
for i in l:
    print(i)

"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None


"""
def func_4(*kargs):
    list1 = list(filter(lambda x:isinstance(x, str),kargs ))
    if list1:
        return list1[0]
    else:
       return None

assert func_4(222,1111,'xixi','hahahah') == "xixi"
assert func_4(7,'name','dasere') == 'name'
assert func_4(1,2,3,4) == None

"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""
def func_5(name=None,**kargs):
    list2 = ['%s:%s' % (x, y) for (x,y) in kargs.items()]
    list2.insert(0,name)
    return ','.join(list2)

assert func_5('lilei') == "lilei"
assert func_5("lilei",years=4) == "lilei,years:4"
assert func_5("lilei",years=10,body_weight=20) == "lilei,years:10,body_weight:20"