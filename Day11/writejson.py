#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : writejson.py
# @Time      : 2018/6/1 16:12
# @software  : PyCharm


import json


def main():
    mydict = {
        'name': '罗大佑',
        'age': 49,
        'qq': 123456789,
        'friend': ['王大锤', '白远方'],
        'card' : [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'BMW', 'max_speed': 380},
            {'brand': 'Benz', 'max_speed': 480}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')


if __name__ == '__main__':
    main()