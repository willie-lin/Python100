#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : buildWiths.py
# @Time      : 2018/6/11 11:23
# @software  : PyCharm

import builtwith, ssl, whois

print(builtwith.parse('http://www.bootcss.com'))
print(builtwith.parse('https://www.zhihu.com'))
print(builtwith.parse('https://www.jd.com'))

ssl._create_default_https_context = ssl._create_unverified_context

print(builtwith.parse('https://www.jd.com'))
print(builtwith.parse('https://www.jianshu.com/'))

whois('jd.com')