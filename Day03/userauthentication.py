#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : userauthentication.py
# @Time      : 2018/5/30 10:29
# @software  : PyCharm

username = input('请输入用户名： ')
password = input('请输入密码：')

if username == 'admin' and password == '123456':
    print('hello')
else:
    print('error')