import subprocess

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    return subprocess.check_output(f"ping -c 1 {host}", shell=True, text=True)


@app.route("/preview")
def preview():
    return requests.get(request.args["url"], timeout=5).text
