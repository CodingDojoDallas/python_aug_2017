from flask import Flask, render_template, redirect, request,session
import random
app = Flask(__name__)
app.secret_key = 'somethingSecret'



@app.route('/')     #methods=['GET'] by default
def index():    
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])       #must methods=['POST'] to take in info filled out from index
def process_money():



app.run(debug=True)