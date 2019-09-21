import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')


def process_file(path, filename):
    remove_watermark(path, filename)
    # with open(path, 'a') as f:
    #    f.write("\nAdded processed content")


def remove_watermark(path, filename):
    input_file = PdfFileReader(open(path, 'rb'))
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
        output.addPage(page)
    output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    output.write(output_stream)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# app = Flask(__name__)
#
# def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/')
# def my_form():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             print('No file attached in request')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             print('No file selected')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
#             return redirect(url_for('uploaded_file', filename=filename))
#     # return render_template('my-form.html')
#     return render_template('index.html')
#
# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text
#
# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"

@app.route('/testbox', methods=['GET', 'POST'])#, methods = ['GET'])
def read_box():
    if request.method == 'POST':
        print ("box")
        print(request.form)
    # return request.form
    return render_template('index.html')

@app.route('/click/', methods=['GET', 'POST'])#, methods=['POST', 'GET'])#, methods = ['GET'])
def test_form():
    if request.method == 'POST':
        print ("box")
        print(request.form)
    return "asdf2"

@app.route('/', methods=['POST'])
def submit():
    # return 'You entered: {}'.format(request.form['text'])
    print('You entered: {}'.format(request.form['text']))
    return render_template('index.html')
# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

# exampleFormControlSelect2
#
# @app.route('/foo', methods=['POST'])
# def foo():
#     # grab reddit data and write to csv
#     return jsonify({"message": "you're a superstar"})
