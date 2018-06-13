#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Bank.py
# @Time      : 2018/6/4 9:22
# @software  : PyCharm

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁，才能执行下面的
        self._lock.acquire()
        try:
            # 计算存款余额
            new_balance = self._balance + money
            # 模拟受理时间0.001
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁操作保证正常异常的锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个线程同时存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额：￥%d元' % account.balance)


if __name__ == '__main__':
    main()