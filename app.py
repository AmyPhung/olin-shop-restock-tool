import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter



app = Flask(__name__, static_url_path="/static")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# QR Code Output Paste
# @app.route('/', methods=['POST'])
# def submit():
#     print('You entered: {}'.format(request.form['text']))
#     return render_template('index.html')
# @app.route('/click/', methods=['GET', 'POST'])#, methods=['POST', 'GET'])#, methods = ['GET'])
# def test_form():
#     if request.method == 'POST':
#         print ("box")
#         print(request.form["exampleFormControlTextarea1"])
#     return "asdf2"
#
@app.route('/', methods=['POST'])
def submit():
    # return 'You entered: {}'.format(request.form['text'])
    print('You entered: {}'.format(request.form['text']))
    return render_template('index.html')
#
#
# # Labels -----------------------------------------------------------------------
# UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
# DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
# ALLOWED_EXTENSIONS = {'pdf'}
#
# DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# # limit upload size upto 8mb
# app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
