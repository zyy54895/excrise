print('第一题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#1.用小于5行的代码解决周末习题中的1.6题。
a = "aAsmr3idd4bgs7Dlsf9eAF"
#1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）

f1 = sorted([m for m in a if not m.isdigit()], key=lambda x: (x.lower(), x.islower()))
print(f1)

print('第二题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
#2. 已知字典：
ainfo = {'b': 'python', 'a': 'haha', 'c': 'hehe', 'f': 'xiaoming'}

#2.1 迭代字典，输出结果：
t1 = [(x, y) for x, y in ainfo.items()]
print(t1)

#2.2 用2种方法输出结果：
#方法1：
t2 = sorted(ainfo.items(), key=lambda x: x[1])
for i in t2:
    print(i[0])

#方法2：
t3 = sorted(zip(ainfo.values(), ainfo.keys()))
for i in t3:
    print(i[1])

#2.3 写出查找字典里面值等于'haha'的key的代码
match_data = {}
for (key, value) in ainfo.items():
    if value =='haha':
        match_data[key] = value
print(match_data)
