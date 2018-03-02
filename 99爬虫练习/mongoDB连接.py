from pymongo import MongoClient

#建立MongoDB数据库连接
client = MongoClient('localhost', 27017)

#连接所需数据库,test为数据库名
db = client.test

#连接所用集合，也就是我们通常所说的表，test为表名
collection = db.test

#接下里就可以用collection来完成对数据库表的一些操作

#查找集合中所有数据
for item in collection.find():
    print(item)

#查找集合中单条数据
print(collection.find_one())

#向集合中插入数据
collection.insert({'name': 'asd', 'age': 25, 'addr': 'Cleveland'})

#更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
collection.update({'Name': 'Tom'}, {'Name': 'asd'})

#删除集合collection中的所有数据
collection.remove()

#删除集合collection
collection.drop()