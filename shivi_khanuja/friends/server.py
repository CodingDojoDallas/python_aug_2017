from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'world')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)