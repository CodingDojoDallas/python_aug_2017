from flask import Flask, request, redirect, render_template, session, flash 
from mysqlconnection import MySQLConnector
app = Flask(__name__) 
mysql = MySQLConnector(app,'friends') 
@app.route('/') 
def index(): 
    query = 'select * from friends' 
    friends = mysql.query_db(query) 
    return render_template('index.html',all_friends = friends) 
@app.route('/friends', methods=['POST']) 
def create(): 
    query = 'insert into friends(first_name, last_name, occupation, created_at, updated_at) values(:first_name, :last_name, :occupation, now(), now())' 
    data = { 
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'], 
    'occupation' : request.form['occupation'] 
} 
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)