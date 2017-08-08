from flask import Flask, render_template, redirect, request
app = Flask(__name__)

users = []

@app.route('/')
def survey():
  return render_template('index.html')

@app.route('/users', methods=['POST'])
def createuser():
    print request.form['name']
    print request.form['location']
    print request.form['language']
    print request.form['comments']
    userDict = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comments': request.form['comments'],
    }
    users.append(userDict)
    return redirect('/result')

@app.route('/result')
def info():
    return render_template('result.html', users=users)

app.run(debug=True)
