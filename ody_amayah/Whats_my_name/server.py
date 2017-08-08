from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
   print "username"
   return redirect('/process')

@app.route('/process')
def process():
    return redirect('/')

app.run(debug=True)
