from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
import md5, os ,binascii

app = Flask(__name__)

mysql = MySQLConnector(app,'wall')
app.secret_key = "secret_key"

@app.route('/') #GET request
def home():
	return redirect('/users/new')

@app.route('/users/new') #GET request
def new_users():
	return render_template('new_users.html')

@app.route('/users', methods=['POST'])
def create_user():
	#validate data
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirmation = request.form['confirmation']

	is_valid = True

	if len(first_name) < 2 or len(last_name) < 2:
		is_valid = False
		flash("Name fields must have at least two characters")
	if email == "":
		is_valid = False
		flash("Email cannot be blank")
	if len(password) < 8:
		is_valid = False
		flash("Password must be at least four characters")
	if password != confirmation:
		is_valid = False
		flash("Passwords do not match")

	if is_valid == True:
		#salt
		salt = binascii.b2a_hex(os.urandom(15))
		#hash password
		hashed_pw = md5.new(password + salt).hexdigest()
		#INSERT to DB
		query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
		data = {
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'password': hashed_pw,
			'salt': salt
		}

		user_id = mysql.query_db(query, data)
		session['user_id'] = user_id
		session['first_name'] = first_name
		session['is_logged_in'] = True

		return redirect('/success')
	else:
		return redirect ('/users/new')

@app.route('/success')
def success():

	query = "SELECT * FROM messages ORDER BY id DESC;"
	messages = mysql.query_db(query)

	# query = "SELECT * FROM users JOIN users ON users.id = messages.user_id;"
	# message_un=mysql.query_db(query)


	print messages
	return render_template('wall.html', messages=messages)

@app.route('/sessions', methods=['POST'])
def login():
	#confirm email
	query = "SELECT * FROM users WHERE email = :email"
	data = { 'email': request.form ['email'] }
	user = mysql.query_db(query, data)

	is_valid = True

	if len(user) == 0:
		flash("Invalid credentials")
		return redirect('/users/new')

	hashed_login_pw = md5.new(request.form['password'] + user[0]['salt']).hexdigest()

	if len(user) != 0 and hashed_login_pw == user[0]['password']:
		session['user_id'] = user[0]['id']
		session['first_name'] = user[0]['first_name']
		session['is_logged_in'] = True
		return redirect('/success')
	else:
		flash('Invalid credentials')
		return redirect('users/new', session=session)

@app.route('/users/logout', methods=['POST'])
def logout():
	session['user_id'] = None
	session['first_name'] = None
	session['is_logged_in'] = False
	return redirect('/users/new')

@app.route('/messages', methods=['POST'])
def messages():
	hidden_id = request.form['hidden_id']
	message = request.form['message']

	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
	data = {
		'user_id': hidden_id,
		'message': message,
	}
	message = mysql.query_db(query, data)

	# print message
	# print hidden_id

	return redirect('/success')

@app.route('/comments', methods=['POST'])
def comments():
	comments = request.form['comments']

	query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW());"
	data = {
		'user_id': hidden_comment_id,
		'message_id': message_id,
		"comment": comment
	}

	comment = mysql.query_db(query, data)
	print comment
	print hidden_comment_id
	print message_id

	return redirect ('/success')


app.run(debug=True)
