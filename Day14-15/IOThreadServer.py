#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : IOThreadServer.py
# @Time      : 2018/6/4 11:08
# @software  : PyCharm


from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread



def main():

    # 自定义模块
    class FileTransferhandler(Thread):

        def __init__(self, cclient):
            super.__init__()
            self.cclient = cclient

        def run(self):
            my_dict = { }
            my_dict['filename'] = 'xxxxx.jpg'
            # JSon是纯文本不能携带二进制数据
            # 图片可以处理成base64编码
            my_dict['filedata'] = data
            json_str = dumps(my_dict)

            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('127.0.0.1', 5566))
    server.listen(512)
    print('服务器启动监听')
    with open('xxxxx.jpg', 'rb') as f :
        # data = b64decode(f.read()).decode('utf-8')
        data = b64encode(f.read()).decode('utf-8')
    while True:

        client , addr = server.accept()
        FileTransferhandler(client).start()


if __name__ == '__main__':
    main()