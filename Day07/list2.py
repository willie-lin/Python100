#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历表元素

    for fruit in fruits:
        print(fruit.title(), end=',  ')
    print()

    # 列表切片

    fruits2 = fruits[1:5]
    print(fruits2)

    fruits3 = fruits

    fruits4 = fruits[:]
    print(fruits3)

    print(fruits4)

    fruits5 = fruits[-3: -1]
    print(fruits5)

    fruits6 = fruits[::-1]

    print(fruits6)




if __name__ == '__main__':
    main()