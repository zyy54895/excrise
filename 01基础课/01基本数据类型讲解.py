#coding=utf-8
#@description:周末作业

print('第一题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#一.已知字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

s = 'i,am,lilei'
#方法1
print(s[2:4])
#方法2
c = s.split(',')
print(c[1])

print('第二题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#二.在python中，如何修改字符串？

#答案：可以用字符串的replace方法.
ainfo = 'i love php'
rinfo = ainfo.replace('php', 'python')
print(rinfo)

print('第三题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#三.bool("2012" == 2012) 的结果是什么。

##答案：结果是fasle,==判断对象的数据类型，尽管看起来数值是一样的，但是他们的类型不同，一个是字符串，一个是数字
print(bool("2012" == 2012))


print('第四题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##四.已知一个文件 test.txt，内容如下：
'''
2012来了。
2012不是世界末日。
2012欢乐多。
'''
f = open('test.txt', 'r')
content = f.read()
#dcontent = content.encode('utf-8')

##1.请输出内容
print(content)

##2.请计算该文本的原始长度
print(len(content))

##3.请去除该文本的换行
ccontent = content.replace('\n', '')
print(ccontent)

##4.请替换其中的字符"2012"为"2013"。
print(content.replace('2012', '2013'))

##5.请取出最中间的长度为5的子串。
if len(ccontent)%2 ==0:     #判断奇偶
    mid = len(ccontent)/2
else:
    mid = (len(ccontent)+1)/2
print(ccontent[int(mid):int(mid+5)])

##6.请取出最后2个字符。
print(content[-2:])

##7.请从字符串的最初开始，截断该字符串，使其长度为11.
print(content[:11])

##8.请将{4}中的字符串保存为test1.py文本.

rinfo = content.replace('2012', '2013')
f = open('test1.py', 'w')
f.write(rinfo)
f.close() ##关闭文件

print('第五题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##五.请用代码的形式描述python的引用机制。

import sys

cinfo = '1234'
print(id(cinfo))
print(sys.getrefcount('1234') )

binfo = '1234'
print(id(binfo))
print(sys.getrefcount('1234'))

print('第六题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##六.已知如下代码

print('str对象"中文编程"的引用计数')
print('开始:%s' % sys.getrefcount('中文编程'))
a = "中文编程"
print("a:%s" % id(a))##引用计数开始是3，然后a变量引用了字符串对象3 + 1 =4
print('第1次引用:%s' %sys.getrefcount('中文编程'))

b = a
print("b:%s" % id(b))##4 + 1 = 5
print('第2次引用:%s' %sys.getrefcount('中文编程'))

c = a
print("c:%s" % id(c))## 5 + 1 = 6
print('输出结果:%s' %sys.getrefcount('中文编程'))##输出结果是6

print('str对象"python编程"的引用计数')
print('开始:%s' % sys.getrefcount('python编程'))

a = "python编程"
print("a:%s" % id(a))###6-1 = 5##a引用另外一个字符串对象
print('第1次引用:%s' % sys.getrefcount('python编程'))

b = u'%s' %a
print("b:%s" % id(b))###5-1 = 4
print('第2次引用:%s' % sys.getrefcount('python编程'))##输出结果是4

d = "中文编程"
print("d:%s" % id(d))###新建一个变量，引用字符串 4 + 1 = 5

e = a
print("e:%s" % id(e))

c = b
print(sys.getrefcount('中文编程'))

b2 = a.replace("中","中")
print("b2:%s" % id(b2))

print('result-----------------')
##1.请给出str对象"中文编程"的引用计数
print(sys.getrefcount('中文编程'))
##2.请给出str对象"python编程"的引用计数
print(sys.getrefcount('python编程'))

print('第七题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##七.已知如下变量

a = "字符串拼接1"
b = "字符串拼接2"
#
##1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣
##方法1：在做大量的字符串对象拼接的时候不推荐

c = a + b

##方法2：

c = "%s%s" % (a, b)

###方法3：

c = "{a}{b}" .format(a=a, b=b)

##方法4：

c = "".join([a, b])
print('将a与b拼接成字符串c:%s' % c)

##2.请将a与b拼接成字符串c，并用逗号分隔。

c = '%s,%s' % (a, b)
print('请将a与b拼接成字符串c，并用逗号分隔:%s' % c)

##3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。

print('新拼接出来的字符串长度:%s' % len(c))
print('取出其中的第七个字符:%s' % c[6])

print('第八题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案

import string
##1.包含0-9的数字。
#print(help(string))
print('string输出包含0-9的数字：%s' % string.digits)

##2.所有小写字母。
print('string输出所有小写字母：%s' % string.ascii_lowercase)

##3.所有标点符号。
print('string输出所有标点符号：%s' % string.punctuation)

##4.所有大写字母和小写字母。
print('string输出所有大写字母和小写字母：%s' % string.ascii_letters)

##5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
strinfo = '%s%s%s%s' % (string.digits,string.ascii_lowercase,string.punctuation,string.ascii_letters)
print('{1}-{4}点中的字符串拼接成一个字符串:%s' % strinfo)

print('第九题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##九.已知字符串

a = "i,am,a,boy,in,china"

##1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
ac = "i,am,a,%(sex)s,in,%(country)s" % {'sex': 'girl', 'country': 'china'}
bc = "i,am,a,{sex},in,{country}" .format(sex='girl', country='india')

print(ac)
print(bc)

##2.请使用2种办法取出其间的字符"boy"和"china"。
##方法1
print(a[7:10])
print(a[-5:])

##方法2
cinfo = a.split(',') ##cinfo=[i,am,a,boy,in,china]
print(cinfo[3])
print(cinfo[-1])

##3.请找出第一个"i"出现的位置。

print(a.find('i'))

##4.请找出"china"中的"i"字符在字符串a中的位置。
print(a.find('i', a.find('china')))
print(a.rfind('i'))

##5.请计算该字符串一共有几个逗号
print(a.count(','))

print('第十题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
##十.请将模块string的帮助文档保存为一个文件。

import sys
import string

f = open('string-help.log', 'w')
sys.stdout = f
help(string)
f.close()
