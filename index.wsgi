#-*- coding:utf-8 -*-
import os.path
import re
import tornado.web



from app import home,func
import tornado.wsgi


settings = {
                'template_path' : os.path.join(os.path.dirname(__file__),"templates"),
                'static_path' : os.path.join(os.path.dirname(__file__),"static"),
                'xsrf_cookies' : True,
                'autoescape' : None,
                'cookie_secret' : "xxxxxxx",
                'login_url' : "/login",
            }
            
application = tornado.web.Application([
    (r"/", home.MainHandler),

    (r"/weixin", func.WeixinHandler),
   
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    main()