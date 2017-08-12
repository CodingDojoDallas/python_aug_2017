from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii
app = Flask(__name__)
app.secret_key = 'mykeysecret'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def home():
    
    return redirect('/friends')

@app.route('/friends', methods=["POST"])
def create():

    query = 'insert into friends (first_name, last_name, occupation, created_at, updated_at) values (:first_name,:last_name,:occupation,now(),now())'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/friends')
    
@app.route('/friends')
def index():
    friends = mysql.query_db('select * from friends')
    return render_template('get_friends.html', friends=friends)

@app.route('/friends/new')
def new():
    return render_template('new_friend.html')

app.run(debug=True)