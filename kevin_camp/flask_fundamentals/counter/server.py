from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	try:
		session['counter'] += 1
	except:
		session['counter'] = 1
	return render_template('index.html')

@app.route('/add2', methods=['POST'])
def addtwo():
	print 'Two Visits Added'
	session['counter'] += 1
	return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True)
