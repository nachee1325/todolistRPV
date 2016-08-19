from flask_pymongo import pymongo
from pymongo import MongoClient
def connect_to_db():
	try:
		client = MongoClient('ds161255.mlab.com',61255)
		client.prvtodo.authenticate('admin','t1wDWE_L17zd')
		db = client.prvtodo
		print "connected!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
