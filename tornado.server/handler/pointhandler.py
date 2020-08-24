
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient

import setting

import glob

from PIL import Image

import io
import os.path
from os.path import basename

import json

import subprocess

class TestHandler(tornado.web.RequestHandler):
    def get(self, word):
        print('getsurvey handler', word);       
        self.write('ok');


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class GetSlide(tornado.web.RequestHandler):
	def post(self):
		slide = int(self.get_argument('slideIndex'));
		slide += 1
		print('slide#=',  slide);
		print('slide', slide);
		self.write({
			'slideIndex': slide,
			})
		# self.render('slide' + slide + '.html')
    
class GetImgListHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3001")
        # self.set_header("Access-Control-Allow-Headers", "x-kopernio-plugin-version")

    def post(self):
        imgList = glob.glob("./rc1_n/*.png");
        
        x = {}

        for img in imgList:
            imgName = basename(img).split(".")[0]
            x[imgName] = img;
        print('img list', imgList[0: 7], len(imgList))
        print('x', x)

        self.set_header('Access-Control-Allow-Origin', "*")
        self.write({'img': x}) 
    def options(self, *args, **kwargs):
        pass