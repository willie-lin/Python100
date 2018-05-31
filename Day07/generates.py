#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : generates.py
# @Time      : 2018/5/31 10:19
# @software  : PyCharm

import random

def generate_code(code_len=4):
    '''
    生成指定长度的验证码
    :param code_len: 默认长度
    :return: 有大小写字母数字构成的随机码
    '''

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%._+='
    last_pos = len(all_chars) - 1

    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
        # print(code)
    return code


if __name__ == '__main__':
    print(generate_code(16))