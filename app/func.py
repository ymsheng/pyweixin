#-*- coding:utf-8 -*-
import os.path
import re
import tornado.web
import urllib
import json
from xml.dom import minidom 
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
        
        
class WeixinHandler(tornado.web.RequestHandler):
    def check_xsrf_cookie(self):
        pass
        
    def get(self):
    	echostr = self.get_argument("echostr")
        self.write(echostr)
        
    def post(self):
    	message = self.request.body
        if not message:
            return
            
      
        msgDict = {}  #use info and content 
        nowtime = int(time.time())

        dom = minidom.parseString(message)
        root = dom.firstChild 
        childs = root.childNodes    
    	for child in childs: 
            if child.nodeType == child.TEXT_NODE:  
                pass
            else:
                msgDict[child.nodeName]=child.childNodes[0].data
        
        content = msgDict['Content']  #user content
        response = """<xml>
       			<ToUserName><![CDATA[%s]]></ToUserName>
       			<FromUserName><![CDATA[%s]]></FromUserName>
        		<CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
 		     	</xml> """ % (msgDict['FromUserName'],msgDict['ToUserName'],nowtime,'text','欢迎来到微信的公众帐号')
        self.write(response)
        
        
        
