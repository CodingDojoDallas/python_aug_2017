from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)
app.secret_key = 'loginregissofun'

mysql = MySQLConnector(app, 'flaskWall602')

def get_current_user():
    query = 'SELECT id, name, email FROM users WHERE id = :user_id'
    data = { 'user_id': session['user_id'] }
    current_user = mysql.query_db(query, data)
    return current_user[0]

@app.route('/') #GET REQUEST
def home():
    return redirect('/users/new')

@app.route('/users/new') # GET REQUEST
def users_new():
    return render_template('new_user.html')

@app.route('/users', methods=['POST']) #POST REQUEST
def create_user():
    #validate the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    is_valid = True

    if name == '':
        is_valid = False
        flash('Name cannot be blank.')
    if email == '':
        is_valid = False
        flash('Email cannot be blank.')
    if len(password) < 4:
        is_valid = False
        flash('Password must be at least four characters')
    if password != password_confirmation:
        is_valid = False
        flash('Passwords do not match')

    if is_valid == True:
        # step 1: generate the salt
        salt = binascii.b2a_hex(os.urandom(15))
        # step 2: hash the password
        hashed_pw = md5.new(password + salt).hexdigest()
        # step 3: save in DB
        query = "INSERT INTO users (name, email, password, salt, created_at, updated_at) VALUES (:name, :email, :password, :salt, NOW(), NOW())"
        data = {
            'name': name,
            'email': email,
            'password': hashed_pw,
            'salt': salt
        }
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        session['is_logged_in'] = True
        return redirect('/wall')
    else:
        return redirect('/users/new')

@app.route('/wall')
def success():
    current_user = get_current_user()
    query = "SELECT users.id as message_user_pk, users.name as message_user_name, messages.id as message_pk, messages.message, messages.updated_at as message_timestamp, comments.id as comment_pk, comments.message_id, comments.comment, comments.updated_at as comment_timestamp, users2.id as comment_user_pk, users2.name as comment_user_name FROM users LEFT JOIN messages ON users.id = messages.user_id LEFT JOIN comments ON messages.id = comments.message_id LEFT JOIN users as users2 ON users2.id = comments.user_id;"

    messages = mysql.query_db(query);

    new_messages = []

    message_ids = []
     
    for message in messages:
        if message['message_pk'] not in message_ids:
            message_ids.append(message['message_pk'])
            myMsgObj = {
                'pk': message['message_pk'],
                'message': message['message'],
                'user_name': message['message_user_name'],
                'timestamp': message['message_timestamp'],
                'comments': []
            }
            if message['comment_pk'] != None:
                #create a comment obj
                myCommentObj = {
                    'pk' : message['comment_pk'],
                    'user_name' : message['comment_user_name'],
                    'comment' : message['comment'],
                    'timestamp' : message['comment_timestamp']
                }
                myMsgObj['comments'].append(myCommentObj)
            new_messages.append(myMsgObj)
        else:
            #just want to extract the comment                
            myCommentObj = {
                'pk' : message['comment_pk'],
                'user_name' : message['comment_user_name'],
                'comment' : message['comment'],
                'timestamp' : message['comment_timestamp']
            }
            new_messages[-1]['comments'].append(myCommentObj)


    # message = {
    #     'pk': 1,
    #     'user_name': 'Cody',
    #     'message' : 'my Message',
    #     'comments': [
    #         {
    #             'pk' : 1,
    #             'user_name', 'Cody'
    #             'comment': 'My first Comment'
    #         },
    #         {
    #             'pk' : 2,
    #             'user_name', 'Cody'
    #             'comment': 'My second Comment'
    #         },
    #     ]
    # }
    return render_template('wall.html', session=session, current_user=current_user, messages=new_messages)

@app.route('/sessions', methods=['POST']) # POST REQUEST
def login():
    # step 1: confirm the email
    query = "SELECT * FROM users WHERE email = :email"
    data = { 'email': request.form['email'] }
    user = mysql.query_db(query, data)

    if len(user) == 0:
        flash('invalid credentials')
        return redirect('/users/new')

    hashed_input_password = md5.new(request.form['password'] + user[0]['salt']).hexdigest()
    if len(user) != 0 and hashed_input_password == user[0]['password']:
        session['user_id'] = user[0]['id']
        session['is_logged_in'] = True
        return redirect('/wall')
    else:
        flash('Invalid credentials')
        return redirect('/users/new')

@app.route('/messages', methods=['POST']) #POST REQUEST
def create_message():
    #step 1: validations
    if request.form['message'] == '':
        flash('Message cannot be blank');
        return redirect('/wall')
    #step 2: write the query
    query = 'INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())'
    #step 3: attach user id
    data = {
        'message' : request.form['message'],
        'user_id' : session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments', methods=['POST']) #POST REQUEST
def create_comment():
    if request.form['comment'] == '':
        flash('Comment cannot be blank');
        return redirect('/wall')
    query = 'INSERT INTO comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())'
    data = {
        'comment' : request.form['comment'],
        'message_id' : request.form['message_id'],
        'user_id' : session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/users/logout') #GET REQUEST
def logout():
    session['user_id'] = None
    session['is_logged_in'] = False
    return redirect('/users/new')

app.run(debug=True)