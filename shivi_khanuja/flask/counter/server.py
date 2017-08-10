from flask import Flask , render_template, redirect, session
app = Flask (__name__)
app.secret_key = 'SecretPath'

@app.route('/')
def index():
    
    session['counter'] += 1
    return render_template ('index.html')

@app.route('/add2', methods=['POST'])

def addtwo():
    print 'Two visits added'
    session['counter'] += 1
    return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
    print 'Reset'
    session['counter'] = 0
    return redirect('/')

app.run(debug= True)

    

   
