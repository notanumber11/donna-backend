import os

import flask
from flask import Flask, redirect, render_template, request, url_for, jsonify

from local_test import default_call

print("Starting flask...")
app = Flask(__name__)


open_ai_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        return jsonify(default_call())

    result = request.args.get("result")
    return render_template("index.html", result=result)
