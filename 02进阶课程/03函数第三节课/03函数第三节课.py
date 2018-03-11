#conding : UTF-8

#1.定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def test():
    '''
    测试说明

    '''
    pass

def test2():
    pass


def get_fundoc(func):
    if func.__doc__:
        return (func.__doc__)
    else:
        return ('Not Found doc')

result1 = get_fundoc(test)

#2.定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。

def get_cjsum(*num_list):
    try:
        import math
        result_sum = 0
        assert type(num_list) == list, 'type_error'
        assert num_list, 'len_error'
        for i in range(len(num_list)):
            assert type(i) == int, 'num_error'
            if len(num_list) == 1:
                result_sum = math.pow(num_list[0], 2)
            else:
                result_sum = result_sum + math.pow(num_list[i], 2)
        return int(result_sum)
    except AssertionError as e:
        return e
result2 = get_cjsum(*[x for x in range(1,101)])
result = get_cjsum([])
#可考虑使用递归函数，暂时没有思路

#3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：
'''
a = [1,2,3]

def list_info(list):
要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。
'''


#4.定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(类型为str)，否则返回 “fun is not function"。