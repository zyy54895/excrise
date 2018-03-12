#coding=utf-8

'''
定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()

list_info = Listinfo([44,222,111,333,454,'sss','333'])

定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''

class Listinfo(list):

    def add_key(self,keyname):
        return self.append(keyname)

    def get_key(self,num):
        return [x for x in self if type(x) == num]

    def update_list(self,*list1):
        m_list = list(list1)
        return self+m_list

    def del_key(self):
        while self:
            self.pop()




list1 = Listinfo([44,222,111,333,454,'sss','333'])
list2 = list1.get_key(float)
list3 = list1.update_list(1,2,3)
