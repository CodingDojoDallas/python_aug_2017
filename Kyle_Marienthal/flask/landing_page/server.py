from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/ninjas')
def ninja_page():
    return render_template("ninjas.html")

@app.route('/dojos/new', methods=["POST"])
def dojo_page():
    return render_template("dojos.html")

@app.route('/dojos/new', methods=["POST"])
def redirect():
    return redirect("/")
# not sure how to fix this one

app.run(debug=True)
