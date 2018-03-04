import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path = input('输入文件路径：')
df = pd.read_excel(path + '.xlsx')
name = df.columns
time = df[name[0]]

for i in range(1, len(name)):
    plt.plot(time, df[name[i]])
    # plt.plot(time,df[name[2]])
    # plt.show()
#plt.plot(s1)

# plt.legend()
plt.show()
plt.figure(figsize=(12, 10))
