#!/usr/bin/env/python
# -*-coding:utf-8-*-


#author:Wenming Yan
#create time:20190829

list = [64, 25, 12, 22, 11]


for i in range(len(list)):
    min_indext = i
    for j in range(i+1,len(list)):
        if list[min_indext] > list[j]:
            min_indext = j

    list[i],list[min_indext]=list[min_indext],list[i]

print('排序后的分组：')
for n in range(len(list)):
    print("%d" % list[n])






