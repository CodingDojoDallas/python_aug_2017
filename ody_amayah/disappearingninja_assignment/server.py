from flask import Flask, render_template, request, redirect,session,flash
app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def index():
    return render_template('index.html', ninja='No ninjas here')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<username>')
def show_user_image(username):
    return render_template('purple.html', username=username

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 404

app.run(debug=True)
