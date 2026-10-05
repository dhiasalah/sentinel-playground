import subprocess

import requests
import re
from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        return "Invalid host", 400
    return subprocess.check_output(["ping", "-c", "1", host], text=True)


@app.route("/preview")
def preview():
    return requests.get(request.args["url"], timeout=5).text
