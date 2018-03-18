# conding=utf-8


# 1.打开文件
## open函数：
## open(name[.mode[.buffering]])

# 2.文件模式（mode)
## 值                功能描述
## 'r'                读模式
## 'w'                写模式
## 'a'                追加模式
## 'b'                二进制模式(可添加到其他模式中使用)
## '+'                读/写模式（可添加到其他模式中使用）

# 3.文件缓冲区
## 参数为0：I/O操作无缓冲
## 参数为1：I/O操作有缓冲，数据先写到内存里，使用flush函数或者close函数更新至硬盘
## 参数大于1：代表缓冲区的大小（单位字节）
## 参数为-1：代表使用默认缓冲区的大小

# 4.文件读取

##方法1
try:
    f = open(r'/home/zyy/桌面/ubuntu配置/test', 'r')
    print(f.read())
finally:
    if f:
        f.close()

##方法2：
with open(r'/home/zyy/桌面/ubuntu配置/test', 'r') as filereader:
    # print(filereader.read())
    for line in filereader.readlines():
        print(line.strip())

###tips:
###调用read()一次将文件内容读到内存，但如果文件过大，会出现内存不足，一般对于大文件，可以反复调用read(size)方法
###readline()可以每次读取一行内容
###readlines()可以一次读取所有内容并且按行返回列表

#5.文件写入
##写文件与读文件相同，区别是在调用open方法时，传入标识符'w'或者'wb'

f = open(r'test', 'w')
f.write('qq')
f.close()

with open(r'/home/zyy/桌面/ubuntu配置/test', 'w') as filewriter:
    filewriter.write('asd\naa')

