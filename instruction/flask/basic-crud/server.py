from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'mysuperdupersecret'

mysql = MySQLConnector(app, 'flaskUsers')

@app.route('/') # GET REQUEST
def home():
    return redirect('/users')

@app.route('/users', methods=['POST']) # POST REQUEST
def create():
    #validate data first
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
        query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW());"
        data = {
            'name': request.form['name'],
            'email': request.form['email'], 
            'password': request.form['password'],
        }
        mysql.query_db(query, data)
        return redirect('/users')
    else:
        return redirect('/users/new')


@app.route('/users') #GET request
def index():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('get_users.html', users=users)

@app.route('/users/new')
def new():
    return render_template('new_user.html')

@app.route('/users/<user_id>')
def show(user_id):
    query = "SELECT * FROM users WHERE users.id = :user_id;"
    data = {
        'user_id': user_id,
    }
    user = mysql.query_db(query, data);
    return render_template('show_user.html', user=user[0])

@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT * FROM users WHERE users.id = :user_id;"
    data = {
        'user_id': user_id,
    }
    user = mysql.query_db(query, data);
    return render_template('edit_user.html', user=user[0])

@app.route('/users/<user_id>/update', methods=['POST']) # POST REQUEST
def update(user_id):
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
        query = "UPDATE users SET name = :name, email = :email, password = :password, updated_at = NOW() WHERE id = :user_id;"
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'password': request.form['password'],
            'user_id': user_id,
        }
        mysql.query_db(query, data)
        return redirect('/users')
    else:
        return redirect("/users/{}/edit".format(user_id))

@app.route('/users/<user_id>/destroy', methods=['POST']) #POST REQUEST
def destroy(user_id):
    query = "DELETE FROM users WHERE id = :user_id;"
    data = {
        'user_id': user_id
    }
    mysql.query_db(query, data)
    return redirect('/users')


app.run(debug=True)
