from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    print 'IndeX ROute'
    query = "SELECT * FROM friends"                      # define your query
    friends = mysql.query_db(query)  
    # print friends                                        # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template
@app.route('/friends', methods=['POST'])
def create():
    print 'create route'
    print '*'*25
    query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())'
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'occupation': request.form['occupation']
            }
    # add a friend to the database!
    mysql.query_db(query, data)
    
    return redirect('/')
@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])
app.run(debug=True)