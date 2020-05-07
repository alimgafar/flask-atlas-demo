from flask import render_template
from myapp import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/task/<id>")
def showTask(id):
	return "List a specific task in the collection: " + id

@app.route("/tasks")
def ListTasks():
	return "List all tasks in collection"

@app.route("/add")
def addTask():
	id = "somevalue"
	return "Add a new task in the collection and return the id: " + id

@app.route("/edit/<id>")
def editTask(id):
	return "Edit a specific task in the collection: " + id

# Soft delete - it flags the task as being removed, but does not delete the entry in the db
@app.route("/remove/<id>")
def removeTask(id):
	return "Marks a specific task removed from the collection: " + id

# Hard delete - it premanently removes the task from the collection 
@app.route("/delete/<id>")
def deleteTask(id):
	return "Deletes a specific task from the colleciton " + id

@app.route("/showSignUp")
def showSignUp():
    return render_template("/signups.html")

