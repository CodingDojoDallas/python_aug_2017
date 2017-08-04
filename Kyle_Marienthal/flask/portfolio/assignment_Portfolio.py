from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('portfolio.html')

@app.route('/project')
def pLists():
    return render_template('project.html')

@app.route('/about') 
def aboutMe():
    return render_template('about.html')

app.run(debug=True)