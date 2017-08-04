from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojo():
    return render_template('dojos.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    return redirect('/')

app.run(debug=True)
