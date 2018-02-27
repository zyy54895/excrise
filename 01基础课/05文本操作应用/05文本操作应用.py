
import linecache
import time

now = time.time() #代码开始时间

data_keys = ('bid', 'uid', 'username', 'ugrade', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_mid', 'geo', 'lat', 'lon', 'place', 'hashtags', 'ats', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')  #建立字典键值
keys = dict(zip(data_keys, (m for m in range(0, len(data_keys)))))   #建立字典

f = linecache.getlines('twitter数据挖掘片段.txt')  #获取文本内容
lines = [x[1:-1].split(',') for x in f] #拆分,去除前面双引号以及最后换行符,并生成列表

#1.该文本里，有多少个用户。（要求：输出为一个整数。）
uesrs = set([line[keys['username']] for line in lines])





