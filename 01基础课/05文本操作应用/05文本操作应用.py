
import linecache
import time

now = time.time() #代码开始时间

data_keys = ('bid', 'uid', 'username', 'ugrade', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_mid', 'geo', 'lat', 'lon', 'place', 'hashtags', 'ats', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')  #建立字典键值
keys = dict(zip(data_keys, (m for m in range(0, len(data_keys)))))   #建立字典

f = linecache.getlines('twitter数据挖掘片段.txt')  #获取文本内容
lines = [x[1:-1].split(',') for x in f] #拆分,去除前面双引号以及最后换行符,并生成列表

#1.该文本里，有多少个用户。（要求：输出为一个整数。）
username_unset = [line[keys['username']] for line in lines]   #将用户名输出一个list，中间有重复的内容
username_set = set(username_unset)     #用户名去重并排序
user_total = len(username_set)
assert type(user_total) == int
print('该文本内用户总数为：%s' % user_total)

#2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
users = list(username_set)
assert type(users) == list

#3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

def isVaildDate(date):             #判断字符串是否为时间格式
    try:
        if ":" in date:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False


lines_from_created_at_source = [line[keys['created_at']] for line in lines]   #将所有发布日期生成一个list
date_time = [lines_from_created_at_source[i][1:-1] for i in range(len(lines_from_created_at_source)) if isVaildDate(lines_from_created_at_source[i][1:-1]) == True] #去除无效日期
year_month =[date_time[i][0:7] for i in range(len(date_time)) if date_time[i][0:7] == '2012-11'] #筛选出2012-11月份
count_created_at_from_2012_11 = len(year_month)
assert type(count_created_at_from_2012_11) == int

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
year_month_day = [date_time[i][0:10] for i in range(len(date_time))]#取出发布日期中的年月日
year_month_day_list = list(set(year_month_day))
assert type(year_month_day_list) == list

#5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
hours = [int(date_time[i][11:13]) for i in range(len(date_time))]  #取出小时数
hours_dict = {}
for i in hours[:]:
    if i in hours_dict:
        hours_dict[i] += 1
    else:
        hours_dict[i] = 1        #输出为字典

max = 0
for j in hours_dict.keys():
    if hours_dict[j] > max :
        max = hours_dict[j]
        hours_value = j     #找出字典中最大值
assert type(max) == int
print('在%s' %hours_value, '点到%s' % (hours_value+1), '点发布的数据最多,发布数为%s' % max)

#6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

date_user_source = list(zip([username_unset[i][1:-1] for i in range(len(username_unset))], [lines_from_created_at_source[j][1:11] for j in range(len(lines_from_created_at_source))])) #建立（用户名，日期）列表
date_uesr_error = [x for x in range(len(date_user_source)) if isVaildDate(date_user_source[x][1]) == False] #找出错误日期index
date_users_tuple = [date_user_source[x] for x in range(len(date_user_source)) if not x in date_uesr_error]   #去除错误的日期
date_users_dict = {}
# for i in range(len(date_users_tuple)):
#      if date_users_tuple[i][1] in date_users_dict.keys():

