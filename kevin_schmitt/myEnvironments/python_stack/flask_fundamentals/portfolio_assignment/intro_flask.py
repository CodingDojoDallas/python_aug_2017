from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_everyone():
    return 'Hello Everyone!'


@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/flask_page_test')
def flask_page():
  return render_template('flask_page_test.html')

@app.route('/another_page')
def another_page():
  return render_template('another_page.html')

app.run(debug=True)
