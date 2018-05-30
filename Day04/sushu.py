#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : sushu.py
# @Time      : 2018/5/30 14:39
# @software  : PyCharm

from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))

is_prime = True
for x in range(2, end +1):
    if num % x ==0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
