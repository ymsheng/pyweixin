#-*- coding:utf-8 -*-
import os.path
import re
import tornado.web

class MainHandler(tornado.web.RequestHandler):
     def get(self):
         self.write("Hello, python weixin!!!")

