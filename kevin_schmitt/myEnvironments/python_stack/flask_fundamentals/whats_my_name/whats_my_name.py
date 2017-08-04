from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')     #methods=['GET'] by default
def index():    
    return render_template('index.html')

@app.route('/process', methods=['POST'])       #must methods=['POST'] to take in info filled out from index
def process():
     print request.form['name']      #you HAVE to improt request at top for this to work
     return redirect('/end')

@app.route('/end')    
def end():    
    return 'This is the end of the road.!'
    


app.run(debug=True)