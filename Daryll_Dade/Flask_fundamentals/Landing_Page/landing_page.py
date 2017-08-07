from flask import flask
app = Flask(__name__)

@app.route('/')


def hello_world():
    retun "Hello_world"

app.run(debug=True)
