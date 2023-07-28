from flask import Flask, render_template
import os
import json

app = Flask(__name__)

TESTHOLDER = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/values/{value}")
def endpoint1(value):
    TESTHOLDER.append(value)
    return json.dumps({"values": TESTHOLDER})


@app.route("/values")
def endpoint1():
    return json.dumps({"values": TESTHOLDER})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
