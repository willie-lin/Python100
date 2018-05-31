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
    content = '许多年前 你曾是个朴素的少年爱上一个人 就不怕付出自己一生相信爱会永恒 相信每个陌生人相信你会成为最想成为的人习惯说谎 就是变得成熟了吗有一套房子之后 才能去爱别人吗总是以为 成功之后 就能抚平伤痕欲望边埋着 错过的人当青春耗尽 只剩面目可憎'
    while True:
        # 清理屏幕输出

        os.system('cls')
        print(content)

        time.sleep(0.2)

        content = content[1:] + content[0]


if __name__ == '__main__':
    main()