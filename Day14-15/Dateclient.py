#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Dateclient.py
# @Time      : 2018/6/4 11:03
# @software  : PyCharm


from socket import socket

def main():
    # 创建套接字默认使用ipv4和TCP

    client = socket()
    # 2.连接到服务器
    client.connect(('127.0.0.1', 1999))

    # 服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()