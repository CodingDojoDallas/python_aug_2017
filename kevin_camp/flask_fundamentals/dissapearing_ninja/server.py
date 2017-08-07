from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/ninja')

def ninja():
  return render_template('ninja.html')

@app.route("/ninja/<filename>")	#routes to seperate html according to color
def turtle(filename):
    if  filename == "purple":
        filename = "donatello"
    elif filename == "blue":
        filename = "leonardo"
    elif filename == "red":
        filename = "raphael"
    elif filename == "orange":
        filename = "michelangelo"

    if filename == "donatello" or filename == "leonardo" or filename == "michelangelo" or filename == "raphael":


        return render_template("newninja.html", filename = filename)
    else:
        return render_template("newninja.html", filename = "notapril")

app.run(debug=True)
