# from flask import Flask
from flask import *

app = Flask(__name__)

@app.route("/")
def get():
    return {"return": "ok"}

@app.route("/", methods = ['POST'])
def post():
    print(request.data)
    return {"return": "ok"}

if __name__ =='__main__':
    app.run(debug = True)