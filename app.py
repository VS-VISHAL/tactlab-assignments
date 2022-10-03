from flask import Flask,render_template
import random
import json

app  = Flask(__name__)
PORT = 3009

    
@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "good morning" : "hello tactlab"
    }

    return render_template("vishal.html", result = result)


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)