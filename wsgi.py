from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/favicon.ico")
def favico():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'assets/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/")
def home2():
    return render_template("index.html")

@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/work.html")
def work():
    return render_template("work.html")

@app.route("/components.html")
def components():
    return render_template("components.html")

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")
