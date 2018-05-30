#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : fact.py
# @Time      : 2018/5/30 16:26
# @software  : PyCharm


def factorial(num):
    """
    求阶乘

    :param num: 非负整数

    :return: num的阶乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(factorial(m) // factorial(n) // factorial(m - n))