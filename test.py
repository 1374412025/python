import os
import sys
import math
a=math.pi
a=1
print (a)
print("-----------------------")

print ("Hello, Python!")
print("-----------------------")

list =["a", "b", "c","d","e"]
print (list)

print("-----------------------")
c=range(len(list))
for i in c:
    print(list[i])

#print("-----------------------")
#n=sys.stdin.readline()
#print (n)

print("-----------------------")
print(list[-1])
print( list[: :1])
print( list[: :-1])
print( list[: :-2])
print(list[-1:-5:-2])

print("-----------------------")
list.pop(4)
print(list)
list.insert(0,"k")
print(list)
list.reverse()
print(list)
print("-----------------------")

print("format应用-----------------------")
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
print("网站名：{0}, 地址 {1}".format("菜鸟教程", "www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print("遍历字典-----------------------")
dict2 = {'key1':1, 'key2':2}
mykey = [key for key in dict2]  # ['key1', 'key2']
print(mykey)#['key1', 'key2']
myvalue = [value for value in dict2.values()]
print(myvalue)#[1, 2]
key_value = [(k, v) for k, v in dict2.items()]
print(key_value)#[('key1', 1), ('key2', 2)]

print("-----------------------")
a,b=1,2
a,b=b,a
print(a,b)

print("-----------------------")
symbol = "-"
seq = ("a", "b", "c") # 字符串序列
print(symbol.join( seq ))


print("-----获取当前时间------------------")
import time
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print(datetime.datetime.now())

print("------浅拷贝-----------------")
import copy
list1 = [1, 2, 3, [1, 2]]
list2 = copy.copy(list1)
print(list2)#[1, 2, 3, [1, 2]]
list2.append('a')
print(list1)#[1, 2, 3, [1, 2]]
print(list2)#[1, 2, 3, [1, 2], 'a']
list2[3].append('a')
print(list1)#[1, 2, 3, [1, 2, 'a']]
print(list2)#[1, 2, 3, [1, 2, 'a'], 'a']
print("------深拷贝-----------------")
import copy
list1 = [1, 2, 3, [1, 2]]
list2 = copy.copy(list1)
print(list2)#[1, 2, 3, [1, 2]]
list2.append('a')
print(list1)#[1, 2, 3, [1, 2]]
print(list2)#[1, 2, 3, [1, 2], 'a']
list2[3].append('a')
print(list1)#[1, 2, 3, [1, 2, 'a']]
print(list2)#[1, 2, 3, [1, 2, 'a'], 'a']



























