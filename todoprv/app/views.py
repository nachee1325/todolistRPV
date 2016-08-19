
from app import app
from app import api
from flask import render_template, flash, redirect, jsonify, request

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/_get_table')
def _get_table():
	print api.get_table()
	return jsonify(jsonn = api.get_table())

@app.route('/_get_data')
def _get_data():
	taskID = int(request.args.get('taskID'))
	task = str(request.args.get('task'))
	due = request.args.get('due')
	data = {"task": task, "due" : due}
	print api.get_data(taskID)
	print "hi po !!!! "+ str(taskID)
	return jsonify(result = api.get_data(taskID))

@app.route('/_add_task')
def _add_task():
	task = str(request.args.get('task'))
	due = request.args.get('due')
	data = {"task": task, "due" : due, "completed" : False}
	api.add(data)
	print api.get_table()
	return jsonify(result = api.get_table())

@app.route('/_edit_task')
def _edit_task():
	taskID = int(request.args.get('taskID'))
	task = str(request.args.get('task'))
	due = request.args.get('due')
	data = {"task": task, "due" : due}
	api.edit(taskID,data)
	return jsonify(result = api.get_table())

@app.route('/_delete_task')
def _delete_task():
	taskID = int(request.args.get('taskID'))
	api.delete(taskID)
	return jsonify(result = api.get_table())

