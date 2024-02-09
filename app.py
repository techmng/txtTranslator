from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    original_text = request.form['text']
    target_language = request.form['language']
    translated_text = "Converted text"
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )
