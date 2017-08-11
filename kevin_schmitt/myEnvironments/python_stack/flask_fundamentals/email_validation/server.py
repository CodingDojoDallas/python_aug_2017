from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'users')
@app.route('/')
def index():
    print 'IndeX ROute'
    query = "SELECT * FROM users_table"                      # define your query
    persons = mysql.query_db(query)                                       # run query with query_db()
    return render_template('index.html', people=persons) # pass data to our template
@app.route('/register', methods=['POST'])
def create():
    print 'creAte rOute'
    print '*'*25
    query = 'INSERT INTO users_table (email_address, name, created_at, updated_at) VALUES (:email_address, :name, NOW(), NOW())'
    print request.form['email_address']
    print request.form['name']
    data = {
             'email_address': request.form['email_address'],
             'name': request.form['name']
            }
    # add a friend to the database!
    mysql.query_db(query, data)
    
    return redirect('/')
@app.route('/check', methods=['POST'])
def check():
    is_valid = True
    if request.form['email'] == '':
        is_valid = False
        flash("Name cannot be blank.")

    if is_valid == True:
        query = "SELECT * FROM users_table"
        mysql.query_db(query)
        return redirect('/check')
    else:
        
    
        return redirect('/')
app.run(debug=True)

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])
