#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : jichengduotai.py
# @Time      : 2018/6/1 10:47
# @software  : PyCharm


class Person(object):
    ''' 人 '''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s正在看电视。' %  self._name)
        else:
            print('%s 正在看动画片。' % self._name)


class Student(Person):
    ''' 学生'''

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s%s正在学习%s' % (self._grade, self._name, self._age))


class Teacher(Person):
    ''' 老师 '''

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title

    def teach(self, course):
        print('%s%s 正在讲%s.' % (self._name, self.title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_tv()
    t = Teacher('王晶', 38, '教授')
    t.teach('python 程序设计')
    t.watch_tv()


if __name__ == '__main__':
    main()