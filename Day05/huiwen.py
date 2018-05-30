#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : huiwen.py
# @Time      : 2018/5/30 16:02
# @software  : PyCharm

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    print(num2)
    num2 += temp % 10
    print(num2)
    temp //= 10
    print(temp)
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
