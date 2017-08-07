from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_page():
    return render_template("index.html")

@app.route("/createUser", methods=["POST"])
def createUser():
    print "you made it HEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRE"
    return redirect("/lastPage")

@app.route("/lastPage")
def lastPage():
    return "as;dodivhafdiubvqavj asdasdf"


app.run(debug=True)

