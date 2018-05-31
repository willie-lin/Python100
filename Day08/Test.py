#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Test.py
# @Time      : 2018/5/31 15:38
# @software  : PyCharm


class Test:
    def __init__(self, foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    tets= Test("hello")
    tets.__bar()
    print(test.__foo)
