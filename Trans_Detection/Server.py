#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 20:48
# @Author  : blvin.Don
# @File    : Server.py

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()

#添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
authorizer.add_user('user', '12345', './', perm='elradfmw')

#添加匿名用户 只需要路径
authorizer.add_anonymous(u'I:/UAVCode/image')

#初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer

#监听ip 和 端口,因为linux里非root用户无法使用21端口，所以我使用了2121端口
server = FTPServer(('192.168.31.16', 8090), handler)

#开始服务
server.serve_forever()

