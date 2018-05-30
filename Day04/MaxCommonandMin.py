#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : MaxCommonandMin.py
# @Time      : 2018/5/30 14:46
# @software  : PyCharm

x = int(input('x = '))
y = int(input('y = '))
if x > y :
    (x,y) = (y,x)
    # print((x,y)==(y,x))
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break