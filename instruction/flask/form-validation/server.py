from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'learningHowToFlash'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print request.form
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    is_valid = True

    #validations
    if name == '':
        is_valid = False
        flash('Name cannot be blank.')
    elif len(name) < 3:
        is_valid = False
        flash('Name must be at least three characters.')
    special_chars = ['!', '@', '#', '$', '%', '^']
    for char in name:
        if char in special_chars:
            is_valid = False
            flash('Name cannot have special characters')
    
    if email == '':
        is_valid = False
        flash('You must provide a valid email')
    
    if not re.search("\w+\@\w+\.\w+", email):
        is_valid = False
        flash('You must provide a valid email')

    if len(password) < 4:
        is_valid = False
        flash('Password must be at least four characters')
    elif password != password_confirmation:
        is_valid = False
        flash('Your passwords do not match')


    if is_valid == True:
        return redirect('/success') #redirect to next portion of app
    else:
        return redirect('/') #redirect back to form to display error messages

@app.route('/success')
def success():
    return 'You have succesfully registered!'

app.run(debug=True)