from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/createUser", methods=["POST"])
def createUser():
    print "you made it HEEEERRRRE"
    print request.form
    return redirect("/process")

@app.route("/process", methods=["GET"])
def process():
    
    return "your done?"


app.run(debug=True)

