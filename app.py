import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path="/static")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/elements.html', methods=['GET'])
def elements():
    return render_template('elements.html')

@app.route('/generic.html', methods=['GET'])
def generic():
    return render_template('generic.html')
