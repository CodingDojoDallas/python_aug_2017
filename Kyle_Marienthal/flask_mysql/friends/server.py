from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'world')
@app.route('/')
def index():
    countries = mysql.query_db("SELECT * FROM countries")
    cities = mysql.query_db("SELECT * FROM cities")
    return render_template('countries.html', countries=countries, cities=cities)
@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    #send an INSERT query to the DB!!!  Using the form data!!!!
    return redirect('/')
app.run(debug=True)