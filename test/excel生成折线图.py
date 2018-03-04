import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_path_name():                   #选择文件函数
    import win32ui
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    filename = dlg.GetPathName()  # 获取选择的文件名称
    return filename

running=True
while running:
    status=input('Y继续，N退出：')
    if status=='Y':
        filename=get_path_name()
        df=pd.read_excel(filename)
        name=df.columns
        time=df[name[0]]
        for i in range(1,len(name)):
            plt.plot(time,df[name[i]])
        plt.show()
        plt.figure(figsize=(12,10))
    else:
        running=False