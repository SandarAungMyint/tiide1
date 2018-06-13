from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():

     return "Hello Everybody"

 @app.route("/tiide1")
 def tiide1():
     return "Welcome to TIIDE-1 World "                                                                                                 
