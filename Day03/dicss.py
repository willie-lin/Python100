#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : dicss.py
# @Time      : 2018/5/30 10:53
# @software  : PyCharm

from random import randint

face = randint(1, 6)
if face == 1 :
     result = '唱歌'
elif face == 2 :
    result = '跳舞'
elif face == 3 :
    result = '深蹲'
elif face == 4 :
    result = '绕口令'
elif face == 5 :
    result = '冷笑话'
elif face == 6 :
    result = '喝酒'
print(result)