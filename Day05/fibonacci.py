#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : fibonacci.py
# @Time      : 2018/5/30 15:43
# @software  : PyCharm

a = 0
b = 1

for _ in range(20):
    (a,b) = (b, a + b)
    print(a, end= ',  ')
