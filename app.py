from flask import Flask, render_template, request

#we are going to tell python that from here downwards we have a flask application

app = Flask(__name__) 

#this tells the app the route of access on the webserver (like in webscrapping); this one is the main (just a bar)

@app.route('/')
#create a function to render info on the page
def my_function():
    return "Welcome to my personal page: I'm Bob Loblaw!"

@app.route('/student')
def second_function():
    return "I can change pages/routes"

@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    if request.method == "POST":

        ##here you do your logic with the inputs from user

        param = request.form['parameter 1']

        if param.isdigit():

            param = int(param) + 10

        return render_template("main.html", value = param) #this is the value that goes into the html
    
    else: 

        return render_template("main.html", value = "not logical")

#the functions are running in the route above them; they're automatically called my that

if __name__ == '__main__':
    app.run(debug = True, port = 4552) #any local port

