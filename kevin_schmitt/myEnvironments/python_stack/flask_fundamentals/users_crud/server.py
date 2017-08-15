from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii
app = Flask(__name__)
app.secret_key = 'mykeysecret'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def home():
    
    return redirect('/friends')

@app.route('/friends/create', methods=["POST"])
def create():

    query = 'insert into friends (first_name, last_name, occupation, created_at, updated_at) values (:first_name,:last_name,:occupation,now(),now())'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/friends')
    
@app.route('/friends')
def index():
    friends = mysql.query_db('select * from friends')
    return render_template('show_friends.html', friends=friends)

@app.route('/friends/new')
def new():
    return render_template('new_friend.html')

@app.route('/friends/<id>/edit')
def editpage(id):
    return render_template('edit_friends.html', id=id)


@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    occupation = request.form['occupation']
    id = id
    query = 'update friends set id = :id, first_name = :first_name, last_name = :last_name, occupation = :occupation, created_at = now(), updated_at = now() where friends.id= :id'
    data = {
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'occupation': occupation
    }

    friends = mysql.query_db(query, data)
    return redirect('/friends')

@app.route('/friends/<id>')
def showfriend(id):
    query = 'select * from friends where friends.id = :specific_id'
    data = {
        'specific_id': id
    }
    friends = mysql.query_db(query, data)

    return render_template('showonefriend.html', one_friend=friends[0])

@app.route('/friends/<id>/destroy')
def destroy(id):
    id=id
    query = 'delete from friends where friends.id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/friends')
app.run(debug=True)