from flask import Flask, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'thesecretkey'

mysql = MySQLConnector(app, 'name of your database!!!!!!!!!!!')

@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def get_users():


app.run(debug=True)