#give the dir, save images under dir to DB
import pymongo
from pymongo import MongoClient

import os
import glob
from os.path import basename

import pandas as pd

dbIP = 'localhost';

class MADB:

	def connectDB(self, dbname, dbip, port):
		self._conn = MongoClient(dbip, port)
		self._db = self._conn[dbname]
		collectionname = 'resultinfo1'
		self._collection = self._db[collectionname];

	def getMA(self, maName):
		imgRecord = self._collection.find_one({'name': maName});
		return imgRecord;

	def saveMA(self, ma):
		record = self._collection.find_one({'name': ma['name']})
		print(' record ', record, record!=None)
		if(record != None):
			print(' exist! ');
			# malist_exist = record['malist']
			# malist_newadd = ma['malist']
			# malist = malist_exist + malist_newadd;
			magroups = ma['magroups'];
			self._collection.update_one({'name': ma['name']}, {'$set': {'magroups': magroups}});
		else:
			self._collection.insert(ma);
		print('[save] end')

	def saveUserInfo(self, userInfo):
		useridobject = self._collection.insert_one(userInfo);
		global userid 
		userid = useridobject.inserted_id
		record = self._collection.find_one({"_id": userid})
		print("save ok")
		print("userid madb", userid)
		print("record", record)
		return userid;

	def saveAnswerInfo(self, answerinfo):
		record = self._collection.find_one({"_id": userid})
		if "answerinfo" in record:
			answerinfoindb = record["answerinfo"]
			answerinfoindb.append(answerinfo)
			self._collection.update_one({"_id":userid}, {"$set": {"answerinfo": answerinfoindb}});
		else:
			answerinfoarray = []
			answerinfoarray.append(answerinfo)
			self._collection.update_one({"_id":userid}, {"$set": {"answerinfo": answerinfoarray}});
		# print("recordd", record)
		# if(record != None):
		
		print("save answer ok");

  #  	def saveAInfo(self, userInfo):
		# record = self._collection.find_one({"username": userInfo["username"]})
		# print("record", record)
		# if(record != None):
		# 	print("record exist")
		# 	passwd = userInfo["password"]
		# 	self._collection.update_one({"username": userInfo["username"]},{"$set": {"password": passwd}})
		# else:
		# 	self._collection.insert_one(userInfo)
		# print("save ok")
# #load raw imgs in dir to DB
# def saveRawImgstoDB(dir):
# 	print('[saveRawImgstoDB] Begin ', dir);
# 	#connect to MongoDB
# 	conn = MongoClient(dbIP, 27017)
# 	#get the DB
# 	db = conn['ImageDB']
# 	collection = db['rawimg']

# 	#get the images in the dir
# 	fileList = glob.glob(dir + '/*');
# 	beginIndex = collection.find({}).count();
# 	for filename in fileList:			
# 		filename = basename(filename)		
# 		doc = collection.find_one({'imgName': filename});
# 		if(doc == None):
# 			print('save raw img to DB ', filename);
# 			collection.insert({
# 				'imgName': filename,
# 				'index': beginIndex,
# 				'crop': False});
# 			beginIndex += 1
# 	print('[saveRawImgstoDB] End');

# #load processed imgs in dir to DB
# def saveProImgstoDB(dir):
# 	print('[saveProImgstoDB] Begin ', dir);
# 	#connect to MongoDB
# 	conn = MongoClient(dbIP, 27017)
# 	#get the DB
# 	db = conn['ImageDB']
# 	collection = db['proimg']

# 	#get the images in the dir
# 	fileList = glob.glob(dir + '/*');
# 	beginIndex = collection.find({}).count();
# 	for filename in fileList:			
# 		filename = basename(filename)
# 		imagename = os.path.splitext(filename)[0]
# 		proInfoDir = (os.path.join(dir, '../proimgmeta/', imagename + '.txt'));
# 		doc = collection.find_one({'imgName': filename});
# 		if(doc == None):
# 			print('save processed img to DB ', filename);
# 			df = pd.read_csv(proInfoDir);
# 			#get the contour info
# 			liContours = [];
# 			for index, row in df.iterrows():				
# 				contour = df.iloc[index].to_json()
# 				liContours.append(contour);
# 			collection.insert({
# 				'imgName': filename,
# 				'index': beginIndex,
# 				'contours': liContours,
# 				});
# 			beginIndex += 1

# 	print('[saveProImgstoDB] End');

# saveProImgstoDB("../../proimg")
