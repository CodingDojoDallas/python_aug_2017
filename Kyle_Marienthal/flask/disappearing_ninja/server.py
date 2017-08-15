from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'   #this line is always needed when using the import 'session'


@app.route('/')     #WORKS
def index():
    return render_template('index.html')

@app.route('/ninja') #WORKS
def ninja():
    return render_template('4ninjas.html')

@app.route('/ninja/blue') #WORKS
def blue():
    return render_template('leo.html')

@app.route('/ninja/orange') #WORKS
def orange():
    return render_template('mike.html')

@app.route('/ninja/red') #WORKS
def red():
    return render_template('raph.html')

@app.route('/ninja/purple') #WORKS
def purple():
    return render_template('don.html')


@app.route('/ninja/<username>') #WORKS
def notApril(username):
    print username
    return render_template('hacked.html', username=username)

app.run(debug=True)