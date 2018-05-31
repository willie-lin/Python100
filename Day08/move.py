#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : move.py
# @Time      : 2018/5/31 16:08
# @software  : PyCharm

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        '''
        构造器
        :param x: 横坐标
        :param y: 纵坐标
        '''

        self.x = x
        self.y = y

    def move_to(self, x, y):
        '''
        移动到指定位置
        :param x: 新的x
        :param y: 新的y
        :return:
        '''

        self.x = x
        self.y = y

    def move_by(self, dx ,dy):
        '''
        移动的增量
        :param dx:
        :param dy:
        :return:
        '''

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        '''
        计算与另一个点的距离
        :param other:
        :return:
        '''

        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()