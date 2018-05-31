#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Class.py
# @Time      : 2018/5/31 14:43
# @software  : PyCharm


class Student(object):

    # __init__  初始化操作

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s只能看《熊出没》.' % self.name)
        else:
            print('%s正在看。' % self.name)


def main():
    # 创建学生对象并制定姓名和年龄
    stu1 = Student('骆昊', 38)

    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()