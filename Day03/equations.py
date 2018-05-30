#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : equations.py
# @Time      : 2018/5/30 10:37
# @software  : PyCharm

'''
        3x - 5 (x > 1)
f(x） =  x + 2 (-1 <= x <= 1 )
        5x +3  ( x < -1)
'''

x = float(input('x = '))

if x > 1 :
    y = 3 * x -5
elif x >= -1 :
    y = x + 2
else:
    y = 5*x + 3
print('f(%.2f) = %.2f' % (x, y))