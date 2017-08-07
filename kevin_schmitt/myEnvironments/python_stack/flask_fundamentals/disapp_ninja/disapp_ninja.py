from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'   #this line is always needed when using the import 'session'


@app.route('/')     #methods=['GET'] by default
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


@app.route('/ninja/<username>')         #great example of using a variable in an html and the image needed on that specific page
def show_user_profile(username):
    print username
    return render_template('blue.html', username=username)

@app.errorhandler(404)         #modifies your 404 url not found page to whatever you have on your html file
def page_not_found(e):
    return render_template('404notFound.html'), 404



# @app.route('/ninja/blue')
# def blue():
#     return render_template('blue.html')

# @app.route('/ninja/red')
# def red():
#     return render_template('red.html')

# @app.route('/ninja/purple')
# def purple():
#     return render_template('purple.html')

# @app.route('/ninja/orange')
# def orange():
#     return render_template('orange.html')

app.run(debug=True)
