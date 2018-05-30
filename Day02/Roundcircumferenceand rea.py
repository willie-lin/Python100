#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Roundcircumferenceand rea.py
# @Time      : 2018/5/30 9:49
# @software  : PyCharm
import math

'''
计算圆的周长和面积
P = 2PI * R
Area = math.Pi * R * R
'''


def PerimeterAndArea():
    radius = float(input('请输入圆的半径R= '))

    perimeter = 2 * radius * math.pi

    area = math.pi * radius * radius

    print('周长：%.2f' % perimeter)
    print('面积：%.2f' % area)


if __name__ == '__main__':
    PerimeterAndArea()