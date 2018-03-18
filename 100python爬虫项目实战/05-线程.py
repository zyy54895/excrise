#多线程
##1.用threading模块创建多线程
import random
import time, threading
# 新线程执行的代码:
def thread_tun(urls):
    print('Current %s is running...' % threading.current_thread().name)
    for url in urls:
        print('%s ---->>> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)

print('%s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=thread_tun, name='Thread_1', args=(['url1', 'url2', 'url3'], ))
t2 = threading.Thread(target=thread_tun, name='Thread_2', args=(['url4', 'url5', 'url6'], ))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)

##2.从threading.Thread继承创建线程类

import random
import threading
import time
class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls
    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s ---->>> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)
print('%s is running...' % threading.current_thread().name)
t1 = myThread(name='Thread_1', urls=['url1', 'url2', 'url3'])
t2 = myThread(name='Thread_2', urls=['url4', 'url5', 'url6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)

#3.线程同步
import threading
mylock = threading.RLock()
num = 0
class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('%s locked,number: %d' % (threading.current_thread().name, num))
            if num>=4:
                mylock.release()
                print('%s released,number: %d' %(threading.current_thread().name, num))
                break
            num+=1
            print('%s released,number:%d' % (threading.current_thread().name, num))
            mylock.release()

if __name__=='__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()

#4.协程
from gevent import monkey; monkey.patch_all()
import gevent
import requests
from gevent.pool import Pool

def run_task(url):
    print('Visit ---> %s' % url)
    try:
        response = requests.get(url)
        data = response.text
        print('%d bytes received from %s' %(len(data), url))
    except Exception as e:
        print(e)
    return 'url:%s --->finish' % url
if __name__=='__main__':
    pool =Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    # greenlets = [gevent.spawn(run_task, url) for url in urls]
    # gevent.joinall(greenlets)                               #采用spawn和joinall方法
    results = pool.map(run_task, urls)
    print(results)
