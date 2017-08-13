from flask import Flask, render_template , request
app = Flask (__name__)

@app.route('/') 
def index():
     return render_template('index.html')

@app.route('/ninja' , methods=['POST'])
def ninja():
    return render_template('ninja.html')

@app.route ('/ninja/<x>')
def showUserProfile(x):
    # myRange = ['red','blue','yellow','green']
    # for x in myRange:
    if x == 'yellow':
        myImg = "../static/img/donatello.jpg"

    elif x == 'red':
        myImg = "../static/img/raphael.jpg"
    elif x == 'green':
        myImg = "../static/img/michelangelo.jpg"
    else :
        myImg = "../static/img/leonardo.jpg"

    print myImg       

    return render_template('ninja.html', myImg=myImg)

app.run(debug=True)
