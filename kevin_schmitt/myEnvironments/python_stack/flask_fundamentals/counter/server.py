from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'   #this line is always needed when using the import 'session'


@app.route('/')     #methods=['GET'] by default
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', count=session['count'])

# def reset_values():
#     session['count']=0
# reset = Button(text="Reset Values!", command=session).place(x=10, y=165)

@app.route('/next', methods=['POST'])
def next():
    session['count'] = 0
    return redirect('/')



app.run(debug=True)
