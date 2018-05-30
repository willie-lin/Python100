#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length = ', len(set1))

    set2 = set(range(1, 10))
    print(set2)

    set1.add(4)
    set1.add(5)
    # 添加集合
    print(set1)

    set2.update([11, 12])
    # 更新集合
    print(set2)

    set2.discard(5)
    # 删除某个元素
    print(set2)

    if 4 in set2:
        set2.remove(4)
        # 删除某个集合中的元素
    print(set2)

    for elem in set2:
        print(elem ** 2, end='  ')
    print()


    set3 = set((1, 2, 3, 3, 3, 2, 1))

    # 将元组转化为集合
    print(set3)
    print(set3.pop())
    print(set3)



if __name__ == '__main__':
    main()