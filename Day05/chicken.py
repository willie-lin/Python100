#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : chicken.py
# @Time      : 2018/5/30 15:12
# @software  : PyCharm

'''
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

'''


  # x = 100 /5 = 20
#  y  = 100 /3 = 33
#  z = 300

for x in range(0,20):
    for y in range(0,33):
         z = 100 - x - y
         if 5 * x + 3 * y + z/3 == 100 :
             print('公鸡: %d 只, 母鸡：%d只,小鸡： %d只' % (x, y, z))

