#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : In2Cm.py
# @Time      : 2018/5/30 10:46
# @software  : PyCharm


value = float(input('请输入长度='))
unit = input('请输入单位：')

if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
if unit == 'cm' or unit == '厘米':
    print('%d厘米 = %f英寸' % (value, value / 2.54))