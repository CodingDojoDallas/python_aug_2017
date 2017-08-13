from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tmnt/<color>')
def familyPicture(color):
    if(color == "blue"):
        img_path = "../static/leonardo.jpg"
    elif(color == "orange"):
        img_path = "../static/michelangelo.jpg"
    elif(color == "red"):
        img_path = "../static/raphael.jpg"
    elif(color == "purple"):
        img_path = "../static/donatello.jpg"
    else:
        
    return render_template('tmnt.html', img_path=img_path)


app.run(debug=True)

# On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
# When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
# /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)
# If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
# /ninja/orange - Ninja Turtle Michelangelo.
# /ninja/red - Ninja Turtle Raphael
# /ninja/purple - Ninja Turtle Donatello
# If a user tries to hack into your web app by specifying a color or string combination other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg
# You'll need to remember how to use static files for this assignment. Take a minute to refresh your memory back to the static files section if you need to :)