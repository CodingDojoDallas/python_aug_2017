from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/ninjas')
def ninja_page():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def dojo_page():
    return render_template("dojos.html")
# this is a comment


app.run(debug=True)
