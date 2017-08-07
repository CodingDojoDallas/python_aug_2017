from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'somethingSecret'



@app.route('/')     #methods=['GET'] by default
def index(): 
    if 'gold' not in session: 
        session['gold']=0
    return render_template('index.html', gold = session['gold'])

@app.route('/process_money', methods=['POST'])       #must methods=['POST'] to take in info filled out from index
def process_money():
    number = 0    
    button = request.form['location']
    if button == 'farm':
        number = random.randint(10,21)
        session['gold'] += number
    elif button == 'cave':
        number = random.randint(5,11)
        session['gold'] += number
    elif button == 'house':
        number = random.randint(2,5)
        session['gold'] += number
    elif button == 'casino':
        number = random.randint(-50,51)
        session['gold'] += number
    
    
    return redirect('/')



app.run(debug=True)