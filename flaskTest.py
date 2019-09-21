from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    # return render_template('my-form.html')
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

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
    return request.form

@app.route('/click/', methods=['GET', 'POST'])#, methods=['POST', 'GET'])#, methods = ['GET'])
def test_form():
    if request.method == 'POST':
        print ("box")
        print(request.form)
    return "asdf2"

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])

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
