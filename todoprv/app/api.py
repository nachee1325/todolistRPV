from app import app
from flask import redirect, jsonify, request
from pymongo import MongoClient

client = MongoClient('ds161255.mlab.com',61255)
client.prvtodo.authenticate('admin','t1wDWE_L17zd')
db = client.prvtodo
collection = db.task_collection

def add(data):
	print data
	try:
		collection.insert_one(data)
		print "successfully added"
		print db.task_collection.find_one()
	except pymongo.errors.ConnectionFailure, e:
		print "add_error: %s" % e


def delete(taskID):
	try:
		output = []

		for j in collection.find():
			output.append({'_id':j['_id'] ,'task':j['task'],'due':j['due']})
		sorted_output = sorted(output, key=lambda k: k['due'])
		print "\DELETE THIS: " + str(taskID)
		collection.remove(sorted_output[taskID])
		# print "successfully remove"

	except pymongo.errors.ConnectionFailure, e:
		print "delete_error: %s" % e

def edit(taskID,data):
	try:
		output = []

		for j in collection.find():
			output.append({'_id':j['_id'] ,'task':j['task'],'due':j['due']})
		sorted_output = sorted(output, key=lambda k: k['due'])
		print "\EDIT THIS: " + str(sorted_output[taskID])
		collection.update_one({"_id":sorted_output[taskID]['_id']}, {"$set":data});

		print "successfully remove"

	except pymongo.errors.ConnectionFailure, e:
		print "delete_error: %s" % e

def get_data(taskID):
	output = []
	sorted_output = []
	for j in collection.find():
		output.append({'_id':str(j['_id']),'task':j['task'],'due':j['due']})
	sorted_output = sorted(output, key=lambda k: k['due'])

	print "\EDIT THIS: " + str(sorted_output)
	return (sorted_output)

def get_table():
	output= []

	for j in collection.find():
		output.append({'_id':str(j['_id']),'task':j['task'],'due':j['due']})
	sorted_output = sorted(output, key=lambda k:k['due'])

	return (sorted_output)



