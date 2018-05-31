#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : clock.py
# @Time      : 2018/5/31 15:47
# @software  : PyCharm
from time import sleep


class Clock(object):

    '''
    数字时钟
    '''

    def __init__(self, hour=0, minute=0, second=0):
        '''
        构造器
        :param hour: 时
        :param minute: 分
        :param second: 秒
        '''

        self._hour = hour
        self._minute = minute
        self._second = second


    def run(self):
        '''
        走字
        :return:
        '''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0


    def __str__(self):
        '''
        显示时间
        :return:
        '''
        return '%02d:%02d:%02d' %  (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 38)
    while True:
        print(clock)
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()