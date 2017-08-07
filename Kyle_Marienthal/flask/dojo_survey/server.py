from flask import Flask, render_template,redirect,request
app = Flask(__name__)

myObj = {}

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/createUser', methods=["POST"])
def makeStudent():
    myObj['name'] = request.form['name']
    myObj["location"] = request.form["location"]
    myObj["language"] = request.form["lang"]
    myObj['comments'] = request.form["comment"]
    print myObj
    return redirect("/applicantCreated")

@app.route("/applicantCreated", methods=["GET"])
def displayInfo():
    return render_template('applicantCreated.html', myObj=myObj)


app.run(debug=True)