from flask import Flask, render_template, redirect, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/users', methods=['POST'])
def createUser():
    print request.form['name']
    print request.form['email']
    userDict = {
        'name': request.form['name'],
        'email': request.form['email'],
    }
    users.append(userDict)
    return redirect('/showUsers')

@app.route('/showUsers')
def showUsers():
    return render_template('show_users.html', users=users)

app.run(debug=True)