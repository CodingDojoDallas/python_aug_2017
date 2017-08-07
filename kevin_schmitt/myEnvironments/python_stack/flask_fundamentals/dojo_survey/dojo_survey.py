from flask import Flask, render_template, redirect, request

app = Flask(__name__)

users=[]

@app.route('/')     #methods=['GET'] by default
def index():    
    return render_template('index.html')

@app.route('/users', methods=['POST'])       #must methods=['POST'] to take in info filled out from index
def process():
     print request.form['name']          #you HAVE to improt request at top for this to work
     print request.form['email']
     userDict = {
         'name': request.form['name'],
         'email': request.form['email'],
         'location':request.form['location'],
         'language':request.form['language'],
     }
     users.append(userDict)
     return redirect('/result')

@app.route('/result')    
def end():    
    return render_template('result.html', users=users)


app.run(debug=True)