
#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : listMaxandMin.py
# @Time      : 2018/5/31 11:15
# @software  : PyCharm


def max2(x):
    m1, m2 = (x[0], x[1] if x[0] > x[1] else (x[1], x[0]))
    for index in range(2, len(x)):
        if x[index] > m1 :
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


if __name__ == '__main__':
    max2(9)