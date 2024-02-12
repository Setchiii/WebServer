import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect


app = Flask(__name__)


@app.route("/favicon.ico")
def favico():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'assets/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/<string:page_name>.html')
def render_page(page_name):
    return render_template(f'{page_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('requests.csv', 'a', newline='') as csvfile:
                fieldnames = ['email', 'subject', 'message']
                writer = csv.DictWriter(
                    csvfile, delimiter=";", fieldnames=fieldnames)
                writer.writerow(data)
                return redirect('/thankyou.html')
        except Exception as e:
            return f'Something went wrong. Try again! {e}'
    else:
        return 'Something went wrong. Try again!'
