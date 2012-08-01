#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

import os

class CFileOpener:

    prefix = "gedit sftp://kirichenko@your.sftpORAnyElseServer.com:8022"
    postfix = ""

    @staticmethod
    def open(path):
        print 'opening file ' + CFileOpener.prefix + path + CFileOpener.postfix
        os.system(CFileOpener.prefix + path + CFileOpener.postfix)

class WSHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print 'new connection'

    def on_message(self, message):
        print 'message received %s' % message
        CMainProc.fileOpener.open(message)

    def on_close(self):
        print 'connection closed'


class CMainProc:

    fileOpener = CFileOpener()

    def __init__(self, port):
        application = tornado.web.Application([(r'/ws', WSHandler),])
        self.http_server = tornado.httpserver.HTTPServer(application)
        self.http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    myMainProc = CMainProc(8888);
