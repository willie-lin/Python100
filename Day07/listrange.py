#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm


import sys


def main():

    f = [x for x in range(1,10)]
    print(f)

    f1 = [x + y for x in 'ABCDE' for y in '1234567']
    print(f1)

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间

    f3 = [x ** 2 for x in range(1, 1000)]
    print(f3)

    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)


    f4 = (x ** 2 for x in range(1,1000))
    print(f4)

    print(sys.getsizeof(f4))

    for val in f4:
        print(val)




if __name__ == '__main__':
    main()