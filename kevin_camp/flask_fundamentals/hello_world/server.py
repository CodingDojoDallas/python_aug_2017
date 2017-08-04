from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name = "Artist formerly known as 'Prince'")

app.run(debug=True)
