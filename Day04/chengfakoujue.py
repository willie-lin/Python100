#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : chengfakoujue.py
# @Time      : 2018/5/30 11:29
# @software  : PyCharm

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d ' % (i, j , i * j), end='\t')
    print()