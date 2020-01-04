#!/usr/bin/python3

#from flask import Flask, render_template
# Most basic layout + multiple page creation
"""
app = Flask(__name__)  #name = root path

# @ signifies a decorator - way to wrap a function + modify its behaviour
# all of the function and decorator below, is just connecting a url to a function which returns something

@app.route('/')  # / is the root directory reference (e.g. /user)
def index():  #index just cos it's the home page
    return "This is the home page"  #text seen by user

@app.route("/hi")  #creates another webpage (HAS to have a / before name)
def hi():
	return "<h2>Hi there guys</h2>"  #builds a second page on our server ( localhost:5000/hi )
	
@app.route("/profile/<username>")  #username is a variable inside the webpage, so it has to be between < >
def profile(username):
	return "<h2>Hey there %s</h2>" % username  #username depends on what is typed in
	
@app.route("/age/<int:age>")  #when it's an int it HAS to be specified  
def age(age):
	return "<h2>You are %d years old</h2>" % age

if __name__  == "__main__":  #used to say = ONLY run the app when clicked and called directly, NOT imported.
    app.run(debug = True)  #just start the app, but in debug mode, which is better, as code just refreshes
"""
# Methods of running a program
"""
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
	return "Method used is: %s" % request.method
	
@app.route("/forum", methods = ["GET","POST"])
def forum():
	if request.method == "POST":
		return "You are using POST"
	else:
		return "You are using GET my friend"

if __name__ == "__main__":
	app.run()
"""
#HTML tesmplates + static files
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/profile/<name>")
def profile(name):
	return render_template("profile.html", name = name)

if __name__ == "__main__":
	app.run()
"""
#Connecting Url's to an HTML file
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<user>")
def index(user = None):
	return render_template("user.html", user = user)

@app.route("/shopping")
def shopping():
	food = ["Cheese","Tuna","Whatever"]  #passing in a list to html
	return render_template("shopping.html", food = food)
if __name__ == "__main__":
	app.run()

#{% %} in html, means = don't treat it as html, it is actually python etc.