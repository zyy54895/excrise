

import pickle

d = dict(url='index.html', title='首页', content='首页')

f = open('pickle.txt', 'wb')
pickle.dump(d, f)
f.close()

#反序列化
f = open('pickle.txt', 'rb')
d1 = pickle.load(f)
f.close()
