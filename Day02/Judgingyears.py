#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Judgingyears.py
# @Time      : 2018/5/30 10:01
# @software  : PyCharm

'''
被 4 整除和除以100 =0 或者 被400 整除
'''

# year =  int(input('请输入年份= '))
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


def Is_Leap(year):
    # return print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(is_leap)


def Leapyears():
    for year in range(888,2999):
        # Is_Leap(year)
        print('year %d ' % year + 'is %r' % Is_Leap(year))


if __name__ == '__main__':
    Leapyears()