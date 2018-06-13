#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Threading.py
# @Time      : 2018/6/4 8:55
# @software  : PyCharm


from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s ...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！ 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Java从入门到放弃',))
    t1.start()
    t2 = Thread(target=download, args=('下载西部世界1', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总耗时%.3f秒' % (end - start))


if __name__ == '__main__':
    main()