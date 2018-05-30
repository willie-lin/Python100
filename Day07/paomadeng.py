#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm


import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'

    while True:
        # 清理屏幕输出

        os.system('clear')
        print(content)

        time.sleep(0.2)

        content = content[1:] + content[0]


if __name__ == '__main__':
    main()