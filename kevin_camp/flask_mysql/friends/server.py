from flask import Flask, redirect, render_template, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends2')

@app.route('/')
def index():
	query = ("SELECT * FROM friends2")
	friends = mysql.query_db(query)
	print friends
	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
	query = ("INSERT INTO friends2(name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())")
	data ={
		'name': request.form['name'],
		'age': request.form['age']
	}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)
