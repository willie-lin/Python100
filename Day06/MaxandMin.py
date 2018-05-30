#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : MaxandMin.py
# @Time      : 2018/5/30 16:46
# @software  : PyCharm


def gcd(x, y):
    (x,y) = (y,x) if x > y else (x, y)
    # print(x,y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0 :
            return factor


def lcm(x,y):
    return x * y // gcd(x,y)


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


if __name__ == '__main__':
    # print(gcd(2,3))
    # print(lcm(2,3))

    print(is_palindrome(1331))