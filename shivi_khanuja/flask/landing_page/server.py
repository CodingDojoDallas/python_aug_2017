from flask import Flask , render_template , redirect

app = Flask (__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/dojo', methods=['GET'])
def dojo():
    return render_template('dojo.html')  

@app.route('/users' , methods=['POST'])
def createUser():
    print 'Button was clicked!'
    return redirect ('/') 

app.run(debug=True)