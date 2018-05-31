#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : Test.py
# @Time      : 2018/5/31 15:38
# @software  : PyCharm


class Person(object):

    # 限定Person对象只能绑定_name, _age 和 _gender属性

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 -setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    # person.age = 22
    person._gender = '男'
    person.play()


if __name__ == '__main__':
    main()
