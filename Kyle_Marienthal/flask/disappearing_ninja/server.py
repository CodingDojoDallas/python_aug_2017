from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tmnt')
def familyPicture():
    
    return render_template('tmnt.html')

app.run(debug=True)