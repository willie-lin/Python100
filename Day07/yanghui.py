#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : yanghui.py
# @Time      : 2018/5/31 11:21
# @software  : PyCharm


def main():
    num = int(input('Number of rows;'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row +1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()