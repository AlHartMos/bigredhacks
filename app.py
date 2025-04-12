import random

from flask import Flask, render_template
from helpers import encode_message
from lists import quotes, keys

app = Flask(__name__)

key = ""
message = ""
encoded_message = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encode")
def encode():
    global key 
    key = random.choice(keys).upper()
    global message 
    message = random.choice(quotes)
    global encoded_message 
    encoded_message= encode_message(message, key)
    return render_template("encode.html", key=key, message=message)

@app.route("/decode")
def decode():
    global key 
    key = random.choice(keys).upper()
    global message
    message = random.choice(quotes)
    global encoded_message 
    encoded_message = encode_message(message, key)
    return render_template("decode.html", key=key, message=encoded_message)

@app.route("/response")
def response():
    return render_template("response.html", message=message, key=key, encoded_message=encoded_message)