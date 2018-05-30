#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : F2C.py
# @Time      : 2018/5/30 9:38
# @software  : PyCharm

'''
华氏度转摄氏度
F = 1.8C +32
'''
def FtoC():
    f = float(input('请输入华氏度 = '))
    c = (f - 32) / 1.8
    return print('%.1f华氏度 = %.1f摄氏度' % (f ,c))


def CtoF():
    c = float(input('输入你要转换的摄氏度='))
    f = 1.8 * c + 32
    return print('%.1f摄氏度 = %.1f华氏度' % (c, f))


if __name__ == '__main__':
    # FtoC()
    CtoF()