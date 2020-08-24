#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.pointhandler import IndexHandler
from handler.pointhandler import TestHandler
from handler.pointhandler import GetSlide
from handler.pointhandler import GetImgListHandler
from handler.dbHandler import SaveUserInfoHandler
from handler.dbHandler import SaveAnswerInfoHandler

url=[
	# (r'/', IndexHandler),
    (r'/test/(\w+)', TestHandler),
    (r'/slide', GetSlide),
    (r'/saveUserInfo', SaveUserInfoHandler),
    (r'/saveanswerinfo', SaveAnswerInfoHandler),
    (r'/getImgList', GetImgListHandler),

]