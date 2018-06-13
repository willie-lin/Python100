#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Duojincheng.py
# @Time      : 2018/6/1 17:46
# @software  : PyCharm

from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_task(filename):
    print('启动下载进程,进称号[%d].' %  getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('python 从入门到放弃.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('下班回家', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()