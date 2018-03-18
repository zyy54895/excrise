# conding=utf-8

#一、多进程
#1.使用os模块中的fork方式实现多进程
##fork方法是调用一次，返回两次，操作系统将当前进程（父进程）复制出一份子进程，这两个进程几乎完全相同。子进程中永远返回0，父进程返回子进程的id
import os
if __name__ == '__main__':
    print('currnet Process (%s) start...'%(os.getpid()))
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('i am a child process(%s) and my parent process is(%s)' % (os.getpid(), os.getppid()))
    else:
        print('I(%s) created a child process(%s).' % (os.getpid(), pid))

#2.使用multiprocessing模块创建多进程

import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print('child process %s (%s) running...' % (name, os.getpid()))
if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i), ))
        print('process will start.')
        p.start()
    p.join()
    print('process end')

#3.multiprocessing提供了一个Pool类来代表进程池对象
from multiprocessing import Pool
import os, time, random

def run_task(name):
    print('task %s (pid=%s) is running...' % (name, os.getpid()))
    time.sleep(random.random()*3)
    print('task %s end.' % name)

if __name__ == '__main__':
    print('current process %s' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i, ))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocesses done.')

##tips:
###Pool对象调用join()方法会等待所有子进程执行完毕，调用jion()之前必须先调用close（），调用close()之后就不能添加新的Process了

#4.进程间通信

##Queue通信：
###Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。有两个方法:Put和Get可以进行Queue操作
###1.Put方法用以插入数据到队列中，有两个可选参数blocked和timeout。如果blocked为True，并且timeout为正值，该方法会阻塞timeout指定的时间，直至队列有剩余空间
###2.Get方法可以从队列读取并且删除一个元素。也有有两个可选参数blocked和timeout

from multiprocessing import Process,Queue
import os, time, random

#写数据进程执行的代码
def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

#读数据进程执行的代码
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__ == '__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q, ['url1', 'url2', 'url3']))
    proc_writer2 = Process(target=proc_write, args=(q, ['url4', 'url5', 'url6']))
    proc_reader = Process(target=proc_read, args=(q, ))
    #启动子进程proc_writer,写入:
    proc_writer1.start()
    proc_writer2.start()
    #启动子进程proc_reader,读取:
    proc_reader.start()
    #等待proc_writer结束:
    proc_writer1.join()
    proc_writer2.join()
    #proc_reader进程里是死循环，只能强行终止
    proc_reader.terminate()

##Pipe通信

##Pipe常用来在两个进程间进行通信，两个进程分别位于管道的两端
###Pipe返回（conn1,conn2),有duplex参数，若为True，代表管道为全双工模式,conn1,conn2均可收发;若为False,conn1负责接收消息,conn2负责发送消息
###send和recv为发送和接收消息的方法

import multiprocessing
import random
import time,os

def proc_send(pipe, urls):
    for url in urls:
        print('Process(%s) send: %s' % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print('Process(%s) rev: %s' % (os.getpid(), pipe.recv()))
        time.sleep(random.random())

if __name__ == '__main__':
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1], ))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
