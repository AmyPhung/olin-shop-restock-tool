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


# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

exampleFormControlSelect2

@app.route('/foo', methods=['POST'])
def foo():
    # grab reddit data and write to csv
    return jsonify({"message": "you're a superstar"})
