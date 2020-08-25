import tornado.web
from tornado.options import options

import json
from bson import ObjectId
from bson import BSON
from bson import json_util

import json

import pymongo

from handler.madb import MADB

ssDB = MADB()
ssDB.connectDB("UserStudyT","localhost",27017)
print(ssDB)
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o);
#         return json.JSONEncoder.default(self, o);

class SaveUserInfoHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_default_header()
    def post(self):
        print("save start")
        userInfo_age = self.get_argument("age")
        userInfo_gender = self.get_argument("gender")
        userInfo_studyinterest = self.get_argument("studyinterest")
        userInfo_academiclevel = self.get_argument("academiclevel")
        userInfo_experience = self.get_argument("experience")

        userid = ssDB.saveUserInfo({
            "userage": userInfo_age,
            "usergender": userInfo_gender,
            "userstudyinterest": userInfo_studyinterest,
            "useracademiclevel": userInfo_academiclevel,
            "userexperience": userInfo_experience,
        })
        print("userid", userid)
        self.set_header("Access-Control-Allow-Origin", "*")
        # self.write({"userid": JSONEncoder().encode(userid)})
        self.write("save ok")

    def options(self):
        # self.set_header('Access-Control-Allow-Origin', '*')
        # self.set_header("Access-Control-Allow-Credentials", "true")
        # self.set_header("Access-Control-Allow-Methods", "*")
        self.set_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        # self.set_header("Access-Control-Allow-Headers", "Content-Type,Access-Token")
        # self.set_header("Access-Control-Expose-Headers", "*")
        pass
    def set_default_header(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3001")
        # self.set_header("Access-Control-Allow-Headers", "x-kopernio-plugin-version")

        print("setting headers!!!")


class SaveAnswerInfoHandler(tornado.web.RequestHandler):
    def initialize(self):
        # self.set_header("Access-Control-Allow-Origin", "http://localhost:3001")
        self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header("Access-Control-Allow-Headers", "x-kopernio-plugin-version")

    def post(self):
        print("save answer start")
        # self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        # self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


        user_question = self.get_argument("question");
        user_answer = self.get_argument("answer");
        user_answerinterval = self.get_argument("answerinterval");
        user_imgsrc = self.get_argument("imgsrc")
        # print("answer", json.loads(answerinfo))
        print(user_question.split("?,"))
        ssDB.saveAnswerInfo({
            "imgsrc": user_imgsrc,
            "question": user_question,
            "answer": user_answer,
            "answerinterval": user_answerinterval,
        })
        print(user_question)
        # self.set_header("Access-Control-Allow-Origin", "http://localhost:3001")
        self.write({"save": "ok"})

    def options(self):
        pass