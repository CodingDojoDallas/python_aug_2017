from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'   #this line is always needed when using the import 'session'


@app.route('/')     #methods=['GET'] by default
def index():
    return render_template('index.html')




@app.route('/guess', methods=['POST'])
def number_guessing_game():    
    number = random.randint(1,101)
    numguess = int(request.form['numguess'])

    for nums in range(1, 101):      
        if numguess == number:                
            return render_template('win.html')
        elif numguess > number:
            return render_template('toohigh.html')
        elif numguess < number:
            return render_template('toolow.html')
        
app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')      

    
    



app.run(debug=True)
