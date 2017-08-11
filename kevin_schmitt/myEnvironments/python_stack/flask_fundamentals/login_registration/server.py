from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'mykeysecret'
mysql = MySQLConnector(app,'login_users')
@app.route('/')
def index():
    query = "SELECT * FROM users"                      # define your query
    users = mysql.query_db(query)  
    # print friends                                        # run query with query_db()
    return render_template('index.html', users=users) # pass data to our template
@app.route('/users', methods=['POST'])
def create():
    is_valid = True
    if request.form['name'] == '':
        is_valid = False
        flash("Name cannot be blank")
    if request.form['email'] == '':
        is_valid = False
        flash("Email cannot be blank")
    if request.form['password'] == '':
        is_valid = False
        flash("Password cannot be blank")

    if is_valid == True:
        query = 'INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW())'
        data = {
                'name': request.form['name'],
                'email': request.form['email'],
                'password': request.form['password']
                }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        return redirect('/')



@app.route('/user/<users_id>')
def show(users_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM users WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': users_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_user=users[0])
app.run(debug=True)