#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : craps.py
# @Time      : 2018/5/30 15:26
# @software  : PyCharm


from random import randint

money = 1000
while money > 0:
    print('你的总资产：', money)
    need_go_on = False
    while True:
        debt = int(input('请下注:'))
        if debt > 0 and debt <= money :
            break
    first = randint(1, 6) + randint(1,6)
    print('玩家摇了%d点：' % first)
    if first == 7 or first==11:
        print('玩家胜')
        money += debt
    elif first == 2 or first ==3 or first == 12 :
        print('庄家胜')
        money -= debt
    else:
        need_go_on = True
    while need_go_on:
        current = randint(1,6) + randint(1,6)
        print('玩家摇了%d点' % current)
        if current == 7 :
            print('庄家胜')
            money -= debt
            need_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            need_go_on = False
print('你破产了，游戏结束了')