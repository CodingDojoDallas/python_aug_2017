from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii
app = Flask(__name__)
app.secret_key = 'mykeysecret'
mysql = MySQLConnector(app,'user_reg')

@app.route('/')
def index():
    query = "SELECT * FROM users"                    
    users = mysql.query_db(query)  
    # print friends                                  
    return render_template('index.html', users=users)

@app.route('/usersnew', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']
    
    is_valid = True
    if request.form['name'] == '':
        is_valid = False
        flash("Name cannot be blank")
    if request.form['email'] == '':
        is_valid = False
        flash("Email cannot be blank")
    if len(password) < 4:
        is_valid = False
        flash("Password must be atleast than 4 letters.")
    if password != password_confirmation:
        is_valid = False
        flash("Password must match Confirmation.")

    if is_valid == True:        
        salt = binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()
        query = 'INSERT INTO users (name, email, password, salt, created_at, updated_at) VALUES (:name, :email, :password, :salt, NOW(), NOW())'
        data = {
                'name': name,
                'email': email,
                'password': hashed_pw,
                'salt': salt
                }
        users = mysql.query_db(query, data)
        # session['user_id'] = request.form['id'] We don't enter ID in form
        session['name'] = request.form['name']
        session['is_logged_in'] = True
        return redirect('/thewall')
    else:
        return redirect('/')

@app.route('/thewall')
def thewall():
    query = "select users.name, messages.message_text from users join messages on users.id=messages.user_id"                    
    messages = mysql.query_db(query)                
    return render_template('thewall.html', messages=messages)

@app.route('/sessions', methods=['POST'])
def login():
    query = 'select * from users where email = :email'
    data = { 'email': request.form['email'] }
    users = mysql.query_db(query, data)
    print len(users) == 0
    if len(users) == 0:
        flash('Invalid Credentials')
        return redirect('/')
    else:
        hashed_input_password = md5.new(request.form['password'] + users[0]['salt']).hexdigest()
        if hashed_input_password == users[0]['password']:
            session['user_id'] = users[0]['id']
            session['name'] = users[0]['name']
            session['is_logged_in'] = True
            print session['user_id']
            print session['name']
            return redirect('/thewall')
        else:
            flash('WRONG credentials')
            return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    message_text = request.form['message']
    print session['name']
    test = session['user_id']
    print test
    print test
    query = 'INSERT INTO messages (message_text, created_at, updated_at, user_id) VALUES (:message_text, NOW(), NOW(), :user_id)'
    data = {
        'message_text': message_text,
        'user_id': test
    }
    mysql.query_db(query, data)
    return redirect('/thewall')


app.run(debug=True)