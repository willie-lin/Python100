#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : list.py
# @Time      : 2018/5/30 17:21
# @software  : PyCharm


def main():
    scores = {'wj': 99, 'lily': 100, 'yr': 59}

    print(scores['wj'])
    print(scores['lily'])

    for elem in scores:
        print('%s\t -->\t%d' % (elem, scores[elem]))

    scores['yr']  = 65
    scores['zgwl'] = 71
    scores.update(lm=67, fqh=85)
    print(scores)

    if 'wzt' in scores:
        print(scores['wzt'])
    print(scores.get('wzt'))
    print(scores.get('wzt',60))

    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('yr'),65)

    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()