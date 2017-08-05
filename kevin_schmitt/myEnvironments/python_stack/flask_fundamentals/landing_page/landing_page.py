from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')     #methods=['GET'] by default

def index():    
    return render_template('index.html')


@app.route('/ninjas')  
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos', methods=['GET'])
def dojos():
  return render_template('dojos.html')

@app.route('/users', methods=['POST'])
def createUser():
    print'You triggered my function!'
    return redirect('/')
    


app.run(debug=True)