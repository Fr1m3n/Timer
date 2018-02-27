from flask import render_template
from app import app
import random

@app.route('/')
def main():
    a = str(random.randint(0, 10000))
    return render_template("main.html",
                           title = 'main',
                           rand = a)


@app.route('/index.html')
def index():
    return render_template("index.html")


