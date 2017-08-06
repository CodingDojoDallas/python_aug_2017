from flask import Flask, render_template, redirect, request,session
import random
app = Flask(__name__)
app.secret_key = 'somethingSecret'

goldAmount = 0

@app.route('/')     #methods=['GET'] by default
def index():    
    return render_template('index.html', goldAmount = goldAmount)

@app.route('/process_money', methods=['POST'])       #must methods=['POST'] to take in info filled out from index
def process_money():
    number = 0
    button = request.form['name']
    if button == 'farm':
        number = random.randint(10,21)
        # goldAmount = goldAmount + number
    elif button == 'cave':
        number = random.randint(5,11)
        # goldAmount = goldAmount + number
    elif button == 'house':
        number = random.randint(2,5)
        # goldAmount = goldAmount + number
    elif button == 'casino':
        number = random.randint(-50,51)
        # goldAmount = goldAmount + number
    
    
    return redirect('/')



app.run(debug=True)