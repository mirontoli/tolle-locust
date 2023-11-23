from time import sleep
from random import randint
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Anatoly"

@app.route("/heavier")
def hello_heavier():
    sec = randint(1,10000)/1000
    sleep(sec)
    return "Hello Anatoly Heavier"