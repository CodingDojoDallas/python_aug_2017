from flask import Flask, render_template , redirect , request

app = Flask (__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def process():
    print request.form['name']
    return redirect('/end')


@app.route('/end')
def end():
    return 'It ends here' 
app.run(debug=True)