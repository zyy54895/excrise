print('第一题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下

a = "aAsmr3idd4bgs7Dlsf9eAF"

#1.1 请将a字符串的大写改为小写，小写改为大写。
#方法1
b1 = []
for i in range(len(a)):
    if a[i].islower():
        b1.append(a[i].upper())
    elif a[i].isupper():
        b1.append(a[i].lower())
    else:
        b1.append(a[i])
b2 = "" .join(b1)
print(b2)
#方法2
print(a.swapcase())

#1.2 请将a字符串的数字取出，并输出成一个新的字符串。
#方法1
c1 = []
for i in range(len(a)):
    if a[i].isdigit():
        c1.append(a[i])
c2 = "".join(c1)
print(c2)
#方法2
print(''.join([s for s in a if s.isdigit()]))

#1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
d1 = a.lower() #将大写转换为小写
#方法1
key = []
num = []
for i in range(len(d1)):
    if d1[i] not in key:
        key.append(d1[i])   #找到所有key

for i in range(len(key)):
    num.append(d1.count(key[i])) #计数

dic = dict(zip(key, num)) #合成字典
print(dic)
#方法2
lists1 = list(a.lower())
dicts = {}
for i in lists1[0:]:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1
print(dicts)
#1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
e1 = a.lower()
#方法1
e2 = []
for i in range(len(e1)):
    if e1[i] not in e2:
        e2.append(e1[i])
e3 = ''.join(e2)
print(e3)

#1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'

print(a[::-1])

#1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）

f1 = []
for i in range(len(a)):
    if not a[i].isdigit():
        f1.append(a[i])    #去除数字

f1.sort(key=lambda x: (x.lower(), x.islower()))
print(f1)

#1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
g = 'boy'
g1 = list(g)
g2 = list(a)
num1 = 0
for i in range(len(g1)):
    if g1[i] in g2:
       num1 += 1

if num1 == len(g1):
    print(True)
else:
    print(False)

#1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。

def panduan(i_str, ii_str):
    ri_list = list(i_str)
    rii_list = list(ii_str.lower())
    num = 0
    for i in range(len(ri_list)):
        if ri_list[i] in rii_list:
            num += 1
    if num == len(ri_list):
        print(i_str+'所有字母在'+ii_str+'中')
    else:
        print(False)

panduan('boy', a)
panduan('girl', a)
panduan('bird', a)
panduan('dirty', a)

#1.9 输出a字符串出现频率最高的字母（不区分大小写）
dicts = {}
h = list(a)
for i in h[0:]:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1       #生成字典，同1.3
mid = 0
for j in dicts.keys():
    if dicts[j] > mid:
        mid = dicts[j]
        key = j

print('出现频率最高的字母是：%s' % key + '\n出现的次数是：%s' % mid)

print('第二题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。
import os
txt = os.popen('python -m this').read()
txt = txt.replace('\n', '')
l1 = txt.split(' ')

l2 = ['be', 'is', 'than']
dict1 = dict.fromkeys(l2, 0)
for i in l1[0:]:
    if i in dict1.keys():
        dict1[i] += 1
print(dict1)

print('第三题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。

size = 102324123499123

print('%s kb' % (size >> 10))
print('%s mb' % (size >> 20))

print('第四题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
a = [1, 2, 3, 6, 8, 9, 10, 14, 17]

print(str(a)[1:-1].replace(', ', ''))


