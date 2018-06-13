#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : phonematche.py
# @Time      : 2018/6/1 17:16
# @software  : PyCharm


import re


def main():
    pattern = re.compile(r'(?<=\D)1[3456789]\d{1,9}(?=\D)')

    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------------------------------------------------------')

    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------------------------------------------------------')

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
