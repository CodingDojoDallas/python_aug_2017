from flask import Flask, render_template, redirect, flash, session, request
from mysqlconnection import MySQLConnector
import md5, os, binascii
app = Flask(__name__)
app.secret_key = 'thesecretkey'
mysql = MySQLConnector(app,'loginandreg')
@app.route('/') #get request
def home():
    return redirect('/users/new')
@app.route('/users/new') #get request
def users_new():
    return render_template('new_user.html')
@app.route('/users',methods=['POST'])#POST request
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    is_valid = True
    if first_name == '':
        is_valid = False
        flash('First_Name cannot be blank.')
    if last_name == '':
        is_valid = False
        flash('Last_Name cannot be blank.')
    if email == '':
        is_valid = False
        flash('Email cannot be blank.')
    if len(password) < 8:
        is_valid = False
        flash('Password should be atleast eight characters')
    if password != password_confirmation:
        is_valid =  False
        flash('password do not match')

    if is_valid == True:
           
        salt = binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()
        query = "INSERT INTO login  (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, now(), now())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': hashed_pw,
            'salt': salt
         }
        mysql.query_db(query,data)

 
        return redirect('/success')
    else:
        return redirect('/users/new')           
@app.route('/success')
def success():
    return render_template('success.html')
#validate the data
app.run(debug=True)