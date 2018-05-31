#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : getsuffix.py
# @Time      : 2018/5/31 11:10
# @software  : PyCharm

def get_suffix(filenae, has_dot=False):
    '''
    获取文件后缀名
    :param filenae: 文件名
    :param has_dot: 返回的后缀名是否要带点
    :return: 文件后缀名
    '''

    pos= filenae.rfind('.')
    if 0 < pos < len(filenae) -1:
        index = pos if has_dot else pos + 1
        return filenae[index]
    else:
        return ''

