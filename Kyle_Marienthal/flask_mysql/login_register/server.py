from flask import Flask, render_template, redirect, flash, session, request
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)
app.secret_key = 'thesecretkey'

mysql = MySQLConnector(app, 'login_register')

@app.route('/') #get request
def home():
    return redirect('/users/new')

@app.route('/users/new') #get request
def users_new():
    return render_template('new_user.html')

@app.route('/users',methods=['POST'])#POST request
def create_user():
    #validate the data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    is_valid = True

    if first_name == '':
        is_valid = False
        flash('First Name cannot be blank.')
    if last_name == '':
        is_valid = False
        flash('Last Name cannot be blank.')
    if email == '':
        is_valid = False
        flash('Email cannot be blank.')
    if len(password) < 5:
        is_valid = False
        flash('Password cannot be blank.')
    if password != password_confirmation:
        is_valid = False
        flash('Passwords didnt match')

    if is_valid == True:
        #step 1: generate the salt
        salt = binascii.b2a_hex(os.urandom(15))
        #step 2: hash the password
        hashed_pw = md5.new(password + salt).hexdigest()
        #step 3: save in the DB
        query = "INSERT INTO users(first_name, last_name, email, password, salt, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': hashed_pw,
            'salt': salt
        }
        user_id = mysql.query_db(query,data)
        session['user_id'] = user_id
        session['is_logged_in'] = True
        return redirect('/success')
    else:
        return redirect('/users/new')

@app.route('/success')
def success():
    return render_template('success.html', session=session)

@app.route('/sessions', methods=['POST'])
def login():
    #step1: confirm email
    query = "SELECT * FROM users WHERE email = :email"
    data = { 'email':request.form['email'] }
    user = mysql.query_db(query,data)

    is_valid = True

    if len(user) == 0:
        flash('invalid credentails')
        return redirect('/users/new') 

    hashed_input_password = md5.new(request.form['password'] + user[0]['salt']).hexdigest()
    if len(user) != 0 and hashed_input_password == user[0]['password']:
        session['user_id'] = user[0]['id']
        session['is_logged_in'] = True  
        return redirect('/success')
    else:
        flash('Invalid credentials')
        return redirect('/users/new')

@app.route('/users/logout', methods=['POST'])
def logout():
    session['user_id'] = None
    session['is_logged_in']= False
    return redirect('/users/new')




app.run(debug=True)