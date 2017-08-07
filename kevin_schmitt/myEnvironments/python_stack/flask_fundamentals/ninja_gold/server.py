from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'somethingSecret'


@app.route('/')     #methods=['GET'] by default
def index(): 
    if 'gold' not in session: 
        session['gold']=0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html', gold = session['gold'], activities = session['activities'])

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

    #Earned 15 gold from the farm! 08/07/2017

    session['activities'].append("Earned {} gold from the {}!  {}".format(number,button,str(datetime.now())))

    
    return redirect('/')





app.run(debug=True)