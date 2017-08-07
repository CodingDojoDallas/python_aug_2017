from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "somethingReallySecret"

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def createUser():
    print request.form['name']
    print request.form['email']
    user_dict = {
        'name': request.form['name'],
        'email': request.form['email'],
    }
    session['user_name'] = request.form['name']
    return redirect('/showUsers')

@app.route('/showUsers')
def show_users():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('show_users.html', user_name=session['user_name'], count=session['count'])

@app.route('/route/<param>')
def route_params(param):
    if param == 'Cody':
        return render_template('params.html', param=param)
    else:
        return render_template('params2.html')

app.run(debug=True)
