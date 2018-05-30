#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm


'''
tuple 练习
'''

def main():
    # 定义元组
    t = ('渔安', 37, True, '上海')
    print(t)

    # 获取元组中的元素
    print(t[0])
    print(t[3])

    # 给元组赋值
    # t[0] = 'wj' # TypeError: 'tuple' object does not support item assignment

    t = ('wj', 24, True, '四川成都')

    print(t)

    # 元组转列表

    persion = list(t)

    print(persion)

    # 修改列表

    persion[0] = 'yuan'

    persion[1] = 23

    print(persion)

    # 列表转化为元组

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)

    print(fruits_tuple)

    

if __name__ == '__main__':
        main()