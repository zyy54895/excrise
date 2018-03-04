import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def straight(value,num):
    a=[value]
    for i in range(num):
        value+=2
        a.append(value)
    return(a)
value=input("数组数字：")
num=input("输入循环次数：")
i=0
column=[i]
for i in range(int(num)):
    i=i+1
    column.append(i)
ss = straight(int(value),int(num))
plt.plot(column,ss)
plt.show()




