from flask import Flask
app = Flask(__name__)  #name = root path
# @ signifies a decorator - way to wrap a function + modify its behaviour
# all of the function and decorator below, is just connecting a url to a function which returns something

@app.route('/')  # / is the root directory reference (e.g. /user)
def index():  #index just cos it's the home page
    return "<h2>Homepage: Welcome user</h2>"  #text seen by user

@app.route("/age/<int:age>")  #when it's an integer it HAS to be specified  
def age(age):
	return "<h2>You are %d years old</h2>" % age

#os.environ.get("SECRET") #This is the environmental variables which are not in use now.

if __name__  == "__main__":  #used to say = ONLY run the app when clicked and called directly, NOT imported.
	app.run(debug = True)  #just start the app, but in debug mode, which is better, as code just refreshes without having to restart it
	# alternatively you can just do app.run()
