import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def webhook():
    print(request.data)
    return "Hello, from GITHUB webhook"


@app.route("/webhookcallback", methods=["GET", "POST"])
def hook():
    print(request.data)
    return "Hello, from webhook"


if __name__ == '__main__':
    app.run(debug=True, port=5000)