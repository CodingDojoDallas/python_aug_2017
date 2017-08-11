from flask import Flask, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'thesecretkey'

mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users', methods=['POST'])
def create():
    is_valid = True
    if request.form['email'] == '':
        is_valid = False
        flash('email cannot be blank') 

    if is_valid == True:
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW());"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/users')
    else:
        return redirect('/users/new')

@app.route('/users')
def index():
    users = mysql.query_db('SELECT * FROM users')
    return render_template('get_users_emails.html', users=users)

@app.route('/users/new')
def new():
    return render_template('new_user.html')

app.run(debug=True)