#!/usr/bin/python

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    try:
       version = os.environ['APP_VERSION']
    except Exception:
       version = "Missing environment APP_VERSION"
       pass
    return "app v %s" %version

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
